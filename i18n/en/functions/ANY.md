# ANY

**Category:** 文字列操作

## Signature

```
ANY(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The item to select randomly. Must be a string, generic array, integer, or real number |

## Returns

On success: One randomly selected element
On failure: VOID

When a string is treated as a simple array, returns one random element from it. For a generic array, also returns one random element. For a numeric value (integer or real), returns that value unchanged. You can get the index of the selected element with the LSO function.

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
