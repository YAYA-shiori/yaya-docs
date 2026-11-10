# TOSTR
**Category:** 型取得/変換

## Signature
```
TOSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要轉換的整數、實數或通用陣列 |

## Returns
- 成功：轉換後的字串
- 失敗：VOID

## Description
將整數、實數或通用陣列轉換為字串。傳入通用陣列時，會傳回以逗號連接各元素的字串。

## Example
```
_i = 100
_result = TOSTR( _i )
// "100"

_array = ('さくら','ねここ','まゆら')
_result = TOSTR( _array )
// "さくら,ねここ,まゆら"
```

## Compatibility
- YAYA：自初期版本起
- AYA：5.8 以後
- Tc574-4 / Tc602-5：修正整數最小值（-9223372036854775808）只會顯示為 `-` 的問題
- Tc574-4 / Tc601-1：修正將 1e57 以上的實數轉換為字串時，末尾有時會混入雜訊的問題

## See Also
- TOINT
- TOREAL
