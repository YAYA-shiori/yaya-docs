# GETTIMEZONE
**Category:** システム情報

## Signature
```
GETTIMEZONE( [ sec ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| sec | (Optional) Integer number of seconds elapsed since EPOCH (1970-01-01 00:00:00 UTC). If omitted, uses the current system time |

## Returns
A generic array with the following structure:

| Index | Value | Details |
|------------|---|------|
| 0 | Offset from UTC | Seconds; east is positive (Japan is `32400`). Includes daylight saving time when applicable |
| 1 | Daylight saving time flag | 0 = standard time / 1 = daylight saving time |
| 2 | Name | Windows: OS display name (`東京 (標準時)` in a Japanese environment). Linux / macOS: abbreviation (such as `JST` or `EDT`) |
| 3 | IANA name | A name such as `Asia/Tokyo`. Empty string if unavailable (same as `coreinfo.timezone` in [GETSETTING](GETSETTING.md)) |

If `sec` is outside the supported range (approximately ±900 million years), a warning W0012 is issued ([GETLASTERROR](GETLASTERROR.md) returns 12) and `-1` is returned.

## Description
Returns information about the OS local time zone for the time represented by `sec`. In time zones that observe daylight saving time, whether daylight saving time applies and the offset are determined according to the rules in effect at the time represented by `sec`.

The offset at index 0 is the same as the difference used when [GETTIME](GETTIME.md) / [GETSECCOUNT](GETSECCOUNT.md) treat a time as local time.

- Windows: The IANA name is obtained by converting the OS time zone name (`Tokyo Standard Time`) with ICU (`icu.dll`, Windows 10 1903 and later). On older versions of Windows, an empty string is returned. For Windows time zones that correspond to multiple IANA names, a representative name is returned (`Pacific Standard Time` becomes `America/Los_Angeles`)
- Linux / macOS: The IANA name is obtained from the environment variable `TZ`, or, if it is not set, the target of the `/etc/localtime` link (`.../zoneinfo/Asia/Tokyo`), or, if that is unavailable, `/etc/timezone`. If `TZ` is in POSIX format such as `JST-9`, that string is returned as is

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
- YAYA: Tc606-1 and later

## See Also
- GETTIME
- GETSECCOUNT
- GETSETTING
