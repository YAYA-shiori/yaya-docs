# Operators

Operators are used to perform calculations.

## Arithmetic operators

These are the familiar operations of addition, subtraction, multiplication, and division.

| Operator | Description | Example |
|--------|------|-----|
| `x + y` | Add x and y | `1+1` → `2` |
| `x - y` | Subtract y from x | `2-1` → `1` |
| `x * y` | Multiply x by y | `6*2` → `12` |
| `x / y` | Divide x by y. The remainder is discarded | `4/3` → `1` |
| `x % y` | Get the remainder when x is divided by y | `4%3` → `1` |

You can use `x % 2` to determine whether a number is even or odd: 0 means even, and 1 means odd.

## Logical operators

These check whether values are equal, unequal, greater than or less than one another, and so on. They determine whether something is “true” or “false” (correct or incorrect). They are usually used after an `if` or `for` statement to set the conditions for branching or looping. Branching lets you change a talk based on such things as the name of the ghost you switched from or its total startup time.

| Operator | Description |
|--------|------|
| `x == y` | True if x and y are equal |
| `x != y` | True if x and y are not equal |
| `x && y` | True if both x and y are true. True if both operands around `&&` are true (AND) |
| `x \|\| y` | True if either x or y is true. True if either operand around `\|\|` is true (OR) |
| `x > y` | True if x is greater than y. Does not include equal values. `10 > 1` is true, while `10 > 100` and `10 > 10` are false |
| `x >= y` | True if x is greater than or equal to y. Includes equal values. `10 >= 1` and `10 >= 10` are true, while `10 >= 100` is false |
| `x < y` | The opposite of `>`; true if x is less than y |
| `x <= y` | The opposite of `>=`; true if x is less than or equal to y |
| `!x` | Not x (negation). `!(1==1)` is false. In this example, it is more usual to write `1!=1` |
| `y _in_ x` | True if y is in the string x. `"さくら" _in_ "あさくら"` is true. Note the order |
| `y !_in_ x` | True if y is not in the string x. `"さくら" !_in_ "あさくら"` is false. Note the order |

## String operations

Use `+` to concatenate strings.

```
_c = "さくら" + "と" + "うにゅう"
// 結果: "さくらとうにゅう"
```

## Array operations

Use `,` to create an array containing x and y.

```
_array = (_hoge, _fuga, _gonyo)
```

`_array` contains three values.

## Related

- [Grammar/4. Arithmetic](../grammar/04-arithmetic.md)
