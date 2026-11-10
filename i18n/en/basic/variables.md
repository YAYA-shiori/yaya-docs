# Variables

## Overview

A variable is like a box that can store numbers or characters (strings). Since it is a box, you have to put something in it, but when you do, its previous contents are erased.

**Note:** Variable declarations can only be made inside functions.

## Basic Usage

```
_a = 1
_b = 2
```

Assign 1 to `_a` and 2 to `_b`. You can use them after assigning values.

```
_c = _a + _b
```

This puts the result of 1 + 2, which is 3, into `_c`.

## String Variables

Variables can also contain characters.

```
_a = "紅茶"
_b = "ケーキ"
```

Characters can also be added with `+`. So,

```
_c = _a + "と" + _b
```

this puts `"紅茶とケーキ"` in `_c`.

## Handling Sakura Script

Sakura Script is only executed when written as a string. For example,

```
\![open,inputbox,OnTest,60000]
```

writing it this way will not work correctly. It

```
"\![open,inputbox,OnTest,60000]"
```

must be written as a string.

## Variable Expansion

To display the contents of a variable during a talk, write `%(variable name)`.

```
_hoge = "紅茶"
"\0\s[0]飲み物なら%(_hoge)をどうぞ\e"
```

This displays “飲み物なら紅茶をどうぞ” (“If you want a drink, please have some tea”).

## Related

- [Grammar/3. Values and Variables](../grammar/03-values-and-variables.md)
- [Grammar/6. Expansion of Embedded Elements in Strings](../grammar/06-string-embedding.md)
