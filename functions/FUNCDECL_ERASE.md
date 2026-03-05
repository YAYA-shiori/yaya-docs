# FUNCDECL_ERASE

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/FUNCDECL_ERASE

## Signature

```
FUNCDECL_ERASE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 監視対象の変数名 |
| function_name | 変数削除時に実行する関数名。空文字列（`''` または `""`）を指定すると登録解除 |

## Returns

- 成功時: 1
- 失敗時: 0

変数が削除されたとき、指定した関数が自動的に呼び出される。呼び出される関数の引数は以下の通り:

- `_argv[0]`: 変数名
- `_argv[1]`: 変数の現在の値

呼び出された関数の戻り値はシステムによって無視される。

## Compatibility

- YAYA: Tc565-1 以降

## See Also

- FUNCDECL_WRITE
- FUNCDECL_READ
