# LINT.GetUserDefFuncUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetUserDefFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函数名 |

## Returns
- 成功：指定函数中使用的用户自定义函数名的通用数组
- 无候选项：空的通用数组
- 错误：-1

## Description
列举指定函数中使用的用户自定义函数名，并以通用数组返回。不包括系统函数（若要同时列举系统函数，请使用 `LINT.GetFuncUsedBy`）。

函数名已去重，并按名称排序。不包括通过 `EVAL` 等从字符串调用的函数。有关限制的详细信息，请参阅[LINT类函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：从Tc568-1起可用

## See Also
- LINT.GetFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
