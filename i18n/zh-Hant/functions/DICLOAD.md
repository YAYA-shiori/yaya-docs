# DICLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICLOAD( filename [, code] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | 要讀取的辭典檔案名稱 |
| code | 字元編碼 ID 或字元編碼名稱（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。省略、空字串或 `default` 時，依照基本設定檔的設定處理。若名稱不明，會發出警告 W0012，不讀取任何內容並傳回 1 |

## Returns

- `0`：成功
- `1`：失敗

## Description

動態讀取指定的辭典檔案。

注意事項：

- 辭典有問題時會發生錯誤，且不會進行任何變更。
- 讀取的辭典要到下一次請求呼叫時才會生效，目前正在執行的函式會受到保護。
- 讀取後，字串嵌入元素的範圍展開語法將無法運作。請考慮使用能立即識別讀取之辭典內容的 EVAL。
- 讀取的辭典可以使用 DICUNLOAD 解除載入，但有一些限制。
- 透過 [THREADSTART](THREADSTART.md) 啟動的執行緒運作期間，會發出警告 W0032，不讀取任何內容並傳回 1。

## Compatibility

- YAYA：Tc556-1 以後
- Tc608-1：變更為工作執行緒運作期間無法讀取
- Tc574-8 / Tc603-1：修正以數值傳入字元編碼 ID 時遭到忽略的問題。現在傳入未知的字元編碼名稱時，會發出警告 W0012 並判定為失敗（之前會依照基本設定檔的設定讀取）

## See Also

- DICUNLOAD
- EVAL
