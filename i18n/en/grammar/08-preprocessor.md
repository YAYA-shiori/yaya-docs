# Preprocessing

## Overview

Preprocessor commands that run when dictionary files are loaded.

## #define

Performs direct string substitution on the raw text of a dictionary file:

```
#define before after
```

Applies to all text after the declaration, through the end of that file. Substitutions are performed in the order they are declared, so write the substitutions that should be applied first before the others.

## #globaldefine

Similar to `#define`, but with a wider scope:

```
#globaldefine before after
```

Remains in effect across all dictionary files loaded afterward. Placing it at the beginning of the first dictionary file makes it effective across the entire project.

**Processing order:** Substitutions from `#define` are performed first, followed by substitutions from `#globaldefine`:

```
#globaldefine tea green
#define tea milk
"teacup"
```

Result: `"milkcup"` (`#define` takes precedence)

## \_\_AYA\_SYSTEM\_FILE\_\_

Available from YAYA Tc543-1 onward. Returns the path relative to the current file as seen by the DLL:

```
"__AYA_SYSTEM_FILE__"
```

Example: outputs `"aya_aitalk.txt"`

## \_\_AYA\_SYSTEM\_LINE\_\_

Available from Tc543-1 onward. Works like `__AYA_SYSTEM_FILE__` and returns the current line number in the file being executed.

## \_\_AYA\_SYSTEM\_FUNC\_\_

Available from Tc574-2 onward (for the 600 series, from Tc602-2 onward). When written inside a function, it is replaced with that function's name:

```
OnTest
{
	LOGGING("__AYA_SYSTEM_FUNC__: called")
}
```

Example: outputs `"OnTest: called"`

- Only text inside the function's `{` `}` is replaced. Function name disambiguation options (such as `:nonoverlap`) are not included
- It is replaced even when included in the replacement text of a `#define`, so it can be used in macros for logging
- It can also be used inside functions added with [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md)

## #ifdef / #ifndef / #elifdef / #elifndef / #else / #endif

Available from Tc574-2 onward (for the 600 series, from Tc602-2 onward). Switches whether part of a dictionary is loaded, depending on whether a name is defined:

```
#ifdef 名前
（名前が定義されていれば読み込む）
#elifdef 別の名前
（最初の名前が未定義で、別の名前が定義されていれば読み込む）
#else
（どれにも当てはまらなければ読み込む）
#endif
```

- `#ifndef` / `#elifndef` mean “if not defined”
- `#elifdef` / `#elifndef` / `#else` are optional. You can write any number of `#elifdef` / `#elifndef` directives
- They can be nested
- Leading whitespace is ignored, so you can indent them. They can also be used inside functions
- You can write a `//` comment at the end of a line
- You cannot write conditional expressions (there is no `#if`)

Lines in sections that are not loaded are not parsed. Calls to nonexistent system functions or syntax unknown to that version of YAYA do not cause errors. `#define` / `#globaldefine` directives in those sections are not registered either.

However, comments (`/* */`), line continuation using `/` at the end of a line, and here-documents are processed first. `#endif` and similar directives written inside a here-document are not treated as preprocessor directives.

### Names checked

| Name | Condition under which it is defined |
|---|---|
| Name of a `#define` | Defined earlier in that file |
| Name of a `#globaldefine` | Defined in a dictionary file loaded earlier (or earlier in the same file) |
| `__AYA_SYSTEM_YAYA5__` | YAYA 500 series |
| `__AYA_SYSTEM_YAYA6__` | YAYA 600 series |
| `__AYA_SYSTEM_SYSFUNC_function name__` | That system function exists (for example, `__AYA_SYSTEM_SYSFUNC_FREADJSON__`) |
| `__AYA_SYSTEM_FILE__` / `__AYA_SYSTEM_LINE__` / `__AYA_SYSTEM_FUNC__` | Always defined |

`__AYA_SYSTEM_YAYA5__` / `__AYA_SYSTEM_YAYA6__` / `__AYA_SYSTEM_SYSFUNC_function name__` are names used only for `#ifdef`-family checks; they do not replace text in the dictionary.

`#globaldefine` is affected by the loading order. `#globaldefine` directives in dictionary files loaded later are not visible.

### Dictionaries shared by the 500 and 600 series

Using syntax or functions added in the 600 series causes errors when loading in the 500 series (such as E0071 for calls to unknown functions). You can use `#ifdef` to write separate versions that do not cause errors in either series:

```
#ifdef __AYA_SYSTEM_YAYA6__
LoadConfig
{
	FREADJSON('config.json')
}
#else
LoadConfig
{
	// 500 系向けの代わりの処理
}
#endif
```

When writing separate versions based on whether a specific system function exists, use `__AYA_SYSTEM_SYSFUNC_function name__`. This can continue to be used as-is when functions are added in future versions:

```
#ifdef __AYA_SYSTEM_SYSFUNC_DUMPJSON__
	_s = DUMPJSON(_data)
#else
	_s = ''
#endif
```

Older versions of YAYA that do not recognize `#ifdef` (Tc574-1 and earlier, Tc602-1 and earlier) report error E0076 for lines such as `#ifdef`, and parse all the contents of the section. When distributing a shared dictionary, specify the YAYA versions it supports.

## #error / #warning

Available from Tc574-2 onward (for the 600 series, from Tc602-2 onward). Issues an error or warning when loading:

```
#ifndef __AYA_SYSTEM_YAYA6__
#error この辞書は YAYA 600 系（Tc602-2 以降）が必要です
#endif
```

- `#error` issues error E0104. This is a dictionary error, so the dictionary is loaded in emergency mode
- `#warning` issues warning W0028. Loading continues
- The text written after the directive is appended to the message (excluding any `//` comment at the end of the line)
- These directives do nothing in sections that are not loaded due to directives such as `#ifdef`

## Errors

| Number | Description |
|---|---|
| E0074 | A name is missing after an `#ifdef`-family directive, there are two or more names, or text follows `#else` / `#endif` |
| E0101 | `#elifdef` / `#elifndef` / `#else` / `#endif` has no corresponding `#ifdef` / `#ifndef` |
| E0102 | `#elifdef` / `#elifndef` / `#else` follows `#else` |
| E0103 | `#ifdef` / `#ifndef` is not closed with `#endif` (displays the line of the innermost `#ifdef`) |
| E0104 | `#error` |
| W0028 | `#warning` |
