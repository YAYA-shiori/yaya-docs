# TRANSLATE
**Category:** 文字列操作

## Signature
```
TRANSLATE( text, format_from, format_to )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| text | The string to replace characters in |
| format_from | The list of characters to replace (with formatting; see below) |
| format_to | The list of replacement characters. Specify an empty string to delete characters |

## Returns
- Success: The string after replacement
- Failure: -1

## Description
Replaces characters in a string quickly, one character at a time. It provides functionality equivalent to Perl's tr/// (with no options).

### Format

**Simple enumeration**: Maps characters one-to-one. Characters not in the list are unchanged.
```
TRANSLATE('ぬるぽガッ', 'ぽガ', 'りゴ') // 'ぬるりゴッ'
TRANSLATE('あああいいいううう', 'あい', 'おえ') // 'おおおえええううう'
```

**Range specification**: Use a hyphen to specify a range of character codes for replacement. The character codes used are UCS-2 (Unicode), so you can check them by switching the character palette in your IME to Unicode mode.
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

The range “ァ-ヶ” is specified because the Unicode tables have overlapping ranges for katakana and hiragana. If you write the dictionary in Shift_JIS, “ゖ” will appear garbled; in that case, write it as follows.

```
_wokyu = TRANSLATE('ティータイムは大事にしないとネー', 'ぁ-んァ-ン', 'ァ-ンぁ-ん')
```

## Compatibility

- YAYA: Tc546-1 and later
- Tc546-2: Added escape sequences
- Tc547-1: Added deletion (set the third argument to an empty string)

## See Also
- ZEN2HAN
- HAN2ZEN
- REPLACE
