# ASORT

**Category:** 配列操作

## Signature

```
ASORT(option, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| option | 用逗号分隔指定排序行为的字符串。可组合指定比较类型（`string`（默认）、`int`、`double`、`length`）、顺序（`ascending`（默认）、`descending`）、是否区分大小写（`case`）以及返回值格式（`index`） |
| array | 要排序的通用数组（不能使用简易数组） |

## Returns

返回排序后的通用数组。发生错误或输入数组为空时，返回空数组。指定 `index` 选项时，返回一个数组，其中表示排序后各元素在原数组中的位置。

## Description

用逗号分隔指定 `option`，其中包括比较类型、顺序和返回值格式这 3 种选项。

- 比较类型：`string`（未指定时的默认值）、`int`、`double`、`length`。`length` 与 `string` 一起使用，不按字符内容而按字符串长度排序（例如写作 `'string,descending,length'`）
- 顺序：`ascending`（升序；未指定时的默认值）、`descending`（降序）
- 返回值格式：指定 `index` 后，返回的不是排序后的数组本身，而是一个数组，其中表示“排序后各位置对应的是排序前第几个元素”。例如，将 `'Z','G','A'` 按字符串升序排序后，顺序为 A、G、Z，因此会返回整数数组 `2,1,0`

对于每种比较类型，都会将各个元素转换为以下值后进行比较。不考虑元素类型，因此即使数组中混有整数和字符串，也会按照指定的比较类型排序。

| 比较类型 | 比较的值 |
|---|---|
| `string` | 将元素转换为字符串后得到的值。按字典序排序。不区分大小写（添加 `case` 后区分大小写） |
| `length` | 将元素转换为字符串后的长度 |
| `int` | 将元素转换为整数后的值 |
| `double` | 将元素转换为实数后的值 |

使用 `string` 且不区分大小写时，像 `"A"` 和 `"a"` 这样只有大小写不同的元素会被视为相同的值。

```
_a = ('b', 'A', 'c', 'B', 'a')
ASORT('string', _a)        // A,a,b,B,c （A と a、b と B の順は決まらない）
ASORT('string,case', _a)   // A,B,a,b,c
```

被视为相同值的元素之间的顺序不作保证（不一定会保持它们在原数组中的顺序）。

### 元素为数组或哈希时（Tc600-3 及以上）

元素也可以是数组或哈希（[值的嵌套](../grammar/13-nesting.md)）。比较的值如下所示。

- `string` / `length`：[TOSTR](TOSTR.md) 所生成的相同字符串（数组为 `1,2`，哈希为 `k=a` 的形式）
- `int` / `double`：始终为 0

返回值中的元素会保持数组或哈希的形式（保留嵌套结构）。

```
_v = PARSEJSON('[[3,1],[1,2],"b",[1,10],5]')
ASORT('string', _v)   // (1,10),(1,2),(3,1),5,"b"
```

因为按字符串进行比较，`(1,10)` 会排在 `(1,2)` 前面（按照 `"1,10"` 和 `"1,2"` 的字典序）。此外，在 `int` / `double` 下，所有数组和哈希都会被视为相同的值，它们的顺序不作保证。要按哈希特定键的值排序时，请创建一个由键值组成的数组，使用 `index` 选项对其排序，再按该顺序取出原数组中的元素。

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

- YAYA：Tc540-1 及以上
- `index` 选项：Tc545-1 及以上

## See Also

- ASEARCH
- ASEARCHEX
