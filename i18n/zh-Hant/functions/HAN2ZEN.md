# HAN2ZEN
**Category:** 文字列操作

## Signature
```
HAN2ZEN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要轉換的字串 |
| type | （可省略）以逗號分隔指定要轉換的字元種類。省略時轉換所有種類 |

`type` 可指定的值：
| 值 | 對象 |
|----|------|
| `number` | 數字（0〜9） |
| `alphabet` | 英文字母 |
| `symbol` | 符號等 |
| `kana` | 片假名、標點符號等 |

## Returns
- 成功時：轉換後的字串
- 失敗時：VOID

## Description
將字串中的半形英文字母、數字及片假名轉換為全形。可透過 `type` 限定要轉換的字元種類。

## Example
```
_result = HAN2ZEN('2007ABC', 'number,alphabet')
// 結果: "２００７ＡＢＣ"
```

## Compatibility
- YAYA：TC513-901 以後

## See Also
- ZEN2HAN
- TRANSLATE
