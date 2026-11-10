# RE_SEARCH
**Category:** 正規表現

## Signature
```
RE_SEARCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to search |
| regexp | Regular expression pattern |

## Returns
- **1**: A matching portion was found
- **0**: No match

## Description
Checks whether any portion of the target string matches the regular expression. Use RE_MATCH to check whether the entire string matches exactly.

You can get details about the match using RE_GETSTR, RE_GETPOS, and RE_GETLEN.

## Example
```
if (RE_SEARCH(reference[0], 'こんに?ち[はわ]|今日[はわ]')){
  "こんにちは、%(username)"
}
```

This example returns a greeting if the user's input contains "こんにちは", "こんにちわ", or similar text. Opening an input box with `\![open,inputbox,OnTalk,0]` can help you create something like a conversation. This example responds when any of "こんにちは", "こんにちわ", "こんちは", "こんちわ", "今日は", "今日わ", "コンニチハ", or "コンニチワ" appears in the text (for example, in "こんにちはー、ほにゃらら") (when written as `'こんに?ち[はわ]|今日[はわ]|コンニチ[ハワ]'`).

As a tip, if you do the following, the ghost will always reply "そうかもしれない" when the text ends in `？` or `?` (for example, "元気？" or "ハンガーって美味しいよね?"), making it easier to sustain a conversation (although you should add more response patterns).

```
if (RE_SEARCH(reference[0], '(？|\?)$')){
    "そうかもしれない"
}
```

## Compatibility
- YAYA: Supported since the initial version
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular expressions](../grammar/14-regular-expressions.md))

## See Also
- RE_MATCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
