# THREADCLOSE
**Category:** スレッド

## Signature
```
THREADCLOSE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) が返したスレッドの ID |

## Returns
| 値 | 意味 |
|----|------|
| 0 | 終わっているスレッドの記録を捨てた |
| 1 | まだ動いているので中断を求めた。終わったら記録を捨てる |
| -1 | その ID のスレッドがない |

引数が足りない・整数でないときは、警告 W0008 / W0009 を出して -1 を返します。

## Description
スレッドの記録（状態と返り値）を捨てます。動いているスレッドには [THREADSTOP](THREADSTOP.md) と同じ中断を求め、終わった時点で記録を捨てます。捨てたあとは、その ID を [THREADSTATE](THREADSTATE.md) などに渡すと -1 になります。

捨てなくても、終わったスレッドの記録は 256 件を超えると古いものから消えます。結果を使い終わったスレッドは、捨てておくと記録が残りません。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
_v = THREADRESULT(_id)
_r = THREADCLOSE(_id)
```

## Compatibility
- Tc608-1以降

## See Also
- THREADSTART
- THREADSTOP
- THREADSTATE
