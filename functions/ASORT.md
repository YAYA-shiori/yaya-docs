# ASORT

**Category:** 配列操作
**Source:** マニュアル/関数/ASORT

## Signature

```
ASORT(option, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| option | ソート動作をカンマ区切りで指定する文字列。比較型（`string`（デフォルト）・`int`・`double`・`length`）、順序（`ascending`（デフォルト）・`descending`）、戻り値形式（`index`）を組み合わせて指定 |
| array | ソート対象の汎用配列（単純配列は使用不可） |

## Returns

ソートされた汎用配列を返す。エラー時または入力配列が空の場合は空の配列を返す。`index` オプションを指定した場合は、ソート後の各要素の元の配列における位置を示す配列を返す。

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
