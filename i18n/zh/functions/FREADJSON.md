# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要读取的 JSON 文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| charset | 文件的字符编码（可省略）。可指定为字符串（`"UTF-8"` `"Shift_JIS"` 等。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时使用 UTF-8 |

## Returns
- 成功时：转换 JSON 后得到的值（参见下方的[值的对应关系](#値の対応)）
- 失败时：空值（VOID）

## Description
读取并解析整个 JSON 文件，将其转换为哈希、数组等值后返回。无需使用 [FOPEN](FOPEN.md) 打开文件。

JSON 解析使用 [parson](https://github.com/kgabis/parson)。

- 忽略开头的 UTF-8 BOM
- 允许使用 `/* */` 和 `//` 注释（虽然不符合 JSON 规范，但为了便于在配置文件等场景中使用而允许）
- 最顶层不必是对象或数组（也可以读取内容只有 `123` 或 `"abc"` 的文件）

### 值的对应关系

| JSON | YAYA |
|------|------|
| 对象 | 哈希 |
| 数组 | 通用数组（可以嵌套包含数组或哈希的元素） |
| 字符串 | 字符串 |
| 数值（整数值） | 整数 |
| 数值（其他） | 实数 |
| `true` / `false` | 整数 1 / 0 |
| `null` | 空值（VOID） |

- 数值在内部会以实数形式解析，因此即使有小数点（如 `1.0`），只要值为整数，就会变成整数。此外，超过 2^53 的整数可能会有误差。超出整数范围（-2^63 以上、2^63 以下）的值会变成实数
- 对象的键顺序不会保留，而是按哈希键的顺序（数值 < 字符串）排列（参见 [HASH_KEYS](HASH_KEYS.md)）
- `"1"` 和 `"01"` 这类在 YAYA 的哈希中不被视为相同键的键，会作为不同的键保留。对于 `"1"` 这类规范形式的整数字符串键，既可以通过 `h[1]` 也可以通过 `h["1"]` 获取
- 值为 `null` 的键也会保留在哈希中。[HASH_EXIST](HASH_EXIST.md) 会返回 1

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 无法打开文件 | W0025 | 25 |
| 无法作为 JSON 解析 | W0026 | 26 |

## Example
data.json：
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
```

## Compatibility
- YAYA：Tc601-1及以后
- Tc602-1：修复了在小数点为 `,` 的区域设置（如德语）环境下，无法解析包含小数的 JSON 的问题
- Tc603-1：传入未知字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按 OS 默认编码处理）

## See Also
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [嵌套值与多维赋值](../grammar/13-nesting.md)
