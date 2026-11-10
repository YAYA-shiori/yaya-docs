# Regular Expressions

System functions whose names begin with `RE_` search, split, and replace strings using regular expressions. This page covers the basics of using regular expressions from YAYA, as well as subroutine calls available from Tc606-6 onward.

From Tc606-6 onward, the regular expression engine is the Ukagaka shared regular expression engine [uka_regexp](https://github.com/ukatech/uka_regexp). Its syntax and behavior are similar to PCRE2 (Perl Compatible Regular Expressions). **For details on the syntax (lookahead and lookbehind, Unicode properties, recursion, control verbs, and so on), see the [uka_regexp README](https://github.com/ukatech/uka_regexp/blob/main/README.md).** The basic patterns described on this page continue to work as before.

## Choosing a Function

| What you want to know | Function |
|---|---|
| Whether any part of a string matches | [RE_SEARCH](../functions/RE_SEARCH.md) |
| Whether the entire string matches | [RE_MATCH](../functions/RE_MATCH.md) |
| Find all matching parts | [RE_GREP](../functions/RE_GREP.md) |
| Split a string at matching parts | [RE_SPLIT](../functions/RE_SPLIT.md) |
| Replace matching parts | [RE_REPLACE](../functions/RE_REPLACE.md) (does not support `$1` and similar), [RE_REPLACEEX](../functions/RE_REPLACEEX.md) (supports them) |
| Find matching elements in an array | [RE_ASEARCH](../functions/RE_ASEARCH.md) (first match), [RE_ASEARCHEX](../functions/RE_ASEARCHEX.md) (all matches) |
| Check the matched content, position, and length | [RE_GETSTR](../functions/RE_GETSTR.md), [RE_GETPOS](../functions/RE_GETPOS.md), [RE_GETLEN](../functions/RE_GETLEN.md) |
| Change the matching options | [RE_OPTION](../functions/RE_OPTION.md) |

```
if RE_SEARCH(reference[0], 'こんに?ち[はわ]') {
  "こんにちは"
}
```

## Writing Patterns

Pass the pattern as a string. **Single quotes are recommended.** In double-quoted strings, `%(...)` and similar expressions are expanded as embedded expressions, while single-quoted strings do not expand them. In either type of string, `\` is passed directly to the regular expression, so you can write `\d`.

```
RE_SEARCH("abc123", '\d+')    // 1
```

### Basic Syntax

| Pattern | Meaning |
|---|---|
| `abc`、`あ` | The character itself. Special characters (`.` `*` `+` `?` `(` `)` `[` `]` `{` `}` `^` `$` `\|` `\`) represent themselves when preceded by `\` |
| `.` | Any single character except a newline |
| `[abc]`、`[a-z]`、`[^abc]` | A set of characters, a range, or anything outside the set |
| `\d` `\w` `\s` | Digits (`0-9`), word characters (`A-Za-z0-9_`), whitespace (spaces, tabs, newlines, and so on) |
| `\D` `\W` `\S` | Anything other than `\d` `\w` `\s` |
| `^`、`$` | The start and end of a string (or the start and end of a line with the `m` option) |
| `\b` | A word boundary |
| `*`、`+`、`?` | Repetition of 0 or more, 1 or more, or 0 or 1 times |
| `{3}`、`{2,4}`、`{2,}` | Repetition 3 times, 2–4 times, or 2 or more times |
| `*?`、`+?`、`??` | Repetition that matches as few characters as possible (lazy matching) |
| `a\|b` | `a` or `b` |
| `(...)` | A group. You can retrieve the matched content or use it in a replacement string |
| `(?:...)` | A non-capturing group |
| `(?<name>...)` | A named group |

!!! note "`\d` `\w` `\s` `\b` match ASCII only"
    `\d` does not match full-width digits, and `\w` does not match Japanese characters. To test for Japanese text, use Unicode properties. Hiragana uses `\p{Hiragana}`, katakana uses `\p{Katakana}`, and kanji uses `\p{Han}`.

    ```
    RE_SEARCH("あ", '\p{Hiragana}')            // 1
    RE_SEARCH("２０２４", '^\d+$')            // 0（全角の数字）
    RE_REPLACEEX("ひらがなカタカナ", '\p{Katakana}+', '[$0]')   // ひらがな[カタカナ]
    ```

These are not the only available syntax forms. For details on lookahead `(?=...)`, lookbehind `(?<=...)`, possessive quantifiers, atomic groups, `\Q...\E`, and so on, see the uka_regexp README.

### Options

Use [RE_OPTION](../functions/RE_OPTION.md) to set options that apply to subsequent regular expression functions. **No options are set by default.**

| Character | Meaning |
|---|---|
| `i` | Ignore case |
| `m` | Make `^` and `$` match the start and end of lines (treat the string as multiline) |
| `s` | Make `.` match newlines |
| `x` | Ignore whitespace in the pattern and treat everything from `#` to the end of the line as a comment |

```
RE_OPTION("im")
```

You can also specify options within a pattern. `(?i)` makes the rest of the pattern case-insensitive, while `(?i:...)` applies case-insensitivity only inside the parentheses. Use `(?-i)` to disable it.

```
RE_SEARCH("ABC", '(?i)abc')       // 1
RE_SEARCH("ABC", '(?i:a)BC')      // 1
```

By default, only LF (`\n`) is treated as a newline. To treat CR LF as a newline as well, write `(*ANYCRLF)` at the beginning of the pattern.

## Checking Matched Content

When a match is found, [RE_GETSTR](../functions/RE_GETSTR.md), [RE_GETPOS](../functions/RE_GETPOS.md), and [RE_GETLEN](../functions/RE_GETLEN.md) return the content, position (zero-based), and length as arrays. These values are overwritten when you next call a regular expression function.

```
_r = RE_SEARCH("abc123def", '(\d+)')
_s = RE_GETSTR()      // ("123", "123")
_p = RE_GETPOS()      // (3, 3)
_l = RE_GETLEN()      // (3, 3)
```

- Element 0 of the array is the part matching the entire pattern. Elements 1 and onward are the parts matching groups (`(...)`). Named groups are also listed in numerical order
- **Groups that did not participate in the match are not included in the array**, so later elements shift forward. When `(a)|(b)` is applied to `"a"`, only one additional element is returned (two in total: the whole match and `(a)`)
- [RE_GREP](../functions/RE_GREP.md) and [RE_SPLIT](../functions/RE_SPLIT.md) return one element for each matched part. RE_GREP returns the number of matches

```
_n = RE_GREP("a1b22c333", '\d+')   // 3
_s = RE_GETSTR()                   // ("1", "22", "333")
```

!!! warning "Discarding a return value makes it an output candidate"
    If you write `RE_SEARCH(...)` without using its return value, that value is added to the function's output candidates. When you only want to check the result, assign it to a variable, as in `_r = RE_SEARCH(...)`.

## Replacement

[RE_REPLACE](../functions/RE_REPLACE.md) uses the replacement string as-is. The replacement string for [RE_REPLACEEX](../functions/RE_REPLACEEX.md) supports the following patterns.

| Pattern | Meaning |
|---|---|
| `$0`、`$&` | The entire matched part |
| `$1`、`$2`、… | The first, second, and subsequent groups. `$10` and higher are read as two digits only if a group with that number exists |
| `${1}`、`${name}` | Specify a group by number or name (useful when digits follow the reference) |
| `` $` ``、`$'` | The text before or after the matched part |
| `$+` | The highest-numbered group that matched |
| `$_` | The entire original string |
| `$$` | A literal `$` |
| `\1`〜`\9` | Same as `$1`〜`$9` |
| `\\` `\n` `\r` `\t` `\a` `\e` `\f` `\v` | A backslash, newline, carriage return, tab, and other control characters |

Groups that did not participate in the match become empty strings.

```
RE_REPLACEEX("2024-05-17", '(\d+)-(\d+)-(\d+)', '$3/$2/$1')    // 17/05/2024
RE_REPLACEEX("abc", '(?<first>a)', '${first}-')               // a-bc
RE_REPLACEEX("aaaa", 'a', 'b', 2)                             // bbaa（2 回まで置換）
```

## Subroutine Calls (Tc606-6 onward)

You can call parts of a regular expression by name. Even if the pattern does not define a group such as `(?<date>...)`, YAYA **looks up that name in variables or functions and incorporates it as a pattern**.

You can write a call in any of the following ways (they all mean the same thing).

- `(?&name)`
- `(?P>name)`
- `\g<name>`、`\g'name'`
- `(?R<name>)`、`(?R'name')`

When using a form that contains `'` inside a single-quoted string, write it twice as `''` (`'^\g''name''$'`), or use a double-quoted string.

```
_date = '\d{4}-\d{2}-\d{2}'
_r = RE_SEARCH("今日は2024-05-17です", '(?&date)')     // 1
```

### Name Lookup

A name `name` that is not defined in the pattern is looked up in the following order. The first usable value found is used as a subpattern.

1. Local variable `_name` (if the name begins with `_`, the local variable with that name)
2. Global variable `name`
3. Function `name` (the return value of calling it with no arguments)

- **Strings and numbers** are usable values. VOID, arrays, and hashes cannot be used, so lookup continues to the next candidate
- If no candidate is found, or the incorporated value is an invalid pattern, a regular expression error (W0016) occurs
- If no variable is found, a function with the same name is called. To avoid calling a function unintentionally, **use a unique name for each subpattern so it does not overlap with other functions or variables**
- A subpattern can call other subpatterns. It can also call itself recursively
- Variable and function values are read again each time a regular expression function is called. Functions are called each time, so a function whose content changes randomly can produce a different pattern on each call
- If a named group defined in the pattern (`(?<name>...)`) has the same name, the definition takes precedence, and no variable or function is looked up

```
// 部品を関数で用意する
Digits4 { '\d{4}' }
Digits2 { '\d{2}' }

IsDate
{
  RE_MATCH(reference[0], '(?&Digits4)-(?&Digits2)-(?&Digits2)')
}
```

You can combine subpatterns to make long patterns easier to read.

```
_y = '\d{4}'
_m = '\d{2}'
_date = '(?&y)-(?&m)-(?&m)'
_r = RE_MATCH("2024-05-17", '(?&date)')     // 1
```

Recursion can be used to match nested structures. The following example matches strings with balanced parentheses.

```
_paren = '\((?:[^()]++|(?&paren))*\)'
_r = RE_MATCH("(a(b)c)", '(?&paren)')     // 1
```

!!! note "Groups inside subpatterns"
    A `(...)` written inside a subpattern disappears from the results when the call returns. Only groups in the calling pattern can be retrieved with functions such as [RE_GETSTR](../functions/RE_GETSTR.md). Also, options such as `(?i)` in the calling pattern are not inherited by subpatterns. They start with the options set by [RE_OPTION](../functions/RE_OPTION.md).

## Errors

| Situation | Result |
|---|---|
| The pattern syntax is invalid, or a subroutine name cannot be resolved | Warning W0016. Treated as no match (`GETLASTERROR` is 16) |
| The backtracking limit is exceeded, for example due to nested repetitions, or there is not enough memory | Warning W0017. Treated as no match (`GETLASTERROR` is 17) |

Patterns such as `(a+)+$`, which cause exponential growth in backtracking, can reach the limit when applied to long strings. When the limit is reached, the result is treated as no match and W0017 is issued.
