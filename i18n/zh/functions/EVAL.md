# EVAL

**Category:** メタ操作・特殊関数

## Signature

```
EVAL( string )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 作为 YAYA 脚本执行的文本字符串。可以是一个表达式，也可以是一系列语句（Tc574-6 / Tc602-9 及以后） |

## Returns

- 成功时：执行结果。如果只有赋值而没有输出，则为 VOID（无返回值）
- 解析失败时：原样返回参数字符串

## Description

将参数字符串作为 YAYA 脚本执行。可用于展开表达式或在运行时合成函数名等。

### 单个表达式

如果字符串是一个表达式，则返回该表达式求值后的值。赋值表达式会将值赋给调用方的变量。

```
_x = EVAL('1 + 2')          // 3
EVAL('_name = "Emily"')     // 呼び出し元のローカル変数 _name に代入される
```

### 一系列语句（Tc574-6 / Tc602-9 及以后）

如果引号之外存在 `;`、`{`、`}` 或换行符，或者首个单词是 `return`、`if`、`while`、`for`、`foreach`、`switch`、`void`、`parallel` 之一，则会作为一系列语句执行。可以像写在函数主体的 `{ }` 中一样编写。

```
_r = EVAL('_a = 1; _b = _a + 2; _b')   // 3

_r = EVAL('if _hour < 12 { "おはよう" } else { "こんにちは" }')

_r = EVAL('_s = 0; foreach _list; _v { _s += _v }; _s')
```

如果传入的字符串包含换行（例如使用 here document），就可以像在词典中编写一样书写。换行符和 `;` 一样会作为语句分隔符，还可以使用 `//` 或 `/* */` 注释，以及通过行末的 `/` 连接行。

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

Tc574-8 / Tc603-1 及以后，传入的代码中也可以编写 here document。

返回值遵循与函数返回值相同的规则。如果有多个作为输出的表达式，则会从中选择一个；可以通过 `--` 拼接输出；如果写入 `return`，则会在那里结束执行并返回该值。

一系列语句的执行方式与在调用方的 `{ }` 中编写一个代码块相同。

- 可以读写调用方的局部变量（包括 `_argv` 和 `_argc`）
- 在其中新建的局部变量会在 EVAL 结束后消失
- `break` / `continue` / `return` 会在 EVAL 内部生效，不会影响调用方的循环或函数

```
Foo
{
	_count = 1
	_r = EVAL('_count += 10; _tmp = _count * 2; _tmp')
	// _r は 22、_count は 11、_tmp はここでは存在しない
}
```

不能编写函数定义或 `#define` 等预处理器指令。要定义函数时，请使用 APPEND_RUNTIME_DIC。

引号中的 `;`、`{`、`}` 或换行符不会被视为分隔符。`EVAL('"a;b"')`，以及用 `"` 括住包含换行的字符串并展开内嵌元素的用法，仍会像以前一样作为单个表达式求值。

### 在字符串中包含 `"` 或 `%` 时

在传递给 EVAL 的字符串中使用双引号时，请使用 `CHR(34)`。例如，要将 `"test"` 赋给变量 `i`，请按以下方式编写（Tc569-8 及以后也可以连续写两个 `""`。[值与变量](../grammar/03-values-and-variables.md#文字列)）。

```
EVAL("i=%(CHR(34))test%(CHR(34))")
```

如果希望在 EVAL 执行时展开 `%`，也请将 `%` 写成 `CHR(37)`。以下示例会执行 `"%(foo)"`。

```
EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")
```

将 EVAL 的结果转换为字符串的 `TOSTR(EVAL("formula"))` 和内嵌展开 `"%(formula)"` 会产生相同的结果。

## Example

```
EVAL("i=1")

EVAL("i=%(CHR(34))test%(CHR(34))")

EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")

EVAL('_n = 0; while _n < 3 { _n++ }; _n')   // 3
```

## Compatibility

- YAYA：从初版开始支持
- AYA：5.8 及以后
- Tc574-6 / Tc602-9：新增执行一系列语句的功能（以 `;` 或换行分隔的多个语句，以及 if/for 等控制语句）；此前只能执行单个表达式，传入一系列语句时会解析失败并原样返回参数字符串
- Tc574-8 / Tc603-1：新增在传入的代码中使用 here document 的功能（此前会发生 E0007）

## See Also

- ISEVALUABLE
- APPEND_RUNTIME_DIC
- [外壳模式](../grammar/01-basic-settings.md#シェルモード)（没有词典时，会对 request 输入执行 EVAL 并返回）
