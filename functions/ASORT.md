# ASORT

**Category:** 配列操作

## Signature

```
ASORT(option, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| option | ソート動作をカンマ区切りで指定する文字列。比較型（`string`（デフォルト）・`int`・`double`・`length`）、順序（`ascending`（デフォルト）・`descending`）、大文字小文字の区別（`case`）、戻り値形式（`index`）を組み合わせて指定 |
| array | ソート対象の汎用配列（単純配列は使用不可） |

## Returns

ソートされた汎用配列を返す。エラー時または入力配列が空の場合は空の配列を返す。`index` オプションを指定した場合は、ソート後の各要素の元の配列における位置を示す配列を返す。

## Description

比較型ごとに、各要素を次の値に変換して比べる。要素の型は見ないので、整数と文字列が混ざった配列も、指定した比較型で並べる。

| 比較型 | 比べる値 |
|---|---|
| `string` | 要素を文字列にしたもの。辞書順に並べる。大文字小文字を区別しない（`case` を付けると区別する） |
| `length` | 要素を文字列にしたものの長さ |
| `int` | 要素を整数にしたもの |
| `double` | 要素を実数にしたもの |

`string` で大文字小文字を区別しないときは、`"A"` と `"a"` のように大文字小文字だけが違う要素は同じ値とみなす。

```
_a = ('b', 'A', 'c', 'B', 'a')
ASORT('string', _a)        // A,a,b,B,c （A と a、b と B の順は決まらない）
ASORT('string,case', _a)   // A,B,a,b,c
```

同じ値とみなされた要素どうしの順番は保証されない（元の配列の順を保つとは限らない）。

### 要素が配列やハッシュのとき（Tc600-3以降）

要素が配列やハッシュ（[値の入れ子](../grammar/13-nesting.md)）でも並べられる。比べる値は次のようになる。

- `string` / `length`: [TOSTR](TOSTR.md) と同じ文字列（配列は `1,2`、ハッシュは `k=a` の形）
- `int` / `double`: 常に 0

返り値の要素は、配列やハッシュのまま（入れ子のまま）返る。

```
_v = PARSEJSON('[[3,1],[1,2],"b",[1,10],5]')
ASORT('string', _v)   // (1,10),(1,2),(3,1),5,"b"
```

文字列にして比べるので、`(1,10)` は `(1,2)` より前になる（`"1,10"` と `"1,2"` の辞書順）。また `int` / `double` では配列やハッシュはすべて同じ値とみなされ、その順番は保証されない。ハッシュの特定のキーの値で並べたいときは、キーの値の配列を作って `index` オプションで並べ、その順に元の配列の要素を取り出す。

```
_list = PARSEJSON('[{"n":3,"s":"c"},{"n":1,"s":"a"},{"n":2,"s":"b"}]')
_keys = IARRAY()
foreach _list ; _e { _keys ,= _e["n"] }
_sorted = IARRAY()
foreach ASORT('int,index', _keys) ; _i { _sorted ,= _list[_i] }
// _sorted の "n" は 1,2,3 の順
```

## Example

```
_array = ('BBBB','CCC','AA')
ASORT('string,ascending', _array)         // "AA,BBBB,CCC" を出力
ASORT('string,descending,length', _array) // "BBBB,CCC,AA" を出力
```

## Compatibility

- YAYA: Tc540-1 以降
- `index` オプション: Tc545-1 以降

## See Also

- ASEARCH
- ASEARCHEX
