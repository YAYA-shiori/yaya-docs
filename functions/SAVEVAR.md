# SAVEVAR
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/SAVEVAR

## Signature
```
SAVEVAR( [path] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 保存先ファイル名（省略時はDLL名 + "_variable.cfg"、例: yaya_variable.cfg） |

## Returns
なし（VOID）

## Description
変数を保存します。unload時に行われる処理と同等です。

保存先ファイルを任意のパスに指定することもできます。

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- RESTOREVAR
