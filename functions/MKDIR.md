# MKDIR
**Category:** ファイル操作
**Source:** マニュアル/関数/MKDIR

## Signature
```
MKDIR(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 作成するディレクトリのパス |

## Returns
- 成功: 1
- 失敗: 0

## Description
ディレクトリを作成します。フルパスの指定に対応しています。相対パスの場合、基準点はDLLの位置になります。

**制限事項:** 一階層づつしか作成できません。存在しない複数階層のネストを一度に指定するとエラーになります。

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8から使用可能

## See Also
- RMDIR
