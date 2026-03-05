# FDIGEST

**Category:** ファイル操作
**Source:** マニュアル/関数/FDIGEST

## Signature

```
FDIGEST(path, type)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | ダイジェスト値を計算するファイルのパス。フルパス指定可。相対パスはDLLのロード位置を基準とする |
| type | ハッシュアルゴリズムの種類。"CRC32"（32ビットCRC）、"MD5"、"SHA-1"/"SHA1"のいずれか |

## Returns

- 成功時: ダイジェスト値を16進数文字列で返す
- 失敗時（ファイルが存在しない・値の生成に失敗した場合）: -1

## Compatibility

- YAYA: Tc527-1 で初回リリース。Tc530-1 で CRC32 サポートを追加

## See Also

- STRDIGEST
