# INSERT
**Category:** 文字列操作

## Signature
```
INSERT( src , pos , insert )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要插入内容的原始字符串 |
| pos | 插入位置（0=开头）。指定负值时，将其视为从末尾开始的偏移量（Tc574-8 / Tc603-1及之后） |
| insert | 要插入的字符串 |

## Returns
- 成功时：插入后的字符串
- 出错时：VOID

## Description
在字符串 `src` 中由 `pos` 指定的位置插入字符串 `insert`。位置0表示字符串开头。

当 `pos` 为负值时，会将 `src` 的字符数加到该位置上（-1 表示最后一个字符之前）。如果结果仍为负数，则在开头插入；如果大于 `src` 的字符数，则在末尾插入。

```
INSERT('abc', 1, 'X')    // aXbc
INSERT('abc', -1, 'X')   // abXc
INSERT('abc', 10, 'X')   // abcX
INSERT('abc', -10, 'X')  // Xabc
```

## Compatibility
- YAYA: 从初始版本起可用
- AYA: 5.8及之后
- Tc574-8 / Tc603-1：将负数位置改为从末尾开始计数，并将越界位置调整到开头或末尾（此前会报错并中断处理）。改为向 `insert` 传入数值时也会执行插入（此前不会插入任何内容）
