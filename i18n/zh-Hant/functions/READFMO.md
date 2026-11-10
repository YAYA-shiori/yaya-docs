# READFMO
**Category:** システム情報

!!! warning "僅限 Windows"
    此函式只能在為 Windows 編譯的 yaya 中運作。

## Signature
```
READFMO( [ name ] [ , charset ] )
```

## Parameters
| 引數 | 說明 |
|-----------|-------------|
| name | （可省略）FMO 識別碼。省略時為 "Sakura" |
| charset | （可省略）字元編碼（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。省略時使用 OS 預設值。於 Tc569-13 新增。若值無效，會顯示警告 W0012，且不傳回任何內容 |

## Returns
- 成功：以字串形式傳回 FMO 內容
- 失敗：VOID（不傳回任何內容）

## Description
以字串形式取得檔案對應物件（FMO）的內容。FMO 的前 4 個位元組是表示大小的無號整數，讀取時會移除這 4 個位元組。若 FMO 內含 null 位元組（0x00），其行為未定義。

## Compatibility
- YAYA：於版本 Tc524-1 引入
- Tc574-8 / Tc603-1：傳入不明字元編碼名稱或無效 ID 時，會顯示警告 W0012，且不傳回任何內容（在此之前會以 OS 預設值讀取）
