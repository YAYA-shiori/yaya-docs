# DESERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
DESERIALIZEVAR( name, text )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 復元先の変数名の文字列。`_` で始まればローカル変数、それ以外はグローバル変数。存在しなければ作る |
| text | [SERIALIZEVAR](SERIALIZEVAR.md) が返す書式の文字列 |

## Returns
復元できれば 1。`text` が書式として読めなかったときや、引数が不正なときは 0（変数には何もしません）。

## Description
`text` を、[SAVEVAR](SAVEVAR.md#保存形式) がセーブファイルに書く値の書式として読み、`name` の変数に格納します。変数が元から持っていた値は置き換わり、型も `text` の内容で決まります（整数 / 実数 / 文字列 / 配列 / ハッシュ）。

[LETTONAME](LETTONAME.md) と同じく、変数に設定された setter / watcher は呼びません。デリミタや setter / watcher / destorier の設定は変えません。

次の場合は警告を出して 0 を返し、変数を作りも変えもしません。

| 場合 | 警告 |
|------|------|
| 引数が足りない | W0008 |
| `name` か `text` が文字列でない | W0009 |
| `name` が空文字列 | W0010 |
| `name` が変数名として使えない（`,` を含む、システム関数や予約語と同名など） | W0012 |
| `text` が書式として読めない（空文字列、ダブルクォートのない文字列、`:` のない配列、`IVOID` だけの値など） | W0026 |

## Example
```
a = (1, "x", 2.5)
_s = SERIALIZEVAR("a")
_r = DESERIALIZEVAR("b", _s)   // b が (1, "x", 2.5) になる。_r は 1

DESERIALIZEVAR("n", "0.5")     // n が実数 0.5 になる
DESERIALIZEVAR("m", "abc")     // 0。警告 W0026
```

ローカル変数への復元:

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_r = DESERIALIZEVAR("_y", SERIALIZEVAR("_x"))
// _y は _x と同じ入れ子の配列になる
```

## Compatibility
- Tc607-3以降

## See Also
- SERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- LETTONAME
- PARSEJSON
