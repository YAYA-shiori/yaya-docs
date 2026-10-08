# STRENCODE
**Category:** 文字列操作

## Signature
```
STRENCODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | エンコード対象の文字列 |
| code | エンコードに使う文字コードID（省略時は0）、または文字コードの名前（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。知らない名前なら警告 W0012 を出して 0 を返す |
| type | エンコード形式。`url`（URLエンコード）、`form`（スペースを + に変換するフォームエンコード）、`base64`（Base64）を指定。省略時は `url` |

## Returns
- 成功時: エンコードされた文字列
- 失敗時: 0

## Description
指定した文字コードとエンコード形式で文字列をエンコードします。文字コードIDについては[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)を参照してください。

## Compatibility
- YAYA: Tc521-1以降（Tc532-1で `GETSTRURLENCODE` から改名）
- Tc574-8 / Tc603-1: 知らない文字コードの名前を渡すと、警告 W0012 を出して0 を返すようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also
- STRDECODE（デコード関数）
