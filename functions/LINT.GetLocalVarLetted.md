# LINT.GetLocalVarLetted
**Category:** デバッグ

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

以下も代入として列挙されます。
- 複合代入（`+=` `-=` など）と `++` `--`
- 配列要素への代入（`_a[0] = 1` は `_a`）（Tc574-1以降）
- `foreach _list ; _v` のループ変数 `_v`（Tc574-1以降）
- `foreach _list ; _k, _v` の2つのループ変数 `_k` `_v`（Tc600-3以降）

`case` 構文が内部で生成するローカル変数（`_CaSe_ExPr_PrEfIx_` で始まる名前）は列挙されません（Tc574-1以降）。

制約の詳細は [LINT系関数の仕様と制約](../other/lint-functions.md) を参照してください。

## Compatibility
- YAYA: Tc568-1以降で使用可能
- Tc574-1: 配列要素への代入と foreach のループ変数を列挙するように変更。case の内部変数を除外
- Tc600-3: 2変数の foreach のループ変数を両方とも列挙

## See Also
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetGlobalVarUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetFuncUsedBy
- LINT.GetVarRefs
