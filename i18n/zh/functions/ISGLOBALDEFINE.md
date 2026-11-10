# ISGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
ISGLOBALDEFINE( define )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| define | 要确认是否通过 `#globaldefine` 定义的名称 |

## Returns
- 1：存在定义
- 0：不存在定义

## Description
检查是否存在通过 `#globaldefine` 指令定义的名称。

## Compatibility
- YAYA: Tc562-1及之后

## See Also
- SETGLOBALDEFINE
