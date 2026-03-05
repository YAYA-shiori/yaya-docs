# LINT.GetUserDefFuncUsedBy
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetUserDefFuncUsedBy

## Signature
```
LINT.GetUserDefFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 指定関数内で使用されているユーザー定義関数名の汎用配列
- 候補なし: 空の汎用配列
- エラー: -1

## Description
指定した関数内で使用しているユーザー定義関数名を列挙し、汎用配列で返します。システム関数は含まれません（システム関数も含めて列挙する場合は `LINT.GetFuncUsedBy` を使用してください）。

## Compatibility
- YAYA: Tc568-1以降で使用可能

## See Also
- LINT.GetFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
