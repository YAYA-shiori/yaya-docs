# FATTRIB

**Category:** ファイル操作

## Signature

```
FATTRIB( path )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path to the file or directory whose information you want to retrieve. A full path can be specified. Relative paths are based on the location passed to DLL load |

## Returns

Returns an 11-element generic array. Returns `-1` on failure.

| Index | Contents |
|-------------|------|
| `[0]` | Can be archived (Windows only) = 1; otherwise = 0 |
| `[1]` | Compressed (Windows only) = 1; otherwise = 0 |
| `[2]` | Directory = 1; otherwise = 0 |
| `[3]` | Hidden file (Windows only) = 1; otherwise = 0 |
| `[4]` | Normal file = 1; otherwise = 0 |
| `[5]` | Offline file (Windows only) = 1; otherwise = 0 |
| `[6]` | Read-only (Windows only) = 1; otherwise = 0 |
| `[7]` | System file (Windows only) = 1; otherwise = 0 |
| `[8]` | Temporary file (Windows only) = 1; otherwise = 0 |
| `[9]` | File creation date and time. On UNIX, the inode modification time |
| `[10]` | File's last modification date and time |

The time unit is seconds (epoch), measured from 1970/1/1 0:00. To convert this to a regular date and time, use something like `GETTIME(_attrib[10])`.

## Description

Retrieves various information about a file or directory. A full path can be specified. Relative paths are based on the location passed to DLL load (in most cases, the location of the DLL).

## Example

```
_attrib = FATTRIB('hoge.txt')
_attrib[10]          // 最終更新日時（エポック秒）
GETTIME(_attrib[10]) // 読みやすい形式に変換
```

## Compatibility

- YAYA: Supported since the initial release
- AYA: 5.8 and later (however, [9]–[10] are unavailable in versions earlier than 5.8)

## See Also

- FSIZE
- GETTIME
