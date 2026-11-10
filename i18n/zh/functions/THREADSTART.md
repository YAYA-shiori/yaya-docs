# THREADSTART
**Category:** スレッド

## Signature
```
THREADSTART( name [, arg ... ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 要在其他线程中执行的用户自定义函数名称（字符串） |
| arg | 传递给函数的参数。可以省略。传入多个参数时，它们会依次成为 `_argv[0]`、`_argv[1]`、… |

## Returns
线程 ID（大于等于 1 的整数）。无法启动时返回负值。

| 值 | 含义 |
|----|------|
| 大于等于 1 | 已启动。之后的 `THREAD*` 函数使用此 ID |
| -1 | 不存在该名称的函数（警告 W0035） |
| -2 | 超出可同时运行的线程数（32） |
| -3 | 正在执行 unload 处理，无法创建新线程 |
| -4 | OS 无法创建线程 |
| -5 | 此构建版本不支持线程（Emscripten） |

参数不足或不是字符串时，会发出警告 W0008 / W0009 并返回 -1。

## Description
在另一个线程中运行指定函数。可用于并行执行耗时处理，而不必与 SSP 交互（`request`）。调用方不会等待线程结束，而是立即返回。

```
OnBoot
{
	work.done = 0
	work.id = THREADSTART('Work.Heavy', 1000000)
	'計算を始めました'
}

Work.Heavy
{
	_sum = 0
	for _i = 0; _i < _argv[0]; _i++ {
		_sum += _i
	}
	work.sum = _sum     // 結果はグローバル変数に書いておく
	work.done = 1
}

OnSecondChange
{
	if work.done {
		'計算が終わりました: ' + TOSTR(work.sum)
	}
}
```

接收线程结果有以下 3 种方式。

- 使用 [THREADRESULT](THREADRESULT.md) 接收函数的返回值
- 将结果写入全局变量后结束（如上例）。其他线程也共享全局变量
- 使用 [DIRECTSSTP](DIRECTSSTP.md) 通知 SSP。从工作线程中调用时，等待通信期间不会阻止其他处理

### 运行方式
- **全局变量是共享的，局部变量则彼此独立**。线程函数拥有自己的局部变量
- 同一时间只有一个线程会执行词典中的函数。工作线程会在语句边界处让出执行权，**来自 SSP 的 `request` 会优先执行**。即使工作线程正在运行，`request` 也只需等到工作线程到达下一个语句边界就能返回。这不会通过使用多个 CPU 来加快计算
- **等待外部的缓慢响应时，其他线程不会停止**。从工作线程调用的 [REQUESTLIB](REQUESTLIB.md)（SAORI）、[EXECUTE_WAIT](EXECUTE_WAIT.md)、[EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)、[DIRECTSSTP](DIRECTSSTP.md)、[SLEEP](SLEEP.md) 会在等待期间让出执行权。[THREADJOIN](THREADJOIN.md) 也一样。在 SSP 的 `request` 中调用的 `REQUESTLIB` / `EXECUTE_WAIT`，如果有工作线程正在运行，也会在等待期间让工作线程运行（`SLEEP` 在 `request` 中仍会像以往一样等待）。除这些等待操作之外的系统函数（例如处理大型文件）无法在一次调用完成前让出执行权或中断
- 最多可同时运行 32 个线程。已结束线程的记录可通过 [THREADCLOSE](THREADCLOSE.md) 清除；超过 256 条时会从最旧的记录开始删除
- 线程使用启动时的函数。函数定义（中间代码）由 SSP 的 `request` 和所有线程共享。每次调用函数时，计算表达式期间产生的值都会单独保存，因此，**多个线程可以同时执行同一个函数**（递归调用自身也一样）。启动线程时不会根据词典大小消耗内存或时间，因此无论同时运行多少个线程，增加的资源都只与线程本身使用的资源有关（在包含 2 万个函数、2.5MB 的词典中，启动约需 2ms，每个工作线程增加的内存不足 0.1MB）
- `fncdepth` 和 `looplimit` 的值会沿用启动时的设置

### 限制
- 工作线程运行期间，修改词典或函数的 [DICLOAD](DICLOAD.md)、[DICUNLOAD](DICUNLOAD.md)、[APPEND_RUNTIME_DIC](APPEND_RUNTIME_DIC.md)、[UNDEFFUNC](UNDEFFUNC.md) 会发出警告 W0032 并失败。[EVAL](EVAL.md) 可以使用
- 工作线程产生的警告和错误日志会立即写入文件，但会在下一个 `request` 中统一发送给 SSP 或检查工具（由于约定 SHIORI 回调必须在调用 `request` 的线程中执行）
- 工作线程中的 `GETLASTERROR`、`LSO`、`RE_GETSTR` 等会按线程分别保存

### unload 与中断
收到 `unload` 时，会请求所有正在运行的工作线程中断，并最多等待 5 秒。工作线程会在下一个语句边界处以与 `return` 相同的方式退出函数（[SLEEP](SLEEP.md) 的等待会立即返回）。如果线程仍未结束（例如仍在耗时系统函数中），就会作为最后手段强制停止，并发出警告 W0034。在 Windows 以外的平台上无法强制停止，因此会放弃等待正在通信等操作中等待的线程并继续执行（正在执行词典函数的线程则会一直等待到其结束）。

!!! warning "不要在工作线程中使用会长时间阻塞的函数"
    强制停止可能会破坏线程的中间状态。请将耗时处理拆分成较小的 `for` / `while` 循环，或在循环中插入 `SLEEP`。这样就能通过 [THREADSTOP](THREADSTOP.md) 或 `unload` 安全地停止线程。

## Example
启动 2 个线程，等待它们都结束，并接收返回值。

```
Work.Add
{
	_argv[0] + _argv[1]
}

Work.Both
{
	_a = THREADSTART('Work.Add', 1, 2)
	_b = THREADSTART('Work.Add', 10, 20)
	_r = THREADJOIN(_a)
	_r = THREADJOIN(_b)
	TOSTR(THREADRESULT(_a)) + ',' + TOSTR(THREADRESULT(_b))   // 3,30
}
```

## Compatibility
- Tc608-1 及更高版本
- Tc608-2：不再为每个线程复制函数表，改为所有线程共享（在 Tc608-1 中，包含 2 万个函数、2.5MB 的词典，启动约需 18ms，每个工作线程约需 13MB）。多个线程可以同时执行同一个函数

## See Also
- THREADSTATE
- THREADSTOP
- THREADJOIN
- THREADRESULT
- THREADCLOSE
- SLEEP
- DIRECTSSTP
