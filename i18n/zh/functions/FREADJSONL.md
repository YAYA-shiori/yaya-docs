# FREADJSONL
**Category:** ファイル操作

## Signature
```
FREADJSONL( path [, start [, maxlines [, key ...]]] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| path | 要读取的 JSON Lines 文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| start | 开始读取的字节位置（可省略，默认为 0）。如果指向行中间，则跳过该行，从下一行开始读取（[从行中间读取](#行の途中から読む)）。范围为 0 至 2147483647 |
| maxlines | 读取行数的上限（可省略，默认为 0，表示读到文件末尾）。空行和无法解析的行也计入行数 |
| key | 要提取的键（可省略，可指定任意多个）。如果每行的顶层是对象，则只返回这些键的值（[指定键读取](#キーを指定して読む)）。只能是字符串 |

## Returns
- 成功时: 包含以下键的哈希
  - `rows`: 可解析为 JSON 的各行的值组成的数组（转换方式与 [FREADJSON](FREADJSON.md#値の対応) 相同）
  - `pos`: 与 `rows` 各元素对应的行首字节位置组成的数组（顺序与 `rows` 相同）
  - `end`: 读取结束的位置。继续读取时，将其传给 `start`
  - `skipped`: 无法解析为 JSON 而跳过的行数
- 失败时: 空（VOID）

## Description
读取 JSON Lines 文件（每行包含一个 JSON 的文本文件，扩展名为 `.jsonl`），返回由各行的值组成的数组。无需事先用 [FOPEN](FOPEN.md) 打开文件。

结果与使用 [FREAD](FREAD.md) 逐行读取并用 [PARSEJSON](PARSEJSON.md) 解析相同，但由于以 UTF-8 编码一次读取文件并逐行解析，不必按行数重复调用函数和转换字符串，因此速度更快。适合读取对话记录或历史记录等行数增长到数万行且不断追加内容的文件。

- 字符编码仅支持 UTF-8，忽略开头的 BOM
- 行分隔符为 LF，忽略行尾的 CR，跳过仅含空白字符的行
- 无法解析为 JSON 的行会被跳过，不发出警告，并计入 `skipped`。顶层不是对象或数组的行（如 `42`），只要能解析也会放入 `rows`
- 不能写 `/* */` 或 `//` 注释（JSON Lines 不支持注释，这与 [FREADJSON](FREADJSON.md) 不同）
- `pos` 中的位置是从文件开头起算的字节数，与 [FSEEK](FSEEK.md) 和 [FTELL](FTELL.md) 使用的位置相同

### 最后一行尚未写完时
如果最后一行不是以换行符结尾，只要能解析为 JSON 就读取该行；否则不读取并保留该行（因为可能有其他程序正在写入）。此时 `end` 指向该行的开头。将 `end` 传给下一次的 `start`，即可在写入完成后从该行开始读取。

### 从行中间读取
如果 `start` 前一个字节不是换行符，则将 `start` 视为位于行中间，并丢弃最初的一个（不完整的）行。只想读取文件末尾时，可以传入从 `FSIZE` 减去要读取的字节数所得的位置。如果 `start` 位于行首（0、上次的 `end` 或 `pos` 的值），则从该行开始读取。

如果 `start` 大于或等于文件大小，则不读取任何内容，`rows` 和 `pos` 为空数组，`end` 为 `start`。

### 指定键读取
指定 `key` 后，如果某行的顶层是对象，则只将这些键的值放入哈希，再放入 `rows`。虽然会解析整行 JSON，但结果转换（字符串转换和哈希创建）只针对指定的键进行，因此从包含请求正文等大型值的行中只提取时间等信息时速度更快，结果也更小。

- 只能指定顶层的键。不能用 `.` 指向下层（`"a.b"` 指的是名称中包含 `.` 的键）
- 行中不存在的键不会在结果哈希中创建。值为 `null` 的键与转换整行时一样，以 VOID 值保留
- 对于顶层不是对象的行，不使用 `key`，而是转换整行
- 也可以通过数组传递键（作为函数参数时，外层数组会展开）。可以写成 `FREADJSONL("a.jsonl", 0, 0, _keys)`

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串；start、maxlines 不是整数；key 不是字符串 | W0009 | 9 |
| start 为负数或超过 2147483647；maxlines 为负数 | W0012 | 12 |
| 无法打开文件 | W0025 | 25 |

## Example
history.jsonl:
```
{"display":"こんにちは","timestamp":1790311762291,"project":"C:\\work\\a"}
{"display":"つづき","timestamp":1790311800000,"project":"C:\\work\\b"}
```

```
_r = FREADJSONL("history.jsonl", 0, 0, "timestamp", "project")
_r["rows"][0]["project"]    // C:\work\a
_r["rows"][1]["timestamp"]  // 1790311800000
_r["pos"][1]                // 2 行目の頭のバイト位置
_r["skipped"]               // 0
```

只读取新增内容（记住 `end`，并在下次调用时传给 `start`）:
```
if GETTYPE(lastpos) == 0 {
    lastpos = 0
}
_r = FREADJSONL("history.jsonl", lastpos, 0, "timestamp", "project")
lastpos = _r["end"]
foreach _r["rows"]; _row {
    // 新しく書き足された行だけが順に入る
}
```

## Compatibility
- Tc608-6: 新增

## See Also
- [FREADJSON](FREADJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [FREAD](FREAD.md)
- [FSEEK](FSEEK.md)
