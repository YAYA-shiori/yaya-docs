# THREADCLOSE
**Category:** スレッド

## Signature
```
THREADCLOSE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 傳回的執行緒 ID |

## Returns
| 值 | 意義 |
|----|------|
| 0 | 丟棄已結束執行緒的記錄 |
| 1 | 執行緒仍在執行，因此要求中斷；結束後會丟棄記錄 |
| -1 | 沒有該 ID 的執行緒 |

引數不足或不是整數時，會發出警告 W0008 / W0009 並傳回 -1。

## Description
丟棄執行緒的記錄（狀態和傳回值）。對仍在執行的執行緒，會像 [THREADSTOP](THREADSTOP.md) 一樣要求中斷，並在執行緒結束時丟棄記錄。丟棄後，將該 ID 傳給 [THREADSTATE](THREADSTATE.md) 等函式時會得到 -1。

即使不丟棄，已結束執行緒的記錄超過 256 筆時，也會從最舊的記錄開始刪除。使用完結果的執行緒，最好將其記錄丟棄，以免記錄繼續保留。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
_v = THREADRESULT(_id)
_r = THREADCLOSE(_id)
```

## Compatibility
- Tc608-1 以後

## See Also
- THREADSTART
- THREADSTOP
- THREADSTATE
