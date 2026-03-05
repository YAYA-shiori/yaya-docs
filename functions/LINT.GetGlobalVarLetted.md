# LINT.GetGlobalVarLetted
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetGlobalVarLetted

## Signature
```
LINT.GetGlobalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 指定関数内で代入されているグローバル変数名の汎用配列
- 候補なし: 空の汎用配列
- エラー: -1

## Description
指定した関数内でグローバル変数への代入（let）が行われている箇所を列挙し、汎用配列で返します。読み取りのみの箇所は列挙されません。読み取りも含めて列挙する場合は `LINT.GetGlobalVarUsedBy` を使用してください。

## Compatibility
- YAYA: Tc568-1以降で使用可能

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
