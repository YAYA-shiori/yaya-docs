# LICENSE
**Category:** メタ操作・特殊関数

## Signature
```
LICENSE()
LICENSE
```

## Parameters
无

## Returns
存储YAYA许可证文本的通用数组。各项以换行符分隔。

## Description
返回YAYA许可证文本。除YAYA本体的许可证外，还包括内置库（MT19937、parson、TinyXML-2、SQLite）的许可证文本。

## Compatibility
- YAYA：从Tc530-1起可用
- Tc601-1：添加了parson和TinyXML-2的许可证文本
- Tc602-11：添加了SQLite（公有领域）的说明

## See Also
- LETTONAME
- LINT.GetFuncUsedBy
