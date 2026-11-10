# STRDECODE
**Category:** 文字列操作

## Signature
```
STRDECODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要解碼的字串 |
| code | 用於轉換的字元編碼 ID（省略時為 0），或字元編碼名稱（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。如果名稱不明，會顯示警告 W0012 並傳回 0 |
| type | 解碼格式。指定 `url`（URL 編碼）或 `base64`（Base64）。省略時為 `url` |

## Returns
- 成功時：解碼後的字串
- 失敗時：0

## Description
使用指定的字元編碼和編碼格式解碼字串。字元編碼 ID 請參閱[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)。

## Compatibility
- YAYA：Tc521-1 之後（Tc532-1 時由 `GETSTRURLDECODE` 更名）
- Tc574-8 / Tc603-1：傳入不明的字元編碼名稱時，會顯示警告 W0012 並傳回 0（此前不會顯示警告，而是將其視為 OS 預設值）

## See Also
- STRENCODE（編碼函式）
