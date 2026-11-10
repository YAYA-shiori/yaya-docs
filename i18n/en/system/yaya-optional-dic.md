# yaya_optional.dic

## Overview

`yaya_optional.dic` is a system dictionary containing supplemental utility functions that are not required but are useful to have. It is loaded automatically along with `shiori3.dic` ([yaya_shiori3.dic](./yaya-shiori3-dic.md)). It provides functions for manipulating Sakura Script tags, formatting strings, initializing balloons, and detecting ghosts (FMO), among other things.

## SHIORI3FW.EscapeDangerousTags

```
SHIORI3FW.EscapeDangerousTags( script )
```

Disables (escapes) “dangerous” Sakura Script tags in a string. It escapes only the backslash in tags that perform dangerous operations (such as starting a browser or mailer, or switching to passive mode) to `\\`, leaving safe tags unchanged.

The tags currently considered “dangerous” are as follows.

- Tags containing any of the following strings inside `\![]`: `updatebymyself` / `vanishbymyself` / `enter,passivemode` / `leave,passivemode` / `lock,repaint` / `unlock,repaint` / `biff` / `open,browser` / `open,mailer` / `raise`
- The `\j[]` tag

| Argument | Description |
|------|------|
| `script` | The string to disable |

Returns the disabled string.

```
_safe = SHIORI3FW.EscapeDangerousTags(外部から受け取ったテキスト)
```

## SHIORI3FW.EscapeAllTags

```
SHIORI3FW.EscapeAllTags( script )
```

Escapes “all” Sakura Script tags in a string. Anything that begins with `\` is escaped. Use this when you want to display user input directly in a balloon, for example.

| Argument | Description |
|------|------|
| `script` | The string to escape |

Returns the escaped string.

```
_display = SHIORI3FW.EscapeAllTags('\0\s[0]これはタグではなくテキストです。\e')
// → "\\0\\s[0]これはタグではなくテキストです。\\e" として表示される
```

[SHIORI3FW.RemoveAllTags](./yaya-shiori3-dic.md#shiori3fwremovealltags) **deletes** tags, while this function **escapes and displays** them.

## SHIORI3FW.TranslateSystemChar

```
SHIORI3FW.TranslateSystemChar( text [ , 置換文字 ] )
```

Replaces YAYA system-reserved characters, such as operators and delimiters, with the specified character. This is useful when you want to create a safe string that can be used as a variable name or identifier.

| Argument | Description |
|------|------|
| `text` | The text to process |
| `置換文字` | The replacement character (defaults to `_` if omitted) |

```
_varname = SHIORI3FW.TranslateSystemChar('hello world!')
// → "hello_world_"

_varname = SHIORI3FW.TranslateSystemChar('foo/bar', '-')
// → "foo-bar"
```

## String Formatting

These functions are useful when you want to align the display width of items such as menus in a balloon. Character counts are specified in **half-width character equivalents** (one full-width character = two half-width characters).

| Function | Description |
|------|------|
| `SHIORI3FW.MakeLongText(テキスト, 文字数)` | If the text is shorter than the specified number of half-width character equivalents, pads the end with spaces to match the length. If it is already at least that long, returns the original text unchanged |
| `SHIORI3FW.MakeShortText(テキスト, 文字数)` | If the text exceeds the specified number of half-width character equivalents, truncates the end and appends `...` or `..`. If it is within the specified length, returns the original text unchanged |
| `SHIORI3FW.MakeJustText(テキスト, 文字数)` | Combines the two functions above to format text to exactly the specified number of half-width character equivalents |

```
_item  = SHIORI3FW.MakeJustText('設定', 20)
_short = SHIORI3FW.MakeShortText('これはとても長いテキストです', 10)   // "これは..." のように切り詰められる
```

## SHIORI3FW.InitBalloons

```
SHIORI3FW.InitBalloons()
```

Generates Sakura Script that clears the balloons of all currently active scopes. Use this to reset balloons at once in a multi-scope environment. It takes no arguments and returns a Sakura Script string formed by concatenating `\p[n]\c\b[-1]` for all scopes.

```
OnMyEvent
{
	SHIORI3FW.InitBalloons + '\0\s[0]初期化しました。\e'
}
```

## FMO-Related Functions

FMO (File Mapping Object) is the shared memory managed by SSP that contains “information about currently running ghosts.” The following functions let you check whether other ghosts are present and retrieve their information.

### SHIORI3FW.IsGhostExist

```
SHIORI3FW.IsGhostExist( name [ , fmoname ] )
```

Uses FMO to check whether a ghost with the specified name (\0 name) is currently running. Because it uses FMO, it retrieves the information available at the moment the function is called. Internally, it calls `SHIORI3FW.RefreshFMOTable`.

| Argument | Description |
|------|------|
| `name` | Ghost name |
| `fmoname` | The FMO name to check (optional; defaults to `Sakura` if omitted. Usually, you can omit it) |

Returns 1 if the ghost is running, or 0 if it is not.

```
if SHIORI3FW.IsGhostExist('ゆっくり霊夢') {
	'\0\s[0]霊夢がいるよ！\e'
}
```

### SHIORI3FW.RefreshFMOTable

```
SHIORI3FW.RefreshFMOTable( [ fmoname [ , hwnd ] ] )
```

Uses the [READFMO](../functions/READFMO.md) function to build FMO as an easy-to-process string array. FMO contains information about “currently running” ghosts, so this function lets you retrieve information about running ghosts in real time. If the FMO contents have not changed since the previous call, parsing is skipped (cached).

| Argument | Description |
|------|------|
| `fmoname` | The FMO name to read (optional; defaults to `Sakura` if omitted. The Unicode version is `SakuraUnicode`. Usually, you can omit it) |
| `hwnd` | The window handle of the ghost to ignore (optional; defaults to `SHIORI3FW.HWnd[0]` if omitted. Usually, you can omit it) |

This function has no return value, but builds the following global variables. These variables are automatically deleted when SHIORI exits.

Ghosts started “temporarily” (such as SSTPVIEWER or dummy entries) are automatically excluded from the FMO table.

#### SHIORI3FW.FMOTable

The format is a simple array, delimited by commas and `|`. In SSP, all fields are populated, but some fields may be absent (empty) in other baseware. It is also unavailable on operating systems other than Windows.

```
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
...
```

| Field | Meaning |
|------|------|
| `id` | The ID representing the ghost. Usually a string that is not useful to know |
| `name` | \0 name |
| `keroname` | \1 name |
| `hwnd` | The \0 window handle |
| `kerohwnd` | The \1 window handle |
| `path` | The ghost's installation directory (usually the location of `ssp.exe`, but SSP can have multiple ghost installation locations) |
| `ghostpath` | The ghost's base directory, where `install.txt` and `thumbnail.png` are located |

#### SHIORI3FW.SakuraNameList

This is a generic array containing only the \0 names extracted from the data above. For example, you can easily select one running ghost at random and get its name by using `ANY(SHIORI3FW.SakuraNameList)`.

```
// 起動中の全ゴースト名を列挙する例
SHIORI3FW.RefreshFMOTable
_list = SHIORI3FW.SakuraNameList
_n = ARRAYSIZE(_list)
for _i = 0; _i < _n; _i++ {
	// _list[_i] にさくら名が入っている
}
```

#### SHIORI3FW.FMOCache

The raw FMO data read on the previous call (for caching). It is rarely referenced directly.

#### Notes

Normally, information about the current ghost is not included in the variables above (because `SHIORI3FW.HWnd[0]` is specified for `hwnd`). To include the current ghost, set `hwnd` to -1 or another value.

## SHIORI3FW.HTTPCodeToMessage

```
SHIORI3FW.HTTPCodeToMessage( コード )
```

Converts an HTTP status code returned by a network update or similar operation into a Japanese error message. Returns an empty string if there is no matching code.

| Code | Return value |
|--------|--------|
| `'403'` | `'アクセス拒否'` |
| `'404'`、`'410'` | `'ファイル無し'` |
| `'500'`、`'502'`、`'503'` | `'サーバ側の不調'` |
| `'timeout'` | `'タイムアウト'` |
| `'fileio'` | `'ファイル書き込みエラー'` |
| `'artificial'` | `'手動中断'` |

```
OnNetworkUpdateComplete
{
	if reference[1] != '200' {
		_msg = SHIORI3FW.HTTPCodeToMessage(reference[1])
		'\0\s[0]更新に失敗しました：%(_msg)\e'
	}
}
```

## Related

- [yaya_shiori3.dic](./yaya-shiori3-dic.md)
- [System dictionary function manual (yaya-dic)](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
