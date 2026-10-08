# STRDECODE
**Category:** 文字列操作

## Signature
```
STRDECODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | デコード対象の文字列 |
| code | 変換に使う文字コードID（省略時は0）、または文字コードの名前（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。知らない名前なら警告 W0012 を出して 0 を返す |
| type | デコード形式。`url`（URLエンコード）または `base64`（Base64）を指定。省略時は `url` |

## Returns
- 成功時: デコードされた文字列
- 失敗時: 0

## Description
指定した文字コードとエンコード形式で文字列をデコードします。文字コードIDについては[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)を参照してください。

## Compatibility
- YAYA: Tc521-1以降（Tc532-1で `GETSTRURLDECODE` から改名）
- Tc574-8 / Tc603-1: 知らない文字コードの名前を渡すと、警告 W0012 を出して0 を返すようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also
- STRENCODE（エンコード関数）
