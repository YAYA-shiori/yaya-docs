# CUTSPACE

**Category:** 文字列操作

## Signature

```
CUTSPACE(string)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| string | 要处理的字符串 |

## Returns

成功时：移除字符串开头和末尾的空白字符（半角空格、全角空格、制表符）后得到的字符串
失败时：VOID

移除字符串两端的空白字符。中间的空白（单词之间）会保留。

## Example

```
CUTSPACE(' さくら  まゆら   ') // 「さくら  まゆら」を返す
```

## Compatibility

- YAYA: 从初版开始可用
- AYA: 5.8 及以上版本
