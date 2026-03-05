# LINT.GetLocalVarLetted
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetLocalVarLetted

## Signature
```
LINT.GetLocalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 指定関数内でローカル変数への代入が行われている変数名の汎用配列。ネストしたスコープへの出入りは `{` / `}` で表現される
- 候補なし（`{` `}` のみの場合も含む）: 空の汎用配列
- エラー: -1

## Description
指定した関数内でローカル変数への代入（let）が行われている箇所を列挙し、汎用配列で返します。読み取りのみの箇所は列挙されません。代入と読み取りの両方を列挙するには `LINT.GetLocalVarUsedBy` を使用してください。

変数名は代入が行われた順に返され、ネストしたスコープ（波括弧ブロック）への出入りは `{` および `}` で示されます。

## Compatibility
- YAYA: Tc568-1以降で使用可能

## See Also
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetGlobalVarUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetFuncUsedBy
