# FATTRIB

**Category:** ファイル操作

## Signature

```
FATTRIB( path )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要获取各种信息的文件或目录的路径。可以指定完整路径。相对路径以 DLL 的 load 参数所传入的位置为基准 |

## Returns

返回包含 11 个元素的通用数组。失败时返回 `-1`。

| 索引 | 内容 |
|-------------|------|
| `[0]` | 可存档（仅 Windows）= 1，其他 = 0 |
| `[1]` | 已压缩（仅 Windows）= 1，其他 = 0 |
| `[2]` | 目录 = 1，其他 = 0 |
| `[3]` | 隐藏文件（仅 Windows）= 1，其他 = 0 |
| `[4]` | 普通文件 = 1，其他 = 0 |
| `[5]` | 脱机文件（仅 Windows）= 1，其他 = 0 |
| `[6]` | 只读（仅 Windows）= 1，其他 = 0 |
| `[7]` | 系统文件（仅 Windows）= 1，其他 = 0 |
| `[8]` | 临时文件（仅 Windows）= 1，其他 = 0 |
| `[9]` | 文件创建时间。UNIX 中为 inode 修改时间 |
| `[10]` | 文件的最后修改时间 |

日期时间的单位是以 1970/1/1 0 时为基准的秒数（epoch）。要转换为普通日期时间信息，可使用 `GETTIME(_attrib[10])`。

## Description

获取文件或目录的各种信息。也可以指定完整路径。对于相对路径，以 DLL 的 load 参数所传入的位置（多数情况下是 DLL 所在位置）为基准。

## Example

```
_attrib = FATTRIB('hoge.txt')
_attrib[10]          // 最終更新日時（エポック秒）
GETTIME(_attrib[10]) // 読みやすい形式に変換
```

## Compatibility

- YAYA：从初版开始支持
- AYA：5.8 及以上（但 5.8 之前的版本无法使用 [9]～[10]）

## See Also

- FSIZE
- GETTIME
