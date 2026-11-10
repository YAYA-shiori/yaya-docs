# LINT.GetGlobalVarUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetGlobalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函数名 |

## Returns
- 成功：指定函数中使用的全局变量名的通用数组
- 无候选项：空的通用数组
- 错误：-1

## Description
列举指定函数中使用的全局变量名，并以通用数组返回。赋值和读取的位置都会列入。

变量名已去重，并按名称排序。因此，即使与 `LINT.GetGlobalVarLetted` 组合使用，也无法判断哪些变量“被赋值但未被读取”。有关限制的详细信息，请参阅[LINT类函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：从Tc568-1起可用

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
