# DIRECTSSTP

**Category:** 通信・プロセス間通信

## Signature

```
DIRECTSSTP( hwnd , request [ , charset ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| hwnd | Specify the destination window handle for DirectSSTP as an integer. |
| request | The DirectSSTP request string to send. |
| charset | The character encoding, specified by ID or text name ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). Defaults to UTF-8. |

## Returns

- On success: The DirectSSTP response string
- On failure: -1

## Description

Sends DirectSSTP to the specified hwnd and returns the result.

Returns an empty string if the destination does not respond (for example, if the destination is a window that does not return an SSTP response).

When called from a thread started with [THREADSTART](THREADSTART.md), other threads can run while it waits for a response. It will not be blocked even if SSP calls back with `request` in response to the send. This can be used to notify SSP of the processing result.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) | Return value |
|------|------|------|------|
| Too few arguments | W0008 | 8 | -1 |
| hwnd is not an integer (numeric strings are also invalid; convert it with [TOINT](TOINT.md) before passing it) | W0009 | 9 | -1 |
| hwnd is 0 or refers to a nonexistent window | W0012 | 12 | -1 |
| charset is an unknown name or invalid ID | W0012 | 12 | -1 |
| Sending failed, or the destination did not respond within 5 seconds | W0013 | 13 | -1 |

## Compatibility

- YAYA: Tc572-1 and later
- Tc574-3 / Tc602-4: Fixed the issue where a response from the destination could not be received and sending to SSP returned an empty string after waiting about 3 seconds. Nonexistent windows and send failures now return a warning and -1
- Tc574-8 / Tc603-1: Passing an unknown character encoding name or invalid ID now issues warning W0012 and returns -1 without sending (previously, UTF-8 or the OS default encoding was used)
- Tc608-1: Other threads can now run while a call from a worker thread waits for a response

## See Also

- THREADSTART
