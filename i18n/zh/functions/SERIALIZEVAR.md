# SERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SERIALIZEVAR( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 变量名的字符串。以 `_` 开头时为局部变量，否则为全局变量 |

## Returns
将变量的值转换为与存档文件中相同格式的字符串。

变量不存在、值为 VOID，或者变量已通过 [ERASEVAR](ERASEVAR.md) 删除时，会发出警告 W0012 并返回 VOID。

## Description
将指定变量的值转换为与 [SAVEVAR](SAVEVAR.md#保存形式) 写入存档文件时相同格式的字符串。将其传递给 [DESERIALIZEVAR](DESERIALIZEVAR.md) 后，可以将相同的值恢复到另一个变量中。

存档文件的一行格式为 `变量名,值,"分隔符",watcher|setter|destorier`，但此函数返回的**只有值的部分**。不包含变量名、分隔符、watcher / setter / destorier 以及字符编码的指定。

与 JSON 不同，它能保留整数与实数、整数键与字符串键、VOID 与空字符串等之间的区别。嵌套数组和哈希也会以 `IARRAY{...}` / `IHASH{...}` 的形式原样写出。

返回的字符串为单行，换行等控制字符会进行转义。

## Example
```
a = 5
b = "x,y"
c = (1, "x", 2.5)
d = IHASH("k", 1)

SERIALIZEVAR("a")   // 5
SERIALIZEVAR("b")   // "x,y"（ダブルクォートを含む）
SERIALIZEVAR("c")   // 1:"x":2.5
SERIALIZEVAR("d")   // "k"=1:IHASH=IHASH
```

也可以指定局部变量。

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_s = SERIALIZEVAR("_x")   // IHASH{"k"=1:IHASH=IHASH}:"s"
```

## Compatibility
- Tc607-3以降

## See Also
- DESERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- DUMPJSON
