# THREADSTATE
**Category:** スレッド

## Signature
```
THREADSTATE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 返回的线程 ID |

## Returns
表示线程状态的整数。

| 值 | 含义 |
|----|------|
| -1 | 不存在该 ID 的线程（已通过 [THREADCLOSE](THREADCLOSE.md) 清除，或旧记录已被删除） |
| 0 | 正在运行（包括等待执行的情况） |
| 1 | 已执行完函数并结束 |
| 2 | 已中断（[THREADSTOP](THREADSTOP.md)、[THREADCLOSE](THREADCLOSE.md)、unload） |
| 3 | 因错误而结束（包括被强制停止的线程） |

参数不足或不是整数时，会发出警告 W0008 / W0009 并返回 -1。

## Description
检查线程是否正在运行或已经结束。此函数会立即返回，不会等待，因此适合在 `OnSecondChange` 等事件中反复检查。要等待线程结束时，请使用 [THREADJOIN](THREADJOIN.md)。

!!! note "避免阻塞 SSP 的响应"
    在宿主的 `request` 中长时间等待 [THREADJOIN](THREADJOIN.md)，会阻塞 SSP 的响应。在需要向 SSP 返回的处理中，请使用 `THREADSTATE` 检查；如果线程尚未结束，就留到下次处理机会再检查。

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
- Tc608-1 及更高版本

## See Also
- THREADSTART
- THREADJOIN
- THREADRESULT
