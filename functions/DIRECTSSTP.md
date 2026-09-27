# DIRECTSSTP

**Category:** 通信・プロセス間通信

## Signature

```
DIRECTSSTP( hwnd , request [ , charset ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| hwnd | DirectSSTPの送信先ウィンドウハンドルを整数値で指定。 |
| request | 送信するDirectSSTPリクエスト文字列。 |
| charset | 文字コード。IDまたはテキスト形式で指定。省略時はUTF-8。 |

## Returns

- 成功時: DirectSSTPのレスポンス文字列
- 失敗時: -1

## Description

指定したhwndにDirectSSTPを送信し、結果を返します。

送信先が応答を返さなかった場合（送信先がSSTPの応答を返さないウインドウだった場合など）は、空文字列を返します。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) | 返り値 |
|------|------|------|------|
| 引数が足りない | W0008 | 8 | -1 |
| hwnd が整数でない（数字の文字列も不可。[TOINT](TOINT.md) で変換して渡す） | W0009 | 9 | -1 |
| hwnd が 0、もしくは存在しないウインドウ | W0012 | 12 | -1 |
| 送信に失敗した、もしくは送信先が5秒以内に応答しなかった | W0013 | 13 | -1 |

## Compatibility

- YAYA: Tc572-1以降
- Tc574-3 / Tc602-4: 送信先からの応答を受け取れず、SSPに送っても約3秒待ったうえで空文字列を返していたのを修正。存在しないウインドウと送信の失敗を警告と -1 で返すようにした
