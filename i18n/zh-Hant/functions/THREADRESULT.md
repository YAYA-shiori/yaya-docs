# THREADRESULT
**Category:** スレッド

## Signature
```
THREADRESULT( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 傳回的執行緒 ID |

## Returns
執行緒函式的傳回值。

下列情況會傳回空值（VOID）。

- 執行緒仍在執行
- 執行緒遭到中斷或因錯誤結束（[THREADSTATE](THREADSTATE.md) 為 2 或 3）
- 沒有該 ID 的執行緒

引數不足或不是整數時，會發出警告 W0008 / W0009 並傳回空值。

## Description
取得正常結束的執行緒函式所傳回的值。若函式有多個候選結果（隨機選擇的輸出），則會取得結束時選出的其中一個結果。

也可以不接收傳回值，改為寫入全域變數。請參閱 [THREADSTART](THREADSTART.md)。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
THREADRESULT(_id)   // 7
```

## Compatibility
- Tc608-1 以後

## See Also
- THREADSTART
- THREADJOIN
- THREADSTATE
