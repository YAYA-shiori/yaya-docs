# ASORT

**Category:** 配列操作

## Signature

```
ASORT(option, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| option | 以逗號分隔指定排序方式的字串。可組合指定比較型別（`string`（預設）・`int`・`double`・`length`）、順序（`ascending`（預設）・`descending`）、是否區分大小寫（`case`），以及傳回值格式（`index`） |
| array | 要排序的通用陣列（不可使用簡易陣列） |

## Returns

傳回排序後的通用陣列。發生錯誤或輸入陣列為空時，傳回空陣列。指定 `index` 選項時，則傳回一個陣列，表示排序後各元素在原陣列中的位置。

## Description

`option` 會以逗號分隔，依序指定比較型別、順序及傳回值格式這三種選項。

- 比較型別：`string`（未指定時的預設值）、`int`、`double`、`length`。`length` 會與 `string` 一起使用，依字串長度而非字元內容排序（例如寫成 `'string,descending,length'`）
- 順序：`ascending`（升冪；未指定時的預設值）、`descending`（降冪）
- 傳回值格式：指定 `index` 時，不會傳回排序後的陣列本身，而會傳回一個陣列，表示「排序後各位置的元素原本在第幾個位置」。例如將 `'Z','G','A'` 依字串升冪排序後，順序會是 A、G、Z，因此會傳回整數陣列 `2,1,0`

依比較型別，會將各元素轉換為下列值再進行比較。不會檢查元素的型別，因此即使陣列中混有整數和字串，也會依指定的比較型別排序。

| 比較型別 | 比較值 |
|---|---|
| `string` | 將元素轉換成字串後的值。依字典順序排序。不區分大小寫（加上 `case` 時則會區分） |
| `length` | 將元素轉換成字串後的長度 |
| `int` | 將元素轉換成整數後的值 |
| `double` | 將元素轉換成實數後的值 |

使用 `string` 且不區分大小寫時，像 `"A"` 和 `"a"` 這種只有大小寫不同的元素會視為相同值。

```
_a = ('b', 'A', 'c', 'B', 'a')
ASORT('string', _a)        // A,a,b,B,c （A と a、b と B の順は決まらない）
ASORT('string,case', _a)   // A,B,a,b,c
```

被視為相同值的元素之間，其順序不受保證（不一定會維持原陣列的順序）。

### 元素為陣列或雜湊時（Tc600-3 以後）

元素即使是陣列或雜湊（[值的巢狀結構](../grammar/13-nesting.md)），也可以排序。比較值如下。

- `string` / `length`：[TOSTR](TOSTR.md) 所使用的相同字串（陣列為 `1,2`，雜湊為 `k=a` 的形式）
- `int` / `double`：一律為 0

傳回值中的元素會以原本的陣列或雜湊形式（保持巢狀結構）傳回。

```
_v = PARSEJSON('[[3,1],[1,2],"b",[1,10],5]')
ASORT('string', _v)   // (1,10),(1,2),(3,1),5,"b"
```

由於是以字串比較，`(1,10)` 會排在 `(1,2)` 前面（字典順序比較 `"1,10"` 與 `"1,2"`）。另外，使用 `int` / `double` 時，所有陣列和雜湊都會視為相同值，彼此的順序不受保證。若要依雜湊中特定鍵的值排序，請建立存放鍵值的陣列，以 `index` 選項排序，再依該順序取出原陣列中的元素。

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

- YAYA：Tc540-1 以後
- `index` 選項：Tc545-1 以後

## See Also

- ASEARCH
- ASEARCHEX
