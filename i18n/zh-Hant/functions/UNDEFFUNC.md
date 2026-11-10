# UNDEFFUNC
**Category:** メタ操作・特殊関数

## Signature
```
UNDEFFUNC( funcname )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| funcname | 要解除載入的函式名稱 |

## Returns
- 0：成功
- 1：失敗

## Description
解除載入指定的函式。

如果解除載入會造成辭典檔案發生問題，則會產生錯誤，不會進行任何操作。此外，已被其他位置參照的函式無法解除載入。

由 [THREADSTART](THREADSTART.md) 啟動的執行緒仍在執行時，會發出警告 W0032，不進行任何操作並傳回 1。

## Compatibility
- YAYA：Tc561-1 以後
- Tc608-1：變更為工作執行緒執行期間無法解除載入

## See Also
- DICUNLOAD
- UNDEFGLOBALDEFINE
