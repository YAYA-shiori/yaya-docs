# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | 要設定的字元編碼 ID，或字元編碼名稱（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。若名稱無法識別，會顯示警告 W0012，且不變更設定 |

## Returns

沒有傳回值（VOID）。

## Description

指定讀寫檔案時使用的字元編碼。必須在 FOPEN 之前呼叫。可以為各個檔案變更字元編碼，字元編碼會在呼叫 FOPEN 時決定。設定會在人格目前的工作階段中維持不變，結束後則會重設。若未呼叫 FCHARSET，預設字元編碼會依照基本設定檔案中的 charset.file 或 charset 設定。

使用 UTF-8 時，讀取檔案若在檔案開頭找到 BOM（Byte Order Mark），會自動移除。以 UTF-8 寫入時不會寫入 BOM。

## Compatibility

- YAYA：自初版起支援
- AYA：5.8 以後
- Tc574-8 / Tc603-1：傳入無法識別的字元編碼名稱時，改為顯示警告 W0012 且不變更設定（此前不會顯示警告，而是視為作業系統預設值）

## See Also

- FOPEN
- FCLOSE
- FATTRIB
