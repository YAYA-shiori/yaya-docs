# GETSTRBYTES
**Category:** 文字列操作

## Signature
```
GETSTRBYTES( string [ , code ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要計算位元組數的目標字串 |
| code | 字元編碼 ID（省略時為 0），或字元編碼名稱（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。依指定的編碼計算位元組數。若名稱無法辨識，會發出警告 W0012 並傳回 0 |

## Returns
- 成功時：儲存字串所需的位元組數（整數）
- 失敗時：0

## Description
計算「儲存字串所需的位元組數」的函式。可用來查詢各種字元編碼所需的記憶體用量。

## Compatibility
- YAYA：從初期版本開始即可使用
- AYA：5.8 以後
- Tc574-8 / Tc603-1：傳入無法辨識的字元編碼名稱時，會發出警告 W0012 並傳回 0（此前不會發出警告，而是視為 OS 預設編碼）

## See Also
- GETSETTING
- GETSYSTEMFUNCLIST
