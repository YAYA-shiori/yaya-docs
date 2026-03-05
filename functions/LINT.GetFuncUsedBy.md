# LINT.GetFuncUsedBy
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetFuncUsedBy

## Signature
```
LINT.GetFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 指定関数内で使用されている関数名（ユーザー定義関数・システム関数両方）の汎用配列
- 候補なし: 空の汎用配列
- エラー: -1

## Description
指定した関数内で使用しているすべての関数名（ユーザー定義関数・システム関数を含む）を列挙し、汎用配列で返します。コードの依存関係解析や開発時の検査に使用するLint系ユーティリティ関数です。

## Compatibility
- YAYA: Tc568-1以降で使用可能

## See Also
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
