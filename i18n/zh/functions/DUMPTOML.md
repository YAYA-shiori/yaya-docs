# DUMPTOML
**Category:** 型取得/変換

## Signature
```
DUMPTOML( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | 要转换为 TOML 的哈希（可以包含嵌套结构）。TOML 的顶层是表，因此不能传入哈希以外的值 |
| pretty | 为 1 时使用 `[表]` 标题进行格式化；为 0 时每个顶层键占一行。省略时为 1 |

## Returns
- 成功时：TOML 字符串
- 失败时或没有参数时：空字符串

## Description
将哈希转换为 TOML 字符串并返回。这是 [PARSETOML](PARSETOML.md) 的逆向转换。

与 [DUMPJSON](DUMPJSON.md) / [DUMPXML](DUMPXML.md) 不同，省略 pretty 时会进行格式化（1）。

### 值的对应关系

| YAYA | TOML |
|------|------|
| 哈希 | 表。键仅包含字母数字字符、`_`、`-` 时会原样写出，否则会写为 `"..."`。顺序与哈希的键顺序相同 |
| 仅含哈希的通用数组 | 表数组（pretty 为 1 时使用 `[[名称]]`） |
| 通用数组 | 数组 |
| 整数 | 整数。64bit 整数也能无误差地写出 |
| 实数 | 实数。必须带小数点或指数（`1.0`、`0.1`、`1e+300`）。NaN 写为 `nan`，无穷大写为 `inf` / `-inf` |
| 字符串 | 字符串（见下文） |
| 空（VOID） | 不写出（TOML 没有 null，因此会省略对应的键） |

- 整数 1 / 0 会写为 `1` / `0`，不会写为 `true` / `false`
- 日期时间字符串（由 [FREADTOML](FREADTOML.md) 读取的字符串）也会作为字符串写为 `"..."` 
- 数组元素为空（VOID）时无法表示，因此会产生错误 W0027
- 小数点始终为 `.`，不受区域设置影响

字符串通常写为 `"..."`，并对 `"`、`\` 和控制字符进行转义。包含 `\` 且不含 `'` 和换行符的字符串（如 Windows 路径）会写为不转义的 `'...'`，以便阅读。

### 格式化形式（pretty 为 1）

- 按照表的键和值 → 下层表（`[a.b]`）→ 表数组（`[[a.c]]`）的顺序写出，并在表与表之间插入空行
- 不包含键和值、只包含下层表的表会省略标题（仅写出 `[a.b]` 也会定义 `a`）
- 包含换行符的字符串会写为多行 `"""..."""`
- 超过 80 个字符的数组，或包含数组、哈希元素的数组，会按每个元素一行的形式写出（缩进 4 个空格，并在每个元素后加逗号）
- 换行符为 LF，最后一行后也会添加换行符

pretty 为 0 时，每个顶层键占一行，下层哈希会写为内联表（`{ k = v }`），表数组会写为内联表数组。

使用 [PARSETOML](PARSETOML.md) 读回后会还原为原始值（省略空值的部分除外）。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| value 不是哈希，或数组元素中存在空值（VOID） | W0027（也会输出原因） | 27 |

## Example
```
_n = IHASH()
_n["title"] = "設定"
_n["ghost"] = IHASH("name", "さくら", "age", 17)
_n["ghost"]["shell"] = IHASH("name", "master")

DUMPTOML(_n)
// title = "設定"
//
// [ghost]
// age = 17
// name = "さくら"
//
// [ghost.shell]
// name = "master"

DUMPTOML(_n, 0)
// ghost = { age = 17, name = "さくら", shell = { name = "master" } }
// title = "設定"

DUMPTOML(("a", 1))          // 空文字列（警告 W0027）
```

## Compatibility
- YAYA: Tc602-5以降

## See Also
- [FWRITETOML](FWRITETOML.md)
- [PARSETOML](PARSETOML.md)
- [DUMPJSON](DUMPJSON.md)
- [DUMPYAML](DUMPYAML.md)
