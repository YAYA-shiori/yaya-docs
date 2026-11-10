# Arrays

## Overview

An array is like a collection of variables.

With regular variables, you would write

```
_a = 1
_b = 2
_c = 3
_d = 4
_e = 5

_sum = _a + _b + _c + _d + _e
```

but with an array, you can write

```
_a = (1,2,3,4,5)

_sum = _a[0] + _a[1] + _a[2] + _a[3] + _a[4]
```

Note that indexes start at 0, so the last index is 4.

Arrays show their true power when combined with loops. Instead of writing `_a[0]`, `_a[1]`, `_a[2]`, … as above, you can write the following.

```
_a = (1,2,3,4,5)

_sum = 0
for _i = 0 ; _i < 5 ; _i++
{
  _sum += _a[_i]
}
```

You can use the variable `_i` to retrieve each value in `_a`, instead of writing `_a[0]`, `_a[1]`, `_a[2]`, …. Inside the `for` loop, `_i` is incremented by 1 while it is less than 5, so it accesses `_a[0]`, `_a[1]`, `_a[2]`, … in order.

## Get the size dynamically with ARRAYSIZE

The example above only works if you already know that the array has a size of 5. The following works regardless of the size of the array.

```
_a = (1,2,3,4,5)

_sum = 0
for _i = 0 ; _i < ARRAYSIZE(_a) ; _i++
{
  _sum += _a[_i]
}
```

[ARRAYSIZE](../functions/ARRAYSIZE.md) determines the size of the array `_a` and returns 5. As long as `_a` is an array, its size does not matter.

Arrays can also contain strings.

```
_sweets = ("プリン", "チョコレート", "クレープ", "甘口いちごスパ")
_talk = ""
for _i = 0 ; _i < ARRAYSIZE(_sweets) ; _i++
{
  _talk += _sweets[_i] + "に"
}
"\1\s[10]\0\s[0]" + _talk + "・・・今日は全部食べちゃうよ！\1なんかまざっとる！\e"
```

## foreach loop (the easiest method)

With `foreach`, you do not need `_i = 0`, `ARRAYSIZE`, or `_i++`. Instead, write the equivalent of `_a[_i]` (here, `_var`).

```
_a = (1,2,3,4,5)

_sum = 0
foreach _a ; _var
{
  _sum += _var
}
```

The values in `_a` are assigned to `_var` in order. The loop ends automatically when it reaches the end of the array.

## Related

- [Grammar/5. Arrays](../grammar/05-arrays.md)
- [ARRAYSIZE](../functions/ARRAYSIZE.md)
