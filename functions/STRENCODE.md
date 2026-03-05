# STRENCODE
**Category:** 文字列操作
**Source:** マニュアル/関数/STRENCODE

## Signature
```
STRENCODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | エンコード対象の文字列 |
| code | エンコードに使う文字コードID（省略時は0） |
| type | エンコード形式。`url`（URLエンコード）、`form`（スペースを + に変換するフォームエンコード）、`base64`（Base64）を指定。省略時は `url` |

## Returns
- 成功時: エンコードされた文字列
- 失敗時: 0

## Description
指定した文字コードとエンコード形式で文字列をエンコードします。文字コードIDについてはマニュアルの文字コード一覧を参照してください。

## Compatibility
- YAYA: Tc521-1以降（Tc532-1で `GETSTRURLENCODE` から改名）

## See Also
- STRDECODE（デコード関数）
