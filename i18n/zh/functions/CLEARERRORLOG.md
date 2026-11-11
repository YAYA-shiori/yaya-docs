# CLEARERRORLOG

**Category:** デバッグ

## Signature

```
CLEARERRORLOG()
```

## Parameters

无

## Returns

空数组

清除 YAYA 内部处理过程中累积的错误和警告日志。执行后，GETERRORLOG 返回的错误数组将变为空数组。

## Description

清除 YAYA 内部发生的错误和警告日志。执行后，通过 GETERRORLOG 获取的错误数组将变为空数组。

## Compatibility

- YAYA：Tc567-2 及更高版本

## See Also

- GETERRORLOG
- [读取时发生词典错误时的行为](../grammar/01-basic-settings.md#読み込み時に辞書エラーが起きた際の挙動)
