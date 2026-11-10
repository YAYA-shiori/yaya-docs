# DIRECTSSTP

**Category:** 通信・プロセス間通信

## Signature

```
DIRECTSSTP( hwnd , request [ , charset ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| hwnd | 以整數指定 DirectSSTP 的目的視窗控制代碼。 |
| request | 要傳送的 DirectSSTP 請求字串。 |
| charset | 字元編碼。以 ID 或文字形式指定（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。省略時為 UTF-8。 |

## Returns

- 成功時：DirectSSTP 的回應字串
- 失敗時：-1

## Description

將 DirectSSTP 傳送至指定的 hwnd，並傳回結果。

如果目的端未傳回回應（例如目的端是無法回應 SSTP 的視窗），則傳回空字串。

從以 [THREADSTART](THREADSTART.md) 啟動的執行緒呼叫時，等待回應期間其他執行緒仍可執行。即使 SSP 因應傳送而回呼 `request`，也不會造成等待。可用來將處理結果通知 SSP。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) | 傳回值 |
|------|------|------|------|
| 引數不足 | W0008 | 8 | -1 |
| hwnd 不是整數（數字字串也不行。請使用 [TOINT](TOINT.md) 轉換後再傳入） | W0009 | 9 | -1 |
| hwnd 為 0，或是不存在的視窗 | W0012 | 12 | -1 |
| charset 是未知名稱或無效的 ID | W0012 | 12 | -1 |
| 傳送失敗，或目的端在 5 秒內沒有回應 | W0013 | 13 | -1 |

## Compatibility

- YAYA：Tc572-1 以後
- Tc574-3 / Tc602-4：修正了無法接收目的端回應的問題；即使傳送至 SSP，也會等待約 3 秒後才傳回空字串。現在會以警告和 -1 傳回視窗不存在或傳送失敗的狀況
- Tc574-8 / Tc603-1：傳入未知的字元編碼名稱或無效的 ID 時，改為不傳送，並傳回警告 W0012 和 -1（此前會以 UTF-8 或 OS 預設值傳送）
- Tc608-1：從工作執行緒呼叫時，等待回應期間其他執行緒仍可執行

## See Also

- THREADSTART
