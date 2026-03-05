# RMDIR
**Category:** ファイル操作
**Source:** マニュアル/関数/RMDIR

## Signature
```
RMDIR( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 削除するディレクトリのパス（フルパスまたは相対パス。相対パスはDLLロード位置が基準） |

## Returns
- **1**: 削除成功
- **0**: 失敗

## Description
ディレクトリを削除します。空のディレクトリしか削除できません。ファイルが含まれているディレクトリを削除しようとするとエラーになります。

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- MKDIR
