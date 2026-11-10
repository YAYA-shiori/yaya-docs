# REQUESTLIB
**Category:** 外部ライブラリ

## Signature
```
REQUESTLIB( path , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLL 的位置。相對於 YAYA 所在位置的相對路徑，或絕對路徑。 |
| string | 傳遞給 request 函式的字串 |

## Returns
- 成功：request 函式產生的字串
- 失敗：VOID（不傳回任何內容）

## Description
呼叫預先載入的外部程式庫的 request 函式，並取得其結果。外部程式庫的 DLL 必須具有與 YAYA 相同的介面（匯出 load/unload/request 函式）。

Tc604-1 之後，若指定以 [LOADLIB](LOADLIB.md) 載入的 SAORI-basic 執行檔，YAYA 會啟動該執行檔，並傳回 SAORI/1.0 的回應（[詳細資訊](LOADLIB.md#saori-basic)）。

### 與執行緒的關係
若要等待回應較慢的外部程式庫，從 [THREADSTART](THREADSTART.md) 啟動的執行緒中呼叫它，等待期間 SSP 的 `request` 和其他執行緒仍可繼續運作。

- 外部程式庫視為一次只能由一個執行緒呼叫，因此對同一個程式庫的呼叫會依序執行。其他執行緒正在呼叫同一個程式庫時，會等到呼叫結束後才執行。不同的程式庫則可以同時呼叫
- 即使其他執行緒對正在呼叫中的程式庫執行 [UNLOADLIB](UNLOADLIB.md)，該程式庫也不會被卸載（警告 W0013）
- 外部程式庫會從 `THREADSTART` 執行緒所在的執行緒呼叫。COM 或視窗等需要由特定執行緒呼叫的 SAORI，從工作執行緒呼叫時可能無法運作
- 呼叫過程中無法中斷。[THREADSTOP](THREADSTOP.md) 會在該呼叫傳回後生效

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 版及之後的版本即可使用
- Tc604-1：開始支援 SAORI-basic 執行檔
- Tc608-1：等待期間允許其他執行緒繼續運作（有 `THREADSTART` 執行緒時）。對同一個程式庫的呼叫改為依序執行

## See Also
- LOADLIB
- UNLOADLIB
- THREADSTART
