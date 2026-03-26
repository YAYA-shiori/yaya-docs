# DIRECTSSTP

**Category:** 通信・プロセス間通信
**Source:** マニュアル/関数/DIRECTSSTP

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

## Compatibility

- YAYA: Tc572-1以降
