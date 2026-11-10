# THREADSTATE
**Category:** スレッド

## Signature
```
THREADSTATE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 傳回的執行緒 ID |

## Returns
表示執行緒狀態的整數。

| 值 | 意義 |
|----|------|
| -1 | 沒有該 ID 的執行緒（已透過 [THREADCLOSE](THREADCLOSE.md) 捨棄，或舊紀錄已刪除） |
| 0 | 執行中（包含等待執行順序） |
| 1 | 已執行完函式並結束 |
| 2 | 已中斷（[THREADSTOP](THREADSTOP.md)、[THREADCLOSE](THREADCLOSE.md)、unload） |
| 3 | 因錯誤而結束（包含遭強制停止的執行緒） |

引數不足或不是整數時，會發出警告 W0008 / W0009 並傳回 -1。

## Description
檢查執行緒是否正在執行或已結束。此函式會立即返回，不會等待，因此適合在 `OnSecondChange` 等事件中反覆確認。若要等到執行緒結束，請使用 [THREADJOIN](THREADJOIN.md)。

!!! note "避免阻塞 SSP 的回應"
    若在主機的 `request` 中長時間等待 [THREADJOIN](THREADJOIN.md)，SSP 的回應會停止。要回應 SSP 時，請使用 `THREADSTATE` 檢查；若尚未結束，請留待下次再處理。

## Example
```
OnSecondChange
{
	if THREADSTATE(work.id) == 1 {
		'終わりました: ' + TOSTR(THREADRESULT(work.id))
	}
}
```

## Compatibility
- Tc608-1 以後

## See Also
- THREADSTART
- THREADJOIN
- THREADRESULT
