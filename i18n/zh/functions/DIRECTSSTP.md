# DIRECTSSTP

**Category:** 通信・プロセス間通信

## Signature

```
DIRECTSSTP( hwnd , request [ , charset ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| hwnd | 以整数值指定 DirectSSTP 的目标窗口句柄。 |
| request | 要发送的 DirectSSTP 请求字符串。 |
| charset | 字符编码。以 ID 或文本格式指定（[字符编码的名称](../grammar/11-character-encoding.md#文字コードの名前)）。省略时为 UTF-8。 |

## Returns

- 成功时：DirectSSTP 响应字符串
- 失败时：-1

## Description

向指定的 hwnd 发送 DirectSSTP，并返回结果。

如果目标没有返回响应（例如目标是不返回 SSTP 响应的窗口），则返回空字符串。

从通过 [THREADSTART](THREADSTART.md) 启动的线程中调用时，在等待响应期间其他线程可以继续运行。即使 SSP 因发送而回调 `request`，也不会让调用方等待。可用于将处理结果通知 SSP。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) | 返回值 |
|------|------|------|------|
| 参数不足 | W0008 | 8 | -1 |
| hwnd 不是整数（数字字符串也不行。请用 [TOINT](TOINT.md) 转换后传入） | W0009 | 9 | -1 |
| hwnd 为 0，或窗口不存在 | W0012 | 12 | -1 |
| charset 是未知名称或无效 ID | W0012 | 12 | -1 |
| 发送失败，或目标在 5 秒内未响应 | W0013 | 13 | -1 |

## Compatibility

- YAYA：Tc572-1 及之后
- Tc574-3 / Tc602-4：修复了无法接收目标响应的问题；此前即使发送给 SSP，也会等待约 3 秒后返回空字符串。现在会以警告和 -1 返回窗口不存在或发送失败的情况
- Tc574-8 / Tc603-1：传入未知字符编码名称或无效 ID 时，现在会不发送请求并返回警告 W0012 和 -1（此前会使用 UTF-8 或操作系统默认编码发送）
- Tc608-1：从工作线程调用时，在等待响应期间其他线程可以继续运行

## See Also

- THREADSTART
