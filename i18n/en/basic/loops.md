# Loops

## for loops

Write a `for` statement as follows.

```
for 初期条件 ; 終了条件 ; 各ループの最後に実行される処理
{
  ...
}
```

For example, to loop 10 times:

```
for _i = 0 ; _i < 10 ; _i = _i + 1
{
  _i + "回目\n"
}
```

This outputs the 0th, 1st, …, and 9th iterations, each on a new line. Note that the final operation in each loop (`_i = _i + 1`) runs after the loop body—that is, after `_i + "回目\n"` has been output.

In this example, after `"9回目\n"` is output, `_i` is incremented by 1 to become 10. The condition then evaluates to false, and the loop ends. From 0 to 9, this makes a total of 10 iterations.

Common operators used in loop statements include `++`, `--`, `+=`, and `-=`.

| Operator | Meaning |
|--------|------|
| `a++` | `a = a+1` |
| `a--` | `a = a-1` |
| `a+=b` | `a = a+b` |
| `a-=b` | `a = a-b` |

Therefore, you can also write the `for` statement above as follows.

```
for _i = 0 ; _i < 10 ; _i++
{
  _i + "回目\n"
}
```

**Note:** The usual form does not enclose the condition in parentheses, but you can enclose it as in `while (_i < 10)`. Enclosing the entire header as in `for (_i = 0; _i < 10; _i++)` is supported from Tc603-6 onward (it results in an error through Tc603-5).

## while loops

In addition to `for` statements, you can write loops using `while` statements.

```
while ループ継続条件
{
  ...
}
```

The `for` statement above can be written as follows.

```
_i = 0
while _i < 10
{
  _i + "回目\n"
  _i++
}
```

If the condition in a `while` statement is always true, it becomes an infinite loop and processing will never end.

```
while 1 == 1
{
  ...
}
```

`1 == 1` is an identity that is always true, so this becomes an infinite loop. Also, in YAYA, bool values (boolean values) are evaluated numerically as 0 or nonzero, so the following also becomes an infinite loop.

```
while 1
{
  ...
}
```

## break statements

Use `break` to exit a loop partway through a `for` or `while` statement.

```
_i = 0
while 1
{
  if _i >= 10
  {
    break
  }
  _i + "回目\n"
  _i++
}
```

This may look like an infinite loop because the condition in the `while` statement is always true. However, it contains the operation “if `_i` is 10 or greater, `break`,” so it works the same as the 10-iteration loop described above.

## Related

- [Syntax/7. Flow control](../grammar/07-flow-control.md)
