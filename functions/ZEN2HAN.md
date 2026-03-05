# ZEN2HAN
**Category:** 文字列操作
**Source:** マニュアル/関数/ZEN2HAN

## Signature
```
ZEN2HAN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 変換する文字列 |
| type | （省略可）変換する文字種をカンマ区切りで指定。省略時はすべて変換 |

### typeに指定できる値
| 値 | 対象文字種 |
|----|-----------|
| `number` | 数字（0〜9） |
| `alphabet` | 英字 |
| `symbol` | 記号・句読点 |
| `kana` | カタカナおよび句読点 |

## Returns
- 成功: 変換後の文字列
- 失敗: VOID

## Description
文字列中の全角英数字・カタカナを半角に変換する。typeパラメータで変換対象の文字種を絞り込むことができる。

## Example
```
ZEN2HAN('２００７ABCアイウエオ', 'number,alphabet')
// "2007ABCアイウエオ" (数字と英字のみ変換、カタカナは変換しない)
```

## Compatibility
- YAYA: TC513-901 以降

## See Also
- HAN2ZEN
- TRANSLATE
