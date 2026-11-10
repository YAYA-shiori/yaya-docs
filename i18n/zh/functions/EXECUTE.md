# EXECUTE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要启动的文件或应用程序的路径。相对路径的可靠性较低，因此建议使用绝对路径。 |
| option | 传递给应用程序的参数（可省略）。用于在浏览器中打开 URL 等情况。 |
| dir | 启动进程的工作目录（可省略）。相对路径与 FOPEN 等相同，以 DLL 的加载目录为基准。省略或指定空字符串时不指定目录。YAYA 或 SSP 的当前目录不会改变。 |

## Returns

- 成功时：大于等于 0 的整数（取决于操作系统。在 Windows 中为 ShellExecute 的返回值，在 POSIX 环境中为 0）
- 失败时：-1（包括 dir 指定的目录不存在的情况）

## Description

将命令字符串传递给命令处理器，以启动外部应用程序或文件。这是经过改进的 C 语言 system() 函数，会在应用程序结束前返回，不会等待应用程序结束。

## Example

```
_val = EXECUTE('IEXPLORE.EXE','http://www.yahoo.co.jp/')
```

使用 Internet Explorer 打开 Yahoo 主页。

## Compatibility

- YAYA：从初版开始支持
- Tc604-1：新增第 3 个参数 dir（工作目录）。新增对 POSIX 环境的支持（此前始终返回 -1）

## See Also

- EXECUTE_WAIT
- [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)
