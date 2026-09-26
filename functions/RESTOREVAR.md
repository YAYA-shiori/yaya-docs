# RESTOREVAR
**Category:** メタ操作・特殊関数

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

ファイルの形式は [SAVEVAR](SAVEVAR.md#保存形式) を参照してください。Tc600-3以降はハッシュと入れ子の値も復元できます。Tc600-3 より前のバージョンで保存したファイルもそのまま読めます。

## Compatibility
- YAYA: 初期リリースから使用可能
- Tc600-3: ハッシュと入れ子の値の復元に対応

## See Also
- SAVEVAR
