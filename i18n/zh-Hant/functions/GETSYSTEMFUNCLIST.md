# GETSYSTEMFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETSYSTEMFUNCLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （可省略）只傳回以指定字串開頭的系統函式名稱。省略時會傳回所有系統函式 |

## Returns
- 成功時：系統函式名稱的通用陣列
- 失敗時：IARRAY

## Description
傳回系統函式清單。指定 `prefix` 時，只會傳回以該字串開頭的系統函式名稱。省略時會傳回所有系統函式的清單。

## Compatibility
- YAYA：Tc557-1 以後

## See Also
- GETVARLIST
- GETFUNCLIST
