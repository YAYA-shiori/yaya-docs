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

清除 YAYA 内部处理中累积的错误和警告日志。执行后，GETERRORLOG 返回的错误数组将变为空。

## Description

清除 YAYA 内部发生的错误和警告日志。执行后，通过 GETERRORLOG 获取的错误数组将变为空。

## Compatibility

- YAYA: Tc567-2版及之后

## See Also

- GETERRORLOG
