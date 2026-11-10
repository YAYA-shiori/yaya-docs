# FOPEN

**Category:** ファイル操作

## Signature

```
FOPEN(path, option)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | File name. A full path can be specified. Relative paths are resolved from the location passed to DLL load |
| option | Specifies how to open the file. Specify a string from the “Mode” or “Alias” column below |

### Text Access

| Mode | Alias | Behavior | If the file exists | If the file does not exist |
|--------|------|-------------|--------------------|--------------------|
| `"r"` | `"read"` | Read text | Success | Error |
| `"w"` | `"write"` | Write text | Set size to 0 (overwrite) | Create new file |
| `"a"` | `"append"` | Append text | Append to the end | Create new file |

### Binary Access

| Mode | Alias | Behavior | If the file exists | If the file does not exist |
|--------|------|-------------|--------------------|--------------------|
| `"rb"` | `"read_binary"` | Read binary data | Success | Error |
| `"wb"` | `"write_binary"` | Write binary data | Set size to 0 (overwrite) | Create new file |
| `"ab"` | `"write_binary_append"` | Append binary data | Append to the end | Create new file |

### Random Access

| Mode | Alias | Behavior | If the file exists | If the file does not exist |
|--------|------|-------------|--------------------|--------------------|
| `"r+"` | `"read_random"` | Read and write text | Success | Error |
| `"w+"` | `"write_random"` | Read and write text | Set size to 0 (overwrite) | Create new file |
| `"a+"` | `"append_random"` | Read and write text | Append to the end | Create new file |
| `"rb+"` | `"read_binary_random"` | Read and write binary data | Success | Error |
| `"wb+"` | `"write_binary_random"` | Read and write binary data | Set size to 0 (overwrite) | Create new file |
| `"ab+"` | `"append_binary_random"` | Read and write binary data | Append to the end | Create new file |

## Returns

- 1: Success
- 0: Failure
- 2: File is already open

## Description

Open a file.

- You must open a file with `FOPEN` before reading from or writing to it
- For text access, you can change the character encoding by calling [FCHARSET](FCHARSET.md) before `FOPEN`
- In short, this works the same as C's `fopen`. YAYA also implements this using C's `fopen`
- For text access, the sequence 0x0d-0x0a (CR-LF) is converted to a single 0x0a before reading. Conversely, when writing, 0x0a is converted to 0x0d-0x0a. Also, 0x1a has a special meaning as EOF
- For random access, use [FSEEK](FSEEK.md) to specify the file position for reading, and [FTELL](FTELL.md) to get the position

## Compatibility

- YAYA: Available since the initial release (text access only)
- AYA: Version 5.8 and later (text access only)
- TC529-2: Added binary access and random access

## See Also

- FCHARSET
- FCLOSE
- FSEEK
- FTELL
- FREAD
