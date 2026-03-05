# LINT.GetGlobalVarUsedBy
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetGlobalVarUsedBy

## Signature
```
LINT.GetGlobalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 指定関数内で使用されているグローバル変数名の汎用配列
- 候補なし: 空の汎用配列
- エラー: -1

## Description
指定した関数内で使用しているグローバル変数名を列挙し、汎用配列で返します。代入・読み取り両方の使用箇所が対象となります。

## Compatibility
- YAYA: Tc568-1以降で使用可能

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
