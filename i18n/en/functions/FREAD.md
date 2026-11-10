# FREAD

**Category:** ファイル操作

## Signature

```
FREAD(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Relative path to the file specified with FOPEN (relative to yaya.dll) |

## Returns

- On success: The string containing the one line read (line-ending characters such as CR and LF are removed). Converted from the character encoding specified by FCHARSET to YAYA's internal encoding
- On reaching the end of the file: -1
- On failure: Empty string

You must open the file with FOPEN beforehand.

## Description

Read one line from a file.

- You must open the file with `FOPEN` before calling `FREAD`
- The character encoding is converted from the encoding specified by `FCHARSET` to YAYA's internal encoding
- Line-ending characters (CR, LF) at the end of the line are removed

### Note

If you write code like the following to detect EOF, a line containing only `-1` in the file may be mistaken for EOF, causing reading to stop.

```
_line = FREAD(_filename);
if(_line == -1) { break; }
```

You can avoid this by writing the following instead.

```
_line = FREAD(_filename);
if(GETTYPE(_line) == 1 && _line == -1) { break; }
```

The EOF value `-1` is an integer, while `"-1"` read from a file is a string. Use [GETTYPE](GETTYPE.md) to check the value's type, and treat it as EOF only when it is the integer `-1`.

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- FWRITE
- FREADBIN
- FOPEN
- FREADENCODE
- FWRITE2
- FCHARSET
