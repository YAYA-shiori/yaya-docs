# THREADSTOP
**Category:** スレッド

## Signature
```
THREADSTOP( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) が返したスレッドの ID |

## Returns
| 値 | 意味 |
|----|------|
| 1 | 中断を求めた |
| 0 | そのスレッドはすでに終わっている |
| -1 | その ID のスレッドがない |

引数が足りない・整数でないときは、警告 W0008 / W0009 を出して -1 を返します。

## Description
スレッドに中断を求めます。終わるのを待たずにすぐ戻ります。終わりを確かめるには [THREADSTATE](THREADSTATE.md) か [THREADJOIN](THREADJOIN.md) を使います。

スレッドは次の文の切れ目（`while` / `for` の周回の切れ目を含む）で、`return` と同じ形で今の関数を抜け、呼び出し元の関数も同じ形で抜けて、スレッドが終わります。[SLEEP](SLEEP.md) や [THREADJOIN](THREADJOIN.md) で待っているスレッドは、待ちを途中でやめて戻ります。中断されたスレッドの状態は 2 になり、[THREADRESULT](THREADRESULT.md) は空の値を返します。

システム関数 1 回の呼び出しの途中（大きな正規表現、`REQUESTLIB` など）では止まらず、その呼び出しが終わってから止まります。

## Example
```
OnClose
{
	_r = THREADSTOP(work.id)
	_r = THREADJOIN(work.id, 2000)   // 2 秒まで終わりを待つ
}
```

## Compatibility
- Tc608-1以降

## See Also
- THREADSTART
- THREADSTATE
- THREADJOIN
- THREADCLOSE
