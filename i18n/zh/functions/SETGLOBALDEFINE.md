# SETGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
SETGLOBALDEFINE( define_name , define_value )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| define_name | 由 #globaldefine 定义的名称 |
| define_value | 由 #globaldefine 赋予的值 |

## Returns
- **1**：成功
- **0**：失败

## Description
其效果等同于在内存中名为 `_RUNTIME_DIC_` 的词典里写入 `#globaldefine`。

## Compatibility
- YAYA：Tc562-1 及之后

## See Also
- ISGLOBALDEFINE
- UNDEFGLOBALDEFINE
- PROCESSGLOBALDEFINE
