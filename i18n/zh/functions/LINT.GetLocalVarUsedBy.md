# LINT.GetLocalVarUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetLocalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要解析的函数名 |

## Returns
- 成功：指定函数中使用的局部变量名组成的通用数组。进入或离开嵌套作用域时，以 `{` / `}` 表示
- 无候选项（也包括只有 `{` `}` 的情况）：空的通用数组
- 错误：-1

## Description
列举指定函数中使用的局部变量名，并以通用数组返回。赋值和读取的使用位置都属于对象。

变量名按照使用顺序返回，进入或离开嵌套作用域（花括号块）时，以 `{` 和 `}` 表示。

在 Tc574-1 及之后的版本中，同一语句中的赋值目标变量（包括 `foreach` 的循环变量）会排在该语句的最后。这是因为赋值会在右值求值后执行。

```
_z = _z + 1      // → _z（読み）, _z（代入）
_a[0] = _b       // → _b, _a
```

不会列举 `case` 语法在内部生成的局部变量（以 `_CaSe_ExPr_PrEfIx_` 开头的名称）（Tc574-1 及之后的版本）。

返回值不区分读取和赋值。有关限制的详细信息，请参阅 [LINT 系列函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：Tc568-1 及之后的版本可用
- Tc574-1：变更为将同一语句中的赋值目标排在最后。排除 case 的内部变量

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
