# THREADRESULT
**Category:** スレッド

## Signature
```
THREADRESULT( id )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 返回的线程 ID |

## Returns
线程函数的返回值。

以下情况会返回空值（VOID）。

- 线程仍在运行
- 线程被中断或因错误结束（[THREADSTATE](THREADSTATE.md) 为 2 或 3）
- 不存在该 ID 对应的线程

参数不足或不是整数时，会发出警告 W0008 / W0009 并返回空值。

## Description
获取正常结束的线程函数所返回的值。当函数有多个候选项（随机选择的输出）时，获取的是线程结束时选中的那一个。

也可以不接收返回值，而改为写入全局变量。请参阅 [THREADSTART](THREADSTART.md)。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
THREADRESULT(_id)   // 7
```

## Compatibility
- Tc608-1 及以上

## See Also
- THREADSTART
- THREADJOIN
- THREADSTATE
