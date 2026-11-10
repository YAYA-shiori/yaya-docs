# EXECUTE_CAPTURE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_CAPTURE( path [, option [, dir [, options ]]] )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| path | 要执行的文件路径。与 [EXECUTE_WAIT](EXECUTE_WAIT.md) 一样，相对路径的可靠性较低，因此建议使用绝对路径。也可以指定 PATH 中的命令名 |
| option | 传递给程序的参数（可省略）。与 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同 |
| dir | 要启动的进程的工作目录（可省略）。与 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同。省略或指定为空字符串时，不指定目录 |
| options | 指定运行方式的哈希（可省略）。使用 [IHASH](IHASH.md) 创建。使用下表中的键。省略键时采用默认行为 |

### options 的键

| 键 | 值 | 含义 |
|------|----|------|
| stdin | 字符串 | 传递给程序标准输入的内容。省略时，不传递任何内容并立即结束输入（不会因此停止一直等待输入的程序） |
| stderr | `"separate"` / `"merge"` / `"discard"` | 标准错误输出的处理方式。`"separate"`（默认）会将其与标准输出分开捕获。`"merge"` 会将其合并到标准输出中（按输出顺序写入 `stdout`，`stderr` 为空）。`"discard"` 会丢弃输出 |
| timeout | 整数（毫秒） | 如果程序在这段时间内没有结束，则终止程序并返回。0（默认）表示不限制时间 |
| maxsize | 整数（字节） | `stdout`、`stderr` 各自的上限。超过上限时会终止程序并返回。默认值为 16777216（16MiB），可指定的最大值为 1073741824 |
| charset | 字符编码名称或数值 | 传递 `stdin` 字符串，以及将 `stdout`、`stderr` 转换为字符串时使用的字符编码（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。省略或指定为空字符串时，使用操作系统默认值（Windows 为 ANSI 代码页，POSIX 为 UTF-8）。不影响 path、option、dir |

值为 VOID 的键会被视为未指定。

## Returns

返回包含以下键的哈希。

| 键 | 值 |
|------|----|
| exitcode | 程序的退出代码。无法确认程序已结束时（`"failed"`，以及程序结束前发生的 `"timeout"` / `"canceled"` / `"truncated"`）为 -1。在 POSIX 环境中因信号而结束时也为 -1 |
| stdout | 标准输出的内容（字符串） |
| stderr | 标准错误输出的内容（字符串）。当 `stderr` 选项为 `"merge"` / `"discard"` 时为空 |
| status | 结束方式。参见下表 |

| status | 含义 |
|--------|------|
| ok | 程序已结束（即使退出代码不是 0，也会是 `"ok"`） |
| timeout | 程序未能在 `timeout` 指定的时间内结束，因此已将其终止 |
| canceled | 因 [THREADSTOP](THREADSTOP.md) 或 unload 请求中断线程，因此已将程序终止 |
| truncated | `stdout` 或 `stderr` 超过了 `maxsize`，因此已将程序终止。内容会截断到 `maxsize` |
| failed | 无法启动程序（例如找不到可执行文件、工作目录不存在）。参数或选项无效时也会返回 `"failed"` |

发生 `timeout` / `canceled` / `truncated` 时，此前已捕获的输出也会放入 `stdout` / `stderr`。

## Description

启动外部程序，等待其结束，并捕获标准输出和标准错误输出。也可以向标准输入传递字符串。此函数相当于其他语言中的 `subprocess.run`（Python）、`Open3.capture3`（Ruby）和 `execFileSync`（Node.js）。

```
_r = EXECUTE_CAPTURE('cmd.exe', '/c ver')
if _r['status'] == 'ok' && _r['exitcode'] == 0 {
	_r['stdout']
}
```

以下示例会向标准输入传递内容并接收结果。

```
_in = 'b' + CHR(13,10) + 'a' + CHR(13,10)
_r = EXECUTE_CAPTURE('sort.exe', '', '', IHASH('stdin', _in))
_r['stdout']       // "a" と "b" が並ぶ
```

以下示例会将标准错误输出合并到标准输出，并在 10 秒后终止程序。

```
_r = EXECUTE_CAPTURE('tool.exe', '--run', '', IHASH('stderr', 'merge', 'timeout', 10000))
```

### 与 EXECUTE_WAIT 的区别

- **不会使用 Shell 关联**。因此，无法使用默认应用程序打开文档或 URL（如需此功能，请使用 [EXECUTE_WAIT](EXECUTE_WAIT.md) 或 [EXECUTE](EXECUTE.md)）。Windows 会直接启动可执行文件（`CreateProcess`），并传递由 `"` 括起的 `path` 后接 `option` 的命令行。也可以启动 `.bat` / `.cmd`，但不要将来自脚本外部的字符串混入 `option`。POSIX 会将命令交给 `/bin/sh -c`。实际存在的文件会被视为单个名称；如果文件不存在，则会作为 Shell 命令从 PATH 中查找
- Windows 不会打开控制台窗口
- 标准输出和标准错误输出通过管道接收，因此某些程序的输出方式（如缓冲）会与连接到终端时不同
- 不会转换换行符。Windows 程序的输出会保留为 `CRLF`
- 如果输出中包含 NUL（`\0`），字符串会在此处结束
- 无法启动程序时，不会发出警告，而是返回 `status` 为 `"failed"` 的哈希

### 等待期间的行为

- 等待期间，[THREADSTART](THREADSTART.md) 启动的线程以及来自 SSP 的 `request` 不会停止（与 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同）
- 如果线程因 [THREADSTOP](THREADSTOP.md) 或 unload 请求中断，则会先**终止程序**，再以 `"canceled"` 返回。[EXECUTE_WAIT](EXECUTE_WAIT.md) 在 Windows 中也会让已启动的程序继续运行，但此函数会将其终止。在 POSIX 中也可以中断
- 终止程序时，POSIX 会一并终止程序创建的进程组（包括 `sh -c` 启动的子进程）。Windows 只会终止已启动的进程，不会终止该进程启动的其他进程
- 程序结束后，其他进程可能仍在占用标准输出或标准错误输出（例如通过 `start` 或 `&` 启动的常驻程序）。这种情况下，输出中断 0.5 秒后就会停止读取，并以 `"ok"` 返回。无法捕获该进程之后输出的内容。如果输出持续不断，则经过 `timeout` 指定的时间或收到中断请求时，会以 `"timeout"` / `"canceled"` 返回（程序本身已经结束，因此会返回 `exitcode`）
- 向标准输入写入数据和读取标准输出、标准错误输出会并行进行，因此即使同时处理大量输入和大量输出，程序也不会与此函数相互等待

### 错误

| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| path 不存在 | W0008 | 8 |
| path、dir、options 或选项值的类型无效 | W0009 | 9 |
| `stderr` / `timeout` / `maxsize` / `charset` 的值无效 | W0012 | 12 |
| 无法将 `stdin` 转换为指定的字符编码 | W0027 | 27 |
| 无法将输出转换为字符串（该输出会变为空） | W0027 | 27 |
| options 中包含未知键（为便于发现拼写错误而发出警告。其他键仍然有效，程序会继续运行） | W0012 | 12 |

path 等无效并发出警告时，也会返回 `status` 为 `"failed"` 的哈希。

## Compatibility

- Tc608-3: 新增

## See Also

- [EXECUTE_WAIT](EXECUTE_WAIT.md)
- [EXECUTE](EXECUTE.md)
- [IHASH](IHASH.md)
- [THREADSTART](THREADSTART.md)
