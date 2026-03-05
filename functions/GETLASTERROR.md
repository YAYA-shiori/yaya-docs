# GETLASTERROR
**Category:** デバッグ
**Source:** マニュアル/関数/GETLASTERROR

## Signature
```
GETLASTERROR
GETLASTERROR()
```

## Parameters
なし

## Returns
直近のシステム関数呼び出しのエラーコード（整数）。エラーがない場合は0。

## Description
直近に実行したシステム関数呼び出しのエラーコードを返す関数。

## Error Codes
| コード | 意味 |
|--------|------|
| 0 | エラーなし |
| 8 | 引数が不足している |
| 9 | 引数の値が不正 |
| 10 | 空文字列は処理できない |
| 11 | 結果を格納できる変数がない |
| 12 | 範囲外または不正な値 |
| 13 | 処理が失敗した |
| 14 | 外部ライブラリが読み込まれていない |
| 15 | ファイルが開かれていない |
| 16 | 正規表現の構文エラーまたは複雑すぎる |
| 17 | 正規表現処理中の未定義エラー |
| 18 | 変数が期待される箇所に非変数の引数が渡された |

## Example
```
SETLASTERROR(0)
// システム関数を呼び出す
if !GETLASTERROR {
    "エラーが発生しました。"
}
```

## Compatibility
- YAYA: 初期バージョンから使用可能
- AYA: バージョン5.8以降

## See Also
- SETLASTERROR
