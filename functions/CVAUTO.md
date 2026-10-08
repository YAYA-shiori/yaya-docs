# CVAUTO

**Category:** 型取得/変換

## Signature

```
CVAUTO(var [, strict_convert])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 変換対象の変数 |
| strict_convert | （省略可、デフォルト: 0）0以外を渡すと、変換結果をさらに文字列変換した結果が、元の文字列と一致する場合のみ変換する（[CVAUTOEX](CVAUTOEX.md) と同じ動作。Tc571-2以降） |

## Returns

戻り値なし（変数をその場で変換する）

引数に文字列の形式を持つ文字列が格納された変数を指定すると、整数として解釈できるなら整数に、実数として解釈できるなら実数に変換して格納しなおす。どちらにも解釈できない場合は、文字列のまま変換しない。汎用配列変数を渡した場合の動作は未定義。

## Example

```
_val = '3.14159'
CVAUTO(_val)
GETTYPE(_val) // 2 を返す（実数型であることを示す）
```

## Compatibility

- YAYA: TC516-901以降
- Tc571-2: `strict_convert` を追加

## See Also

- CVREAL
- CVINT
- CVSTR
- CVAUTOEX
- TOAUTO
