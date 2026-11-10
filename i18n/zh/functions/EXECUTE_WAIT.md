# EXECUTE_WAIT

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_WAIT( path [, option [, dir ]] )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| path | 要执行的文件或应用程序的路径。相对路径的可靠性较低，因此建议使用绝对路径。 |
| option | 传递给应用程序的参数（可省略）。例如，用于在浏览器中打开 URL。 |
| dir | 要启动的进程的工作目录（可省略）。相对路径与 FOPEN 等相同，以 DLL 的加载目录为基准。省略或指定为空字符串时，不指定目录。YAYA 或 SSP 的当前目录不会改变。 |

## Returns

- 成功时：所执行进程的退出代码。如果已将处理交给已启动的应用程序等，且没有需要等待的进程，则为 0
- 失败时：-1（包括 dir 指定了不存在的目录，以及在 POSIX 环境中因信号而结束的情况）

## Description

将命令字符串交给操作系统的命令处理器，以执行外部应用程序或文件。与 EXECUTE 不同，此函数会等待应用程序结束后再返回（同步执行）。相当于 C 语言的 system() 函数。

## Example

```
_val = EXECUTE_WAIT('CL.EXE','HELLOWORLD.C')
```

使用 C 编译器编译 HELLOWORLD.C，并等待编译完成。

从 [THREADSTART](THREADSTART.md) 启动的线程中调用时，即使正在等待外部应用程序结束，来自 SSP 的 `request` 和其他线程也不会停止。在 Windows 中，如果线程因 [THREADSTOP](THREADSTOP.md) 或 `unload` 请求中断，则会停止等待并返回 -1（已启动的应用程序会继续运行）。在 POSIX 中，会一直等待到程序结束。

## Compatibility

- YAYA: TC532-1 及更高版本
- Tc604-1: 添加第 3 个参数 dir（工作目录）。返回值改为退出代码（此前 Windows 在成功时返回 1，POSIX 环境则直接返回 system() 的返回值）
- Tc608-1: 等待期间允许其他线程运行（存在 `THREADSTART` 启动的线程时）

## See Also

- EXECUTE
- [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)（捕获标准输出和标准错误输出。也可以传递标准输入）
- THREADSTART
