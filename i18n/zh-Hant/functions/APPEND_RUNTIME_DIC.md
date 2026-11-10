# APPEND_RUNTIME_DIC

**Category:** メタ操作・特殊関数

## Signature

```
APPEND_RUNTIME_DIC(dic_content)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| dic_content | 與辭典檔案內容相同的字串。可包含多行內容或函式定義 |

## Returns

成功時：0
失敗時：-1

## Description

對名為 `_RUNTIME_DIC_` 的記憶體內辭典，寫入 `dic_content` 的內容，會產生相同的效果。可以動態定義新的使用者自訂函式等。`dic_content` 可包含多行內容或函式定義，其行為與從檔案讀取辭典相同。

在透過 [THREADSTART](THREADSTART.md) 啟動的執行緒運作期間，會顯示警告 W0032，不新增任何內容並傳回 -1。

## Compatibility

- YAYA：Tc562-1 以後
- Tc608-1：變更為工作執行緒運作期間無法新增內容

## See Also

- EVAL
- ISEVALUABLE
