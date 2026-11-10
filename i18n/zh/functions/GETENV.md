# GETENV
**Category:** システム情報

## Signature
```
GETENV( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 要获取的环境变量名称（字符串） |

## Returns
- 成功：环境变量的内容（字符串）
- 失败：空字符串

## Description
按名称获取 OS 环境变量的函数。如果指定的环境变量不存在，则返回空字符串。参数不可省略；省略时会发出警告（W0008）并返回空字符串。

另外，由于不慎操作环境变量设置函数可能会造成危险，目前没有实现计划。

## Compatibility
- YAYA：Tc552-1 及以后
