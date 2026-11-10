# PARSEHEADER
**Category:** 型取得/変換

## Signature
```
PARSEHEADER( str [, conv ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTTP 或 SHIORI 等格式的头部字符串 |
| conv | 可省略。非 0 时，根据与 [TOAUTOEX](TOAUTOEX.md) 相同的规则将值转换为整数或实数。省略时为 0（不转换） |

## Returns
- 成功时：返回具有以下键的哈希
- 失败时：空（VOID）

| 键 | 内容 |
|------|------|
| `start` | 起始行（例如 `GET SHIORI/3.0` 或 `HTTP/1.1 200 OK`）。没有起始行时为空字符串 |
| `header` | 头部的键→值哈希。存在多个相同键时，保留最后出现的值 |
| `key` | 头部键的数组（按出现顺序，包含重复项） |
| `value` | 头部值的数组（按出现顺序）。`conv` 非 0 时，保存转换后的值 |
| `rawvalue` | 转换前的值（字符串）数组（按出现顺序） |
| `body` | 空行之后的字符串。没有空行时为空字符串 |

## Description
解析类似 HTTP、SHIORI、SAORI 或 SSTP 请求／响应的字符串，其格式为“起始行 + `键: 值` 行 + 空行 + 正文”，并将结果整理为哈希和数组后返回。与逐行使用 [STRSTR](STRSTR.md) 或 [SUBSTR](SUBSTR.md) 截取相比，速度更快。

- 换行符可以是 CRLF 或 LF
- 在第一个空行处结束头部，其后的所有内容都成为 `body`
- 每行以第一个 `:` 分隔为键和值。值会跳过 `:` 后紧接的一个空白字符（空格或制表符），其余空白字符会原样保留（`Key:  a` 的值为 ` a`）
- 第一个 `:` 之前为空，或包含空白字符的行，不视为头部行。若此类行是第 1 行，则作为起始行放入 `start`；若是第 2 行或之后的行，则忽略。因此，也可以解析没有起始行、仅包含头部的字符串
- 键区分大小写
- 当 `conv` 设为非 0 时，转换规则与 [TOAUTOEX](TOAUTOEX.md) 相同，只有在转换回字符串后与原值一致时才会进行转换。`12` 会变为整数，而 `007` 和 `1.5` 会保持为字符串

`header` 哈希会按键排序，因此需要按出现顺序处理时，请使用 `key` / `value` / `rawvalue`。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串 | W0009 | 9 |

## Example
```
request
{
	_r = PARSEHEADER(_argv[0], 1)
	// _argv[0] が
	//   GET SHIORI/3.0
	//   Charset: UTF-8
	//   ID: OnBoot
	//   Reference0: 12
	//   Reference1: 007
	// のとき

	_r["start"]                 // GET SHIORI/3.0
	_r["header"]["ID"]          // OnBoot
	_r["header"]["Reference0"]  // 12（整数）
	_r["header"]["Reference1"]  // 007（文字列）
	_r["key"]                   // Charset,ID,Reference0,Reference1
	_r["rawvalue"][2]           // 12（文字列）
}
```

```
_nl = CHR(13) + CHR(10)
_r = PARSEHEADER('HTTP/1.1 200 OK' + _nl + 'Content-Type: text/plain' + _nl + _nl + 'hello')
_r["start"]                     // HTTP/1.1 200 OK
_r["header"]["Content-Type"]    // text/plain
_r["body"]                      // hello
```

对于与 500 系共用的词典，可以通过 `#ifdef __AYA_SYSTEM_SYSFUNC_PARSEHEADER__` 判断是否可用，并据此编写不同内容（[预处理](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)）。

## Compatibility
- YAYA：Tc602-3 及更高版本

## See Also
- [TOAUTOEX](TOAUTOEX.md)
- [HASH_SPLIT](HASH_SPLIT.md)
- [PARSEJSON](PARSEJSON.md)
- [SPLIT](SPLIT.md)
