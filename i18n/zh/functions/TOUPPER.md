# TOUPPER
**Category:** 文字列操作

## Signature
```
TOUPPER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要转换的字符串 |
| locale | （可省略）区域设置名称。省略时使用 C 模式（仅将 a-z 转换为 A-Z） |

## Returns
- 成功：转换后的大写字符串
- 失败：VOID

## Description
将字符串中的所有小写字母转换为大写字母并返回。省略 locale 时使用 C 模式（仅将 a-z 转换为 A-Z）。

locale 的格式与 [setlocale 可用的区域设置字符串](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setlocale-wsetlocale)相同。locale 可指定 `"ja-JP"`、`"tr_TR"`、`"tr_TR.UTF-8"` 等名称。会按照该区域设置的规则进行转换，非 ASCII 字符（`é`→`É`、全角英文字母等）也会转换。在土耳其语（`tr-TR`）中，`i` 会变为 `İ`。`"C"` 和 `"POSIX"` 表示 C 模式，空字符串表示使用操作系统的用户设置区域。也可以使用 [GETSETTING](GETSETTING.md) 的 `coreinfo.locale` 返回的名称。

- Windows：使用操作系统的区域设置名称。也可以使用 `"Japanese_Japan.932"` 这样的 C 运行库区域设置名称
- Linux / macOS：必须使用操作系统中已安装的区域设置（可通过 `locale -a` 查看）。省略字符编码时（例如 `tr_TR`），会优先查找 UTF-8 版本
- 不会影响其他处理，也不会影响进程的区域设置

指定无法使用的区域设置时，会发出警告 W0012（[GETLASTERROR](GETLASTERROR.md) 为 12），并返回使用 C 模式转换的结果。

## Example
```
_str = 'sAkuRa'
_str = TOUPPER( _str )
_str // 'SAKURA'
```

## Compatibility
- YAYA：从初始版本起可用（locale 参数自 Tc569-5 起可用）
- Tc606-1：更改了 locale 的处理方式。可以使用 `ja-JP` 这样的名称指定区域设置，并且无需切换进程的区域设置即可进行转换。指定无法使用的区域设置时，会发出警告 W0012 并使用 C 模式进行转换（此前不会发出警告，而是使用当时的区域设置进行转换）
- AYA：5.8 及以上版本

## See Also
- TOLOWER
- TRANSLATE
