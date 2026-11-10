# EXECUTE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | The path to the file or application to launch. Absolute paths are recommended, as relative paths are unreliable. |
| option | Arguments to pass to the application (optional). Used, for example, to open a URL in a browser. |
| dir | The working directory of the launched process (optional). Relative paths are based on the DLL loading directory, as with FOPEN and similar functions. If omitted or an empty string, no directory is specified. The current directory of YAYA or SSP is unchanged. |

## Returns

- On success: An integer greater than or equal to 0 (OS-dependent: the return value of ShellExecute on Windows, 0 in POSIX environments)
- On failure: -1 (including when dir is a nonexistent directory)

## Description

Passes a command string to the command processor to launch an external application or file. This is an improved version of the C language system() function and returns without waiting for the application to exit.

## Example

```
_val = EXECUTE('IEXPLORE.EXE','http://www.yahoo.co.jp/')
```

Opens the Yahoo homepage in Internet Explorer.

## Compatibility

- YAYA: Supported from the first release
- Tc604-1: Added the third argument, dir (working directory), and support for POSIX environments (previously always returned -1)

## See Also

- EXECUTE_WAIT
- [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)
