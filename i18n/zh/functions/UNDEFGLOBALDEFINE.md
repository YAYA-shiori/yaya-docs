# UNDEFGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
UNDEFGLOBALDEFINE( definename )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| definename | 使用 `#globaldefine` 声明的指令名 |

## Returns
- 0：成功
- 1：失败

## Description
禁用或删除通过 `#globaldefine` 声明的指令。

无法将通过 `#globaldefine` 定义的文本直接插入词典文件。即使将其用引号括起来，预处理器仍会对其进行处理。要避免这种情况，可以将目标字符串拆开后书写（例如，像 `"TEST_" + "DEF"` 这样连接起来）。

## Compatibility
- YAYA: Tc561-1 及以上版本

## See Also
- DICUNLOAD
- SETGLOBALDEFINE
- ISGLOBALDEFINE
- PROCESSGLOBALDEFINE
