# EVAL

**Category:** メタ操作・特殊関数

## Signature

```
EVAL( string )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | Text string to execute as a YAYA script. A single expression or a sequence of statements (Tc574-6 / Tc602-9 and later) |

## Returns

- On success: The result of execution. If there is only an assignment and no output, VOID (no return value)
- If parsing fails: The argument string is returned as-is

## Description

Executes the argument string as a YAYA script. This can be used for expression expansion and for composing function names at runtime.

### Single expression

If the string is a single expression, returns the value obtained by evaluating that expression. An assignment expression assigns to a variable in the caller.

```
_x = EVAL('1 + 2')          // 3
EVAL('_name = "Emily"')     // 呼び出し元のローカル変数 _name に代入される
```

### Sequence of statements (Tc574-6 / Tc602-9 and later)

If there is a `;`, `{`, `}`, or newline outside quotes, or if the first word is one of `return` `if` `while` `for` `foreach` `switch` `void` `parallel`, the text is executed as a sequence of statements. You can write it just as you would inside the `{ }` of a function body.

```
_r = EVAL('_a = 1; _b = _a + 2; _b')   // 3

_r = EVAL('if _hour < 12 { "おはよう" } else { "こんにちは" }')

_r = EVAL('_s = 0; foreach _list; _v { _s += _v }; _s')
```

Pass a string containing newlines, such as a heredoc, to write code in the same form as in a dictionary. Newlines act as statement separators just like `;`. You can also use `//` and `/* */` comments, and join lines with a trailing `/`.

```
_code = <<'
_s = 0
for _i = 1; _i <= 10; _i++ {
	_s += _i
}
_s
'>>
_r = EVAL(_code)   // 55
```

Starting with Tc574-8 / Tc603-1, you can also write heredocs inside the code being passed.

The return value is determined by the same rules as a function's return value. If there are multiple expressions that produce output, one of them is selected; you can concatenate output with `--`, and writing `return` ends execution there and returns its value.

A sequence of statements executes just as if a single block had been written inside the caller's `{ }`.

- You can read and write the caller's local variables (including `_argv` and `_argc`)
- Local variables created inside the code are discarded when EVAL finishes
- `break` / `continue` / `return` are handled within EVAL and do not affect the caller's loop or function

```
Foo
{
	_count = 1
	_r = EVAL('_count += 10; _tmp = _count * 2; _tmp')
	// _r は 22、_count は 11、_tmp はここでは存在しない
}
```

You cannot write function definitions or preprocessor directives such as `#define`. To define a function, use APPEND_RUNTIME_DIC.

A `;`, `{`, `}`, or newline inside quotes is not treated as a separator. As before, `EVAL('"a;b"')` and the use of a string containing newlines enclosed in `"` to expand embedded elements are evaluated as single expressions.

### Including `"` or `%` in a string

When using double quotes in a string passed to EVAL, use `CHR(34)`. For example, to assign `"test"` to the variable `i`, write as follows (starting with Tc569-8, you can also write `""` twice in a row. See [Values and Variables](../grammar/03-values-and-variables.md#文字列)).

```
EVAL("i=%(CHR(34))test%(CHR(34))")
```

To expand `%` when EVAL executes, use `CHR(37)` for `%` as well. The following example executes `"%(foo)"`.

```
EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")
```

`TOSTR(EVAL("formula"))`, which converts the result of EVAL to a string, and the embedded expansion `"%(formula)"` produce the same result.

## Example

```
EVAL("i=1")

EVAL("i=%(CHR(34))test%(CHR(34))")

EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")

EVAL('_n = 0; while _n < 3 { _n++ }; _n')   // 3
```

## Compatibility

- YAYA: Supported since the initial release
- AYA: 5.8 and later
- Tc574-6 / Tc602-9: Added support for executing sequences of statements (multiple statements separated by `;` or newlines, and control statements such as if/for); before this, only a single expression was supported, and passing a sequence of statements failed to parse and returned the argument string as-is
- Tc574-8 / Tc603-1: Added support for heredocs inside the code being passed (before this, it resulted in E0007)

## See Also

- ISEVALUABLE
- APPEND_RUNTIME_DIC
- [Shell mode](../grammar/01-basic-settings.md#シェルモード) (when there is no dictionary, evaluates the request input with EVAL and returns it)
