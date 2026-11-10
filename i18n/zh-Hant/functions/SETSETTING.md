# SETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
SETSETTING( name , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 設定資訊的項目名稱（字串）。指定基本設定檔案中的項目名稱 |
| string | 要設定的值（字串） |

## Returns
- **1**：成功
- **0**：失敗

## Description
變更執行中對話的設定資訊。此函式與 GETSETTING 相對應。

以下設定項目只有在初次載入時才有作用，因此在執行期間變更也不會生效：
- dic
- msglang
- charset.dic
- checkparser

## Compatibility
- YAYA：從初始版本起支援

## See Also
- GETSETTING
- [基本設定](../grammar/01-basic-settings.md)
