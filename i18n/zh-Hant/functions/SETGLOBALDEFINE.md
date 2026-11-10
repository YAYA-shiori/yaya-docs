# SETGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
SETGLOBALDEFINE( define_name , define_value )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| define_name | 以 #globaldefine 定義的名稱 |
| define_value | 指派給 #globaldefine 的值 |

## Returns
- **1**：成功
- **0**：失敗

## Description
此函式的效果等同於在記憶體中名為 `_RUNTIME_DIC_` 的辭典內撰寫 `#globaldefine`。

## Compatibility
- YAYA：Tc562-1 以後

## See Also
- ISGLOBALDEFINE
- UNDEFGLOBALDEFINE
- PROCESSGLOBALDEFINE
