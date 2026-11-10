# GETSYSTEMFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETSYSTEMFUNCLIST( [ prefix ] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| prefix | （可选）仅返回以指定字符串开头的系统函数名称。省略时返回所有系统函数 |

## Returns
- 成功时：系统函数名称的通用数组
- 失败时：IARRAY

## Description
返回系统函数列表。指定 `prefix` 时，仅返回以该字符串开头的系统函数名称。省略时会返回所有系统函数的列表。

## Compatibility
- YAYA：Tc557-1 及以后版本

## See Also
- GETVARLIST
- GETFUNCLIST
