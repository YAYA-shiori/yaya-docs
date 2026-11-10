# RAND
**Category:** 数学関数

## Signature
```
RAND([max])
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| max | （可省略）随机数的上限值。生成范围为 0 到 (max-1)。省略时默认为 100（生成 0～99 的值） |

## Returns
- 成功：指定范围内的随机整数
- 失败：0

## Description
获取随机整数。无需初始化种子即可单独运行。也可以使用 SRAND 设置种子，但基本用法中并非必需。

## Compatibility
- YAYA：从初始版本起可用
- AYA：从版本 5.8 起可用

## See Also
- SRAND
