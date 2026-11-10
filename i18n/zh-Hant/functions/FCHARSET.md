# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| 引數 | 說明 |
|-----------|-------------|
| code | 要設定的字元編碼 ID，或字元編碼名稱（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。若名稱未知，會發出警告 W0012，且不變更設定 |

## Returns

沒有傳回值（VOID）。

## Description

指定讀寫檔案時使用的字元編碼。必須在 FOPEN 之前呼叫。可以針對每個檔案變更字元編碼；字元編碼會在呼叫 FOPEN 時決定。設定會在人格目前的工作階段中維持，但結束後便會重設。若未呼叫 FCHARSET，預設字元編碼會依照基本設定檔中的 charset.file 或 charset 設定。

## Compatibility

- YAYA: 自初版起支援
- AYA: 5.8 以後
- Tc574-8 / Tc603-1: 傳入未知的字元編碼名稱時，會發出警告 W0012，且不變更設定（此前不會發出警告，而是視為 OS 預設值）

## See Also

- FOPEN
- FCLOSE
- FATTRIB
