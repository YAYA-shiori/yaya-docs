# RESTOREVAR
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/RESTOREVAR

## Signature
```
RESTOREVAR( [ path ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | （省略可）復元元のファイル名。省略時はデフォルトのファイル名（DLL名 + "_variable.cfg"、例: yaya_variable.cfg）が使用される |

## Returns
VOID（戻り値なし）

## Description
変数を（ファイルから）ロード（復元）します。処理はロード時に行われる処理と同等です。指定したファイルから変数を復元できます。

## Compatibility
- YAYA: 初期リリースから使用可能

## See Also
- SAVEVAR
