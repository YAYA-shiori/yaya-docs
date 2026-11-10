# LINT.GetVarRefs
**Category:** デバッグ

## Signature
```
LINT.GetVarRefs(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要解析的函数名 |

## Returns
- 成功：返回通用数组，每个元素是由逗号分隔的7项字符串：`kind,category,name,access,line,depth,context`
- 错误：-1

## Description
按出现顺序逐项列出指定函数内变量和函数的出现位置，以及代码块（花括号）的进入和退出，并以通用数组返回。与 `LINT.GetLocalVarUsedBy` 等函数不同，其中包含读写区别、行号、代码块类型和出现位置的语法类型。

每个元素都以逗号分隔，因此可以直接作为简易数组提取各项。

```
_refs = LINT.GetVarRefs('OnTest')
foreach _refs ; _r {
	_kind = _r[0]
	_name = _r[2]
	_line = TOINT(_r[4])
}
```

### 项目

| 编号 | 项目 | 值 |
|------|------|-----|
| 0 | kind | `var`（变量） / `func`（函数） / `{`（代码块开始） / `}`（代码块结束） |
| 1 | category | `var` 时为 `local` / `global`，`func` 时为 `user` / `system`，`{` `}` 时为代码块类型 |
| 2 | name | 变量名或函数名（`{` `}` 时为空） |
| 3 | access | `var` 时为 `r`（读取） / `w`（赋值） / `rw`（读写），`func` 时为 `call`（`{` `}` 时为空） |
| 4 | line | 词典文件中的行号 |
| 5 | depth | 代码块的嵌套深度（函数体为1） |
| 6 | context | 出现位置的语句类型（`{` `}` 时为空） |

### access

| 值 | 对象 |
|----|------|
| `r` | 除赋值目标之外的所有出现位置 |
| `w` | `=` `:=` 的赋值目标、数组元素的 `=` 赋值目标（`_a[0] = 1` 中的 `_a`）、`foreach` 的循环变量（双变量 foreach 中的两个变量。Tc600-3以后） |
| `rw` | `+=` `-=` `*=` `/=` `%=` `,=` 及其 `:=` 形式、`++` `--` 的对象（包括对数组元素的复合赋值） |

由于赋值在求值右侧之后进行，因此在同一语句中，赋值目标（`w` / `rw`）会排在最后。

```
_z = _z + 1
// var,local,_z,r,10,1,subst
// var,local,_z,w,10,1,subst
```

### 代码块类型（`{` `}` 的 category）

| 值 | 对象 |
|----|------|
| `function` | 函数体 |
| `if` / `elseif` / `else` | if 结构 |
| `while` | while 结构 |
| `for` | for 结构 |
| `foreach` | foreach 结构 |
| `switch` | switch 结构 |
| `case` | case 结构 |
| `when` / `others` | case 结构中的 when / others |
| `plain` | 以上情况之外（单独的 `{ }` 或 switch 的各个代码块等） |

`}` 中包含与其对应的 `{` 相同的类型和深度。

### context

| 值 | 对象 |
|----|------|
| `output` | 输出的表达式 |
| `subst` | 包含赋值的表达式 |
| `if` / `elseif` / `while` / `switch` | 各结构的条件表达式 |
| `for-init` / `for-cond` / `for-step` | `for a ; b ; c` 中的 a / b / c |
| `foreach` / `foreach-var` | `foreach a ; b` 中的 a / b（`foreach a ; k, v` 中的 k 和 v 都是 `foreach-var`。Tc600-3以后） |
| `case` / `when` | case 表达式 / when 条件 |
| `parallel` / `void` / `return` | 各结构的表达式 |

例如，`if _c = 1` 会作为 `context` 为 `if` 且 `access` 为 `w` 的条目出现。

### 不会列出的内容

- `case` 结构在内部生成的局部变量（名称以 `_CaSe_ExPr_PrEfIx_` 开头）
- 不包含变量或函数的语句（`break` / `continue` / `return`（无表达式） / `--`、仅输出字面量等）
- when 的标签（字面量）

有关限制的详情，请参阅 [LINT 系列函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：Tc574-1以后可用

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
