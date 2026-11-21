# Cheat sheet

This quick reference summarizes YAYA syntax on one page. For detailed explanations, follow the links for each topic.

## How YAYA works

- A dictionary is a **collection of functions**. Define a function in the form `名前 { ... }`; if its name is an event name such as `OnBoot`, it becomes the response to that event.
- Each line containing an **expression or string** in a function becomes an output candidate. When the function is called, one candidate is randomly selected and returned. Statements such as assignments (`_a = 1`) are not candidates.
- Enclose strings in `"..."`. Sakura Script is also a string, so it must be enclosed.
- Variables have types (integer, real number, string, array, or hash). No declaration is needed. Names beginning with `_` are local variables.
- Neither statements nor variables can be written outside functions. Only preprocessor directives such as `#define` can be written outside them.
- Conditional expressions for `if` and `while` may be enclosed in parentheses, but do not have to be (`if (_a == 1)` and `if _a == 1` are equivalent). The entire header of `for` and `foreach` can also be enclosed in `( )` (Tc603-6 and later; this causes an error in earlier versions).
- Use half-width symbols (full-width symbols such as `（` and `＋` cannot be used).

## Writing functions

```
OnBoot
{
  _name = "さくら"
  "\0\s[0]こんにちは、%(_name)さん。\e"
  "\0\s[0]起動しましたね。\e"
}
```

- In the example above, either `"\0\s[0]こんにちは…"` or `"\0\s[0]起動しましたね。\e"` is returned at random (`_name = …` is not a candidate).
- There is **one candidate per line**. Placing candidates on the same line, as in `"a" "b"`, causes an error. The `/` in `"a" / "b"` means division, not a separator between candidates.
- Write `--` on a line by itself to treat the candidates before and after it as separate groups, select one from each, and concatenate them ([Functions](../grammar/02-functions.md)).
- You can write `{` on the same line as the function name or on the next line.
- Comments use `// 行末まで` and `/* 複数行 */`.
- Separate multiple statements on one line with `;` (`_a = 1 ; _b = 2`).

### Arguments and return values

| Syntax | Meaning |
|--------|------|
| `Func(1, "a")` | Call with arguments. For a call without arguments, `Func` alone is sufficient |
| `_argv[0]` `_argv[1]` | Received arguments (zero-indexed) |
| `_argc` | Number of arguments |
| `Func(&_v)` | Pass a variable by reference. Assigning `_argv[0] = 99` inside `Func` changes `_v` |
| `return` | End the function here. Return one of the candidates collected so far |
| `return 式` | **Discard all** candidates collected so far and return the value of the expression (Tc573-1 and later) |

### Selecting candidates

Add a selection method after the function name with `:` (`Seq : sequential`).

| Specification | Behavior |
|------|------|
| (none) | Select one candidate at random |
| `nonoverlap` | Do not select the same candidate twice in a row |
| `sequential` | Return candidates in order from the top, then return to the beginning |
| `array` | Return all candidates as a generic array |
| `void` | Execute the contents but return nothing |
| `all` | Return all candidates concatenated into one string (Tc567-1 and later) |
| `last` | Return the last candidate (Tc567-1 and later) |

In addition to the selection method, you can add the following modifiers.

| Specification | Behavior |
|------|------|
| `_pool` | Unpack candidates from inner blocks (including the contents of `if`) and select them with the same probability as outer candidates |
| `_pool_nonoverlap` `_pool_sequential` | Use nonoverlapping or sequential selection across all unpacked candidates |
| `melt_` | If the selected output is a generic array, unpack its elements and add them to the outer block's candidates |

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

- Without `_pool`, the inner `{ }` is a single candidate as a whole (the probability of `x` is 1/2, and that of `y` and `z` is 1/4 each). With `_pool`, `x`, `y`, and `z` each have a probability of 1/3.
- If an `if` condition is false, its contents are not added as candidates. You can use `if 条件 { "b" "c" }` to add candidates only when the condition is true.
- Candidates inside `while`, `for`, and `foreach` are added one at a time on each iteration.
- A block with an explicit selection method, such as `nonoverlap : {`, is not unpacked and remains a single candidate.

For details, see [Functions](../grammar/02-functions.md).

## Values and types

| Type | Syntax | Example |
|------|--------|----|
| Integer | Decimal, `0b` (binary), or `0x` (hexadecimal). 64-bit | `10` `0b1010` `0xa` |
| Real number | Include a decimal point | `3.14` |
| String | `"..."` (with expansion), `'...'` (without expansion) | `"a%(_x)"` `'a%(_x)'` |
| Multiline string | `<<"` … `">>` (with expansion), `<<'` … `'>>` (without expansion) | |
| Generic array | `(1, "a", 2.5)` | [Arrays](../grammar/05-arrays.md) |
| Simple array | Comma-separated string `"a,b,c"` | Same as above |
| Hash | `IHASH("キー", 値, …)` (Tc600-3 and later) | [Hashes](../grammar/12-hash.md) |
| VOID | Undefined variables and out-of-range elements | Empty as a string, 0 as a number |

- To include `"` in a string, write it twice (`"1""2"` → `1"2`).
- Use [GETTYPE](../functions/GETTYPE.md) to check the type (VOID is 0, integer is 1, real number is 2, string is 3, generic array is 4, and hash is 5).
- Converting a real number to a string produces six digits after the decimal point (`3.0/4*100` → `75.000000`).
- Integer division truncates the result (`4/3` → `1`). If one operand is a real number, the result is a real number.

## Variables

| Syntax | Meaning |
|--------|------|
| `_a = 1` | Local variable. Valid only within that function (and its inner blocks). Disappears when its block is exited |
| `a = 1` | Global variable. Accessible from any function. Automatically saved on exit and restored at the next startup |
| `ERASEVAR("a")` | Delete a global variable |
| `_a++` `_a--` `_a += 2` | Increment, decrement, and compound assignment (`-=` `*=` `/=` `%=` are also available) |

- An undefined variable becomes 0 in calculations and an empty string in strings (`UNDEF + 1` is `1`).
- Names beginning with a digit or matching a reserved word or function name cannot be used ([Reserved words](../grammar/09-reserved-words.md)).

## Operators

In descending order of precedence ([Arithmetic operations](../grammar/04-arithmetic.md)).

| Type | Operators |
|------|--------|
| Parentheses and subscripts | `( )` `[ ]` |
| Negation | `!` |
| Increment and decrement | `++` `--` |
| Multiplication and division | `*` `/` `%` |
| Addition and subtraction | `+` `-` |
| Comparison | `==` `!=` `>=` `<=` `>` `<` `_in_` `!_in_` |
| Logical | `&&` `\|\|` |
| Assignment | `=` `+=` `-=` `*=` `/=` `%=` `,=` |
| Comma (creates an array) | `,` |

- `0` is false, and any nonzero value is true. Comparison results are `1` or `0`.
- `"or" _in_ "World"` evaluates to `1` when the string on the right contains the string on the left.
- `+` performs **concatenation** if either operand is a string (`"5" + 1` is `"51"`). `*` calculates operands as numbers (`"5" * 2` is `10`).
- `==` is case-sensitive (`"abc" == "ABC"` is `0`).
- There is no ternary operator (`? :`).

## Control structures

```
if _a < 3
{
  "小"
}
elseif _a < 10
{
  "中"
}
else
{
  "大"
}
```

| Task | Syntax |
|--------------|--------|
| Two-way or multi-way branching | `if` / `elseif` / `else` (for a single statement, `{ }` can be omitted, except for nested `if` statements) |
| Branch by value | `case 式 { when 値 { … } when 値1, 値2 { … } others { … } }` |
| Select by position | `switch 式 { 候補0 候補1 … }` (one candidate per line; indexing starts at 0) |
| Repeat by condition | `while 条件 { … }` |
| Repeat a set number of times | `for _i = 0 ; _i < 10 ; _i++ { … }` (all three parts are required; from Tc603-6 onward, the entire header can be enclosed in `( )`) |
| Iterate over an array | `foreach 配列 ; _v { … }` |
| Iterate over keys and values | `foreach 配列またはハッシュ ; _k, _v { … }` (Tc600-3 onward) |
| Exit a loop or skip to the next iteration | `break` / `continue` |

```
case _name
{
  when "さくら" { "さくらだね" }
  when "うにゅう", "うに" { "うにゅうだね" }
  others { "だれ？" }
}
```

- Only **literals** can be used in `when` clauses of `case` (not variables or expressions). Write ranges as `3-5` or `"a"-"d"`.
- Write `when` and `others` inside the `{ }` following `case 式`. If `when` follows without an opening `{`, a load-time error (E0051) occurs.
- The number of loop iterations is limited (default: 1000000; `looplimit`). If the limit is exceeded, `OnLoopLimit` is called.
- `while 1` is an infinite loop. Always include a `break`.

## String embedding

| Syntax | Meaning |
|--------|------|
| `"%(_a)"` `"%(1+2)"` | Evaluate and embed an expression (delimited expansion) |
| `"%_a"` | Embed using the longest matching name. This is slower because the name is looked up at runtime |
| `'%(_a)'` | Single quotes prevent expansion |

For details, see [String embedding](../grammar/06-string-embedding.md).

## Arrays

```
_a = (10, 20, 30)
_a[1]            // 20
_a[0,1]          // 範囲（10,20）
_a ,= 40         // 末尾に追加
_a = ("先頭", _a) // 先頭に追加
_a + "!"         // 全要素に演算（10!,20!,…）
ARRAYSIZE(_a)    // 要素数
```

- An out-of-range element is VOID (`GETTYPE(_a[9])` is 0).
- Simple arrays remain strings and can be read and written using subscripts (`_s = "a,b,c"` → `_s[1]` is `b`). Specify the delimiter as in `_s[1,"|"]`.
- Use [ARRAYSIZE](../functions/ARRAYSIZE.md) for the number of array elements, [ASEARCH](../functions/ASEARCH.md) for searching, [ASORT](../functions/ASORT.md) for sorting, and [SPLIT](../functions/SPLIT.md) for splitting.

## Hashes (Tc600-3 onward)

```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]        // さくら
_h["age"] += 1    // 複合代入も使える
_h["none"]        // VOID（キーが無い）
foreach _h ; _k, _v { … }
```

- A hash must first be created with `IHASH()`.
- Elements are ordered by key, not by insertion order.
- Elements can also contain arrays or hashes ([Nesting values](../grammar/13-nesting.md)).

## Preprocessor

| Syntax | Meaning |
|--------|------|
| `#define 前 後` | Replaces strings after this line in the same file |
| `#globaldefine 前 後` | Replaces strings in all dictionaries loaded after this point |
| `#ifdef 名前` … `#else` … `#endif` | Loads the content if the name is defined (Tc574-2 / Tc602-2 onward) |
| `__AYA_SYSTEM_YAYA6__` | Defined in the 600 series (for dictionaries shared with the 500 series) |
| `__AYA_SYSTEM_FILE__` `__AYA_SYSTEM_LINE__` `__AYA_SYSTEM_FUNC__` | Replaced by the file name, line number, and function name |

For details, see [Preprocessor](../grammar/08-preprocessor.md).

## Configuration file (yaya.txt)

```
dic, basis.dic
charset, UTF-8
log, executelog.txt
```

| Setting | Meaning |
|------|------|
| `dic, ファイル` | Loads a dictionary (`dicif` only if it exists; `dicdir` loads all dictionaries in a folder) |
| `charset, UTF-8` | Character encoding (can also be specified by purpose, such as with `charset.dic`) |
| `log, ファイル` | Outputs an execution log |
| `fncdepth, 数` | Maximum function call depth (default: 32; 0 allows unlimited depth, but execution stops when stack space runs low) |
| `looplimit, 数` | Maximum number of loop iterations (default: 1000000) |
| `embed.lazy, off` | Resolves the name in `"%名前"` at load time (the default, on, looks it up at runtime) |

- The configuration file is named by appending `.txt` to the DLL name (`yaya.txt`). Comments can be written with `//` and `/* */`.
- If there is no configuration file or no dictionaries to load, YAYA enters **shell mode**. It passes submitted expressions directly to `EVAL` and returns the result, so you can use it to test expressions ([Basic settings](../grammar/01-basic-settings.md#シェルモード)).

For details, see [Basic settings](../grammar/01-basic-settings.md).

## Commonly used functions

For the full list, see the [system function list](../system/system-functions-index.md).

| Purpose | Functions |
|------|------|
| Check or change a type | [GETTYPE](../functions/GETTYPE.md) [CVINT](../functions/CVINT.md) [CVSTR](../functions/CVSTR.md) [CVREAL](../functions/CVREAL.md) |
| Arrays | [ARRAYSIZE](../functions/ARRAYSIZE.md) [ASEARCH](../functions/ASEARCH.md) [ASORT](../functions/ASORT.md) [SPLIT](../functions/SPLIT.md) |
| Hashes | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_EXIST](../functions/HASH_EXIST.md) |
| Strings | [STRLEN](../functions/STRLEN.md) [SUBSTR](../functions/SUBSTR.md) [STRSTR](../functions/STRSTR.md) [REPLACE](../functions/REPLACE.md) |
| Execute an expression from a string | [EVAL](../functions/EVAL.md) |
| Delete a variable | [ERASEVAR](../functions/ERASEVAR.md) |
| Convert variables to strings and restore them | [SERIALIZEVAR](../functions/SERIALIZEVAR.md) [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) |
| Random numbers | [RAND](../functions/RAND.md) |
| Run time-consuming processing in a separate thread | [THREADSTART](../functions/THREADSTART.md) [THREADSTATE](../functions/THREADSTATE.md) [THREADJOIN](../functions/THREADJOIN.md) [THREADRESULT](../functions/THREADRESULT.md) [THREADSTOP](../functions/THREADSTOP.md) [THREADCLOSE](../functions/THREADCLOSE.md) |
| Files | [FOPEN](../functions/FOPEN.md) [FREAD](../functions/FREAD.md) [FCLOSE](../functions/FCLOSE.md) |
| Read JSON | [PARSEJSON](../functions/PARSEJSON.md) [FREADJSON](../functions/FREADJSON.md) [FREADJSONL](../functions/FREADJSONL.md) (files with 1 JSON value per line) |

## Related pages

- [Creating a ghost](creating-ghost.md)
- [Migrating from Satori](migration-from-satolili.md)
- [Migrating from AYA](migration-from-aya.md)
