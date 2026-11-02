# SERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SERIALIZEVAR( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 変数名の文字列。`_` で始まればローカル変数、それ以外はグローバル変数 |

## Returns
変数の値を、セーブファイルの値と同じ書式にした文字列。

変数が存在しない、値が VOID、または [ERASEVAR](ERASEVAR.md) で消した変数のときは、警告 W0012 を出して VOID を返します。

## Description
指定した変数の値を、[SAVEVAR](SAVEVAR.md#保存形式) がセーブファイルに書くのと同じ書式の文字列にします。[DESERIALIZEVAR](DESERIALIZEVAR.md) に渡すと、同じ値を別の変数に復元できます。

セーブファイルの 1 行は `変数名,値,"デリミタ",watcher|setter|destorier` ですが、この関数が返すのは**値の部分だけ**です。変数名、デリミタ、watcher / setter / destorier、文字コードの指定は含みません。

JSON と違い、整数と実数、整数のキーと文字列のキー、VOID と空文字列などの区別を保ちます。入れ子の配列・ハッシュも `IARRAY{...}` / `IHASH{...}` の形でそのまま書き出します。

返す文字列は 1 行で、改行などの制御文字はエスケープされます。

## Example
```
a = 5
b = "x,y"
c = (1, "x", 2.5)
d = IHASH("k", 1)

SERIALIZEVAR("a")   // 5
SERIALIZEVAR("b")   // "x,y"（ダブルクォートを含む）
SERIALIZEVAR("c")   // 1:"x":2.5
SERIALIZEVAR("d")   // "k"=1:IHASH=IHASH
```

ローカル変数も指定できます。

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_s = SERIALIZEVAR("_x")   // IHASH{"k"=1:IHASH=IHASH}:"s"
```

## Compatibility
- Tc607-3以降

## See Also
- DESERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- DUMPJSON
