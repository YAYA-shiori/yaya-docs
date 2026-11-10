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
The error code (integer) from the most recent system function call. Returns 0 if there is no error.

## Description
A function that returns the error code from the most recent system function call.

## Error Codes
| Code | Meaning |
|--------|------|
| 0 | No error |
| 8 | Insufficient arguments |
| 9 | Invalid argument value |
| 10 | Empty strings cannot be processed |
| 11 | No variable available to store the result |
| 12 | Out-of-range or invalid value |
| 13 | Processing failed |
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
