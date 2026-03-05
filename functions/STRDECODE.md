# STRDECODE
**Category:** 文字列操作
**Source:** マニュアル/関数/STRDECODE

## Signature
```
STRDECODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | デコード対象の文字列 |
| code | 変換に使う文字コードID（省略時は0） |
| type | デコード形式。`url`（URLエンコード）または `base64`（Base64）を指定。省略時は `url` |

## Returns
- 成功時: デコードされた文字列
- 失敗時: 0

## Description
指定した文字コードとエンコード形式で文字列をデコードします。文字コードIDについてはマニュアルの文字コード一覧を参照してください。

## Compatibility
- YAYA: Tc521-1以降（Tc532-1で `GETSTRURLDE­CODE` から改名）

## See Also
- STRENCODE（エンコード関数）
