# SLEEP
**Category:** デバッグ

## Signature
```
SLEEP(millisecond)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| millisecond | 等待时间（毫秒） |

## Returns
- 成功时：0
- 失败时：-1

## Description
将处理暂停指定的毫秒数。

指定较长的等待时间会导致整个应用程序冻结，因此建议仅用于短时间等待或调试。

从通过 [THREADSTART](THREADSTART.md) 启动的线程调用时，等待期间其他线程（包括来自 SSP 的 `request`）可以继续运行。如果收到 [THREADSTOP](THREADSTOP.md) 或 `unload` 发出的中断请求，会在等待过程中提前返回。

## Compatibility
- YAYA：Tc564-1 及之后
- Tc608-1：从工作线程调用时，等待期间其他线程可以继续运行；收到中断时会提前返回

## See Also
- THREADSTART
