# LINT.GetLocalVarLetted
**Category:** デバッグ

## Signature
```
LINT.GetLocalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函数名 |

## Returns
- 成功：指定函数中被赋值的局部变量名的通用数组。嵌套作用域的进入和退出以 `{` / `}` 表示
- 无候选项（也包括仅包含 `{` `}` 的情况）：空的通用数组
- 错误：-1

## Description
列举指定函数中对局部变量进行赋值（let）的位置，并以通用数组返回。不列举仅有读取的位置。若要同时列举赋值和读取的位置，请使用 `LINT.GetLocalVarUsedBy`。

变量名按赋值发生的顺序返回，嵌套作用域（花括号块）的进入和退出以 `{` 和 `}` 表示。

以下情况也会作为赋值列举。
- 复合赋值（`+=` `-=` 等）以及 `++` `--`
- 对数组元素赋值（`_a[0] = 1` 会列举为 `_a`）（Tc574-1起）
- `foreach _list ; _v` 中的循环变量 `_v`（Tc574-1起）
- `foreach _list ; _k, _v` 中的两个循环变量 `_k` `_v`（Tc600-3起）

不会列举 `case` 语法在内部生成的局部变量（以 `_CaSe_ExPr_PrEfIx_` 开头的名称）（Tc574-1起）。

有关限制的详细信息，请参阅[LINT类函数的规格与限制](../other/lint-functions.md)。

## Compatibility
- YAYA：从Tc568-1起可用
- Tc574-1：修改为列举对数组元素的赋值和 foreach 循环变量；排除 case 的内部变量
- Tc600-3：修改为同时列举双变量 foreach 的两个循环变量

## See Also
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetGlobalVarUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetFuncUsedBy
- LINT.GetVarRefs
