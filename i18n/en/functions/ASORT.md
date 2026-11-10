# ASORT

**Category:** 配列操作

## Signature

```
ASORT(option, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| option | A comma-separated string specifying the sort behavior. Combine a comparison type (`string` (default), `int`, `double`, or `length`), order (`ascending` (default) or `descending`), case sensitivity (`case`), and return format (`index`). |
| array | The generic array to sort (simple arrays cannot be used) |

## Returns

Returns the sorted generic array. Returns an empty array on error or if the input array is empty. If the `index` option is specified, returns an array indicating the original positions of the elements in the sorted array.

## Description

Specify `option` as a comma-separated list of three kinds of settings: comparison type, order, and return format.

- Comparison type: `string` (default if not specified), `int`, `double`, or `length`. Use `length` together with `string` to sort by string length rather than string content (write it as `'string,descending,length'`, for example)
- Order: `ascending` (ascending order; default if not specified) or `descending` (descending order)
- Return format: If `index` is specified, returns an array indicating which element each position in the sorted result corresponds to in the original array, rather than the sorted array itself. For example, sorting `'Z','G','A'` in ascending string order produces the order A, G, Z, so the returned array is `2,1,0`

For each comparison type, the elements are converted to the following values before comparison. Element types are ignored, so an array containing both integers and strings is sorted using the specified comparison type.

| Comparison type | Value compared |
|---|---|
| `string` | The element converted to a string. Sorted in lexicographic order. Case-insensitive (`case` makes it case-sensitive) |
| `length` | The length of the element converted to a string |
| `int` | The element converted to an integer |
| `double` | The element converted to a real number |

When `string` is used without case sensitivity, elements that differ only in case, such as `"A"` and `"a"`, are treated as having the same value.

```
_a = ('b', 'A', 'c', 'B', 'a')
ASORT('string', _a)        // A,a,b,B,c （A と a、b と B の順は決まらない）
ASORT('string,case', _a)   // A,B,a,b,c
```

The order of elements treated as having the same value is not guaranteed (their original order is not necessarily preserved).

### When elements are arrays or hashes (Tc600-3 and later)

Elements can be sorted even when they are arrays or hashes ([nested values](../grammar/13-nesting.md)). The values compared are as follows.

- `string` / `length`: The same strings as in [TOSTR](TOSTR.md) (arrays have the form `1,2`; hashes have the form `k=a`)
- `int` / `double`: Always 0

Elements in the return value remain arrays or hashes (and remain nested).

```
_v = PARSEJSON('[[3,1],[1,2],"b",[1,10],5]')
ASORT('string', _v)   // (1,10),(1,2),(3,1),5,"b"
```

Since the values are compared as strings, `(1,10)` comes before `(1,2)` (the lexicographic order of `"1,10"` and `"1,2"`). With `int` / `double`, all arrays and hashes are treated as having the same value, and their order is not guaranteed. To sort by the value of a specific hash key, create an array of the key values, sort it with the `index` option, and retrieve the elements from the original array in that order.

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

- YAYA: Available since the initial release
- `index` option: Tc545-1 and later

## See Also

- ASEARCH
- ASEARCHEX
