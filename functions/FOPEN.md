# FOPEN

**Category:** ファイル操作
**Source:** マニュアル/関数/FOPEN

## Signature

```
FOPEN(path, option)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | ファイル名またはフルパス。相対パスはDLLのロードディレクトリを基準とする |
| option | ファイルを開くモードを指定する文字列（下記参照） |

### テキストアクセスモード

| モード | 別名 | 動作 |
|--------|------|------|
| "r" | "read" | 読み取り専用。ファイルが存在しない場合はエラー |
| "w" | "write" | 書き込み。既存ファイルは切り詰め |
| "a" | "append" | 追記。ファイルが存在しない場合は新規作成 |

### バイナリアクセスモード

| モード | 別名 | 動作 |
|--------|------|------|
| "rb" | "read_binary" | バイナリ読み取り専用 |
| "wb" | "write_binary" | バイナリ書き込み。既存ファイルは切り詰め |
| "ab" | "write_binary_append" | バイナリ追記 |

### ランダムアクセスモード

| モード | 別名 | 動作 |
|--------|------|------|
| "r+" | "read_random" | テキスト読み書き |
| "w+" | "write_random" | テキスト読み書き。既存ファイルは切り詰め |
| "a+" | "append_random" | テキスト読み書き（追記） |
| "rb+" | "read_binary_random" | バイナリ読み書き |
| "wb+" | "write_binary_random" | バイナリ読み書き。既存ファイルは切り詰め |
| "ab+" | "append_binary_random" | バイナリ読み書き（追記） |

## Returns

- 1: 成功
- 0: 失敗
- 2: ファイルはすでに開いている

## Compatibility

- YAYA: 初回リリースから利用可能（テキストアクセスのみ）
- AYA: バージョン 5.8 以降（テキストアクセスのみ）
- バイナリ・ランダムアクセスは TC529-2 以降で追加

## See Also

- FCHARSET
- FCLOSE
- FSEEK
- FTELL
- FREAD
