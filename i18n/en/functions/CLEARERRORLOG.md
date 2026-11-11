# CLEARERRORLOG

**Category:** デバッグ

## Signature

```
CLEARERRORLOG()
```

## Parameters

None

## Returns

An empty array

Clears the error and warning logs accumulated by YAYA's internal processing. After execution, the error array returned by GETERRORLOG will be empty.

## Description

Clears the logs of errors and warnings that occurred internally in YAYA. After execution, the error array returned by GETERRORLOG will be empty.

## Compatibility

- YAYA: Version Tc567-2 and later

## See Also

- GETERRORLOG
- [Behavior when a dictionary error occurs during loading](../grammar/01-basic-settings.md#読み込み時に辞書エラーが起きた際の挙動)
