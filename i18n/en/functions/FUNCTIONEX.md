# FUNCTIONEX
**Category:** 外部ライブラリ

## Signature
```
FUNCTIONEX( 'path' , 'Argument0', 'Argument1', ... )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Specify the path of the SAORI to call, relative to yaya.dll. For SAORI-universal, specify a DLL; for SAORI-basic, specify an executable file (Tc604-1 or later) |
| Argument* | Arguments to SAORI. For SAORI-basic, these become command-line arguments to the executable |

## Returns
- For SAORI-universal: Returns the value of Result. At the same time, the SAORI-universal Value data is stored in the `valueex` array
- For SAORI-basic: Returns standard output. If there are multiple lines, they are joined with the four characters `\r\n`; each line is stored separately in the `valueex` array (Tc604-1 or later)

## Description
A function that runs a SAORI module (external plugin).

This is not a system function; it is defined in the system dictionary (yaya_shiori3.dic) and calls SAORI using [LOADLIB](LOADLIB.md) and [REQUESTLIB](REQUESTLIB.md).

It supports both SAORI-universal and SAORI-basic. For SAORI-universal, Result is returned as the return value, and the Value data is stored in the `valueex` array.

For SAORI-basic, YAYA itself runs the executable from Tc604-1 onward, so you can specify the executable path as-is (it also works in POSIX environments). For details on how to run it, see [LOADLIB](LOADLIB.md#saori-basic).

```
_result = FUNCTIONEX('SAORI\sample.exe', 'はろーわーるど')
```

In earlier versions, call it through a SAORI-universal such as proxy_ex.dll (specify the path to proxy_ex.dll as path, the path to the SAORI-basic executable as Argument0, and any arguments to SAORI-basic after that).

When `path` begins with `internal_` (such as `internal_crypto`), it calls a module built into the baseware (SSP 2.9.13 or later) via DIRECTSSTP (SAORI over DirectSSTP), without loading a DLL. Returns 0 if unavailable. For details, see [yaya_shiori3.dic](../system/yaya-shiori3-dic.md#ベースウェアの内蔵モジュールsaori-over-directsstp).

For details on how to use SAORI, see the Tips section “Using SAORI.”

## Compatibility
- Available since the earliest versions of YAYA
- Tc604-1: Added the ability to specify a SAORI-basic executable directly (before this, it had to be called through proxy_ex.dll or a similar module)

## See Also
- [Using SAORI](../tips/saori-usage.md)
- LOADLIB
- REQUESTLIB
