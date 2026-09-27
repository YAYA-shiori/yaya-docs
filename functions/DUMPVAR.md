# DUMPVAR

**Category:** デバッグ

## Signature

```
DUMPVAR()
```

## Parameters

None

## Returns

返り値はありません（VOID）。

## Description

変数のダンプをログ出力します。実行するとその時点の全変数の状態をデフォルトのログファイル（通常 ayame.log）に書き出します。スクリプト実行中の特定時点での変数状態を確認するためのデバッグユーティリティです。

## 出力形式

1行に1変数を、`[番号] 変数名 = 値` の形で書き出します。値には型が付きます。

| 型 | 書式 |
|---|---|
| 整数・実数・文字列 | `(int)5`、`(double)2.500000`、`(string)abc` |
| VOID | `(nop/void)` |
| 汎用配列 | `(array) : ` に続けて要素を空白で区切る |
| ハッシュ（Tc600-4以降） | `(hash) : ` に続けて `キー=値` を空白で区切る |
| 入れ子の要素（Tc600-4以降） | 配列は `(array)[ ... ]`、ハッシュは `(hash){ ... }` で囲む |

```
[0] count = (int)3
[1] list = (array) : (int)1 (string)p
[2] h = (hash) : (string)a=(int)1 (string)l=(array)[ (int)1 (int)2 ] (string)n=(hash){ (string)x=(double)2.500000 }
```

## Compatibility

- YAYA: Tc529-2以降
- Tc600-4: ハッシュと入れ子の値を出力するようにした（それまではハッシュが `(unknown type)`、入れ子の要素が `(?UNKNOWN)` になっていた）
