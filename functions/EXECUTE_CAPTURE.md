# EXECUTE_CAPTURE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_CAPTURE( path [, option [, dir [, options ]]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 実行するファイルのパス。[EXECUTE_WAIT](EXECUTE_WAIT.md) と同じく、相対パスは信頼性が低いため、絶対パスの使用を推奨。PATH にあるコマンド名も指定できる |
| option | プログラムに渡す引数（省略可）。[EXECUTE_WAIT](EXECUTE_WAIT.md) と同じ |
| dir | 起動するプロセスの作業ディレクトリ（省略可）。[EXECUTE_WAIT](EXECUTE_WAIT.md) と同じ。省略するか空文字列なら指定しない |
| options | 動作を指定するハッシュ（省略可）。[IHASH](IHASH.md) で作る。下の表のキーを使う。キーを省いたものは既定の動作になる |

### options のキー

| キー | 値 | 意味 |
|------|----|------|
| stdin | 文字列 | プログラムの標準入力に渡す内容。省略すると、何も渡さずにすぐ入力の終わりになる（入力を待ち続けるプログラムも止まらない） |
| stderr | `"separate"` / `"merge"` / `"discard"` | 標準エラー出力の扱い。`"separate"`（既定）は標準出力とは別に取り込む。`"merge"` は標準出力に混ぜる（出力された順のまま `stdout` に入り、`stderr` は空）。`"discard"` は捨てる |
| timeout | 整数（ミリ秒） | この時間で終わらなければ、プログラムを終了させて戻る。0（既定）は無制限 |
| maxsize | 整数（バイト） | `stdout`・`stderr` それぞれの上限。超えたらプログラムを終了させて戻る。既定は 16777216（16MiB）、指定できる最大は 1073741824 |
| charset | 文字コードの名前または数値 | `stdin` の文字列を渡すとき、`stdout`・`stderr` を文字列にするときの文字コード（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。省略または空文字列なら OS の既定（Windows は ANSI コードページ、POSIX は UTF-8）。path・option・dir には影響しない |

値が VOID のキーは、指定していないものとして扱う。

## Returns

次のキーを持つハッシュ。

| キー | 値 |
|------|----|
| exitcode | プログラムの終了コード。終了を確認できなかったとき（`"failed"`、プログラムが終わる前の `"timeout"` / `"canceled"` / `"truncated"`）は -1。POSIX 環境でシグナルにより終了したときも -1 |
| stdout | 標準出力の内容（文字列） |
| stderr | 標準エラー出力の内容（文字列）。`stderr` オプションが `"merge"` / `"discard"` のときは空 |
| status | 終わり方。下の表を参照 |

| status | 意味 |
|--------|------|
| ok | プログラムが終了した（終了コードが 0 でなくても `"ok"`） |
| timeout | `timeout` の時間で終わらなかったので終了させた |
| canceled | [THREADSTOP](THREADSTOP.md) や unload でスレッドの中断を求められたので終了させた |
| truncated | `stdout` か `stderr` が `maxsize` を超えたので終了させた。内容は `maxsize` までに切り詰める |
| failed | 起動できなかった（実行ファイルが見つからない、作業ディレクトリがない、など）。引数やオプションが不正なときも `"failed"` を返す |

`timeout` / `canceled` / `truncated` のときも、それまでに取り込んだ出力は `stdout` / `stderr` に入る。

## Description

外部のプログラムを起動し、終了を待って、標準出力・標準エラー出力を取り込みます。標準入力に文字列を渡すこともできます。ほかの言語の `subprocess.run`（Python）、`Open3.capture3`（Ruby）、`execFileSync`（Node.js）にあたる関数です。

```
_r = EXECUTE_CAPTURE('cmd.exe', '/c ver')
if _r['status'] == 'ok' && _r['exitcode'] == 0 {
	_r['stdout']
}
```

標準入力に渡して、結果を受け取る例です。

```
_in = 'b' + CHR(13,10) + 'a' + CHR(13,10)
_r = EXECUTE_CAPTURE('sort.exe', '', '', IHASH('stdin', _in))
_r['stdout']       // "a" と "b" が並ぶ
```

標準エラー出力を標準出力に混ぜ、10 秒で打ち切る例です。

```
_r = EXECUTE_CAPTURE('tool.exe', '--run', '', IHASH('stderr', 'merge', 'timeout', 10000))
```

### EXECUTE_WAIT との違い

- **シェルの関連付けは使いません**。文書や URL を既定のアプリケーションで開くことはできません（それには [EXECUTE_WAIT](EXECUTE_WAIT.md) や [EXECUTE](EXECUTE.md) を使います）。Windows は実行ファイルを直接起動し（`CreateProcess`）、`path` を `"` で囲んだものに `option` を続けたコマンドラインを渡します。`.bat` / `.cmd` も起動できますが、`option` にスクリプトの外から来た文字列を混ぜないでください。POSIX は `/bin/sh -c` に渡します。実在するファイルは 1 つの名前として扱い、無ければシェルのコマンドとして PATH から探します
- Windows ではコンソールの窓を開きません
- 標準出力・標準エラー出力はパイプで受け取るので、プログラムによっては、端末につながっているときと出力の仕方（バッファリングなど）が変わります
- 改行は変換しません。Windows のプログラムの出力は `CRLF` のままです
- 出力に NUL（`\0`）が含まれていると、そこで文字列が終わります
- 起動できなかったときは警告を出さず、`status` が `"failed"` のハッシュを返します

### 待っている間の動き

- 待つ間は、[THREADSTART](THREADSTART.md) のスレッドや SSP からの `request` が止まりません（[EXECUTE_WAIT](EXECUTE_WAIT.md) と同じ）
- スレッドが [THREADSTOP](THREADSTOP.md) や unload で中断を求められると、**プログラムを終了させて**から `"canceled"` で戻ります。[EXECUTE_WAIT](EXECUTE_WAIT.md) は Windows でも起動したプログラムをそのままにしますが、こちらは終了させます。POSIX でも中断できます
- 終了させるとき、POSIX はプログラムが作ったプロセスグループごと（`sh -c` が起動した子プロセスも）終了させます。Windows は起動したプロセスだけを終了させ、そのプロセスが起動した別のプロセスは終了させません
- プログラムが終わった後に、別のプロセスが標準出力・標準エラー出力を握り続けていることがあります（`start` や `&` で起動した常駐プログラムなど）。そのときは、出力が途切れてから 0.5 秒で読むのをやめ、`"ok"` で戻ります。そのプロセスが後から出力する分は取り込めません。出力が途切れずに続く間も、`timeout` の時間がたつか中断を求められれば、`"timeout"` / `"canceled"` で戻ります（プログラム自身は終わっているので、`exitcode` は返ります）
- 標準入力への書き込みと、標準出力・標準エラー出力の読み出しは並行して行うので、大きな入力と大きな出力を同時に扱ってもプログラムと互いに待ち合うことはありません

### エラー

| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| path がない | W0008 | 8 |
| path・dir・options・オプションの値の型が不正 | W0009 | 9 |
| `stderr` / `timeout` / `maxsize` / `charset` の値が不正 | W0012 | 12 |
| `stdin` を指定の文字コードに変換できない | W0027 | 27 |
| 出力を文字列にできない（その出力は空になる） | W0027 | 27 |
| options に知らないキーがある（つづりの間違いに気づけるよう警告する。ほかのキーは有効で、実行は続ける） | W0012 | 12 |

path などが不正で警告を出したときも、`status` が `"failed"` のハッシュを返します。

## Compatibility

- Tc608-3: 追加

## See Also

- [EXECUTE_WAIT](EXECUTE_WAIT.md)
- [EXECUTE](EXECUTE.md)
- [IHASH](IHASH.md)
- [THREADSTART](THREADSTART.md)
