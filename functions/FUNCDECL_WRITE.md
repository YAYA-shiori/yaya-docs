# FUNCDECL_WRITE

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/FUNCDECL_WRITE

## Signature

```
FUNCDECL_WRITE(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 監視対象の変数名 |
| function_name | 変数書き込み時に実行する関数名。空文字列（`""` または `''`）を指定すると登録解除 |

## Returns

- 成功時: 1
- 失敗時: 0

指定した変数に書き込みが行われるたびに、登録した関数が自動的に呼び出される。呼び出される関数の引数は以下の通り:

- `_argv[0]`: 変数名
- `_argv[1]`: 代入される新しい値（`=` の右辺）
- `_argv[2]`: 変数の以前の値

呼び出された関数は、変数に実際に書き込まれる値を返す必要がある（`_argv[1]` と異なる値を返すことも可能）。

## Compatibility

- YAYA: Tc565-1 以降

## See Also

- FUNCDECL_READ
- FUNCDECL_ERASE
