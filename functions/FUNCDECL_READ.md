# FUNCDECL_READ

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/FUNCDECL_READ

## Signature

```
FUNCDECL_READ(variable_name, function_name)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| variable_name | 監視対象の変数名 |
| function_name | 変数読み取り時に実行する関数名。空文字列（`''`）を指定すると登録解除 |

## Returns

- 成功時: 1
- 失敗時: 0

変数が読み取られるたびに、指定した関数が自動的に呼び出される（変数の読み取り時に自動的に実行される関数を指定します）。呼び出される関数の引数は以下の通り:

- `_argv[0]`: 変数名
- `_argv[1]`: 変数の現在の値

呼び出された関数は、実際に取得する値を返す必要がある（現在の値と異なる値を返すことも可能）。

## Compatibility

- YAYA: Tc565-1 以降

## See Also

- FUNCDECL_WRITE
- FUNCDECL_ERASE
