# FREADTOML
**Category:** ファイル操作

## Signature
```
FREADTOML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要读取的 TOML 文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| charset | 文件的字符编码（可省略）。可指定为字符串（`"UTF-8"` `"Shift_JIS"` 等。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时使用 UTF-8（TOML 规范规定使用 UTF-8） |

## Returns
- 成功时：转换 TOML 后得到的哈希（参见下方的[值的对应关系](#値の対応)）
- 失败时：空值（VOID）

## Description
读取并解析整个 TOML 文件，将其转换为哈希后返回。无需使用 [FOPEN](FOPEN.md) 打开文件。

TOML 由 YAYA 自行解析。支持 [TOML v1.0.0](https://toml.io/ja/v1.0.0)。也接受 v1.1 新增的内联表中的换行和末尾逗号，以及 `\e` `\xHH` 转义。

- 忽略开头的 UTF-8 BOM。换行符可以是 CRLF 或 LF
- 最顶层始终为哈希。空文件或只有注释的文件会得到空哈希
- 对于规范禁止的写法，例如重复定义相同的键或表、用 `[表]` 重新定义由点分隔键创建的表、之后再向内联表添加内容等，会报错

### 值的对应关系

| TOML | YAYA |
|------|------|
| 表（`[table]`・内联表 `{ }`・点分隔键 `a.b = 1`） | 哈希 |
| 表数组（`[[array]]`） | 哈希的通用数组 |
| 数组 | 通用数组（可以嵌套包含数组或哈希的元素） |
| 字符串（`"..."` `'...'` `"""..."""` `'''...'''`） | 字符串 |
| 整数（`42` `1_000` `0xDEAD` `0o755` `0b1101`） | 整数 |
| 实数（`3.14` `5e+22` `inf` `nan`） | 实数 |
| `true` / `false` | 整数 1 / 0 |
| 日期时间（`1979-05-27T07:32:00Z`、`1979-05-27`、`07:32:00` 等） | 按原样写入的字符串 |

- 超出整数范围（-2^63 以上、2^63 以下）的整数会报错
- 键的顺序不会保留，而是按哈希键的顺序排列（参见 [HASH_KEYS](HASH_KEYS.md)）

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 无法打开文件 | W0025 | 25 |
| 无法作为 TOML 解析 | W0026（也会输出行号和原因） | 26 |

## Example
config.toml：
```toml
# ゴーストの設定
title = "設定"
updated = 2026-09-27T12:00:00+09:00

[ghost]
name = "さくら"
age = 17
visible = true
tags = ["ghost", "shell"]
path = 'C:\ssp\ghost'

[[friends]]
name = "うにゅう"

[[friends]]
name = "まゆら"
```

```
_t = FREADTOML("config.toml")
_t["title"]                 // 設定
_t["updated"]               // 文字列の 2026-09-27T12:00:00+09:00
_t["ghost"]["name"]         // さくら
_t["ghost"]["visible"]      // 1
_t["ghost"]["tags"][1]      // shell
_t["ghost"]["path"]         // C:\ssp\ghost
_t["friends"][1]["name"]    // まゆら

foreach _t["friends"]; _f {
    // _f に {name: うにゅう}、{name: まゆら} のハッシュが順に入る
}
```

## Compatibility
- YAYA：Tc602-5及以后
- Tc603-1：传入未知字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按 OS 默认编码处理）

## See Also
- [PARSETOML](PARSETOML.md)
- [FWRITETOML](FWRITETOML.md)
- [FREADJSON](FREADJSON.md)
- [FREADYAML](FREADYAML.md)
- [嵌套值与多维赋值](../grammar/13-nesting.md)
