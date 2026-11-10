# PROCESSGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
PROCESSGLOBALDEFINE(string)
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| string | 要执行预处理的字符串 |

## Returns
- 成功：应用全局定义后的处理结果字符串
- 失败：-1

## Description
执行与通过 `#globaldefine` 定义的预处理（字符串替换处理）相同的处理。有关预处理器功能的详细信息，请参阅[预处理](../grammar/08-preprocessor.md)。

## Compatibility
- YAYA：从版本 Tc559-1 起可用

## See Also
- [预处理](../grammar/08-preprocessor.md)
