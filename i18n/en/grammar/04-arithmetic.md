# Arithmetic

## Basics

As in the C language, you can perform the four basic arithmetic operations, comparisons, assignments, and more. The order of operations is determined by operator precedence, which assigns a weight to each operator. Parts enclosed in brackets `( )` are evaluated first.

## Operator Precedence (Highest First)

| Precedence | Operator | Description |
|--------|--------|------|
| 1 | `( )` `[ ]` | Brackets |
| 2 | `!` | Negation |
| 3 | `++` `--` | Add 1 / subtract 1 |
| 4 | `*` `/` `%` | Multiplication, division, remainder |
| 5 | `+` `-` | Addition, subtraction |
| 6 | `==` `!=` `>=` `<=` `>` `<` `_in_` `!_in_` | Comparison |
| 7 | `&&` | Logical AND |
| 8 | `\|\|` | Logical OR |
| 9 | `=` `:=` | Assignment |
| 10 | `+=` `-=` `*=` `/=` `%=` `+:=` `-:=` `*:=` `/:=` `%:=` `,=` | Perform an operation and assign |
| 11 | `,` | Enumerate generic array elements (lowest precedence) |

- Assignment operators with a colon (`:`) are retained for backward compatibility and are functionally equivalent to their counterparts without a colon
- `++` `--` `!` are unary operators
- `&` is a prefix symbol placed before a function argument ([feedback operator](#フィードバック演算子)); it is not a binary operator and is therefore not included in this table
- The comma operator (`,`) and square brackets `[ ]` are explained in detail in [Arrays](05-arrays.md)

## Comparison and Truth Values

`_in_` and `!_in_` are operators used to check whether one string is contained in another. `_in_` returns 1 if the string on the left is contained in the string on the right, and 0 if it is not. `!_in_` does the opposite.

```
foo
{
    "or" _in_ "World"
}
```

The function `foo` above returns 1.

Comparison operators return the integer 1 if the result is true, and 0 if it is false. These operators also work correctly with strings; the relative order of values is determined by lexicographic comparison.

Logical truth values are determined as follows.

- False: integer 0, real number 0.0, empty string, empty generic array
- True: everything else

Operations other than assignment output their result directly.

```
foo
{
    (3+2)*4
}
```

This function `foo` outputs 20.

## Left Associativity

When operators with the same precedence appear consecutively, they are always evaluated from left to right. For example,

```
1+2-3
```

is evaluated in the order `1+2` → `3-3`.

```
i = j = 10
```

What happens here? In C, the assignment operator is right-associative, so 10 is assigned to both `i` and `j`. In YAYA, however, expressions are always evaluated from left to right, so this is evaluated in the order `i = j` → `j = 10`. Therefore, 10 is not assigned to `i`.

```
i = (j = 10)
```

Writing it this way also assigns 10 to `i`.

## Type Coercion

If the types of the operands do not match, the result has the following type.

- Integer and real-number operations: the result is a real number
- Addition of an integer / real number and a string: the number is converted to a string, then concatenated with the other string
- Magnitude comparison of an integer / real number and a string: the number is converted to a string, then compared lexicographically
- Operations between an integer / real number and a string (other than addition and magnitude comparison): the operation cannot be performed, but no error occurs. The result is an empty string

Different types can be mixed within a single expression. Type conversion occurs as needed according to the rules above.

```
"10+2は" + (10+2) + "です。"
```

First, `10+2` is evaluated as an integer, yielding 12. The rest of the operations are all additions with strings, so 12 is converted to a string and concatenated as a string.

### Hash Operations (Tc600-3 and later)

- `+`: If the other operand is a scalar or hash, both are converted to strings and concatenated (`IHASH("a",1) + 1` becomes `"a=11"`). If the other operand is an array, concatenation is performed for each array element
- `-` `*` `/` `%` (including compound assignment): Emits warning W0024. The result is not meaningful
- `==`: If both operands are hashes, returns true if their element counts, keys, and values all match. A hash compared with anything other than a hash always returns false

For details, see [Hashes](12-hash.md#値としての振る舞い).

## Controlling the Order of Operations with Parentheses ( )

The part enclosed in parentheses `( )` is given the highest priority in the order of operations. You can nest `( )` as many times as you like; the deeper the nesting, the higher the priority. Simply put, “calculate the part inside the parentheses first.” This is an obvious rule, but depending on how a formula is written, things can get a little complicated. Consider the following example.

```
answer = (_i = 10) + (2*(_i + 10))
```

If you do not understand the rules of operations well, it is difficult to answer precisely what will be assigned to `answer`. Instead of the intended 50, the value 30 is assigned to `answer`.

The first part to be calculated is the deepest part in parentheses: `_i + 10`. At this point, the variable `_i` does not yet exist. Undefined variables are treated as 0 when used in operations with numbers, so `_i + 10` evaluates to 10, and `2*(_i + 10)` evaluates to 20. Later, `(_i = 10)` is evaluated to 10, and the total of 30 is assigned to `answer`.

What we want here is for the assignment `_i = 10` to happen first. In this kind of situation, you can control the order of operations by adding extra parentheses, as follows.

```
answer = (((_i = 10))) + (2*(_i + 10))
```

This greatly increases the priority of the assignment, and this time the correct result (50) is assigned.

You might think that two levels of parentheses around the assignment are enough, but that is incorrect. Two levels of parentheses put it at the same depth as `_i + 10`; however, between `=` and `+`, `+` has higher priority, so `_i + 10` is calculated first.

## Feedback Operator

The feedback operator `&` is a unique operator used in a completely different way from other operators.

```
request
{
    _i = 1
    foo(&_i)
}

foo
{
    _argv[0] = 100
}
```

When passing a variable as an argument in a function call, you can write `&` before it. A variable prefixed with `&` is associated with the corresponding element of the called function's `_argv`. In other words, rewriting `_argv` also rewrites the value of the corresponding variable in the calling function. In the example above, executing `foo` changes the value of `_i` to 100.

You can use the feedback operator as many times as you like, in any position.

```
request
{
    foo(1, 2, &_value, "Hello", &_value2)

    _value + _value2
}

foo
{
    _argv[2] = _argv[0] + _argv[1]
    _argv[4] = _argv[3] + " World"
}
```

The function `request` outputs `"3Hello World"`. Naturally, the feedback operator can only be applied to variables.

You can also pass array elements. In Tc600-4 and later, you can also pass hashes and nested elements ([Multidimensional Assignment](13-nesting.md#多次元代入)).

```
func(&_a[1])            // func の中で _argv[0] を書き換えると _a[1] が変わる
func(&_h["sub"]["x"])   // 同じく _h["sub"]["x"] が変わる（Tc600-4以降）
```

When you pass an array variable as an argument, its elements are expanded and listed in `_argv`. Values are written back based on their positions after expansion.

```
_a = (1, 2)
func(_a, &_x)           // _argv は (1, 2, _x の値)。_argv[2] を書き換えると _x が変わる
func(&_a)               // _argv の _a の要素数ぶんが、配列として _a に戻る
```

Up to Tc603-3, values were written back using the argument position (the argument's ordinal position), so passing an array before another argument could write back to a different element or cause execution to stop because `_argv` was out of range. If the called function had shortened `_argv`, arguments that were no longer present were not written back.

Even when the first argument is enclosed in parentheses (such as `func((1, 2), &_x)` or `func((_a), &_x)`), it behaves as it does when not enclosed (Tc603-5 and later). Up to Tc603-4, the argument separators were not correctly recognized in this case, so `&` write-back did not work. Arguments passed to system functions are also treated as separate arguments, just as they are when not enclosed. For example, `ARRAYSIZE((_a), 1)` returns the number of elements in `_a`, and `TOSTR((1), (2))` returns `"12"` (previously, the first and second arguments were combined into a single array, so `ARRAYSIZE` returned the number of elements plus 1, and `TOSTR` returned `"1,2"`).

## Backward Compatibility

The assignment operator with a colon (`":="`) is retained for backward compatibility, but behaves identically to the one without a colon.
