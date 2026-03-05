# FMOVE

**Category:** ファイル操作
**Source:** マニュアル/関数/FMOVE

## Signature

```
FMOVE( path , dir )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 移動元のファイル名。フルパス指定可。相対パスはDLLのロード位置を基準とする |
| dir | 移動先のディレクトリ名 |

## Returns

- 成功時: 1
- 失敗時: 0

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- FCOPY
- FRENAME
- FDEL
