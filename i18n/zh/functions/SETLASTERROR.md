# SETLASTERROR
**Category:** デバッグ

## Signature
```
SETLASTERROR( code )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| code | 要设置的错误代码（整数值） |

## Returns
无

## Description
设置系统函数的错误代码。可以在 YAYA 脚本执行期间手动设置错误状态。

与 GETLASTERROR 结合使用，以管理系统级错误状态。

## Compatibility
- YAYA：从初始版本起支持
- AYA：5.8 及之后

## See Also
- GETLASTERROR
