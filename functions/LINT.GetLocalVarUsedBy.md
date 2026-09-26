# LINT.GetLocalVarUsedBy
**Category:** デバッグ

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

Tc574-1以降では、同じステートメント内の代入先の変数（`foreach` のループ変数を含む）は、そのステートメントの最後に並びます。代入は右辺の評価後に行われるためです。

```
_z = _z + 1      // → _z（読み）, _z（代入）
_a[0] = _b       // → _b, _a
```

`case` 構文が内部で生成するローカル変数（`_CaSe_ExPr_PrEfIx_` で始まる名前）は列挙されません（Tc574-1以降）。

戻り値には読みと代入の区別がありません。制約の詳細は [LINT系関数の仕様と制約](../other/lint-functions.md) を参照してください。

## Compatibility
- YAYA: Tc568-1以降で使用可能
- Tc574-1: 同一ステートメント内で代入先を最後に並べるように変更。case の内部変数を除外

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
