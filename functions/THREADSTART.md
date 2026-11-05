# THREADSTART
**Category:** スレッド

## Signature
```
THREADSTART( name [, arg ... ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 別スレッドで実行するユーザー関数の名前（文字列） |
| arg | 関数に渡す引数。省略できる。複数渡せば `_argv[0]`、`_argv[1]`、…になる |

## Returns
スレッドの ID（1 以上の整数）。起動できなかったときは負の値。

| 値 | 意味 |
|----|------|
| 1 以上 | 起動した。以後の `THREAD*` 関数にこの ID を渡す |
| -1 | その名前の関数がない（警告 W0035） |
| -2 | 同時に動かせる数（32）を超えた |
| -3 | unload の処理中で、新しいスレッドは作れない |
| -4 | OS がスレッドを作れなかった |
| -5 | このビルドはスレッドに対応していない（Emscripten） |

引数が足りない・文字列でないときは、警告 W0008 / W0009 を出して -1 を返します。

## Description
指定した関数を別のスレッドで動かします。SSP とのやりとり（`request`）とは別に、時間のかかる処理を並行して進めたいときに使います。呼び出した側はスレッドの終わりを待たずにすぐ戻ります。

```
OnBoot
{
	work.done = 0
	work.id = THREADSTART('Work.Heavy', 1000000)
	'計算を始めました'
}

Work.Heavy
{
	_sum = 0
	for _i = 0; _i < _argv[0]; _i++ {
		_sum += _i
	}
	work.sum = _sum     // 結果はグローバル変数に書いておく
	work.done = 1
}

OnSecondChange
{
	if work.done {
		'計算が終わりました: ' + TOSTR(work.sum)
	}
}
```

スレッドの結果の受け取り方は 3 通りあります。

- 関数の返り値を [THREADRESULT](THREADRESULT.md) で受け取る
- グローバル変数に書いて終わる（上の例）。ほかのスレッドとグローバル変数は共有です
- [DIRECTSSTP](DIRECTSSTP.md) で SSP へ知らせる。ワーカースレッドから呼ぶと、通信を待っている間は他の処理を止めません

### 動き方
- **グローバル変数は共有、ローカル変数は独立**です。スレッドの関数は自分のローカル変数を持ちます
- 辞書の関数を同時に実行するのは 1 つのスレッドだけです。ワーカーは文の切れ目で実行を譲り合い、**SSP からの `request` は優先して実行されます**。ワーカーが動いていても、`request` はワーカーの次の文の切れ目まで待つだけで返ってきます。複数の CPU を使って計算を速くするものではありません
- **外部の遅い応答を待つ間は、他のスレッドが止まりません**。ワーカーから呼んだ [REQUESTLIB](REQUESTLIB.md)（SAORI）、[EXECUTE_WAIT](EXECUTE_WAIT.md)、[EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)、[DIRECTSSTP](DIRECTSSTP.md)、[SLEEP](SLEEP.md) は、待つ間に実行を譲ります。[THREADJOIN](THREADJOIN.md) も同じです。SSP の `request` の中で呼んだ `REQUESTLIB` / `EXECUTE_WAIT` も、動いているワーカーがあれば、待つ間にワーカーが動けます（`SLEEP` は、`request` の中ではこれまでどおり待ちます）。これらの待ち以外のシステム関数（大きなファイル処理など）は、1 回の呼び出しが終わるまで実行を譲ることも中断することもできません
- 同時に動かせるのは 32 本までです。終わったスレッドの記録は、[THREADCLOSE](THREADCLOSE.md) で捨てるか、256 件を超えると古いものから消えます
- スレッドは起動した時点の関数を使います。関数の定義（中間コード）は、SSP からの `request` と全てのスレッドで共有します。式を計算している途中の値は、関数を呼び出すたびに別に持つので、**同じ関数を複数のスレッドが同時に実行してもかまいません**（自分自身を再帰で呼んでも同じです）。スレッドを起動するときに辞書の大きさに応じたメモリや時間はかからないので、同時に何本動かしても、増えるのはそのスレッドが使う分だけです（2 万関数・2.5MB の辞書で、起動に約 2ms、ワーカー 1 本あたりのメモリ増加は 0.1MB 未満）
- `fncdepth` と `looplimit` の値は起動時の設定が引き継がれます

### 制限
- ワーカーが動いている間は、辞書や関数を変える [DICLOAD](DICLOAD.md)、[DICUNLOAD](DICUNLOAD.md)、[APPEND_RUNTIME_DIC](APPEND_RUNTIME_DIC.md)、[UNDEFFUNC](UNDEFFUNC.md) は警告 W0032 を出して失敗します。[EVAL](EVAL.md) は使えます
- ワーカーが出した警告やエラーのログは、ファイルにはその場で書かれますが、SSP やチェックツールへは次の `request` の中でまとめて送られます（SHIORI のコールバックは、`request` を呼んだスレッドで呼ぶ約束のため）
- ワーカーの中の `GETLASTERROR`、`LSO`、`RE_GETSTR` などは、スレッドごとに保たれます

### unload と中断
`unload` が来ると、動いているワーカーすべてに中断を求め、5 秒まで終わるのを待ちます。ワーカーは次の文の切れ目で、`return` と同じ形で関数を抜けます（[SLEEP](SLEEP.md) の待ちはすぐ戻ります）。それでも終わらないスレッド（時間のかかるシステム関数の中など）は、最後の手段として強制停止し、警告 W0034 を出します。Windows 以外では強制停止ができないため、通信などで待っているスレッドは見捨てて進みます（辞書の関数を実行中のスレッドは、終わるまで待ち続けます）。

!!! warning "ワーカーで長く止まる関数を使わない"
    強制停止はスレッドの途中の状態を壊しうる手段です。時間のかかる処理は、`for` / `while` で小さく区切るか、`SLEEP` を挟んで書いてください。そうすれば [THREADSTOP](THREADSTOP.md) や `unload` で安全に止まります。

## Example
2 つのスレッドを起動して、両方の終わりを待ち、返り値を受け取ります。

```
Work.Add
{
	_argv[0] + _argv[1]
}

Work.Both
{
	_a = THREADSTART('Work.Add', 1, 2)
	_b = THREADSTART('Work.Add', 10, 20)
	_r = THREADJOIN(_a)
	_r = THREADJOIN(_b)
	TOSTR(THREADRESULT(_a)) + ',' + TOSTR(THREADRESULT(_b))   // 3,30
}
```

## Compatibility
- Tc608-1以降
- Tc608-2: スレッドごとの関数表のコピーをやめ、全スレッドで共有するようにした（Tc608-1 では、2 万関数・2.5MB の辞書で、起動に約 18ms、ワーカー 1 本あたり約 13MB かかっていた）。同じ関数を複数のスレッドが同時に実行できる

## See Also
- THREADSTATE
- THREADSTOP
- THREADJOIN
- THREADRESULT
- THREADCLOSE
- SLEEP
- DIRECTSSTP
