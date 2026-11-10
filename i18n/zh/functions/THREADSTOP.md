# THREADSTOP
**Category:** スレッド

## Signature
```
THREADSTOP( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 返回的线程 ID |

## Returns
| 值 | 含义 |
|----|------|
| 1 | 已请求中断 |
| 0 | 该线程已经结束 |
| -1 | 不存在该 ID 的线程 |

参数不足或不是整数时，会发出警告 W0008 / W0009 并返回 -1。

## Description
请求中断线程。此函数不会等待线程结束，而是立即返回。要确认线程是否结束，请使用 [THREADSTATE](THREADSTATE.md) 或 [THREADJOIN](THREADJOIN.md)。

线程会在下一个语句边界处（包括 `while` / `for` 每次循环的边界）以与 `return` 相同的方式退出当前函数，调用方函数也会以同样的方式退出，随后线程结束。正在通过 [SLEEP](SLEEP.md) 或 [THREADJOIN](THREADJOIN.md) 等待的线程会中止等待并返回。被中断的线程状态为 2，[THREADRESULT](THREADRESULT.md) 会返回空值。

在一次系统函数调用的过程中（例如处理大型正则表达式、`REQUESTLIB` 等）无法停止线程；该调用结束后才会停止。

## Example
```
OnClose
{
	_r = THREADSTOP(work.id)
	_r = THREADJOIN(work.id, 2000)   // 2 秒まで終わりを待つ
}
```

## Compatibility
- Tc608-1 及更高版本

## See Also
- THREADSTART
- THREADSTATE
- THREADJOIN
- THREADCLOSE
