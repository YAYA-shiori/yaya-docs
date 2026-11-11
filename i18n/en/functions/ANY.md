# ANY

**Category:** 文字列操作

## Signature

```
ANY(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The target to choose from at random. A string, generic array, integer, or real number |

## Returns

On success: One randomly selected element
On failure: VOID

When a string is treated as a simple array, this function returns one random element from it. If a variable is passed, its delimiter is taken into account. For a generic array, this function also returns one random element. If the argument is a numeric value (integer or real number), it returns that value as is. You can get the index of the selected element with the LSO function.

## Example

```
_array = ('さくら','まゆら','ねここ')
ANY(_array)  // 「まゆら」などランダムな要素を返す

_str = 'さくら,まゆら,ねここ'
ANY(_str)    // 「ねここ」などランダムな要素を返す

LSO          // 2（「ねここ」のインデックス）を返す
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- LSO
