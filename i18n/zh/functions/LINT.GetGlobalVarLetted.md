# LINT.GetGlobalVarLetted
**Category:** デバッグ

## Signature
```
LINT.GetGlobalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函数名 |

## Returns
- 成功：指定函数中被赋值的全局变量名的通用数组
- 无候选项：空的通用数组
- 错误：-1

## Description
列举指定函数中对全局变量进行赋值（let）的位置，并以通用数组返回。不列举仅有读取的位置。若要同时列举读取的位置，请使用 `LINT.GetGlobalVarUsedBy`。

变量名已去重，并按名称排序。

以下情况也会作为赋值列举。
- 复合赋值（`+=` `-=` 等）以及 `++` `--`
- 对数组元素赋值（`G_a[0] = 1` 会列举为 `G_a`）（Tc574-1起）
- `foreach _list ; G_v` 中的循环变量 `G_v`（Tc574-1起）
- `foreach _list ; G_k, G_v` 中的两个循环变量 `G_k` `G_v`（Tc600-3起）

有关限制的详细信息，请参阅[LINT类函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：从Tc568-1起可用
- Tc574-1：修改为列举对数组元素的赋值和 foreach 循环变量
- Tc600-3：修改为同时列举双变量 foreach 的两个循环变量

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
