# GETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
GETSETTING( string )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| string | 要获取的信息标识符（下文所述字符串或基础设置的条目名称） |

## Returns
- 成功：请求的信息（字符串）
- 失败：空字符串

## Description
返回运行中的文句所设置信息的函数。

`string` 可以指定以下标识符（字符串），也可以为了向后兼容指定数值（0～4）。此外，也可以指定[基础设置](../grammar/01-basic-settings.md)的条目名称。

## Information Types
| 标识符 | 旧数值 | 获取的数据 | 示例 |
|--------|--------|----------------|-----|
| `coreinfo.version` | 0 | YAYA 的版本号 | `"Tc522-1"` |
| （数值1）          | 1 | 当前字符编码 ID（0=Shift_JIS、1=UTF-8、127=操作系统默认值） | `0` |
| `coreinfo.path`    | 2 | 目录的绝对路径 | `"c:\hogehoge\"` |
| `coreinfo.name`    | 3 | DLL 名称 | `"YAYA"` |
| `coreinfo.author`  | 4 | DLL 作者 | `"umeici/The Maintenance Shop"` |
| `coreinfo.savefile` | — | 存档文件的路径 | `"d:/ghost/konno_yayame/..."` |
| `coreinfo.mode`    | — | 运行模式 | `"normal"` 或 `"emergency"` |
| `coreinfo.locale`   | — | 操作系统用户设置中区域（数值和日期格式）的区域设置 | `"ja-JP"` |
| `coreinfo.uilocale` | — | 操作系统用户设置中显示语言的区域设置 | `"ja-JP"` |
| `coreinfo.timezone` | — | 操作系统本地时区的 IANA 名称 | `"Asia/Tokyo"` |

`coreinfo.locale` / `coreinfo.uilocale` 返回 `语言-地区` 格式（BCP 47）的名称。无法获取时返回空字符串。

- Windows：用户的默认区域设置名称（`coreinfo.uilocale` 为显示语言）
- Linux / macOS：根据环境变量确定。`coreinfo.locale` 按 `LC_ALL` → `LC_NUMERIC` → `LANG` 的顺序，`coreinfo.uilocale` 按 `LANGUAGE`（首个语言）→ `LC_ALL` → `LC_MESSAGES` → `LANG` 的顺序，取第一个已设置的值。`ja_JP.UTF-8` 会转换为 `ja-JP`。`C` / `POSIX` 或未设置时返回空字符串
- 返回的名称可直接传递给 [TOUPPER](TOUPPER.md) / [TOLOWER](TOLOWER.md) 的区域设置参数

`coreinfo.timezone` 返回类似 `Asia/Tokyo` 的 IANA 时区名称。无法获取时返回空字符串。

- Windows：使用 ICU（`icu.dll`，Windows 10 1903 及以上版本）转换操作系统的时区名称。更早版本的 Windows 返回空字符串
- Linux / macOS：使用环境变量 `TZ`；未设置时使用 `/etc/localtime` 的链接目标；若该文件也不存在，则使用 `/etc/timezone`。`TZ` 为 `JST-9` 这样的 POSIX 格式时，会原样返回该字符串
- 包含夏令时和偏移量的信息可通过 [GETTIMEZONE](GETTIMEZONE.md) 获取

## Compatibility
- YAYA：从初始版本起可用。`coreinfo.mode` 于 Tc556-2 添加，`coreinfo.locale` / `coreinfo.uilocale` / `coreinfo.timezone` 于 Tc606-1 添加
- AYA：5.8 及以上版本（仅支持数值参数 0～4）

## See Also
- SETSETTING
- [基础设置](../grammar/01-basic-settings.md)
