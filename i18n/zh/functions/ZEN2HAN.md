# ZEN2HAN
**Category:** 文字列操作

## Signature
```
ZEN2HAN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要转换的字符串 |
| type | （可选）以逗号分隔指定要转换的字符类型。省略时转换全部字符 |

### type可指定的值
| 值 | 目标字符类型 |
|----|-----------|
| `number` | 数字（0〜9） |
| `alphabet` | 英文字母 |
| `symbol` | 符号、标点 |
| `kana` | 片假名及标点 |

## Returns
- 成功：转换后的字符串
- 失败：VOID

## Description
将字符串中的全角英数字和片假名转换为半角。可以通过 type 参数筛选转换对象的字符类型。

## Example
```
ZEN2HAN('２００７ABCアイウエオ', 'number,alphabet')
// "2007ABCアイウエオ" (数字と英字のみ変換、カタカナは変換しない)
```

## Compatibility
- YAYA: TC513-901 及之后

## See Also
- HAN2ZEN
- TRANSLATE
