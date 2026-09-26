# SAVEVAR
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/SAVEVAR

## Signature
```
SAVEVAR( [path] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 保存先ファイル名（省略時はDLL名 + "_variable.cfg"、例: yaya_variable.cfg） |

## Returns
なし（VOID）

## Description
変数を保存します。unload時に行われる処理と同等です。

保存先ファイルを任意のパスに指定することもできます。

## 保存形式

1行に1変数を、次の形式で書き出します。

```
変数名,値,"デリミタ",watcher|setter|destorier
```

値の書式は次のとおりです。

| 型 | 書式 | 例 |
|---|---|---|
| 整数・実数 | そのまま | `5`、`2.500000` |
| 文字列 | `"..."`（`"` と制御文字はエスケープ） | `"abc"` |
| 汎用配列 | 要素を `:` で区切る。要素が1つなら末尾に `:IARRAY`、空なら `IARRAY:IARRAY` | `1:"b":2.500000` |
| ハッシュ（Tc600-3以降） | `キー=値` を `:` で区切る。要素が1つなら末尾に `:IHASH=IHASH`、空なら `IHASH=IHASH:IHASH=IHASH` | `"a"=1:"b"="x"` |
| 要素・キー・値の VOID | `IVOID` | `"v"=IVOID` |
| 入れ子の要素（Tc600-3以降） | 配列・ハッシュの書式を `IARRAY{...}` / `IHASH{...}` で囲む | `"l"=IARRAY{1:2}` |

Tc600-3以降のハッシュや入れ子の例:

```
h,"a"=1:"l"=IARRAY{1:2}:"n"=IHASH{"x"=1:"y"="s"},",",
v,IHASH{"k"=1:IHASH=IHASH}:IARRAY,",",
e,"e"=IHASH{IHASH=IHASH:IHASH=IHASH}:"ea"=IARRAY{IARRAY:IARRAY},",",
```

入れ子の内側も同じ規則で書き出すので、何段入れ子にしても元の値に戻せます。

ハッシュや入れ子を含まない変数の書式は、Tc600-3 より前と同じです。Tc600-3以降で保存したファイルを古いバージョンで読むと、ハッシュや入れ子を含む変数だけが崩れます（[600 での変更点](../other/changes-600.md#セーブファイルの互換性)）。

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降
- Tc600-3: ハッシュと入れ子の値の保存に対応

## See Also
- RESTOREVAR
