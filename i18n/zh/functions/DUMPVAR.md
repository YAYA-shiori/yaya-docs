# DUMPVAR

**Category:** デバッグ

## Signature

```
DUMPVAR()
```

## Parameters

无

## Returns

没有返回值（VOID）。

## Description

将变量转储到日志中。执行时会把该时刻所有变量的状态写入默认日志文件（通常为 ayame.log）。这是用于检查脚本执行中特定时刻变量状态的调试工具。

## 输出格式

每行写出一个变量，格式为 `[编号] 变量名 = 值`。值会标注类型。

| 类型 | 格式 |
|---|---|
| 整数、实数、字符串 | `(int)5`、`(double)2.500000`、`(string)abc` |
| VOID | `(nop/void)` |
| 通用数组 | 在 `(array) : ` 之后以空格分隔各元素 |
| 哈希（Tc600-4 及之后） | 在 `(hash) : ` 之后以空格分隔各个 `键=值` |
| 嵌套元素（Tc600-4 及之后） | 数组用 `(array)[ ... ]` 括起，哈希用 `(hash){ ... }` 括起 |

```
[0] count = (int)3
[1] list = (array) : (int)1 (string)p
[2] h = (hash) : (string)a=(int)1 (string)l=(array)[ (int)1 (int)2 ] (string)n=(hash){ (string)x=(double)2.500000 }
```

## Compatibility

- YAYA：Tc529-2 及之后
- Tc600-4：现在会输出哈希和嵌套值（此前哈希会显示为 `(unknown type)`，嵌套元素会显示为 `(?UNKNOWN)`）
