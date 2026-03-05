# SUBSTR
**Category:** 文字列操作
**Source:** マニュアル/関数/SUBSTR

## Signature
```
SUBSTR(src, pos, len)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 取得元の文字列 |
| pos | 取得開始位置（0始まり。負の値は末尾からのオフセット） |
| len | 取得する文字数 |

## Returns
- 成功時: 取得した部分文字列
- pos が文字列長を超える場合: 空文字列 `""`
- pos + len が文字列末尾を超える場合: 末尾まで取得
- エラー時: VOID

## Description
文字列から部分文字列を取り出します。`pos` に負の値を指定した場合は文字列の末尾からのオフセットとして扱われます（例: -2 は末尾から2番目の文字）。

## Example
```
SUBSTR("HOGE", -2, 1)  // 結果: "G"（末尾から2番目の文字）
```

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降（ただし負の pos 値は非対応）

## See Also
- STRSTR（部分文字列検索）
- STRLEN（文字列長取得）
