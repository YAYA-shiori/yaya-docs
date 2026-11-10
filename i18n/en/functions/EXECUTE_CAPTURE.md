# EXECUTE_CAPTURE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_CAPTURE( path [, option [, dir [, options ]]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path of the file to execute. As with [EXECUTE_WAIT](EXECUTE_WAIT.md), relative paths are unreliable, so using an absolute path is recommended. You can also specify a command name found in PATH |
| option | Arguments to pass to the program (optional). Same as [EXECUTE_WAIT](EXECUTE_WAIT.md) |
| dir | Working directory of the process to start (optional). Same as [EXECUTE_WAIT](EXECUTE_WAIT.md). If omitted or an empty string, no directory is specified |
| options | Hash specifying behavior (optional). Create it with [IHASH](IHASH.md). Use the keys in the table below. Omitted keys use their default behavior |

### Keys in options

| Key | Value | Meaning |
|------|----|------|
| stdin | string | Content to pass to the program's standard input. If omitted, nothing is passed and input ends immediately (this will not stop programs that continue waiting for input) |
| stderr | `"separate"` / `"merge"` / `"discard"` | How to handle standard error output. `"separate"` (default) captures it separately from standard output. `"merge"` combines it with standard output (it is placed in `stdout` in the order it was output, and `stderr` is empty). `"discard"` discards it |
| timeout | Integer (milliseconds) | If the program does not finish within this time, terminate it and return. 0 (default) means no limit |
| maxsize | Integer (bytes) | Limit for each of `stdout` and `stderr`. If exceeded, terminate the program and return. The default is 16777216 (16MiB), and the maximum value you can specify is 1073741824 |
| charset | Character encoding name or number | Character encoding used when passing the `stdin` string and converting `stdout` and `stderr` to strings ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If omitted or an empty string, the OS default is used (the ANSI code page on Windows, UTF-8 on POSIX). This does not affect path, option, or dir |

Keys whose value is VOID are treated as if they were not specified.

## Returns

A hash with the following keys.

| Key | Value |
|------|----|
| exitcode | The program's exit code. -1 if completion could not be confirmed (`"failed"`, or `"timeout"` / `"canceled"` / `"truncated"` before the program ended). Also -1 if the program was terminated by a signal in a POSIX environment |
| stdout | Standard output content (string) |
| stderr | Standard error output content (string). Empty when the `stderr` option is `"merge"` / `"discard"` |
| status | How the program ended. See the table below |

| status | Meaning |
|--------|------|
| ok | The program finished (the status is `"ok"` even if the exit code is not 0) |
| timeout | The program did not finish within the `timeout` period, so it was terminated |
| canceled | The thread was asked to stop by [THREADSTOP](THREADSTOP.md) or unload, so the program was terminated |
| truncated | The program was terminated because `stdout` or `stderr` exceeded `maxsize`. The content is truncated to `maxsize` |
| failed | The program could not be started (for example, the executable was not found or the working directory does not exist). Also returns `"failed"` if an argument or option is invalid |

Output captured up to that point is included in `stdout` / `stderr` even when the status is `timeout` / `canceled` / `truncated`.

## Description

Starts an external program, waits for it to finish, and captures its standard output and standard error output. You can also pass a string to its standard input. This function corresponds to `subprocess.run` (Python), `Open3.capture3` (Ruby), and `execFileSync` (Node.js) in other languages.

```
_r = EXECUTE_CAPTURE('cmd.exe', '/c ver')
if _r['status'] == 'ok' && _r['exitcode'] == 0 {
	_r['stdout']
}
```

Example of passing input to standard input and receiving the result.

```
_in = 'b' + CHR(13,10) + 'a' + CHR(13,10)
_r = EXECUTE_CAPTURE('sort.exe', '', '', IHASH('stdin', _in))
_r['stdout']       // "a" と "b" が並ぶ
```

Example of merging standard error output with standard output and stopping after 10 seconds.

```
_r = EXECUTE_CAPTURE('tool.exe', '--run', '', IHASH('stderr', 'merge', 'timeout', 10000))
```

### Differences from EXECUTE_WAIT

- **Shell associations are not used**. You cannot open documents or URLs with their default applications (use [EXECUTE_WAIT](EXECUTE_WAIT.md) or [EXECUTE](EXECUTE.md) for that). On Windows, the executable is started directly (`CreateProcess`), and the command line passed consists of `path` enclosed in `"` followed by `option`. You can also start `.bat` / `.cmd` files, but do not combine strings from outside the script with `option`. On POSIX, the command is passed to `/bin/sh -c`. Existing files are treated as a single name; if the file does not exist, it is searched for in PATH as a shell command
- On Windows, no console window is opened
- Standard output and standard error output are captured through pipes, so some programs may output differently (for example, due to buffering) than when connected to a terminal
- Line breaks are not converted. Output from Windows programs remains `CRLF`
- If the output contains NUL (`\0`), the string ends there
- If the program could not be started, a hash with `status` set to `"failed"` is returned without a warning

### Behavior while waiting

- While waiting, threads started by [THREADSTART](THREADSTART.md) and `request`s from SSP are not blocked (same as [EXECUTE_WAIT](EXECUTE_WAIT.md))
- If the thread is asked to stop by [THREADSTOP](THREADSTOP.md) or unload, the **program is terminated** before the function returns with `"canceled"`. [EXECUTE_WAIT](EXECUTE_WAIT.md) leaves the started program running even on Windows, but this function terminates it. It can also be interrupted on POSIX
- When terminating the program, POSIX terminates the entire process group created by the program (including child processes started by `sh -c`). Windows terminates only the started process, not other processes started by it
- After the program ends, another process may still hold standard output or standard error open (for example, a resident program started with `start` or `&`). In that case, reading stops 0.5 seconds after output ceases, and the function returns `"ok"`. Output produced by that process later cannot be captured. If output continues without stopping, the function returns `"timeout"` / `"canceled"` when the `timeout` period elapses or an interruption is requested (the program itself has already ended, so `exitcode` is returned)
- Writing to standard input and reading from standard output and standard error are done concurrently, so the program and this function will not block waiting on each other when handling large input and output at the same time

### Errors

| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| path is missing | W0008 | 8 |
| The type of path, dir, options, or an option value is invalid | W0009 | 9 |
| The value of `stderr` / `timeout` / `maxsize` / `charset` is invalid | W0012 | 12 |
| `stdin` cannot be converted to the specified character encoding | W0027 | 27 |
| Output cannot be converted to a string (that output will be empty) | W0027 | 27 |
| options contains an unknown key (a warning is issued to help catch typos. Other keys remain valid, and execution continues) | W0012 | 12 |

Even when invalid path or other values cause a warning, a hash with `status` set to `"failed"` is returned.

## Compatibility

- Tc608-3: Added

## See Also

- [EXECUTE_WAIT](EXECUTE_WAIT.md)
- [EXECUTE](EXECUTE.md)
- [IHASH](IHASH.md)
- [THREADSTART](THREADSTART.md)
