# TRANSLATE
**Category:** 文字列操作

## Signature
```
TRANSLATE( text, format_from, format_to )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| text | String to be replaced |
| format_from | List of characters to replace (with formatting; see below) |
| format_to | List of replacement characters. Specify an empty string to delete characters |

## Returns
- Success: Replaced string
- Failure: -1

## Description
Replaces strings character by character at high speed. Provides functionality equivalent to Perl's tr/// (without options).

### Format

**Simple enumeration**: Maps characters one to one. Characters not in the list are not changed.
```
TRANSLATE('ぬるぽガッ', 'ぽガ', 'りゴ') // 'ぬるりゴッ'
```

**Range specification**: Use "-" to specify a character code range for bulk replacement. The character code used is UCS-2 (Unicode), so you can check it by switching your IME's character palette to Unicode mode.
```
TRANSLATE('123456789', '1-9', '①-⑨') // '①②③④⑤⑥⑦⑧⑨'
```

**Escaping**: Use `\-` for a literal hyphen and `\\` for a literal backslash.

```
TRANSLATE('\-\-\-', '\\', '\-') // '------'
```

**Deletion**: If the third argument is an empty string, the matching characters are deleted.
```
TRANSLATE('46cm三連装砲', '0-9a-z', '') // '三連装砲'
```

## Example

Convert hiragana to katakana and katakana to hiragana.

```
_wokyu = TRANSLATE('ティータイムは大事にしないとネー', 'ぁ-ゖァ-ヶ', 'ァ-ヶぁ-ゖ')
// _wokyu の中身 = てぃーたいむハ大事ニシナイトねー
```

The Unicode table specifies the overlapping range of katakana and hiragana, 「ァ-ヶ」. If the dictionary is written in Shift_JIS, 「ゖ」 will be garbled; in that case, write it as follows.

```
_wokyu = TRANSLATE('ティータイムは大事にしないとネー', 'ぁ-んァ-ン', 'ァ-ンぁ-ん')
```

## Compatibility

- YAYA: Tc546-1 and later
- Tc546-2: Added escape sequences
- Tc547-1: Added deletion processing (specifying an empty string for the third argument)

## See Also
- ZEN2HAN
- HAN2ZEN
- REPLACE
