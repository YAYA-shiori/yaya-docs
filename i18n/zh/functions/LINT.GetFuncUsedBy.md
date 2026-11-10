# LINT.GetFuncUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函数名 |

## Returns
- 成功：指定函数中使用的函数名（用户自定义函数和系统函数）的通用数组
- 无候选项：空的通用数组
- 错误：-1

## Description
列举指定函数中使用的所有函数名（包括用户自定义函数和系统函数），并以通用数组返回。此Lint类实用函数用于分析代码依赖关系或在开发时进行检查。

返回的函数名已去重，并按名称排序。如果存在包含嵌入式表达式 `%(式)` 的字符串，也会包含展开时内部使用的 `TOSTR`。有关限制的详细信息，请参阅[LINT类函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：从Tc568-1起可用

## See Also
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
