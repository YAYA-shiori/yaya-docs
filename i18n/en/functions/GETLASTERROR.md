# GETLASTERROR
**Category:** デバッグ

## Signature
```
GETLASTERROR
GETLASTERROR()
```

## Parameters
None

## Returns
The error code (integer) from the most recent system function call. Returns 0 if there was no error.

## Description
Returns the error code from the most recently executed system function call.

The value returned by this function can also be set with [SETLASTERROR](SETLASTERROR.md). To reliably check for errors at a point where one might occur, first reset the value to 0 with `SETLASTERROR(0)`, then call the system function, and check `GETLASTERROR` afterward.

## Error Codes
| Code | Meaning |
|--------|------|
| 0 | No error |
| 8 | Not enough arguments |
| 9 | Invalid argument value |
| 10 | Empty strings cannot be processed |
| 11 | No variable available to store the result |
| 12 | Out of range or invalid value |
| 13 | Operation failed |
| 14 | External library has not been loaded |
| 15 | File is not open |
| 16 | Regular expression syntax error or expression is too complex |
| 17 | Undefined error during regular expression processing |
| 18 | A non-variable argument was passed where a variable was expected |

## Example
```
SETLASTERROR(0)
// システム関数を呼び出す
if !GETLASTERROR {
    "エラーが発生しました。"
}
```

## Compatibility
- YAYA: Available since the initial version
- AYA: Version 5.8 and later

## See Also
- SETLASTERROR
