# DICUNLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICUNLOAD( filename )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | 要解除載入的辭典檔案名稱 |

## Returns

- `0`：成功
- `1`：失敗

## Description

解除載入指定辭典檔案所包含的函式和 globaldefine 群組。辭典檔案有問題時會發生錯誤，且不會有任何變更。若辭典包含其他辭典正在使用的函式，則無法解除載入。

透過 [THREADSTART](THREADSTART.md) 啟動的執行緒運作期間，會發出警告 W0032，不進行任何操作並傳回 1。

## Compatibility

- YAYA：Tc561-1 以後
- Tc608-1：變更為工作執行緒運作期間無法解除載入

## See Also

- DICLOAD
- UNDEFFUNC
- UNDEFGLOBALDEFINE
