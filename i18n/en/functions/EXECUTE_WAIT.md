# EXECUTE_WAIT

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_WAIT( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path of the file or application to execute. Relative paths are unreliable, so using an absolute path is recommended. |
| option | Arguments to pass to the application (optional). Used, for example, to open a URL in a browser. |
| dir | Working directory of the process to launch (optional). Relative paths are based on the DLL loading directory, as with FOPEN and similar functions. If omitted or an empty string, no directory is specified. The current directory of YAYA or SSP does not change. |

## Returns

- On success: Exit code of the launched process. Returns 0 if there is no process to wait for, such as when the request is passed to an already running application
- On failure: -1 (also returned if dir is a nonexistent directory or if the process terminates due to a signal in a POSIX environment)

## Description

Passes a command string to the OS command processor to execute an external application or file. Unlike EXECUTE, this function returns only after the application exits (synchronous execution). It corresponds to the C function system().

## Example

```
_val = EXECUTE_WAIT('CL.EXE','HELLOWORLD.C')
```

Compiles HELLOWORLD.C with a C compiler and waits for it to finish.

When called from a thread started with [THREADSTART](THREADSTART.md), `request`s from SSP and other threads continue running while the function waits for the external application to exit. On Windows, if the thread is requested to stop by [THREADSTOP](THREADSTOP.md) or `unload`, it stops waiting and returns -1 (the launched application continues running). On POSIX, it waits until the application exits.

## Compatibility

- YAYA: TC532-1 and later
- Tc604-1: Added the third argument, dir (working directory). Changed the return value to the exit code (previously, it returned 1 on success on Windows, and returned the value of system() as-is in a POSIX environment)
- Tc608-1: Allows other threads to run while waiting (when a thread started with `THREADSTART` is running)

## See Also

- EXECUTE
- [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md) (captures standard output and standard error output. Can also pass standard input)
- THREADSTART
