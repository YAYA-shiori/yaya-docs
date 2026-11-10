# Values and Variables

## Literal Values

YAYA supports three types of values: integers, real numbers, and strings.

### Integers (int)

Signed 64-bit integers (expanded in Tc566-1; 32-bit before that). Write decimal values as-is. Prefix a value with `0b` to write it in binary, or with `0x` to write it in hexadecimal.

The following function, `int10`, returns the integer 10. All three expressions represent 10 in decimal.

```
int10
{
    10
    0b1010
    0xa
}
```

### Real numbers (double)

Signed 64-bit floating-point numbers. Use them when a value has digits after the decimal point or when you want to handle very large numbers, even if precision may be lost.

Integers and real numbers are distinguished by the presence of a decimal point. When YAYA finds a decimal point in a number, it treats the value as a real number. For example,

```
Test
{
    3/4*100
}
```

produces 0 rather than 75. This is because `3/4` is evaluated as an int, and the fractional part is discarded (operators are evaluated from left to right). To get the intended result,

```
Test
{
    3.0/4*100
}
```

must be used. Since `3.0` is treated as a double when it is evaluated, the result is the real number `75.0`. When a real number is converted to a string, it has 6 digits after the decimal point, so it is output as `75.000000`. To get an integer, use the [TOINT](../functions/TOINT.md) function.

To do this with variable operations, assign a real number when declaring the variable, or use the [TOREAL](../functions/TOREAL.md) function.

```
Test
{
    _A = 3
    _B = 4
    TOREAL(_A)/_B*100
}
```

The decimal point is always `.`, regardless of the OS locale. Real numbers converted from strings and real numbers written in a dictionary are also read using `.` (the same applies to locales where `,` is the decimal point, such as German).

### Strings

Values enclosed in double quotation marks (`"`) are strings, and variable and function expansion ([expansion of embedded elements in strings](06-string-embedding.md)) is performed.

Writing `/` at the end of a line lets you write a string that includes line breaks.

```
"こん\n/
なかんじに\n/
書いてもＯＫ\n/"
```

You can also write a string containing line breaks using the here document described below. Sakura Script must be written as a string to work.

In versions before Tc569-8, strings cannot contain double quotation marks. In Tc569-8 and later, you can add a double quotation mark inside a string by writing two double quotation marks consecutively.

```
"1""2"
```

This defines the string `1"2`.

### Strings (without expansion)

Values enclosed in single quotation marks (`'`) are simple strings that are not expanded. YAYA can embed variables and functions in strings, but expansion is performed only in strings enclosed in double quotation marks.

In versions before Tc569-8, strings cannot contain single quotation marks. In Tc569-8 and later, you can add a single quotation mark inside a string by writing two single quotation marks consecutively.

```
'1''2'
```

This defines the string `1'2`.

Using this in an overly complex way can make the code harder to read later, so it is not recommended. However, the following examples show both types of quotation marks used together:

```
'1''2"3'
"1'2""3"
```

Both define the string `1'2"3`.

### Here documents

String literals that can span multiple lines. Available starting with Tc535-1.

```
<<"
行1
行2
">>
```

creates a string with expansion, while

```
<<'
行1
行2
'>>
```

creates a string without expansion. You can write various expressions before or after a here document, but this is supported only inside dictionary files and causes an error when used with [EVAL](../functions/EVAL.md).

## Arrays and Hashes

In addition to literal values, YAYA has a type for handling groups of values: **generic arrays** ([arrays](05-arrays.md)). **Hashes** (associative arrays, [hashes](12-hash.md)) are also available starting with Tc600-3.

Starting with Tc600-3, arrays and hashes can also contain arrays and hashes as elements (nesting them) ([nested values and multidimensional assignment](13-nesting.md)).

## Variables

A variable is a storage area for a value. A variable can store:

- An integer, real number, or string
- A generic array, whose elements can each store any of the above types
- A hash (starting with Tc600-3)

Variable names can be chosen freely as long as they do not violate any of the following restrictions:

- Begins with a digit from 0 to 9
- Contains any of the following characters: space　`!`　`"`　`#`　`$`　`%`　`&`　`(`　`)`　`*`　`+`　`,`　`-`　`/`　`:`　`;`　`<`　`=`　`>`　`?`　`@`　`[`　`]`　`` ` ``　`{`　`|`　`}`　`~`
- Exactly matches a reserved word
- Exactly matches a function name

Values are stored (assigned) using the assignment operator `=`. To output a variable's contents, write its name, just as you would a function name.

```
request
{
    str = "こんにちは"

    str
}
```

This is a simple example: it stores a string in the variable `str` and then outputs it.

A variable that has not yet been assigned a value has a special type called “undefined.” Note that this does not mean “outputs nothing.”

```
request
{
    "Hello World"
    i
}
```

In this case, `i` does not exist, so it has the “undefined” type. “Undefined” is treated as 0 in operations with numbers, and as `''` (an empty string) in operations with strings. In the example above, either “undefined” or the string `"Hello World"` is returned, with a 1/2 probability.

## Scope and Lifetime

Variables come in two types, depending on their scope:

- Global variables: Variables that can be used by all functions. They last forever (unless deleted with [ERASEVAR](../functions/ERASEVAR.md)).
- Local variables: Variables that can be used only within the current `{ }` and its deeper nested scopes. They last until execution leaves the relevant `{ }`.

The variable name distinguishes the two types: variables whose names begin with an underscore (`_`) are treated as local variables. Using local variables effectively—variables that are “valid only where needed”—makes programs easier to understand.

```
request
{
    _i = "3*2は"

    _j = multi(3)

    _i + _j + "です"
}

multi
{
    _i = _argv[0]
    _i * 2
}
```

`request` and `multi` use a variable with the same name, `_i`, but they are treated as completely separate variables and do not overwrite each other's values. The variables `_argc` and `_argv`, which handle function arguments, are also local variables; they are local because each function stores different values in them.

Note that a local variable is not a “variable that can be used within the current function.” It is a “variable that can be used only within the current `{ }` and its deeper nested scopes.”

```
request
{
    {
        _str = "Hello World"
    }

    _str
}
```

This program does not behave as expected. Since `_str` is valid only inside the `{ }`, it is gone by the time the program tries to retrieve its value for output. Therefore, the `request` function outputs an empty string.

Another difference between global and local variables is their lifetime. As described above, a local variable disappears when execution leaves the `{ }` where it is used. In contrast, global variables can be used anywhere, and their values are automatically saved to a file on `unload` and restored on `load`.

Use the [ERASEVAR](../functions/ERASEVAR.md) function to delete a global variable. Also, due to their nature, it is recommended that global variables be initialized in a function that runs first at startup, such as `OnBoot`.
