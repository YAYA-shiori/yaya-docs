# THREADSTATE
**Category:** スレッド

## Signature
```
THREADSTATE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) が返したスレッドの ID |

## Returns
スレッドの状態を表す整数。

| 値 | 意味 |
|----|------|
| -1 | その ID のスレッドがない（[THREADCLOSE](THREADCLOSE.md) で捨てた、または古い記録が消えた） |
| 0 | 実行中（実行の順番待ちを含む） |
| 1 | 関数を最後まで実行して終わった |
| 2 | 中断された（[THREADSTOP](THREADSTOP.md)、[THREADCLOSE](THREADCLOSE.md)、unload） |
| 3 | エラーで終わった（強制停止したスレッドを含む） |

引数が足りない・整数でないときは、警告 W0008 / W0009 を出して -1 を返します。

## Description
スレッドが動いているか、終わったかを調べます。待たずにすぐ戻るので、`OnSecondChange` などで繰り返し確かめる使い方に向きます。終わるまで待ちたいときは [THREADJOIN](THREADJOIN.md) を使います。

!!! note "SSP の応答を止めないために"
    ホストの `request` の中で [THREADJOIN](THREADJOIN.md) を長く待つと、SSP の応答が止まります。SSP に返す処理では、`THREADSTATE` で確かめて、終わっていなければ次の機会に回してください。

## Example
```
OnSecondChange
{
	if THREADSTATE(work.id) == 1 {
		'終わりました: ' + TOSTR(THREADRESULT(work.id))
	}
}
```

## Compatibility
- Tc608-1以降

## See Also
- THREADSTART
- THREADJOIN
- THREADRESULT
