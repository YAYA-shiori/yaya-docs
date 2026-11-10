# Expanding Embedded Elements in Strings

## Overview

You can embed variables and functions in a string and insert their results at the corresponding positions. There are two types of embedding: “scoped expansion” and “longest-name-match expansion.”

## Scoped Expansion

Enclose an element in `%( )` to embed it.

```
request
{
    _i = "pen"
    "This is a %(_i)."
}
```

Executing `request` outputs `"This is a pen."`. `%( )` behaves like eval (interpreting a string as script code and executing it). You can embed not only a single function or variable, but also a mathematical expression.

```
request
{
    "1+2+3は%(1+2+3)です。"
}
```

`request` outputs `"1+2+3は6です。"`.

Double quotation marks cannot be included inside `%( )`. Therefore, you cannot embed a mathematical expression that contains a string. The following results in an error.

```
request
{
    "This is a %(_i = "pen")."
}
```

In such cases, concatenate the elements as a regular expression without using embedding.

```
request
{
    "This is a " + (_i = "pen") + "."
}
```

Controlling the order of operations with parentheses `( )` works the same way with scoped expansion. See the following example.

```
request
{
    "遊星「%(_i = planet)」は遠い。この遊星は%(color(_i))色をしている。"
}

planet
{
    "mars"
    "saturn"
    "pluto"
}

color
{
    case _argv[0] {
    when "mars";   "red"
    when "saturn"; "yerrow"
    when "pluto";  "blue"
    others;        "unknown"
    }
}
```

The deepest `( )` is the argument to `color(_i)`, so `color` is called before `_i = planet`. Since `_i` is still empty, the result is `"unknown"`. Add extra parentheses to adjust the order of operations.

```
"遊星「%((_i = planet))」は遠い。この遊星は%(color(_i))色をしている。"
```

This produces a consistent string.

**Features:**

- Supports complex expressions and mathematical operations
- Double quotation marks cannot be included in the string
- Since it is parsed statically when the dictionary is loaded, functions defined later with [DICLOAD](../functions/DICLOAD.md), for example, are not recognized. If you need to use such functions, consider using [EVAL](../functions/EVAL.md)

## Longest-Name-Match Expansion

Embedding also works with just `%`, without adding `( )`.

```
request
{
   o      = "pen"
   obj    = "eraser"
   object = "world"
   "This is a %object."
}

obje
{
    "television"
}
```

The target for expansion is the variable / function whose name is the longest match for the string after `%`. In the example above, the best match is the variable `object`, so it is selected. The result is `"This is a world."`.

Since variables are created and deleted over time, the target of expansion can change depending on the circumstances. This is a characteristic not found in scoped expansion.

```
request
{
   val   = "red"
   trans
   --
   value = "blue"
   trans
}

trans
{
    "%value"
}
```

`trans` is executed twice, but `"%value"` behaves differently on the first and second executions. The first time, it is interpreted as the variable `val` followed by `"ue"`; the second time, it is interpreted as the variable `value`. The output of `request` is `"redueblue"`.

### Reusing Expansion Results

You can reuse a previous expansion result using the `%[ ]` syntax.

```
request
{
    "「%planet」は遠い。「%city」も遠い。もっとも%[1]になら行けなくもない。"
}

planet
{
    "mars"
    "saturn"
    "pluto"
}

city
{
    "newyork"
    "moscow"
    "madrid"
}
```

`%[i]` retrieves the result of the i-th expansion, using a zero-based index. In the example above, `%[0]` refers to the result of expanding `%planet`, and `%[1]` refers to the result of expanding `%city`.

`%[ ]` cannot be used in scoped expansion. To reuse a previous result in scoped expansion, assign it to a variable.

### Speed

Expansion using longest-name matching searches for the target each time it runs, so it is dramatically slower than scoped expansion. Unless you really need this behavior, use scoped expansion in general.

### Resolving Names When Loading

Longest-name-match expansion searches for a name among the variables that exist at the time of execution. As a result, a string containing `%`, such as a URL, may suddenly have part of it replaced at some point.

```
"https://example.com/?p=100%off"  // 変数 o や of が作られると、その値に置き換わる
```

If you write `embed.lazy, off` in the configuration file (Tc604-1 or later), names following `%` without parentheses are resolved when the dictionary is loaded.

- The name is determined by the longest match among user-defined functions, system functions, and global variables whose names appear in dictionary expressions (including expressions executed with `EVAL`, etc.). Variables that were only restored from a save file, or created only with `LETTONAME`, are not included. To embed such variables, write `%(name)`
- If the resolved variable does not yet have a value, it becomes an empty string (it does not remain as `%name`)
- If no name matches, the text is treated as a string as-is, including `%`. Warning W0031 is issued for text beginning with an alphabetic character or a full-width character. No warning is issued for two-digit hexadecimal values such as `%E3` (URL encoding), or text beginning with a digit or symbol
- Local variables (`%_name`) continue to be resolved by name at runtime, as before
- The index of `%[i]` counts text that remains as a string as one result (the index does not change based on the `embed.lazy` setting)
