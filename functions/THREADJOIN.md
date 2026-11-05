# THREADJOIN
**Category:** スレッド

## Signature
```
THREADJOIN( id [, timeout ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) が返したスレッドの ID |
| timeout | 待つ時間の上限（ミリ秒）。省略すると終わるまで待つ |

## Returns
| 値 | 意味 |
|----|------|
| 1 | スレッドが終わった（すでに終わっていた場合を含む） |
| 0 | 時間切れで、まだ終わっていない |
| -1 | その ID のスレッドがない |
| -2 | 自分自身は待てない |

引数が足りない・整数でないときは、警告 W0008 / W0009 を出して -1 を返します。

## Description
スレッドが終わるまで待ちます。待っている間、ほかのスレッドは動けます。待っている側のスレッドが中断を求められたときも、待ちをやめて戻ります。

終わったあとの返り値は [THREADRESULT](THREADRESULT.md) で受け取ります。

!!! warning "ホストの request の中で長く待たない"
    SSP からの `request` の中で `THREADJOIN` を長く待つと、その間 SSP の応答が止まります。SSP のウィンドウの処理が止まるだけでなく、そのスレッドから送ろうとした通信（ワーカーが呼んだ [DIRECTSSTP](DIRECTSSTP.md) など）は、SSP が応答できず時間切れになります。短い `timeout` を付けるか、[THREADSTATE](THREADSTATE.md) で確かめる使い方にしてください。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id, 1000)
if _r == 1 {
	THREADRESULT(_id)   // 7
}
```

## Compatibility
- Tc608-1以降

## See Also
- THREADSTART
- THREADSTATE
- THREADRESULT
- THREADSTOP
