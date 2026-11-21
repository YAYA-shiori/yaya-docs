# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str [, key ...] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| str | JSON 字符串 |
| key | 要提取的键（可省略，可指定任意数量。Tc608-6 及以后版本）。如果顶层是对象，则只返回这些键的值（[指定键进行解析](#キーを指定して解析する)）。仅限字符串 |

## Returns
- 成功时：转换 JSON 得到的值
- 失败时：空（VOID）

## Description
解析 JSON 字符串，并将其转换为哈希、数组等值后返回。值的对应关系和注释的处理方式与 [FREADJSON](FREADJSON.md#値の対応) 相同。

用于处理从 SAORI 或外部接收的 JSON 字符串。从文件读取时，使用 [FREADJSON](FREADJSON.md)。

### 指定键进行解析
指定 `key` 时，如果顶层是对象，则只将这些键的值组成哈希返回（Tc608-6 及以后版本）。JSON 仍会被整体解析，但只需对指定的键进行结果转换（字符串转换和哈希创建），因此从包含长字符串或大型嵌套结构的 JSON 中只使用一部分时，速度更快，结果也更小。

- 只能指定顶层的键。不能用 `.` 指向下层（`"a.b"` 指的是名称中包含 `.` 的键）
- JSON 中不存在的键也不会在结果哈希中创建。值为 `null` 的键与整体转换时一样，以 VOID 值保留
- 如果顶层不是对象，则不使用 `key`，而是转换整体
- 也可以用数组传递键（在函数参数中，外层数组会被展开）
- 如果读取每行一个 JSON 的文件，使用 [FREADJSONL](FREADJSONL.md) 更快

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串。key 不是字符串 | W0009 | 9 |
| 无法解析为 JSON | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）

_j = PARSEJSON('{"a": 1, "b": [1, 2], "c": {"d": 4}}', "a", "c")   // Tc608-6 以降。このキーだけのハッシュ
_j["c"]["d"]                // 4
HASH_EXIST("b", _j)         // 0（取り出していない）
```

## Compatibility
- YAYA：Tc601-1 及以后版本
- Tc602-1：修复了在小数点为 `,` 的区域设置（如德语）环境中，解析包含小数的 JSON 时失败的问题
- Tc608-6：可以在 `str` 之后指定要提取的键

## See Also
- [FREADJSON](FREADJSON.md)
- [FREADJSONL](FREADJSONL.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
