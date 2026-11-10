# DUMPJSON
**Category:** 型取得/変換

## Signature
```
DUMPJSON( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | 要转换为 JSON 的值。哈希和数组（包括嵌套结构）也可以作为一个参数传入 |
| pretty | 为 1 时添加换行和缩进进行格式化。省略时为 0（输出为一行） |

## Returns
- 成功时：JSON 字符串
- 没有参数时：空字符串

## Description
将值转换为 JSON 字符串并返回。这是 [PARSEJSON](PARSEJSON.md) 的逆向转换。

### 值的对应关系

| YAYA | JSON |
|------|------|
| 哈希 | 对象。键会转换为字符串（`1` 会变为 `"1"`）。顺序与哈希键的顺序相同 |
| 通用数组 | 数组 |
| 整数 | 数值。64 位整数也能无误地写出 |
| 实数 | 数值。始终附带小数点或指数（`1.0`、`0.1`、`1e+300`） |
| 字符串 | 字符串 |
| 空（VOID） | `null` |

- 整数 1 / 0 会变为数值 `1` / `0`，不会变成 `true` / `false`
- 实数会使用能够在读回后还原为相同值的最短表示形式。NaN 和无穷大无法用 JSON 表示，因此会变为 `null`
- 字符串只会对 `"`、`\` 和控制字符（换行、制表符等）进行转义。日语等非 ASCII 字符以及 `/` 会原样写出
- 小数点始终为 `.`，不受区域设置影响

格式化时使用 4 个空格缩进，换行符为 LF。空数组和空哈希会分别合并为 `[]` / `{}`。

使用 [PARSEJSON](PARSEJSON.md) 读回后可以还原为原值。不过，值为整数的实数（`1.0`）会变成整数。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |

## Example
```
_h = IHASH()
_h["name"] = "さくら"
_h["tags"] = ("ghost", "shell")
_h["height"] = 158.5

DUMPJSON(_h)
// {"height":158.5,"name":"さくら","tags":["ghost","shell"]}

DUMPJSON(_h, 1)
// {
//     "height": 158.5,
//     "name": "さくら",
//     "tags": [
//         "ghost",
//         "shell"
//     ]
// }

DUMPJSON(("a", 1))          // ["a",1]
DUMPJSON(未定義の変数)       // null
```

## Compatibility
- YAYA：Tc602-1 及之后
- Tc602-5：修复了整数的最小值（-9223372036854775808）仅输出为 `-`、导致生成无效 JSON 的问题

## See Also
- [FWRITEJSON](FWRITEJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [DUMPXML](DUMPXML.md)
