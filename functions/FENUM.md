# FENUM

**Category:** ファイル操作
**Source:** マニュアル/関数/FENUM

## Signature

```
FENUM( path [ , delim ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 列挙するディレクトリのパス。フルパス指定可。相対パスはDLLのロード位置を基準とする |
| delim | 区切り文字列（省略時はカンマ） |

## Returns

- 成功時: ファイル名とディレクトリ名を区切り文字で連結した文字列。ディレクトリ名にはバックスラッシュのプレフィックスが付く
- 失敗時: VOID（空）

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降
