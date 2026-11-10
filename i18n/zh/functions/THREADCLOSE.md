# THREADCLOSE
**Category:** スレッド

## Signature
```
THREADCLOSE( id )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 返回的线程 ID |

## Returns
| 值 | 含义 |
|----|------|
| 0 | 丢弃已结束线程的记录 |
| 1 | 线程仍在运行，因此请求中断。线程结束后丢弃记录 |
| -1 | 不存在该 ID 对应的线程 |

参数不足或不是整数时，会发出警告 W0008 / W0009 并返回 -1。

## Description
丢弃线程的记录（状态和返回值）。对于正在运行的线程，会像 [THREADSTOP](THREADSTOP.md) 一样请求中断，并在线程结束时丢弃记录。丢弃后，将该 ID 传递给 [THREADSTATE](THREADSTATE.md) 等函数时会返回 -1。

即使不主动丢弃，已结束线程的记录超过 256 条时，也会从最旧的记录开始删除。使用完线程的结果后，主动丢弃记录即可避免其继续保留。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
_v = THREADRESULT(_id)
_r = THREADCLOSE(_id)
```

## Compatibility
- Tc608-1 及以上

## See Also
- THREADSTART
- THREADSTOP
- THREADSTATE
