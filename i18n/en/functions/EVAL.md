# EVAL

**Category:** メタ操作・特殊関数

## Signature

```
EVAL( string )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | A text string to execute as YAYA script. A single expression or a sequence of statements (Tc574-6 / Tc602-9 and later) |

## Returns

- On success: The result of execution. Returns VOID (no return value) if there is only an assignment and no output
- If parsing fails: Returns the argument string as is

## Description

Executes the argument string as YAYA script. This can be used to expand expressions or construct function names at runtime.

### Single expression

If the string is a single expression, this function returns the value obtained by evaluating that expression. Assignment expressions assign to variables in the calling function.

```
_x = EVAL('1 + 2')          // 3
EVAL('_name = "Emily"')     // 呼び出し元のローカル変数 _name に代入される
```

### Sequence of statements (Tc574-6 / Tc602-9 and later)

If there is a `;`, `{`, `}`, or newline outside quotes, or if the first word is one of `return`, `if`, `while`, `for`, `foreach`, `switch`, `void`, or `parallel`, the string is executed as a sequence of statements. You can write it just as you would inside the `{ }` body of a function.

```
_r = EVAL('_a = 1; _b = _a + 2; _b')   // 3

_r = EVAL('if _hour < 12 { "おはよう" } else { "こんにちは" }')

_r = EVAL('_s = 0; foreach _list; _v { _s += _v }; _s')
```

You can pass a string containing newlines, such as a here document, and write it in the same form as in a dictionary. Newlines act as statement separators just like `;`, and you can also use `//` and `/* */` comments and line continuation using `/` at the end of a line.

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

Starting with Tc574-8 / Tc603-1, you can also write here documents in the code passed to this function.

The return value is determined by the same rules as a function's return value. If there are multiple expressions that produce output, one is selected from among them; you can concatenate output with `--`, and writing `return` ends execution at that point and returns its value.

The sequence of statements is executed as if a single block had been written inside the calling function's `{ }`.

- Local variables in the calling function (including `_argv` and `_argc`) can be read and written
- Local variables newly created inside EVAL are discarded when EVAL finishes
- `break` / `continue` / `return` are handled within EVAL and do not affect the calling function's loops or function

```
Foo
{
	_count = 1
	_r = EVAL('_count += 10; _tmp = _count * 2; _tmp')
	// _r は 22、_count は 11、_tmp はここでは存在しない
}
```

You cannot write function definitions or preprocessor directives such as `#define`. To define a function, use APPEND_RUNTIME_DIC.

APPEND_RUNTIME_DIC can also execute code containing control structures, but EVAL is faster. APPEND_RUNTIME_DIC registers the code in the function table, whereas EVAL only needs to create and execute a single block.

`;`, `{`, `}`, and newlines inside quotes are not treated as separators. As before, `EVAL('"a;b"')` and using a string containing newlines enclosed in `"` to expand embedded elements are evaluated as a single expression.

### Including `"` or `%` in a string

When using a double quote in a string passed to EVAL, use `CHR(34)`. For example, to assign `"test"` to the variable `i`, write as follows (from Tc569-8 onward, you can also write two consecutive `""` characters. See [Values and variables](../grammar/03-values-and-variables.md#文字列)).

```
EVAL("i=%(CHR(34))test%(CHR(34))")
```

To expand `%` when EVAL runs, use `CHR(37)` for `%` as well. The following example executes `"%(foo)"`.

```
EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")
```

`TOSTR(EVAL("formula"))`, which converts the result of EVAL to a string, and embedded expansion `"%(formula)"` produce the same result.

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
- Tc574-6 / Tc602-9: Added support for executing a sequence of statements (multiple statements separated by `;` or newlines, and control statements such as if/for). Previously, only a single expression was supported, and passing a sequence of statements caused parsing to fail and returned the argument string as is
- Tc574-8 / Tc603-1: Added support for here documents in the code passed to this function (previously, this resulted in E0007)

## See Also

- ISEVALUABLE
- APPEND_RUNTIME_DIC
- [Shell mode](../grammar/01-basic-settings.md#シェルモード) (evaluates the request input with EVAL and returns it when there is no dictionary)
