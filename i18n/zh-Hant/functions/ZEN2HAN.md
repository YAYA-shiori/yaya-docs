# ZEN2HAN
**Category:** 文字列操作

## Signature
```
ZEN2HAN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要轉換的字串 |
| type | （可省略）以逗號分隔指定要轉換的字元種類。省略時會全部轉換 |

### type 可指定的值
| 值 | 目標字元種類 |
|----|-----------|
| `number` | 數字（0〜9） |
| `alphabet` | 英文字母 |
| `symbol` | 符號與標點符號 |
| `kana` | 片假名與標點符號 |

## Returns
- 成功：轉換後的字串
- 失敗：VOID

## Description
將字串中的全形英數字與片假名轉換為半形。可以使用 type 參數篩選要轉換的字元種類。

## Example
```
ZEN2HAN('２００７ABCアイウエオ', 'number,alphabet')
// "2007ABCアイウエオ" (数字と英字のみ変換、カタカナは変換しない)
```

## Compatibility
- YAYA：Tc513-901 之後

## See Also
- HAN2ZEN
- TRANSLATE
