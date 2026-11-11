# DICLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICLOAD( filename [, code] )
```

## Parameters

| 參數 | 說明 |
|-----------|-------------|
| filename | 要讀取的辭典檔案名稱 |
| code | 字元編碼 ID，或字元編碼名稱（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。省略、空字串或 `default` 時，會依照基本設定檔中的設定處理。若名稱不明，會顯示警告 W0012，不讀取任何內容並傳回 1 |

## Returns

- `0`：成功
- `1`：失敗

## Description

動態讀取指定的辭典檔案。

注意事項：

- 若辭典有問題，便會發生錯誤，且不會進行任何變更。
- 讀取的辭典要到下一次呼叫 request 時才會生效，目前正在執行的函式則會受到保護。
- 字串嵌入元素的[範圍限定展開](../grammar/06-string-embedding.md#範囲付き展開)在 DICLOAD 後無法運作。請考慮使用能立即識別已讀取辭典內容的 EVAL。
- 讀取的辭典可以透過 DICUNLOAD 卸載，但有一些限制。
- 透過 [THREADSTART](THREADSTART.md) 啟動的執行緒正在執行時，會顯示警告 W0032，不讀取任何內容並傳回 1。

## Compatibility

- YAYA：Tc556-1 以後
- Tc608-1：改為在工作執行緒執行期間無法讀取
- Tc574-8 / Tc603-1：修正以數值傳入字元編碼 ID 時遭到忽略的問題。現在若傳入不明的字元編碼名稱，會顯示警告 W0012 並以失敗結束（此前會依照基本設定檔中的設定讀取）

## See Also

- DICUNLOAD
- EVAL
