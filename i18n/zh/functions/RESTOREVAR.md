# RESTOREVAR
**Category:** メタ操作・特殊関数

## Signature
```
RESTOREVAR( [ path ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | （可省略）恢复源文件名。省略时使用默认文件名（DLL 名 + "_variable.cfg"，例如：yaya_variable.cfg） |

## Returns
VOID（无返回值）

## Description
从文件加载（恢复）变量。处理方式与加载时执行的处理相同。可以从指定文件恢复变量。

文件格式请参阅 [SAVEVAR](SAVEVAR.md#保存形式)。从 Tc600-3 起，也可以恢复哈希和嵌套值。也可以直接读取使用早于 Tc600-3 的版本保存的文件。

## Compatibility
- YAYA：从初始版本起即可使用
- Tc600-3：支持恢复哈希和嵌套值

## See Also
- SAVEVAR
- SERIALIZEVAR
- DESERIALIZEVAR
