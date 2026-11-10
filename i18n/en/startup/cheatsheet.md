# Cheat Sheet

A one-page reference that summarizes how to write YAYA. For details, see the links for each item.

## How YAYA Works

- A dictionary is a **collection of functions**. Define one in the form `Name { ... }`; if you use an event name such as `OnBoot`, it becomes the response to that event.
- **Expressions and strings inside a function are “output candidates,” one per line.** When the function is called, one candidate is selected at random and returned. Statements such as assignments (`_a = 1`) are not candidates.
- Enclose strings in `"..."`. Sakura Script is also a string, so always enclose it.
- Variables have types (integer, real number, string, array, and hash). You do not need to declare them. Names beginning with `_` are local variables.
- You cannot write statements or variables outside functions. Only preprocessor directives such as `#define` can be written outside them.
- You can enclose the condition expressions for `if` and `while` in parentheses or leave them unparenthesized (`if (_a == 1)` and `if _a == 1` are equivalent). You can also enclose the entire header for `for` and `foreach` in `( )` (Tc603-6 and later; earlier versions produce an error).
- Write symbols using half-width characters (full-width characters such as `（` and `＋` cannot be used).

## Writing Functions

```
OnBoot
{
  _name = "さくら"
  "\0\s[0]こんにちは、%(_name)さん。\e"
  "\0\s[0]起動しましたね。\e"
}
```

- In the example above, either `"\0\s[0]こんにちは…"` or `"\0\s[0]起動しましたね。\e"` is returned at random (`_name = …` is not a candidate).
- There must be **one candidate per line**. Placing `"a" "b"` on one line causes an error. `/` in `"a" / "b"` means division; it does not separate candidates.
- Write `--` on a line by itself to treat the candidates before and after it as separate groups, then select one candidate from each group and join them ([Functions](../grammar/02-functions.md)).
- You can write `{` on the same line as the function name or on the next line.
- Comments are written as `// through the end of the line` and `/* multiple lines */`.
- Separate multiple statements on one line with `;` (`_a = 1 ; _b = 2`).

### Arguments and Return Values

| Syntax | Meaning |
|--------|------|
| `Func(1, "a")` | Call with arguments. To call without arguments, just write `Func` |
| `_argv[0]` `_argv[1]` | The received arguments (zero-based) |
| `_argc` | The number of arguments |
| `Func(&_v)` | Pass a variable by reference. If you assign `_argv[0] = 99` inside `Func`, `_v` changes |
| `return` | End the function here. Return one of the candidates collected so far |
| `return expression` | **Discard all** candidates collected so far and return the value of the expression (Tc573-1 and later) |

### Selecting Candidates

Specify a selection method after the function name using `:` (`Seq : sequential`).

| Specification | Behavior |
|------|------|
| (none) | Select one candidate at random |
| `nonoverlap` | Do not select the same candidate as the previous one consecutively |
| `sequential` | Return candidates in order from the top, then start over after the last one |
| `array` | Return all candidates as a generic array |
| `void` | Execute the contents, but return nothing |
| `all` | Return all candidates joined into a single string (Tc567-1 and later) |
| `last` | Return the last candidate (Tc567-1 and later) |

The following modifiers can also be specified independently of the selection method.

| Specification | Behavior |
|------|------|
| `_pool` | Flatten the candidates in inner blocks (including the contents of `if` blocks) and select from them with the same probability as outer candidates |
| `_pool_nonoverlap` `_pool_sequential` | Apply non-repeating or sequential selection to all the flattened candidates |
| `melt_` | If the selected output is a generic array, flatten its elements and add them to the candidates in the outer block |

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

- Without `_pool`, the inner `{ }` is one candidate as a whole (`x` has a 1/2 chance, and `y` and `z` each have a 1/4 chance). With `_pool`, `x`, `y`, and `z` each have a 1/3 chance.
- If an `if` condition is false, its candidates are not added. You can use `if condition { "b" "c" }` to add candidates only when the condition is true.
- Candidates inside `while`, `for`, and `foreach` are added one at a time on each iteration.
- A block with a specified selection method, such as `nonoverlap : {`, remains one candidate and is not flattened.

For details, see [Functions](../grammar/02-functions.md).

## Values and Types

| Type | Syntax | Example |
|------|--------|----|
| Integer | Decimal, `0b` (binary), or `0x` (hexadecimal). 64-bit | `10` `0b1010` `0xa` |
| Real number | Include a decimal point | `3.14` |
| String | `"..."` (with expansion), `'...'` (without expansion) | `"a%(_x)"` `'a%(_x)'` |
| Multiline string | `<<"` … `">>` (with expansion), `<<'` … `'>>` (without expansion) | |
| Generic array | `(1, "a", 2.5)` | [Arrays](../grammar/05-arrays.md) |
| Simple array | A comma-separated string, such as `"a,b,c"` | Same as above |
| Hash | `IHASH("キー", 値, …)` (Tc600-3 and later) | [Hashes](../grammar/12-hash.md) |
| VOID | An undefined variable or an out-of-range element | Empty when treated as a string; 0 when treated as a number |

- To include `"` inside a string, write it twice (`"1""2"` → `1"2`).
- Check the type with [GETTYPE](../functions/GETTYPE.md) (VOID is 0, integer is 1, real number is 2, string is 3, generic array is 4, and hash is 5).
- Real numbers are converted to strings with six decimal places (`3.0/4*100` → `75.000000`).
- Division between integers truncates the result (`4/3` → `1`). If one operand is a real number, the result is a real number.

## Variables

| Syntax | Meaning |
|--------|------|
| `_a = 1` | Local variable. Valid only inside that function (and its inner blocks). It disappears when the block ends |
| `a = 1` | Global variable. Can be used from any function. Automatically saved at shutdown and restored on the next startup |
| `ERASEVAR("a")` | Delete a global variable |
| `_a++` `_a--` `_a += 2` | Addition, subtraction, and compound assignment (also includes `-=` `*=` `/=` `%=`) |

- Undefined variables are treated as 0 in calculations and as empty strings in strings (`UNDEF + 1` is `1`).
- You cannot use names that start with a number or that are the same as reserved words or function names ([Reserved Words](../grammar/09-reserved-words.md)).

## Operators

Listed in order of precedence, from highest to lowest ([arithmetic operations](../grammar/04-arithmetic.md)).

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
- `"or" _in_ "World"` evaluates to `1` if the left string is included in the right string.
- `+` performs **concatenation** if either operand is a string (`"5" + 1` is `"51"`). `*` performs numeric calculations (`"5" * 2` is `10`).
- `==` is case-sensitive (`"abc" == "ABC"` is `0`).
- There is no ternary operator (`? :`).

## Control Structures

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

| What you want to do | Syntax |
|--------------|--------|
| Two-way or multi-way branching | `if` / `elseif` / `else` (except for a nested `if`, you can omit `{ }` for a single statement) |
| Branch by value | `case 式 { when 値 { … } when 値1, 値2 { … } others { … } }` |
| Select by position | `switch 式 { 候補0 候補1 … }` (write one candidate per line; indexing starts at 0) |
| Repeat while a condition is true | `while 条件 { … }` |
| Repeat a specified number of times | `for _i = 0 ; _i < 10 ; _i++ { … }` (all three parts are required; from Tc603-6 onward, you can enclose the entire header in `( )`) |
| Iterate through an array | `foreach 配列 ; _v { … }` |
| Iterate through keys and values | `foreach 配列またはハッシュ ; _k, _v { … }` (from Tc600-3 onward) |
| Exit a loop or continue to the next iteration | `break` / `continue` |

```
case _name
{
  when "さくら" { "さくらだね" }
  when "うにゅう", "うに" { "うにゅうだね" }
  others { "だれ？" }
}
```

- The `when` clauses in `case` can contain **literals only** (not variables or expressions). Write ranges as `3-5` or `"a"-"d"`.
- Write `when` and `others` inside the `{ }` following `case 式`. If you write `when` clauses without an opening `{`, a load-time error (E0051) occurs.
- The number of loop iterations is limited (the default is 1000000; `looplimit`). If the limit is exceeded, `OnLoopLimit` is called.
- `while 1` is an infinite loop. Be sure to write `break`.

## Embedding in Strings

| Syntax | Meaning |
|--------|------|
| `"%(_a)"` `"%(1+2)"` | Evaluate and embed an expression (scoped expansion) |
| `"%_a"` | Embed using the longest matching name. This is slower because the name is looked up at runtime |
| `'%(_a)'` | Single quotes prevent expansion |

For details, see [String Embedding](../grammar/06-string-embedding.md).

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
- Simple arrays are read and written by subscript while remaining strings (`_s = "a,b,c"` → `_s[1]` is `b`). Specify a delimiter as in `_s[1,"|"]`.
- Use [ARRAYSIZE](../functions/ARRAYSIZE.md) for the number of elements, [ASEARCH](../functions/ASEARCH.md) to search, [ASORT](../functions/ASORT.md) to sort, and [SPLIT](../functions/SPLIT.md) to split.

## Hashes (from Tc600-3 onward)

```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]        // さくら
_h["age"] += 1    // 複合代入も使える
_h["none"]        // VOID（キーが無い）
foreach _h ; _k, _v { … }
```

- Hashes must first be created with `IHASH()`.
- Elements are sorted by key, not by insertion order.
- Elements can also contain arrays and hashes ([Nested Values](../grammar/13-nesting.md)).

## Preprocessor

| Syntax | Meaning |
|--------|------|
| `#define 前 後` | Replaces strings in the file after this line |
| `#globaldefine 前 後` | Replaces strings in all dictionaries loaded from this point onward |
| `#ifdef 名前` … `#else` … `#endif` | Loads the section if the name is defined (from Tc574-2 / Tc602-2 onward) |
| `__AYA_SYSTEM_YAYA6__` | Defined for the 600 series (use this in dictionaries shared with the 500 series) |
| `__AYA_SYSTEM_FILE__` `__AYA_SYSTEM_LINE__` `__AYA_SYSTEM_FUNC__` | Replaced with the file name, line number, and function name |

For details, see [Preprocessor](../grammar/08-preprocessor.md).

## Configuration File (yaya.txt)

```
dic, basis.dic
charset, UTF-8
log, executelog.txt
```

| Setting | Meaning |
|------|------|
| `dic, ファイル` | Loads a dictionary (`dicif` loads it only if it exists; `dicdir` loads all files in the folder) |
| `charset, UTF-8` | Character encoding (can also be specified for specific purposes in files such as `charset.dic`) |
| `log, ファイル` | Writes an execution log |
| `fncdepth, 数` | Maximum function call depth (default 32. A value of 0 allows unlimited depth, but execution stops when the remaining stack space is low) |
| `looplimit, 数` | Maximum number of loop iterations (default 1000000) |
| `embed.lazy, off` | Resolves names in `"%名前"` at load time (the default, on, looks them up at runtime) |

- The configuration file is named after the DLL with `.txt` appended (`yaya.txt`). You can write comments using `//` and `/* */`.
- If there is no configuration file or no dictionaries are loaded, YAYA enters **shell mode**. It evaluates the expression you send using `EVAL` and returns the result, so you can use it to check how an expression behaves ([Basic Settings](../grammar/01-basic-settings.md#シェルモード)).

For details, see [Basic Settings](../grammar/01-basic-settings.md).

## Commonly Used Functions

See the [System Functions List](../system/system-functions-index.md) for the complete list.

| Purpose | Function |
|------|------|
| Check or change a type | [GETTYPE](../functions/GETTYPE.md) [CVINT](../functions/CVINT.md) [CVSTR](../functions/CVSTR.md) [CVREAL](../functions/CVREAL.md) |
| Arrays | [ARRAYSIZE](../functions/ARRAYSIZE.md) [ASEARCH](../functions/ASEARCH.md) [ASORT](../functions/ASORT.md) [SPLIT](../functions/SPLIT.md) |
| Hashes | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_EXIST](../functions/HASH_EXIST.md) |
| Strings | [STRLEN](../functions/STRLEN.md) [SUBSTR](../functions/SUBSTR.md) [STRSTR](../functions/STRSTR.md) [REPLACE](../functions/REPLACE.md) |
| Execute an expression from a string | [EVAL](../functions/EVAL.md) |
| Delete a variable | [ERASEVAR](../functions/ERASEVAR.md) |
| Convert a variable to a string and restore it from a string | [SERIALIZEVAR](../functions/SERIALIZEVAR.md) [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) |
| Random numbers | [RAND](../functions/RAND.md) |
| Run time-consuming operations in another thread | [THREADSTART](../functions/THREADSTART.md) [THREADSTATE](../functions/THREADSTATE.md) [THREADJOIN](../functions/THREADJOIN.md) [THREADRESULT](../functions/THREADRESULT.md) [THREADSTOP](../functions/THREADSTOP.md) [THREADCLOSE](../functions/THREADCLOSE.md) |
| Files | [FOPEN](../functions/FOPEN.md) [FREAD](../functions/FREAD.md) [FCLOSE](../functions/FCLOSE.md) |

## Related

- [How to Create a Ghost](creating-ghost.md)
- [Migrating from Satori](migration-from-satolili.md)
- [Migrating from AYA](migration-from-aya.md)
