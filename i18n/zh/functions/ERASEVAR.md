# ERASEVAR

**Category:** メタ操作・特殊関数

## Signature

```
ERASEVAR( name [, name ...] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| name | 要删除的变量名（以字符串指定）。可指定多个。 |

## Returns

没有返回值（VOID）。

## Description

删除变量。变量名必须以字符串形式指定。

```
ERASEVAR("i")          // 正しい例：変数 i を削除
ERASEVAR("i","j","k")  // 正しい例：複数の変数を一度に削除
ERASEVAR(i)            // 誤った例：変数名は文字列リテラルで指定すること
```

可用于删除无需保留在存档数据中的全局变量等。

## Compatibility

- YAYA: 从初版起支持
- TC532-1 及以后：支持同时删除多个变量
- AYA: 5.8 及以后

## See Also

- ERASE
- EVAL
