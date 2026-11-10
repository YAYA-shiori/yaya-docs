# GETENV
**Category:** システム情報

## Signature
```
GETENV( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 要取得的環境變數名稱（字串） |

## Returns
- 成功：環境變數的內容（字串）
- 失敗：空字串

## Description
依名稱取得 OS 環境變數的函式。指定的環境變數不存在時，會傳回空字串。不可省略引數；若省略，會顯示警告（W0008）並傳回空字串。

此外，設定環境變數的函式若使用不慎可能造成危險，因此目前沒有實作計畫。

## Compatibility
- YAYA：Tc552-1 之後
