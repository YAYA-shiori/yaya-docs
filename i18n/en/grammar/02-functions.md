# Functions

## Overview

In YAYA, a “function” is

- given zero or more arguments, and
- selects and returns one output from zero or more “output candidates”

a collection of operations.

The number of arguments is stored in the variable `_argc`, and each argument is stored in the variable `_argv[n]`. n is the argument index, starting at 0.

An output candidate is an item with no left-hand value (the left side of `=`), such as a string or number written directly in a function, or a variable name. If there are multiple output candidates, YAYA selects one of them as the function's output (return value).

Having multiple functions with the same name causes an error (be especially careful when modifying an existing ghost as a base).

The following “basic structure” describes a “function” in YAYA as a generic language DLL. If you are unsure what this means, you can skip this section.

## Basic structure

This shows the complete program code for returning the string `"Hello World"` when `request` is executed.

```
request
{
    "Hello World"
}
```

When a module that has loaded YAYA executes `HGLOBAL request(HGLOBAL h, long *len)`, this script runs and returns `"Hello World"`. The same applies to `load` and `unload`. However, `load` and `unload` do not return a value, so writing output strings has no effect. Write initialization code in `load`, such as setting initial values for variables, and write code in `unload` to perform cleanup.

You only need to write the functions you need; you can omit those you do not need. For example, the previous example does not include `load` or `unload`, but this does not cause an error; they simply do nothing. In an extreme case, no error occurs even if there are no dictionary files at all. In this case, `load` and `unload` do nothing, and `request` returns an empty string.

`load` and `request` each take one argument, which you can retrieve using variables. The variables are named `_argc` and `_argv`, similar to the interface of the C `main` function.

### _argc

The number of arguments. `load` and `request` each take one string argument, so this value is 1. `unload` takes no arguments, so this value is 0.

### _argv

Contains the actual arguments. It is an array with `_argc` elements, and you access each element using the `[i]` operator. The ordinal index i is zero-based. For example, if `_argc` is 1, you can use `_argv[0]`, which contains the argument.

To summarize the basics, here is program code that stores `"Hello"` in the variable `str` in `load`, then combines `str` with the string passed as an argument in `request` and returns the result.

```
load
{
    str = "Hello"
}

request
{
    str + " " + _argv[0] + "!"
}
```

If you execute `request` with `"World"` as the string to process, the result is `"Hello World!"`.

## Syntax

The following rules apply.

- Blank lines (lines containing only a newline), text after `//`, and regions enclosed by `/*` and `*/` are treated as comments
- If a line ends with a slash (`/`), the next line is joined to the end of that line
- You can put whitespace characters freely at the beginning of a line and between words. Whitespace characters are spaces and tabs
- To write multiple statements on one line, separate them with semicolons (`;`)

In other words, the Hello World code shown above can be written on one line as follows.

```
request{"Hello World"}
```

The following also works (though this style is not recommended).

```
req/
uest          {
"/
Hello World"  }
```

Whitespace at the beginning of the line after `/` (the line being joined) is treated as indentation and removed. Therefore, the following string concatenates to `"ABCDEFG"`, not `"ABCD　　EFG"`.

```
"ABCD/
    EFG"
```

Regarding the fourth rule: the following `request` calculates 1+2 and returns it as a Japanese sentence.

```
request
{
    answer = 1 + 2
    "答えは" + answer + "です。"
}
```

You can write it as follows using a semicolon.

```
request
{
    answer = 1 + 2; "答えは" + answer + "です。"
}
```

It is fine to use more semicolons than necessary. They are ignored and do not affect execution. Therefore, if you are used to C syntax, you can write a semicolon at the end of every line.

## Defining and executing user-defined functions

You can create functions with any name besides `load`, `unload`, and `request`. To execute a function you have created, simply write its name.

```
request
{
    hello
}

hello
{
    "Hello World"
}
```

This is the simplest example: `request` returns `"Hello World"` as a result. Here is a slightly more complex example that produces the same result.

```
request
{
    combine("Hello", "World")
}

combine
{
    _argv[0] + " " + _argv[1]
}
```

If you put `( )` after a function name and write comma-separated values inside, those values are treated as arguments passed to that function. In other words, the values are stored in the variables `_argv` and `_argc` and can be referenced inside the function. In this example, inside the `combine` function, `_argc` is 2, `_argv[0]` is `"Hello"`, and `_argv[1]` is `"World"`.

### Names that cannot be used for function names

You can choose function names freely, but names that conflict with the following rules cause an error.

- Begins with a digit from 0 to 9
    - It may be interpreted as a numeric constant
- Begins with an underscore (`_`)
    - Names beginning with an underscore are used for local variables
- Contains any of the following characters: whitespace　`!`　`"`　`#`　`$`　`%`　`&`　`(`　`)`　`*`　`+`　`,`　`-`　`/`　`:`　`;`　`<`　`=`　`>`　`?`　`@`　`[`　`]`　`` ` ``　`{`　`|`　`}`　`~`
    - It is best not to use symbols other than the underscore
- Exactly matches a reserved word
    - Uppercase letters followed by an underscore are used for system functions
    - Also avoid words used for control structures, such as `for`, `while`, and `if`

### Recursive Calls

Functions can be called recursively. The following is a common example that calculates a factorial.

```
request
{
    factorial(5)
}

factorial
{
    if !_argv[0]
        1
    else
        factorial(_argv[0] - 1)*_argv[0]
}
```

`request` returns 120.

## Selection Methods

```
request
{
    "Hello World"
    "こんにちは世界"
    "Hallo Welt"
}
```

When listed this way, these are treated as equally likely “output candidates,” and one of them is selected for output. You can specify one of the following selection methods. However, `void` and `array` / `pool_array` are used only for special purposes.

| Method | Description |
|------|------|
| Not specified / `random` | Select randomly (default) |
| `nonoverlap` | Avoid selecting the same candidate as the one immediately before, as much as possible |
| `sequential` | Output in the order written, returning to the first candidate after the last one |
| `array` | Return a generic array containing all output candidates |
| `void` | Output nothing |
| `all` (Tc567-1) | Combine all candidates into one string |
| `last` (Tc567-1) | Select the last candidate |

Specify the selection method by adding it after the function name, as in `: nonoverlap`.

```
request : nonoverlap
{
    "Hello World"
    "こんにちは世界"
    "Hallo Welt"
}
```

```
request : sequential
{
    "Hello World"
    "こんにちは世界"
    "Hallo Welt"
}
```

For some functions, the number of output candidates changes each time the function is run. For example, the following function has either 2 or 4 candidates, depending on the value of the variable `i`.

```
request : sequential
{
    if i {
        "1"
        "2"
    }
    "3"
    "4"
}
```

If the number of candidates changes, the rotation order for `nonoverlap` and `sequential` is reset and starts over from the beginning. Only in this case, the same value as the previous one may be output again.

### array

The function returns a generic array containing all output candidates.

```
request : array
{
    "This is a pen."
    ("A","B","C")
    3.14
}
```

The output is the generic array `("This is a pen.", "A", "B", "C", 3.14)`.

### void

Nothing is output. In the following example, `request` outputs none of the three candidates.

```
request : void
{
    "Hello World"
    "こんにちは世界"
    "Hallo Welt"
}
```

Note that this means “output nothing,” not “do nothing.” Functions and expressions written inside the block are still processed.

```
increment_i : void
{
    i++
    i
}
```

The function `increment_i` above adds 1 to `i`. Without `void`, this function returns the result of the addition, but with `void` specified, it returns no value and only performs the addition.

### all

Implemented in Tc567-1. Combines all selection candidates into one string.

### last

Implemented in Tc567-1. Selects the last candidate from the selection candidates as the output.

## Modifiers

**`_pool`**: Selects the candidates in blocks inside the block marked with `_pool` at the same level as the outer candidates. It can be applied to the function itself (`OnTest : _pool`) or to a block (`_pool : {`).

Normally, a nested block as a whole counts as one candidate. In the example below, `"x"` has a 1/2 probability, while `"y"` and `"z"` each have a 1/4 probability:

```
OnTest
{
  "x"
  {
    "y"
    "z"
  }
}
```

With `_pool` applied, the candidates in the inner block are separated, so `"x"`, `"y"`, and `"z"` each have a 1/3 probability:

```
OnTest : _pool
{
  "x"
  {
    "y"
    "z"
  }
}
```

- Candidates are separated no matter how deeply they are nested (if you add `"z"` and `"w"` at the third level, there will be four candidates, each with a 1/4 probability)
- The contents of `if`, `elseif`, and `else` blocks are also separated. Candidates in blocks that are not executed because their conditions are false are not added. If you write `if condition { "b" "c" }`, `"b"` and `"c"` are selected with the same probability as the outer candidates only when the condition is true
- Candidates inside `while`, `for`, and `foreach` loops are added one at a time on each iteration (if a `for` loop runs twice, `"y"` inside it counts as two candidates)
- A block with a selection method specified, such as `nonoverlap : {`, is not separated and remains a single candidate
- When combining this with a selection method, write it as `_pool_nonoverlap` or `_pool_sequential` (`_` can be omitted). If no method is specified, it is `random_pool` (you can also write just `pool`), which selects randomly. You can also write `nonoverlap_pool`, `sequential_pool`, or `array_pool`. Duplicate avoidance and ordering are applied to all candidates after they have been separated
- When applied to a block, it affects only the contents of that block. Candidates in the outer block count that block as a single candidate
- `_pool` and `melt_` cannot both be specified for the same block or function

The following example shows how the selection probabilities change depending on whether `_pool` is used. In the function below, without `_pool`, `"Hello World"` has a 50% probability, while `"こんにちは世界"` and `"Hallo Welt"` each have a 25% probability. If you write `: random_pool` (or just `_pool`), the three candidates each have a 33.3% probability. `if 1` is always true.

```
request : random
{
    "Hello World"
    if 1 {
        "こんにちは世界"
        "Hallo Welt"
    }
}
```

```
OnTest : _pool_nonoverlap
{
  "通常のセリフ"
  if is_rainy {
    "雨の日のセリフ1"
    "雨の日のセリフ2"
  }
}
```

When `is_rainy` is true, the three lines are selected with equal probability, without repeating consecutively. When it is false, only `"通常のセリフ"` is selected.

**`melt_`**: Uses a generic array to create a parallel output effect. When applied to a block, if the output selected in that block is a generic array, its elements are separated and added to the output candidates of the immediately outer block (the same effect as [`parallel`](05-arrays.md)). It can be combined with a selection method, as in `melt_nonoverlap`. It is also inherited by inner blocks that do not specify a selection method.

```
OnTest
{
    "test"
    "test2"
    melt_nonoverlap : {
        ("red","green","blue")
    }
}
```

Result: one of "test", "test2", "red", "green", or "blue".

When applied to the function itself, there is no outer block, so the generic array candidates are separated before selection (Tc574-9 / Tc603-2 and later). A generic array returned with `return` is not separated.

```
OnTest : melt_nonoverlap
{
    "test"
    "test2"
    ("red","green","blue")
}
```

Result: one of the same five candidates as above, selected without repetition.

Up to Tc574-8 / Tc603-1, `melt_` applied to the function itself had no effect, and the generic array remained a single candidate. Also, `melt_` applied to a block at least two levels inside was added to the candidates of the outermost function block, rather than the immediately outer block.

## Nesting

```
request
{
    {
        "Hello World"
        "こんにちは世界"
    }

    "Hallo Welt"
}
```

`{ }` can be nested hierarchically to any depth. Their behavior is the same as that of the outermost `{ }`: one of the contained candidates is selected and output. However, the only selection method available is random selection; you cannot specify `nonoverlap` or `sequential` as you can for the outermost level (from Tc564-1 onward, you can specify these using the “Selection Methods Within Nesting” section below).

In the example above, you might think the result would be the same whether or not `{ }` are present, but that is not the case. Without `{ }`, each item has an equal probability of 1/3 of being output. In the example above, however, one item is first selected from `"Hello World"` and `"こんにちは世界"`, and then the output is selected from that result and the remaining `"Hallo Welt"`. In other words, `"Hello World"` and `"こんにちは世界"` each have a 1/4 chance of appearing, while `"Hallo Welt"` has a 1/2 chance.

### Selection Methods Within Nesting

From Tc564-1 onward, you can add the selection methods described in the previous section to each nested block.

```
request
{
    nonoverlap : {
        "Hello World"
        "こんにちは世界"
    }

    "Hallo Welt"
}
```

To specify a selection method for `{ }` immediately following an `if` statement or similar, separate them with `;` as shown below, or add a line break.

```
request
{
    if 1 ; nonoverlap : {
        "Hello World"
        "こんにちは世界"
    }

    "Hallo Welt"
}
```

```
request
{
    if 1
    nonoverlap : {
        "Hello World"
        "こんにちは世界"
    }

    "Hallo Welt"
}
```

## Output Finalizer

```
request
{
    "Hello"
    "Perfect"
    "Peaceful"
    --
    " Wor"
    --
    "ld"
    "th"
}
```

`--` is an output finalizer that divides the candidates into groups at that point. The selected results from each group are then joined into a single string. Therefore, running the `request` above outputs one of the following.

```
"Hello World"
"Perfect World"
"Peaceful World"
"Hello Worth"
"Perfect Worth"
"Peaceful Worth"
```

`--` must be written on a line by itself. You cannot write it on the same line, as in `"Hello" / "Perfect" -- …`, because `/` is division.

When used together with `nonoverlap`, `sequential`, or `array`, it operates on all possible combinations the function can produce, not on a per-group basis.

For example, `sequential`:

```
request : sequential
{
    "1"
    "2"
    "3"
    --
    "A"
    "B"
}
```

produces output in the following order.

```
"1A" "2A" "3A" "1B" "2B" "3B" "1A" "2A" …
```

`array`:

```
request : array
{
    "1"
    "2"
    "3"
    --
    "A"
    "B"
}
```

outputs a generic array `("1A","1B","2A","2B","3A","3B")`.

YAYA can handle numbers and other types in addition to strings, but the output finalizer converts all of them to strings when joining them, and joins them as strings.
