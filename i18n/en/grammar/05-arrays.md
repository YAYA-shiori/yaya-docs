# Arrays

## Overview

The `[ ]` operator is used to access array elements. There are two types of arrays: **simple arrays**, which split a string and treat it as an array, and **generic arrays**, which handle elements listed with commas.

## Simple Arrays

This feature interprets commas in a string as delimiters and treats the string like an array.

```
request
{
    _a = "this,is,a,pen"
    _a[1]
}
```

`request` outputs `"is"`. The target of the `[ ]` operator does not have to be a variable; it can also be a literal or a function return value. The example above can also be written as follows with the same result.

```
request
{
    "this,is,a,pen"[1]
}
```

### Custom Delimiters

By specifying a delimiter after the index, separated by a comma, you can separate the elements of a simple array using a string other than a comma.

```
request
{
    "This is a island."[2,"is"]
}
```

Since `"is"` is used as the delimiter, the string is split as follows.

| Index | Element |
|------|------|
| `[0]` | `"Th"` |
| `[1]` | `" "` |
| `[2]` | `" a "` |
| `[3]` | `"land."` |

Therefore, `request` returns `" a "`.

### Multidimensional Array-Like Access

By making good use of delimiter specifications, you can retrieve values in a multidimensional array-like manner.

```
request
{
    _ar = "taro|male,ayame|female,hotaru|female"

    _ar[2][1,"|"]
}
```

`_ar[2]` becomes `"hotaru|female"`. Then, `|` is interpreted as the delimiter and `[1]` is retrieved, so the result is `"female"`. In this way, you can easily extract a value at any position by applying a unique delimiter at each level.

For information about the output when an out-of-range index is specified, see [Out-of-Range Elements](#範囲外の要素).

### Multidimensional Arrays Using Simple and Generic Arrays

If you want to handle multidimensional arrays more directly,

```
Food = "うどん,ラーメン,おにぎり"
Color = "赤,青,黄"
```

declare simple arrays like these, then use a generic array to write

```
Word = (Food, Color)
```

and you can get "うどん" with `Word[0][0]` and "黄" with `Word[1][2]`.

### Assignment

The features from here on are limited to variables. You can assign values to elements.

```
request
{
    _a = "this,is,a,pen"
    _a[3] = "eraser"
    _a
}
```

This replaces `"pen"` with `"eraser"`, so the result of executing `request` is `"this,is,a,eraser"`. This also works correctly when a delimiter is specified.

```
request
{
    _s = "This is a island."
    _s[2,"is"] = " beautiful "
    _s
}
```

`request` outputs `"This is beautiful island."`.

Assignment when concatenating `[ ]` operators to access a value in a multidimensional array-like manner is available from Tc600-3 onward ([Nested Values and Multidimensional Assignment](13-nesting.md)). In earlier versions, assignment was only possible for one-dimensional arrays, and the following operation resulted in an error.

```
request
{
    _ar = "taro|male,ayame|female,hotaru|female"

    _ar[1][1,"|"] = "male"
}
```

You can also assign to a position beyond the current number of elements. Delimiters are added automatically, and the number of elements is expanded.

```
request
{
    _m = "fuji/asama/tanigawa"
    _m[5,"/"] = "daisen"
    _m
}
```

`request` outputs `"fuji/asama/tanigawa///daisen"`.

### SETDELIM

The [SETDELIM](../functions/SETDELIM.md) function lets you change the “default delimiter” from a comma to another string. The following is the earlier example rewritten using `SETDELIM`.

```
request
{
    _m = "fuji/asama/tanigawa"
    SETDELIM(_m, "/")
    _m[5] = "daisen"
    _m
}
```

Using `SETDELIM` lets you simply write `_m[5]`. When concatenating `[ ]` operators to access a value in a multidimensional array-like manner, `SETDELIM` is effective only for the first (outermost) `[ ]`.

## Generic Arrays

A generic array is an array structure that can store values of various types together. For ordinary access, it operates faster than a simple array.

### Initialization

```
i = (100,"test",-1.5)
```

List the elements separated by commas. When assigning them, enclose the set of elements in `( )` as shown above. The comma operator has lower precedence than assignment, so without parentheses,

```
i = 100,"test",-1.5
```

is interpreted as `(i = 100),"test",-1.5`, and only 100 is assigned to `i`.

To initialize an array as empty, use the [IARRAY](../functions/IARRAY.md) function. `IARRAY` is a function that returns an “empty generic array.”

```
i = IARRAY
```

If you want to assign just one element during initialization, you need to use a workaround. For example, simply writing `i = 100` assigns a number, not an array. Write it as follows.

```
i = (IARRAY,100)
```

### Adding Elements

```
i = (i,"add")
```

adds `"add"` to the end of the array. You can also add another array.

```
i = (i,("add",123,0.0))
```

Just as `a = a + 1` can be abbreviated as `a += 1`, the example above can also be written as follows.

```
i ,= ("add",123,0.0)
```

You can also insert an element at the beginning using the same syntax.

```
i = ("first",i)
```

You can also insert an element in the middle.

```
i = (100,200,300,400,500,600)
i[2] ,= "insertion"
```

`i` becomes `(100,200,300,"insertion",400,500,600)`. Note that the insertion position is `[3]`, not `[2]`. To insert at `i[2]`, write it as follows.

```
i[2] = ("insertion",i[2])
```

### Deleting Elements

Assign `IARRAY` to the element you want to delete.

```
i = (100,200,300,400,500,600)
i[2] = IARRAY
```

300 is deleted, and `i` becomes `(100,200,400,500,600)`.

### Updating Values

You can simply assign a value to an element. You can also assign to a position beyond the current number of elements; the number of elements is expanded as needed.

### Retrieving Values

As with ordinary variables, specifying an ordinal retrieves the value as is. For information about retrieving values with an out-of-range ordinal, see [Out-of-Range Elements](#範囲外の要素).

```
i = (100,200,300,400,500,600)
i[4]
```

500 is output. The `[ ]` operator does not have to operate on a variable; it can also operate on an immediate value or a function's return value.

```
(100,200,300,400,500,600)[4]
```

500 is output. A generic array can also be used directly as a function's output.

```
request
{
    river[2]
}

river
{
    ("tenryu","bandou-tarou","ishikari","shimanto")
}
```

`request` outputs `"ishikari"`.

### Arrays Cannot Contain Arrays

A `( )` written inside another `( )` is not recognized as a nested array. Instead, it is expanded and simply concatenated.

```
(100,200,(300,400),500,600)
```

Even if written this way, it is ultimately concatenated as follows.

```
(100,200,300,400,500,600)
```

To put an array or hash in an element, see the following section, “Nesting and Multidimensional Assignment.”

### Operations

Operations on individual elements work as usual.

Operations between a generic array and a unary value have the distinctive behavior of applying the unary value's operation to every element.

```
pref = ("gunnma","ohsaka","hokkaido")
pref += "-ken"
```

`pref` becomes `"gunnma-ken","ohsaka-ken","hokkaido-ken"`.

```
answer = (2*(1,2,3))[1]
```

4 is assigned to `answer`, because the result of `2*(1,2,3)` is `(2,4,6)`.

Operations between generic arrays output all possible combinations of operands.

```
pref1 = ("gunma","osaka","hokkai")
pref2 = ("-ken","-fu","-do")
pref3 = pref1 + pref2
```

`pref3` becomes `"gunma-ken","gunma-fu","gunma-do","osaka-ken","osaka-fu","osaka-do","hokkai-ken","hokkai-fu","hokkai-do"`. If an array contains numbers (integers or real numbers), other operations such as subtraction, division, and multiplication are also valid.

### Comparing Elements

When arrays are compared using `==`, their elements are compared individually. In Tc600-3 and later, elements are also considered equal when **both are VOID** (previously, the result was false).

### Function Arguments

In YAYA, function arguments are generic arrays. The contents of `_argv` form a generic array to which the calling function's arguments are assigned as is. In other words, the function call

```
func(1, 2, "test")
```

can also be written as

```
_i = (1,2,"test")
func(_i)
```

This is a very tricky notation, but it works as intended. Note that even in the rewritten script, there are 3 arguments, not 1.

This structure can be used to easily pass a variable number of arguments to another function.

```
request
{
    total(1,2,3,4,5,6)
}

total
{
    calc_total(_argv)
}

calc_total
{
    _answer = 0
    foreach _argv; _val { _answer += _val }
    _answer
}
```

`total` does nothing itself and passes all its arguments directly to `calc_total`. This example passes them directly, but you can also modify them as needed before passing them on.

Be careful when the way arguments are specified becomes complex.

```
_i = (1,2,"test")
func("sky", _i, "sun")
```

The call above is equivalent to the following. Remember that a generic array cannot be multidimensional; it is expanded.

```
func("sky", 1, 2, "test", "sun")
```

### Delimiter and Retrieval Count Specification

```
_i = (2,"is")
"This is a island."[_i]
```

The delimiter specification in a simple array is also a generic array, so you can do things like the above. This is equivalent to the following.

```
"This is a island."[2,"is"]
```

## Nesting and Multidimensional Assignment (Tc600-3 and Later)

You can put a hash in an array element or an array in a hash value. To retrieve a value, write `[ ]` consecutively, as in `_a[1]["x"]`; to assign a value, write them as in `_a[1]["x"] = 5`.

```
_a = (0, IHASH("x", 1), 2)
_a[1]["x"]        // 1
_a[1]["x"] = 5    // 多次元代入
```

In multidimensional assignment, if an intermediate element is a string, it is rewritten as a simple array:

```
_a = ("p,q", "r")
_a[0][1] = "Q"    // _a[0] は "p,Q"
```

However, there is no way to put a new generic array inside a generic array. The `,` operator and `_a[1] = (8,9)` both expand the array and insert its elements. Only when the target element is already an array or hash is it replaced as a whole without being expanded (Tc603-1 and later; [Replacing an Inner Array or Hash as a Whole](13-nesting.md#内側の配列やハッシュを丸ごと書き換える)).

For details, see [Nesting Values and Multidimensional Assignment](13-nesting.md).

## Specifying a Range

You can specify ordinals as a range for both simple and generic arrays. You can retrieve and assign values this way. Specify the range using a generic array. For example, `i[a,b]` represents “elements a through b of `i`.”

```
name = ("さくら","せりこ","奈留","まゆら","毒子","美耳")
i = name[1,3]
name[3,4] = "奎子"
j = name
name[0,2] = IARRAY
k = name
```

- `i` contains `("せりこ","奈留","まゆら")`
- `j` becomes `("さくら","せりこ","奈留","奎子","美耳")`
- `k` becomes `("奎子","美耳")`

The format is the same when the target is a simple array.

```
name = "さくら,せりこ,奈留,まゆら,毒子,美耳"
i = name[1,3]
name[3,4] = "奎子"
j = name
```

`i` becomes `"せりこ,奈留,まゆら"`, and `j` becomes `"さくら,せりこ,奈留,奎子,美耳"`.

You can also specify a delimiter. Specify it immediately after the range.

```
animal = "くま！うさぎ！ねこ！いぬ！わに"
i = animal[0,2,"！"]
animal[2,4,"！"] = "ぶた"
j = animal
```

`i` becomes `"くま！うさぎ！ねこ"`, and `j` becomes `"くま！うさぎ！ぶた"`.

### Handling Range Endpoints

- When `a > b` (`i[3,1]`), a and b are swapped, so the range becomes the same as `i[1,3]`
- The end beyond the last element is treated as the last element. When `n = (1,2,3,4)`, `n[2,9] = 9` changes `n` to `(1,2,9)`
- Negative ordinals are treated as large values beyond the end. They are not clamped to 0 or ignored as out of range. Therefore, `n[-2,1]` specifies the same range as `n[1,末尾]`

```
n = (1,2,3,4)
i = n[-2,1]
n[-2,1] *= 5
```

`i` becomes `(2,3,4)`, and `n` becomes `(1,10,15,20)`. To count from the beginning, use a value of 0 or greater, as in `n[0,1]`.

## Out-of-Range Elements

Reading an out-of-range element returns **VOID**, just as for an undefined variable, for both simple arrays and generic arrays (Tc574-8 / Tc603-1 and later). When a range read is out of range, it returns an empty range (an empty string for a simple array, or an empty array for a generic array).

```
_a = (1, 2)
_a[9]            // VOID
_a[9] == ""      // 1
_a[9] == 0       // 1
_a[9] + 1        // 1 （整数）
GETTYPE(_a[9])   // 0
_a[5, 6]         // 空の配列
"a,b"[5, 6]      // ""
```

- VOID is treated as an empty string when used as a string, and as 0 when used as a number. The results of `== ""` and `if _a[9]` are the same as they would be for an empty string
- Writing an out-of-range element as-is, such as on the last line of a function, does not make it an output candidate (just as for an undefined variable; an empty string would have been an output candidate)
- When `[ ]` is applied to a number (`5[1]`), the number is treated as an array with one element. Index 0 is that number; all other indices are VOID
- Assigning to an element beyond the end (`_a[9] = 1`) fills the intervening elements with VOID. The maximum number of elements used to fill the gap is 16,777,216; an assignment exceeding this limit (such as `_a[2000000000] = 1`) is treated as an out-of-memory condition, execution is interrupted with E0100, and `shiori.OnMemoryError` is called (Tc603-4 and later. Before that, there was no limit, so memory could be exhausted)
- Compound assignment to an out-of-range element (`_a[9] += 1`) also calculates using VOID, so the result is the integer 1 (in the 600 series, starting with Tc602-10; in the 500 series, starting with Tc574-8)
- Up to Tc574-7 / Tc602-13, out-of-range elements in generic arrays returned an empty string, while those in simple arrays returned VOID, so the result differed depending on the array type. Therefore, `_a[9] == 0` was false, `_a[9] + 1` was the string `"1"`, and `GETTYPE(_a[9])` was 3. A range read on a simple array returned VOID when out of range, and a range read on a number also returned VOID when out of range

## Parallel Output

You can write `parallel` before any expression or value. When an output candidate is a generic array, `parallel` makes each of its elements an output candidate.

```
foo0
{
    ("A","B","C")
    "地球"
}

foo1
{
    parallel ("A","B","C")
    "地球"
}
```

The output of `foo0` is either `("A", "B", "C")` or `"地球"`. The output of `foo1` is one of `"A"`, `"B"`, `"C"`, or `"地球"`.

Using `parallel` with anything other than a generic array has no effect, so it is the same as not writing it. For example, the following two statements are equivalent.

```
parallel STRLEN("earth")
STRLEN("earth")
```

The selection modes `array` and `parallel` let you convert between a function's output candidates and a generic array. They can be used in a variety of ways. For example, the very concise function `cyclic` below retrieves elements from a generic array in the order they are written.

```
cyclic : sequential
{
    parallel _argv
}
```

Conversely, writing `void` before any expression or value discards the calculation result, so it does not become an output candidate.
