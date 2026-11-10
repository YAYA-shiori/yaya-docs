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
| locale | （可选）区域设置名称。省略时使用 C 模式（仅将 a-z 转换为 A-Z） |

## Returns
- 成功：转换后的大写字符串
- 失败：VOID

## Description
将字符串中的所有小写字母转换为大写并返回。省略 locale 时使用 C 模式（仅将 a-z 转换为 A-Z）。

locale 可以指定 `"ja-JP"`、`"tr_TR"`、`"tr_TR.UTF-8"` 等名称。转换时遵循相应区域设置的规则，也会转换非 ASCII 字符（`é`→`É`、全角英文字母等）。土耳其语（`tr-TR`）中，`i` 会转换为 `İ`。`"C"` 和 `"POSIX"` 表示 C 模式，空字符串表示使用 OS 的用户设置区域。也可以使用 [GETSETTING](GETSETTING.md) 返回的 `coreinfo.locale` 名称。

- Windows：使用 OS 的区域设置名称。也可以使用 `"Japanese_Japan.932"` 这样的 C 运行时区域设置名称
- Linux / macOS：需要使用 OS 中安装的区域设置（可通过 `locale -a` 查看）。省略字符编码的 `tr_TR` 等名称会优先查找 UTF-8 版本
- 不会影响其他处理，也不会影响进程的区域设置

如果指定了不可用的区域设置，则会发出警告 W0012（[GETLASTERROR](GETLASTERROR.md) 返回 12），并返回以 C 模式转换的结果。

## Example
```
_str = 'sAkuRa'
_str = TOUPPER( _str )
_str // 'SAKURA'
```

## Compatibility
- YAYA：从初始版本起（locale 参数从 Tc569-5 起支持）
- Tc606-1：更改了 locale 的处理方式。可以使用 `ja-JP` 这样的名称指定区域设置，并且转换时不会切换进程的区域设置。指定不可用的区域设置时会发出警告 W0012，并以 C 模式进行转换（此前不会发出警告，而是沿用当时的区域设置进行转换）
- AYA：5.8 及以后

## See Also
- TOLOWER
- TRANSLATE
