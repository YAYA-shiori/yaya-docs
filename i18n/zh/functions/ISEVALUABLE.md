# ISEVALUABLE
**Category:** メタ操作・特殊関数

## Signature
```
ISEVALUABLE( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要作为 YAYA 脚本执行的字符串 |

## Returns
- 1：可以使用 EVAL 对字符串进行求值和执行（语法正确）
- 0：无法对字符串求值（验证失败）

## Description
此函数用于验证指定字符串能否作为 YAYA 脚本通过 EVAL 函数执行。

在使用 EVAL 执行任意字符串之前，可以先用此函数进行验证，从而避免因代码字符串无效而导致运行时错误。

语句序列（以 `;` 或换行符分隔的多个语句，以及 if/for 等控制语句）也会按照与 EVAL 相同的规则进行判断和验证（Tc574-6 / Tc602-9及之后）。

```
ISEVALUABLE('1 + 2')                  // 1
ISEVALUABLE('_a = 1; if _a { 2 }')    // 1
ISEVALUABLE('_a = 1; if { 2')         // 0
```

## Compatibility
- YAYA: Tc562-1及之后
- Tc574-6 / Tc602-9：配合 EVAL 支持执行语句序列的改动，也增加了验证语句序列的功能

## See Also
- EVAL
- APPEND_RUNTIME_DIC
