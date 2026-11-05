# THREADRESULT
**Category:** スレッド

## Signature
```
THREADRESULT( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) が返したスレッドの ID |

## Returns
スレッドの関数の返り値。

次の場合は空の値（VOID）を返します。

- スレッドがまだ動いている
- 中断された・エラーで終わった（[THREADSTATE](THREADSTATE.md) が 2 か 3）
- その ID のスレッドがない

引数が足りない・整数でないときは、警告 W0008 / W0009 を出して空の値を返します。

## Description
正常に終わったスレッドの関数が返した値を受け取ります。関数が複数の候補を持つとき（ランダムに選ばれる出力）は、終わるときに選ばれた 1 つです。

返り値を受け取らずに、グローバル変数へ書く方法もあります。[THREADSTART](THREADSTART.md) を参照してください。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
THREADRESULT(_id)   // 7
```

## Compatibility
- Tc608-1以降

## See Also
- THREADSTART
- THREADJOIN
- THREADSTATE
