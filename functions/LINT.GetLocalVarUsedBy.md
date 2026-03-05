# LINT.GetLocalVarUsedBy
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetLocalVarUsedBy

## Signature
```
LINT.GetLocalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 指定関数内で使用されているローカル変数名の汎用配列。ネストしたスコープへの出入りは `{` / `}` で表現される
- 候補なし（`{` `}` のみの場合も含む）: 空の汎用配列
- エラー: -1

## Description
指定した関数内で使用しているローカル変数名を列挙し、汎用配列で返します。代入・読み取り両方の使用箇所が対象となります。

変数名は使用された順に返され、ネストしたスコープ（波括弧ブロック）への出入りは `{` および `}` で示されます。

## Compatibility
- YAYA: Tc568-1以降で使用可能

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
