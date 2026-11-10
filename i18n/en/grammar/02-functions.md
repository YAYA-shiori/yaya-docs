# Functions

## Overview

A “function” in YAYA is

- a piece of processing that takes zero or more arguments, and
- selects and returns one output from zero or more “output candidates.”

It is a collection of operations.

The number of arguments is stored in the variable `_argc`, and each argument is stored in the variable `_argv[n]`. Here, n is the argument number, starting from 0.

An output candidate is a collection of items without an lvalue (the left side of `=`), such as strings, numbers, or variable names written directly in a function. If there are multiple output candidates, YAYA selects one of them as the function’s output (return value).

Having multiple functions with the same name causes an error (take particular care when modifying an existing ghost).

The following “basic structure” describes a “function” in YAYA as a generic-language DLL. If this is unclear, you can skip this section.

## Basic structure

The following shows the complete program code for a program that returns the string `"Hello World"` when `request` is executed.

```
request
{
    "Hello World"
}
```

When a module that has loaded YAYA executes `HGLOBAL request(HGLOBAL h, long *len)`, this script runs and `"Hello World"` is returned. The same applies to `load` and `unload`. However, `load` and `unload` do not return a value, so writing an output string has no effect. Write initialization code in `load`, such as setting initial values for variables, and write code in `unload` to clean up afterward.

You only need to write the functions you need; you can omit the rest. For example, the code above does not include `load` or `unload`, but this does not cause an error; they simply do nothing. In the extreme case, no error occurs even if there are no dictionary files at all. In this case, `load` and `unload` do nothing, and `request` returns an empty string.

`load` and `request` each take one argument, which can be retrieved through variables. The variable names are `_argc` and `_argv`, similar to the interface of the C language `main` function.

### _argc

The number of arguments. In `load` and `request`, there is one argument, a string, so this is 1. `unload` takes no arguments, so this value is 0.

### _argv

Stores the actual arguments. It is an array with `_argc` elements, and each element is accessed using the `[i]` operator. The ordinal i is zero-based. For example, if `_argc` is 1, `_argv[0]` can be used, and the argument is stored there.

To summarize the basics, the following program code stores `"Hello"` in the variable `str` in `load`, then concatenates the string passed as an argument to `request` with `str` and returns the result.

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

If you execute `request` with `"World"` as the string to be processed, the result is `"Hello World!"`.

## Syntax

The following rules apply.

- Blank lines (lines containing only a newline), text after `//`, and regions enclosed by `/*` and `*/` are treated as comments
- If a line ends with a slash (`/`), the next line is joined to the end of that line
- Whitespace characters can be freely placed at the beginning of a line and between words. Whitespace characters are spaces and tabs
- To write multiple statements on one line, separate them with semicolons (`;`)

In other words, the Hello World code shown earlier can be written on one line as follows.

```
request{"Hello World"}
```

The following also works (although this style is not recommended).

```
req/
uest          {
"/
Hello World"  }
```

Whitespace at the beginning of the line after `/` (the line being joined) is treated as indentation and removed. Therefore, the result of joining the following strings is `"ABCDEFG"`, not `"ABCD　　EFG"`.

```
"ABCD/
    EFG"
```

Regarding the fourth rule: the following `request` calculates 1+2 and returns the result as a Japanese sentence.

```
request
{
    answer = 1 + 2
    "答えは" + answer + "です。"
}
```

Using a semicolon, you can write it as follows.

```
request
{
    answer = 1 + 2; "答えは" + answer + "です。"
}
```

There is no problem with writing more semicolons than necessary. They are ignored and do not affect execution. Therefore, if you are used to C language syntax, you can write a semicolon at the end of every line.

## Defining and executing user-defined functions

You can create functions with any name in addition to `load`, `unload`, and `request`. A created function can be executed simply by writing its name.

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

The example above is the simplest case, and `request` returns `"Hello World"` as a result. Here is a slightly more complex example that produces the same result.

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

If you put `( )` after a function name and list values inside them, separated by commas, those values are treated as arguments passed to the corresponding function. In other words, the values are stored in the variables `_argv` and `_argc` and can be referenced within that function. In the example shown here, `_argc` is 2, `_argv[0]` is `"Hello"`, and `_argv[1]` is `"World"` within the `combine` function.

### Names that cannot be used for function names

You can choose function names freely, but names that conflict with any of the following rules cause an error.

- Starts with a digit from 0 to 9
    - It may be interpreted as a numeric constant
- Starts with an underscore (`_`)
    - Names starting with an underscore are used for local variables
- Contains any of the following characters: whitespace　`!`　`"`　`#`　`$`　`%`　`&`　`(`　`)`　`*`　`+`　`,`　`-`　`/`　`:`　`;`　`<`　`=`　`>`　`?`　`@`　`[`　`]`　`` ` ``　`{`　`|`　`}`　`~`
    - It is best not to use symbols other than the underscore
- Exactly matches a reserved word
    - Uppercase letters and underscores are used for system functions
    - Avoid names used for control structures, such as `for`, `while`, and `if`

### Recursive Calls

Functions can call themselves recursively. The following example demonstrates the most common case: calculating a factorial.

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

## Selection Modes

```
request
{
    "Hello World"
    "こんにちは世界"
    "Hallo Welt"
}
```

When listed this way, these are treated as equally likely "output candidates," and one of them is output. You can specify one of the following selection modes. However, `void` and `array` / `pool_array` are used only for special purposes.

| Mode | Description |
|------|------|
| Unspecified / `random` | Select one at random (default) |
| `nonoverlap` | Avoid selecting the same candidate as immediately before, if possible |
| `sequential` | Output candidates in the order written, then return to the beginning after the last one |
| `array` | Return a generic array containing all output candidates |
| `void` | Output nothing |
| `all` (Tc567-1) | Join all candidates into a single string |
| `last` (Tc567-1) | Select the last candidate |

Specify a selection mode by adding it after the function name, as in `: nonoverlap`.

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

The number of output candidates can vary each time some functions are executed. For example, the following function has either 2 or 4 candidates, depending on the value of the variable `i`.

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

If the number of candidates changes, the cycling order for `nonoverlap` and `sequential` is reset and starts over. Only in this case, the same value as the previous one may be output again.

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

Note that this means "output nothing," not "execute nothing." Functions and expressions written inside the block are still processed.

```
increment_i : void
{
    i++
    i
}
```

The function `increment_i` above adds 1 to `i`. Without `void`, this function returns the result of the addition, but with `void` specified, it returns no value and only performs the addition.

### all

Implemented in Tc567-1. Joins all selection candidates into a single string.

### last

Implemented in Tc567-1. Selects the last candidate as the output from among the selection candidates.

## Modifiers

**`_pool`**: Selects the candidates in blocks inside the block marked with `_pool` at the same level as the outer candidates. It can be applied to the function itself (`OnTest : _pool`) or to a block (`_pool : {`).

Normally, a nested block counts as a single candidate as a whole. In the example below, `"x"` has a 1/2 chance, while `"y"` and `"z"` each have a 1/4 chance:

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

With `_pool`, the candidates in the inner block are separated, so `"x"`, `"y"`, and `"z"` each have a 1/3 chance:

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

- This applies regardless of nesting depth (if you add `"z"` and `"w"` at the third level, all four candidates have a 1/4 chance each)
- The contents of `if`, `elseif`, and `else` blocks are also separated. Candidates in blocks that do not execute because their conditions are false are not added. If you write `if condition { "b" "c" }`, `"b"` and `"c"` are selected with the same probability as the outer candidates only when the condition is true
- Candidates inside `while`, `for`, and `foreach` are added one at a time for each iteration (if a `for` loop runs twice, `"y"` inside it counts as two candidates)
- A block with a selection mode, such as `nonoverlap : {`, is not separated and remains a single candidate
- To combine this with a selection mode, write `_pool_nonoverlap` or `_pool_sequential` (the `_` can be omitted). If no mode is specified, it is `random_pool` (you can also write just `pool`), which selects randomly. You can also write `nonoverlap_pool`, `sequential_pool`, or `array_pool`. Duplicate avoidance and selection order apply to all candidates after they have been separated
- When applied to a block, this applies only to the contents of that block. Candidates in the outer block count the block as a single candidate
- `_pool` and `melt_` cannot both be specified for the same block or function

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

When `is_rainy` is true, the three lines are selected with equal probability, without being repeated consecutively. When it is false, only `"通常のセリフ"` is selected.

**`melt_`**: Uses a generic array to produce a parallel-output effect. When applied to a block, if the output selected in that block is a generic array, its elements are separated and added to the output candidates of the immediately outer block (the same effect as [`parallel`](05-arrays.md)). It can be combined with a selection mode, as in `melt_nonoverlap`. It is also inherited by inner blocks that do not specify a selection mode.

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

When applied to the function itself, there is no outer block, so the generic array candidates are separated before selection (Tc574-9 / Tc603-2 and later). Generic arrays returned with `return` are not separated.

```
OnTest : melt_nonoverlap
{
    "test"
    "test2"
    ("red","green","blue")
}
```

Result: Selection without repetition from the same five candidates as above.

Up to Tc574-8 / Tc603-1, `melt_` applied to the function itself had no effect, and a generic array remained a single candidate. Also, `melt_` applied to a block two or more levels inside the function added its candidates to the outermost block of the function, rather than to the immediately outer block.

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

`{ }` can be nested to any depth. They work the same way as the top-level `{ }`: one of the enclosed candidates is selected and output. However, the only selection method available is random selection; you cannot specify `nonoverlap` or `sequential` as you can for the top level. (From Tc564-1 onward, you can specify the selection method using “Selection Methods in Nested Blocks” below.)

In the example above, you might think the result would be the same whether or not `{ }` were present, but that is not the case. Without `{ }`, each candidate has an equal probability of 1/3 of being output. In the example above, however, first one of `"Hello World"` and `"こんにちは世界"` is selected, and then the result is combined with the remaining `"Hallo Welt"` to select the output. In other words, `"Hello World"` and `"こんにちは世界"` each have a 1/4 chance of appearing, while `"Hallo Welt"` has a 1/2 chance.

### Selection Methods in Nested Blocks

From Tc564-1 onward, you can add the selection method described in the previous section to each nested block.

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

To specify a method for `{ }` immediately following an `if` statement or similar, either separate them with `;` as shown below or add a line break.

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

`--` is an output finalizer. It divides the selection candidates into groups, and the results selected from each group are combined into a single string. Therefore, executing the `request` above outputs one of the following.

```
"Hello World"
"Perfect World"
"Peaceful World"
"Hello Worth"
"Perfect Worth"
"Peaceful Worth"
```

Write `--` on a line by itself. You cannot write it on one line as in `"Hello" / "Perfect" -- …`; `/` is interpreted as division.

When used in combination with `nonoverlap`, `sequential`, or `array`, it operates on all possible combinations of values the function can take (rather than on a per-group basis).

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

produces output in the following order:

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

outputs the generic array `("1A","1B","2A","2B","3A","3B")`.

YAYA can handle numbers and other types in addition to strings, but the output finalizer converts them all to strings when combining them, then concatenates them as strings.
