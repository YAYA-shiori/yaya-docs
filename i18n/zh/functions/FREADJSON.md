# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset [, key ...]] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| path | 要读取的 JSON 文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| charset | 文件的字符编码（可省略）。以字符串（如 `"UTF-8"`、`"Shift_JIS"`；参见[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值指定。省略时为 UTF-8 |
| key | 要提取的键（可省略，可指定任意多个；Tc608-6 及以后版本）。如果顶层是对象，则只返回这些键的值（[指定键读取](#キーを指定して読む)）。只能是字符串。指定时也要写 `charset`（如 `"UTF-8"`） |

## Returns
- 成功时: 转换 JSON 得到的值（参见下方的[值的对应关系](#値の対応)）
- 失败时: 空（VOID）

## Description
读取并解析整个 JSON 文件，将其转换为哈希、数组等值并返回。无需事先用 [FOPEN](FOPEN.md) 打开文件。

JSON 解析使用 [parson](https://github.com/kgabis/parson)。

- 忽略开头的 UTF-8 BOM
- 可以写 `/* */` 和 `//` 注释（虽然不符合 JSON 标准，但允许用于配置文件等场景）
- 顶层不必是对象或数组（也可以读取只有 `123` 或 `"abc"` 的文件）

### 值的对应关系

| JSON | YAYA |
|------|------|
| 对象 | 哈希 |
| 数组 | 通用数组（元素中可以包含数组或哈希，形成嵌套结构） |
| 字符串 | 字符串 |
| 数值（整数值） | 整数 |
| 数值（其他） | 实数 |
| `true` / `false` | 整数 1 / 0 |
| `null` | 空（VOID） |

- 数值在内部按实数解析，因此即使带有小数点，如 `1.0`，只要值为整数就会转换为整数。此外，超过 2^53 的整数可能存在误差。超出整数范围（-2^63 以上、2^63 以下但不含 2^63）的值会转换为实数
- 对象的键不会保持原有顺序，而是按哈希的键顺序排列（数值 < 字符串）（参见 [HASH_KEYS](HASH_KEYS.md)）
- `"1"` 和 `"01"` 等在 YAYA 哈希中不视为相同的键会保留为不同的键。`"1"` 等标准形式的整数字符串键可以通过 `h[1]` 或 `h["1"]` 访问
- 值为 `null` 的键也会保留在哈希中。[HASH_EXIST](HASH_EXIST.md) 返回 1

### 指定键读取
指定 `key` 后，如果顶层是对象，则只将这些键的值放入哈希并返回（Tc608-6 及以后版本）。虽然会解析整个 JSON 文件，但结果转换（字符串转换和哈希创建）只针对指定的键进行，因此只使用大型 JSON 的一部分时速度更快，结果也更小。

- 只能指定顶层的键。不能用 `.` 指向下层（`"a.b"` 指的是名称中包含 `.` 的键）
- 文件中不存在的键不会在结果哈希中创建。值为 `null` 的键与转换整个文件时一样，以 VOID 值保留
- 如果顶层不是对象，则不使用 `key`，而是转换整个文件
- 也可以通过数组传递键（作为函数参数时，外层数组会展开）

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串；key 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 无法打开文件 | W0025 | 25 |
| 无法解析为 JSON | W0026 | 26 |

## Example
data.json:
```json
{
  "name": "さくら",
  "age": 17,
  "tags": ["ghost", "shell"],
  "profile": { "height": 158.5, "visible": true, "memo": null }
}
```

```
_j = FREADJSON("data.json")
_j["name"]                  // さくら
_j["tags"][1]               // shell
_j["profile"]["height"]     // 実数の 158.5
_j["profile"]["visible"]    // 1

foreach _j["tags"]; _t {
    // _t に "ghost"、"shell" が順に入る
}

_j = FREADJSON("data.json", "UTF-8", "name", "tags")   // Tc608-6 以降。このキーだけのハッシュ
_j["name"]                  // さくら
HASH_EXIST("age", _j)       // 0（取り出していない）
```

## Compatibility
- YAYA: Tc601-1 及以后版本
- Tc602-1: 修复了在小数点为 `,` 的区域设置（如德语）环境中解析包含小数的 JSON 失败的问题
- Tc603-1: 传入未知的字符编码名称时，发出警告 W0012 并返回失败（此前会将其视为操作系统默认编码，不发出警告）
- Tc608-6: 可以在 `charset` 后指定要提取的键

## See Also
- [FREADJSONL](FREADJSONL.md)
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [值的嵌套与多维赋值](../grammar/13-nesting.md)
