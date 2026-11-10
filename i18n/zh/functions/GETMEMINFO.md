# GETMEMINFO
**Category:** システム情報

## Signature
```
GETMEMINFO()
```

## Parameters
无（不接受参数）

## Returns
包含运行环境内存信息的通用数组（5 个元素）：

| 索引 | 内容 |
|------------|------|
| 0 | 物理内存使用率 |
| 1 | 物理内存总量 |
| 2 | 物理内存可用容量 |
| 3 | 虚拟内存与物理内存的总量 |
| 4 | 虚拟内存与物理内存的可用容量 |

## Description
获取运行环境内存信息的函数。

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及以后版本可用
