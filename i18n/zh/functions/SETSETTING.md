# SETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
SETSETTING( name , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 设置信息的条目名称（字符串）。指定基本设置文件中的条目名称 |
| string | 要设置的值（字符串） |

## Returns
- **1**：成功
- **0**：失败

## Description
更改运行期间的文设置。此函数与 GETSETTING 相对应。

以下设置条目仅在首次加载时生效，因此在运行时更改不会产生效果：
- dic
- msglang
- charset.dic
- checkparser

## Compatibility
- YAYA：从初始版本起支持

## See Also
- GETSETTING
- [基本设置](../grammar/01-basic-settings.md)
