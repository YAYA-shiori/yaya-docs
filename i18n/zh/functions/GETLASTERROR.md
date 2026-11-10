# GETLASTERROR
**Category:** デバッグ

## Signature
```
GETLASTERROR
GETLASTERROR()
```

## Parameters
无

## Returns
最近一次系统函数调用的错误代码（整数）。如果没有错误，则为 0。

## Description
返回最近一次执行的系统函数调用的错误代码。

## Error Codes
| 代码 | 含义 |
|--------|------|
| 0 | 无错误 |
| 8 | 参数不足 |
| 9 | 参数值无效 |
| 10 | 无法处理空字符串 |
| 11 | 没有可用于存储结果的变量 |
| 12 | 值超出范围或无效 |
| 13 | 处理失败 |
| 14 | 未加载外部库 |
| 15 | 文件未打开 |
| 16 | 正则表达式语法错误或表达式过于复杂 |
| 17 | 正则表达式处理过程中发生未定义错误 |
| 18 | 需要变量的位置传入了非变量参数 |

## Example
```
SETLASTERROR(0)
// システム関数を呼び出す
if !GETLASTERROR {
    "エラーが発生しました。"
}
```

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及以后版本可用

## See Also
- SETLASTERROR
