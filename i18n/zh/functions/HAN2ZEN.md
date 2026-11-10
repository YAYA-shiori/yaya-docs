# HAN2ZEN
**Category:** 文字列操作

## Signature
```
HAN2ZEN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要转换的字符串 |
| type | （可选）以逗号分隔指定要转换的字符类型。省略时转换所有类型 |

`type` 可指定以下值：
| 值 | 对象 |
|----|------|
| `number` | 数字（0〜9） |
| `alphabet` | 英文字母 |
| `symbol` | 符号等 |
| `kana` | 片假名、标点等 |

## Returns
- 成功时：转换后的字符串
- 失败时：VOID

## Description
将字符串中的半角英文字母、数字和片假名转换为全角字符。可以通过 `type` 限定要转换的字符类型。

## Example
```
_result = HAN2ZEN('2007ABC', 'number,alphabet')
// 結果: "２００７ＡＢＣ"
```

## Compatibility
- YAYA：TC513-901 及之后

## See Also
- ZEN2HAN
- TRANSLATE
