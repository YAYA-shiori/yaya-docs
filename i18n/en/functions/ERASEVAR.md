# ERASEVAR

**Category:** メタ操作・特殊関数

## Signature

```
ERASEVAR( name [, name ...] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| name | Variable name to delete (specify as a string). Multiple names can be specified. |

## Returns

There is no return value (VOID).

## Description

Deletes variables. Variable names must be specified as strings.

```
ERASEVAR("i")          // 正しい例：変数 i を削除
ERASEVAR("i","j","k")  // 正しい例：複数の変数を一度に削除
ERASEVAR(i)            // 誤った例：変数名は文字列リテラルで指定すること
```

Can be used to delete global variables that do not need to remain in save data.

## Compatibility

- YAYA: Supported since the first version
- TC532-1 and later: Supports deleting multiple variables at once
- AYA: 5.8 and later

## See Also

- ERASE
- EVAL
