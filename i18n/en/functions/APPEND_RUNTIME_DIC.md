# APPEND_RUNTIME_DIC

**Category:** メタ操作・特殊関数

## Signature

```
APPEND_RUNTIME_DIC(dic_content)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| dic_content | A string equivalent to the contents of a dictionary file. Can include multiple lines and function definitions |

## Returns

On success: 0
On failure: -1

## Description

Has the same effect as writing the contents of `dic_content` to an in-memory dictionary named `_RUNTIME_DIC_`. This allows you to dynamically define new user-defined functions, for example. `dic_content` can contain multiple lines and function definitions, and behaves as if a dictionary had been read from a file.

If a thread started with [THREADSTART](THREADSTART.md) is running, emits warning W0032, adds nothing, and returns -1.

## Compatibility

- YAYA: Tc562-1 and later
- Tc608-1: Prevented additions while a worker thread is running

## See Also

- EVAL
- ISEVALUABLE
