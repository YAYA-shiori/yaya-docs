# Branching

## Overview

Processing can be branched depending on whether an expression is true or false. It is almost always used together with [logical operators](operators.md#論理演算子).

## if〜else〜 Statement

```
if (式)
{
  "正しい"
}
else
{
  "正しくない"
}
```

If “式” is true, the processing in the preceding `{}` is executed; if it is false, the `{}` after `else` is executed. Write comparisons such as `_name == "さくら"` in the expression.

```
_name = "さくら"
if (_name == "さくら")
{
  "さくらです"
}
else
{
  "さくらじゃない！"
}
```

## case〜when Statement

Branching based on labels. The block whose `when` value matches the value of the `case` expression is executed.

```
case _value
{
  when 1
  {
    // _value が 1 の場合
  }
  when 2, 3
  {
    // _value が 2 または 3 の場合
  }
  others
  {
    // どれにもマッチしない場合
  }
}
```

## switch Statement

Selects an output candidate by position (starting from 0).

```
switch _n
{
  "ゼロ番目"
}
{
  "一番目"
}
{
  "二番目"
}
```

## Related

- [Grammar/7. Flow Control](../grammar/07-flow-control.md)
