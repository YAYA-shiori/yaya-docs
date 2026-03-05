# HAN2ZEN
**Category:** 文字列操作
**Source:** マニュアル/関数/HAN2ZEN

## Signature
```
HAN2ZEN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 変換対象の文字列 |
| type | （省略可）変換する文字種をカンマ区切りで指定。省略時は全種類を変換する |

`type` に指定できる値:
| 値 | 対象 |
|----|------|
| `number` | 数字（0〜9） |
| `alphabet` | アルファベット |
| `symbol` | 記号など |
| `kana` | カタカナ・句読点等 |

## Returns
- 成功時: 変換後の文字列
- 失敗時: VOID

## Description
文字列内の半角英文字・数字・カタカナを全角に変換する。`type` で変換対象の文字種を絞り込むことができる。

## Example
```
_result = HAN2ZEN('2007ABC', 'number,alphabet')
// 結果: "２００７ＡＢＣ"
```

## Compatibility
- YAYA: TC513-901以降

## See Also
- ZEN2HAN
- TRANSLATE
