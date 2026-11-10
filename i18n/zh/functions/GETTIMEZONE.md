# GETTIMEZONE
**Category:** システム情報

## Signature
```
GETTIMEZONE( [ sec ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| sec | （可选）从 EPOCH（1970年1月1日 00:00:00 UTC）起经过的秒数（整数）。省略时使用当前系统时间 |

## Returns
返回具有以下结构的通用数组：

| 索引 | 值 | 详情 |
|------------|---|------|
| 0 | 相对于 UTC 的偏移量 | 秒。东为正（日本为 `32400`）。夏令时期间的值包含夏令时偏移 |
| 1 | 夏令时标志 | 0=标准时间 / 1=夏令时 |
| 2 | 名称 | Windows：OS 的显示名称（日语环境中为 `東京 (標準時)`）。Linux / macOS：缩写（如 `JST`、`EDT`） |
| 3 | IANA 名称 | 类似 `Asia/Tokyo` 的名称。无法获取时为空字符串（与 [GETSETTING](GETSETTING.md) 的 `coreinfo.timezone` 相同） |

如果 `sec` 超出可处理范围（约±9亿年），则会发出警告 W0012（[GETLASTERROR](GETLASTERROR.md) 为 12），并返回 `-1`。

## Description
返回 OS 本地时区在 `sec` 所在时刻的信息。对于采用夏令时的时区，是否处于夏令时以及偏移量均根据 `sec` 所在时刻的规则确定。

索引0中的偏移量，与 [GETTIME](GETTIME.md) / [GETSECCOUNT](GETSECCOUNT.md) 按本地时间处理时使用的差值相同。

- Windows：IANA 名称通过 ICU（`icu.dll`，Windows 10 1903 及之后版本）将 OS 时区名称（`Tokyo Standard Time`）转换得到。更旧版本的 Windows 返回空字符串。对应多个 IANA 名称的 Windows 时区会使用其中的代表名称（`Pacific Standard Time` 对应 `America/Los_Angeles`）
- Linux / macOS：IANA 名称依次从环境变量 `TZ`、`/etc/localtime` 的链接目标（`.../zoneinfo/Asia/Tokyo`），或 `/etc/timezone` 中获取。`TZ` 为 `JST-9` 这样的 POSIX 格式时，会直接返回该字符串

## Example
```
// 今のローカルタイムゾーン
_tz = GETTIMEZONE()
_tz[0]   // 32400
_tz[3]   // 'Asia/Tokyo'

// 夏時間のある地域で、ある日時のオフセット（秒）を求める
GETTIMEZONE(GETSECCOUNT(2024, 7, 1, 0, 12, 0, 0))[0]
```

## Compatibility
- YAYA：Tc606-1 及之后

## See Also
- GETTIME
- GETSECCOUNT
- GETSETTING
