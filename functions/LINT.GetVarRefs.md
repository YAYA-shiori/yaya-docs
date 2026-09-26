# LINT.GetVarRefs
**Category:** デバッグ
**Source:** マニュアル/関数/LINT.GetVarRefs

## Signature
```
LINT.GetVarRefs(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 解析対象の関数名 |

## Returns
- 成功: 1件ごとに `kind,category,name,access,line,depth,context` の7項目をカンマで区切った文字列の汎用配列
- エラー: -1

## Description
指定した関数内の変数・関数の出現と、ブロック（波括弧）の出入りを、出現ごとに1件ずつ列挙して汎用配列で返します。`LINT.GetLocalVarUsedBy` などと異なり、読み・書きの区別、行番号、ブロックの種類、出現した構文の種類が含まれます。

各要素はカンマ区切りなので、簡易配列としてそのまま項目を取り出せます。

```
_refs = LINT.GetVarRefs('OnTest')
foreach _refs ; _r {
	_kind = _r[0]
	_name = _r[2]
	_line = TOINT(_r[4])
}
```

### 項目

| 番号 | 項目 | 値 |
|------|------|-----|
| 0 | kind | `var`（変数） / `func`（関数） / `{`（ブロック開始） / `}`（ブロック終了） |
| 1 | category | `var` のとき `local` / `global`、`func` のとき `user` / `system`、`{` `}` のときブロックの種類 |
| 2 | name | 変数名・関数名（`{` `}` では空） |
| 3 | access | `var` のとき `r`（読み） / `w`（代入） / `rw`（読み書き）、`func` のとき `call`（`{` `}` では空） |
| 4 | line | 辞書ファイル中の行番号 |
| 5 | depth | ブロックの入れ子の深さ（関数本体が1） |
| 6 | context | 出現したステートメントの種類（`{` `}` では空） |

### access

| 値 | 対象 |
|----|------|
| `r` | 代入先以外のすべての出現 |
| `w` | `=` `:=` の代入先、配列要素への `=` の代入先（`_a[0] = 1` の `_a`）、`foreach` のループ変数（2変数の foreach では両方。Tc600-3以降） |
| `rw` | `+=` `-=` `*=` `/=` `%=` `,=` とその `:=` 形、`++` `--` の対象（配列要素への複合代入を含む） |

代入は右辺の評価後に行われるため、同じステートメント内では代入先（`w` / `rw`）が最後に並びます。

```
_z = _z + 1
// var,local,_z,r,10,1,subst
// var,local,_z,w,10,1,subst
```

### ブロックの種類（`{` `}` の category）

| 値 | 対象 |
|----|------|
| `function` | 関数本体 |
| `if` / `elseif` / `else` | if 構文 |
| `while` | while 構文 |
| `for` | for 構文 |
| `foreach` | foreach 構文 |
| `switch` | switch 構文 |
| `case` | case 構文 |
| `when` / `others` | case 構文内の when / others |
| `plain` | 上記以外（単独の `{ }` や、switch の各ブロックなど） |

`}` には、対応する `{` と同じ種類と深さが入ります。

### context

| 値 | 対象 |
|----|------|
| `output` | 出力する数式 |
| `subst` | 代入を含む数式 |
| `if` / `elseif` / `while` / `switch` | 各構文の条件式 |
| `for-init` / `for-cond` / `for-step` | `for a ; b ; c` の a / b / c |
| `foreach` / `foreach-var` | `foreach a ; b` の a / b（`foreach a ; k, v` では k と v がどちらも `foreach-var`。Tc600-3以降） |
| `case` / `when` | case の式 / when の条件 |
| `parallel` / `void` / `return` | 各構文の式 |

例えば `if _c = 1` は、`context` が `if` で `access` が `w` の件として現れます。

### 列挙されないもの

- `case` 構文が内部で生成するローカル変数（`_CaSe_ExPr_PrEfIx_` で始まる名前）
- 変数・関数を含まないステートメント（`break` / `continue` / `return`（式なし） / `--`、リテラルだけの出力など）
- when のラベル（リテラル）

制約の詳細は [LINT系関数の仕様と制約](../other/lint-functions.md) を参照してください。

## Compatibility
- YAYA: Tc574-1以降で使用可能

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
