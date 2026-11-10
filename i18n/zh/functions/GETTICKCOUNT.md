# GETTICKCOUNT
**Category:** システム情報

## Signature
```
GETTICKCOUNT( [ flag ] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| flag | 目前实际上没有意义。历史上，指定非 0 值会返回 `GetTickCount() >> 31` 的第 32 位值，曾用于长时间计量 |

## Returns
OS 启动后的经过时间（单位：毫秒）

## Description
以毫秒为单位返回 OS 启动后的经过时间。

在 Windows XP 及更早版本中，经过约 24 天 20 小时后会重置为 0。Vista 及以后版本和其他 OS 没有此限制。

## Compatibility
- YAYA：从初始版本开始即可使用
- AYA 5.8：可用

## See Also
- GETTIME
- GETSYSTEMFUNCLIST
