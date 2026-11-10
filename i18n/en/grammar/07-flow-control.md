# Flow Control

## Conditional Branching

### if / elseif / else Syntax

If the expression evaluates to true, the contents of the following `{ }` are processed. You may enclose the conditional expression in `( )`.

```
request
{
    if !i {
        "iは0である。"
    }
}
```

You can add an `elseif` clause immediately afterward. It is processed only if the `if` condition evaluates to false. You can chain any number of these clauses. You can also place an `else` clause at the end of the `if`–`elseif` chain. It is processed if all preceding `if` and `elseif` conditions evaluate to false.

```
request
{
    if !i {
        "iは0である。"
    }
    elseif i == 5 {
        "iは5である。"
    }
    elseif "A" _in_ TOUPPER(i) {
        "iは文字列で、aもしくはAを含んでいる。"
    }
    else {
        "iは0でも5でもaを含む文字列でもない何物かである。"
    }
}
```

If there is only one script inside the `{ }` processed by `if`, `elseif`, or `else`, you can omit the `{ }`. Therefore, the example above can be rewritten as follows.

```
request
{
    if !i
        "iは0である。"
    elseif i == 5
        "iは5である。"
    elseif "A" _in_ TOUPPER(i)
        "iは文字列で、aもしくはAを含んでいる。"
    else
        "iは0でも5でもaを含む文字列でもない何物かである。"
}
```

However, you cannot omit `{ }` when `if` statements are nested. The following is valid in C, but invalid in YAYA (it causes an error when loaded).

```
if i == 0
    if j == 0
        "iとjはともに0である。"
```

In this case, `{ }` are required, as shown below.

```
if i == 0 {
    if j == 0
        "iとjはともに0である。"
}
```

### case / when syntax

Label-based branching. The `case` statement evaluates an expression, and the `when` clause with a matching label value is executed.

```
request
{
    case i {
    when 0 {
        "iは0である。"
    }
    when "A"
        "iは文字列Aである。"
    others {
        "iは0でもAでもない。"
    }
    }
}
```

The `others` clause is executed if none of the labels match. `others` can be omitted; if omitted, nothing is done.

You can list label values to match by separating them with commas. You can also specify a range to match using a minus sign (for example, `"value1"-"value5"`).

```
request
{
    case name+(i+1) {
    when "Pentium3","Pentium4"
        "Pen!!!は1999年、Pen4は2000年発売発売。"
    when "Pentium5"-"PentiumX" {
        "まだ無い。"
    }
    others
        "分からない。"
    }
}
```

Label values specified in `when` must be literal values. You cannot write variables, functions, or expressions that include operators. If there is only one script inside the `{ }` handled by `when` or `others`, you can omit the `{ }`, just as with `if`.

The general form is as follows.

```
case 式
{
  when 値1
  {
    // 値1の場合
  }
  when 値2, 値3
  {
    // 値2または値3の場合
  }
  others
  {
    // どれにもマッチしない場合
  }
}
```

Write `when` and `others` inside the `{ }` following `case expression`. If you write `when` immediately after `case expression` without `{`, an error occurs while loading (E0051 `case`に続く`{`がありません). You can also write `{` on the same line, as in `case expression {`.

### switch Syntax

Output is chosen at random from the candidates inside `{ }`, but using `switch` lets you specify the candidate to select by its position.

```
request
{
    switch id {
        "idは0である。"
        "idは1である。"
        {
            "idは2である。"
            "idはtwoである。"
        }
        "idは3である。"
    }
}
```

The output string is specified by the value of the variable `id`. Positions are zero-based. When `id` is 2, either `"idは2である。"` or `"idはtwoである。"` is output. Within this nested `{ }` section, the selection is random.

If no candidate corresponding to the value evaluated by `switch` exists inside `{ }`, an empty string is output. For example, in the example above, if `id` is 100, an empty string is output.

Write one candidate per line inside `{ }`. `switch 1 { "a" "b" "c" }` (with each candidate on a separate line) evaluates to `"b"`.

You can also write `{ }` blocks consecutively, with as many blocks as there are candidates, and associate them by position. In this case, a candidate is selected at random from the block at the corresponding position.

```
switch _n
{
  "ゼロ番目"
}
{
  "一番目"
}
```

If an output determiner (`--`) appears inside `switch`, the candidate at the corresponding position in each block is selected.

```
request
{
    switch 1 {
        "かわいい"
        "天才"
        "サル"
        --
        "とは言い難い"
        --
        "ですね。"
        "かもしれません。"
    }
}
```

The output of `request` is `"天才かもしれません。"` . Note that the middle block has no candidate at the specified position, so its output is an empty string ([Functions](02-functions.md#出力確定子)).

## Loop Structures

There are three types of loop structures: `while`, `for`, and `foreach`.

You can set the maximum number of loop iterations with `looplimit` in the [basic settings file](01-basic-settings.md#looplimit-count). Increase it if the limit is insufficient. The default is 1000000 iterations (from Tc574-10 / Tc606-4 onward; before that, it was 10000 iterations). When the limit is reached, [shiori.OnLoopLimit](../system/shiori-OnLoopLimit.md)(function name, line) is called.

### while Loop

While the expression evaluated by `while` is true, the contents of `{ }` are processed repeatedly. The conditional expression may be enclosed in parentheses or not (`while (_i < 3)` and `while _i < 3` behave the same).

```
while 条件式
{
  // 処理
}
```

```
request
{
    _i = 1
    _j = 0
    while _i < 11 {
        _j += _i
        _i++
    }

    "1から10をすべて足すと%(_j)である。"
}
```

The example above briefly demonstrates how `while` works. The next example generates 10 different strings. The output of `request` will be a string reporting the square root of one of the numbers from 1 to 10.

```
request
{
    _i = 1
    while _i < 11 {
        "%(_i)の平方根は%(SQRT(_i))である。"
        _i++
    }
}
```

### for loop

`for` is a pre-test loop structure, like `while`, but has the advantage of letting you write the initialization expression, exit condition, and expression to execute on each loop iteration together in one place. Unlike in C, all parts are required. Infinite loops such as `for ( ; ; )` cannot be used.

```
for 初期化 ; 条件 ; インクリメント
{
  // 処理
}
```

The following rewrites with `for` the example from the `while` section that reports square roots.

```
request
{
    for _i = 1; _i < 11; _i++ {
        "%(_i)の平方根は%(SQRT(_i))である。"
    }
}
```

`_i = 1` is executed just before the loop starts. `_i < 11` is the loop condition, and the loop continues while it is true. `_i++` is the expression executed when one loop iteration is complete and execution returns to the beginning.

To create an infinite loop, write something like `for 1;1;1`. However, since `while 1` is sufficient, you should use `while` when creating an infinite loop, both for readability and execution speed.

From Tc603-6 onward, you can enclose the entire header in parentheses. The same applies to `foreach`.

```
for (_i = 0; _i < 3; _i++) { ... }
foreach (_a; _k, _v) { ... }
```

- You can split the header across multiple lines. You can also write a line that ends with only `(`, as in `for (`, or a line that begins with `)`, as in `) {`
- You can still use the form that closes parentheses around each expression (`for (_i = 0); (_i < 3); (_i++)`) and the form without parentheses
- As before, closing the parentheses before the last expression, as in `for (_i = 0; _i < 3); _i++`, results in an error
- When a section becomes empty if the parentheses are removed, as in `for (; _i < 3; _i++)` or `foreach (_a; )`, only E0027 is reported (no subsequent cascading errors occur)

Up to Tc603-5, when the parentheses enclosing the entire header were split across separate expressions, errors such as E0019 occurred. Making the `for` and `foreach` condition expressions enclosed in `( )` caused an error under the specification through this version.

### foreach loop

Retrieves the value of each element of a simple array or generic array in order (custom delimiters set with `SETDELIM` are also recognized).

```
foreach 配列 ; 変数
{
  // 変数に要素が格納されて実行
}
```

The following example retrieves the values of a simple array, converts them to numbers, and calculates their total.

```
request
{
    _str = "1,3,5,7,9"
    _t   = 0
    foreach _str; _i {
        _t += TOINT(_i)
    }
    _t
}
```

Write the target to process after `foreach`. In the example above, the simple array `_str` is specified. The following `_i` is a variable that stores the retrieved element value, and must be a variable. Even if the delimiter for the target variable has been changed using [SETDELIM](../functions/SETDELIM.md), `foreach` recognizes the delimiter and works correctly.

`foreach` can also process generic arrays.

```
request
{
    _sent = ("I", "am", 31, "years", "old.")
    _t   = ""
    foreach _sent; _i {
        _t += (_i + " ")
    }
    _t
}
```

`request` outputs `"I am 31 years old. "`.

You can modify the simple array or generic array being enumerated from inside a `foreach` loop. Even in that case, enumeration uses the data as it was before the modification.

From Tc600-3 onward, you can also iterate over hashes with `foreach`. Values are assigned to the variable in key order. If a value is an array or hash, the variable will also be an array or hash.

#### Two-variable foreach (Tc600-3 and later)

If you write two variables separated by a comma, the first receives the key and the second receives the value. This also works with arrays and simple arrays; in those cases, the first variable receives an index (integer) starting from 0.

```
foreach 配列またはハッシュ ; キー変数, 値変数
{
  // 処理
}
```

```
_h = IHASH("a", 1, "b", 2)
foreach _h ; _k, _v { _s += _k + '=' + _v + ' ' }   // "a=1 b=2 "
foreach ("p", "q") ; _i, _v { ... }                  // _i = 0, 1
foreach "x,y" ; _i, _v { ... }                       // 簡易配列も同じ
```

You can write either local variables or global variables. If you write three or more variables (`_a, _b, _c`) or write something that is not a variable (`_k, 1`, `_a + _b`), error E0043 occurs.

### break

When `break` appears in a loop, execution exits the innermost currently running loop.

```
request
{
    _j = 0
    for _i = 0; _i < 100; _i++ {
        _j = _i*_i
        if  _j >= 100
            break
    }
    _i - 1
}
```

In the example above, the `for` loop tries to run until `_i`, which starts at 0, reaches 100. However, the loop contains a `break` that exits the loop when the result of squaring `_i` is 100 or greater. Therefore, the loop actually ends when `_i` is 10. Since `request` returns the value of `_i` minus 1, it functions as a function that finds the largest integer whose square does not exceed 100 (9).

### continue

When `continue` appears in a loop, execution immediately returns to the beginning of the loop from that point and proceeds to the next iteration.

```
request
{
    _j = ""
    for _i = 0; _i < 3; _i++
    {
        _j += "go "
        if  _i > 0
            continue
        _j += "ahead "
    }
    _j
}
```

`_i` changes through 0, 1, and 2, but `continue` takes effect when it is 1 or 2, so the expression that adds `"ahead "` to `_j` is not executed. Therefore, `request` outputs `"go ahead go go "`.

## Function return values

### return

When `return` appears, execution of that function ends there. The function's output is selected from the candidates accumulated up to that point.

```
to_rad
{
    if GETTYPE(_argv[0]) == 3 {
        -1
        return
    }
    _argv[0]*2.0*3.14/360.0
}
```

The function `to_rad` converts degrees to radians. If a string is passed as an argument, the program is designed to detect it in the `if` condition and return -1. Since -1 is the only output candidate at the point of `return`, it is output.

### return with an argument (Tc573-1 and later)

A return value can be explicitly specified in the form `return 式`. Arguments can be formulas as well as constants.

```
to_rad
{
    if GETTYPE(_argv[0]) == 3 {
        return -1
    }
    return _argv[0]*2.0*3.14/360.0
}
```

An argument-bearing `return` discards **all** candidates accumulated up to that point and replaces them with the specified value. In the following example, the return value is always `"D"`, and `"A"`, `"B"`, and `"C"` are discarded.

```
test_func
{
    "A"
    "B"
    "C"
    return "D"
}
```
