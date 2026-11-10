# LOADLIB
**Category:** 外部ライブラリ

## Signature
```
LOADLIB(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the DLL or SAORI-basic executable (Tc604-1 and later) to load. Specify a path relative to the YAYA directory or an absolute path |

## Returns
- 1: Load succeeded
- 2: Already loaded
- 0: Load failed

## Description
Loads an external library (DLL) file. On the first call only, it runs LoadLibrary and calls the load function. The external DLL must have the same interface as YAYA (exporting the load/unload/request functions).

### SAORI-basic

From Tc604-1 onward, specifying a file other than a DLL treats it as a SAORI-basic executable (an executable that takes command-line arguments and writes results to standard output). Whether a file is a DLL is determined by its extension.

- Windows: Anything other than `.dll` and files with no extension (such as `.exe`)
- POSIX environments: Anything other than `.dll` `.so` `.dylib` `.bundle` (including files with no extension)

When loading, YAYA only checks whether the file exists (and, in POSIX environments, whether it can be executed); it does not run the file. Each time you pass a SAORI/1.0 request to [REQUESTLIB](REQUESTLIB.md), YAYA starts the executable and generates a response. No proxy_ex.dll or similar file is needed.

- `EXECUTE SAORI/1.0`: Starts the executable with Argument0, Argument1, ... passed as individual command-line arguments (arguments containing spaces or `"` are not split. In POSIX environments, no shell is used)
    - The working directory is the directory containing the executable. Standard input and standard error are not connected
    - After removing trailing newlines from standard output, returns `200 OK` with the lines joined in Result by the 4 characters `\r\n`, and each line placed in Value0, Value1, ... . If the output is empty, returns `204 No Content`
    - If the process does not finish within 10 seconds or the output reaches 16 MB, the process is forcibly terminated and `500 Internal Server Error` is returned. A failure to start the process also returns 500
    - Requests whose SecurityLevel is not local are rejected with `400 Bad Request`
- `GET Version SAORI/1.0`: YAYA returns `200 OK`

The character encoding for arguments and standard output follows the [CHARSETLIBEX](CHARSETLIBEX.md) setting. The default is charset.extension, as with other SAORI modules, but SAORI-basic uses UTF-8 in POSIX environments. On Windows, arguments are passed as Unicode regardless of the character encoding.

## Compatibility
- YAYA: Available since the initial version
- AYA: Available from version 5.8 onward
- Tc604-1: Added support for loading SAORI-basic executables

## See Also
- REQUESTLIB
- UNLOADLIB
- FUNCTIONEX
