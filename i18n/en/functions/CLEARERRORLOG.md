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

Clears the error and warning logs accumulated during YAYA's internal processing. After execution, the error array returned by GETERRORLOG is empty.

## Description

Clears the logs of errors and warnings that occurred internally in YAYA. When executed, the error array returned by GETERRORLOG becomes empty.

## Compatibility

- YAYA: Version Tc567-2 and later

## See Also

- GETERRORLOG
