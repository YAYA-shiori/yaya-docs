# GETSECCOUNT
**Category:** システム情報

## Signature
```
GETSECCOUNT( [yyyy|datetext [, mm [, dd [, wd [, HH [, MM [, SS [, timezone]]]]]]]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| yyyy | Gregorian year (4 digits) |
| mm | Month (1–12) |
| dd | Day |
| wd | Day of the week (specify 0. Any value is ignored) |
| HH | Hour |
| MM | Minute |
| SS | Second |
| timezone | (Optional) Time zone for the specified date and time. Defaults to the OS local time. The format is the same as for [GETTIME](GETTIME.md#タイムゾーンの指定) |
| datetext | Alternative specification: a date string in a format such as `'Sun, 06 Nov 1994 08:49:37 GMT'` or `'2024-01-01T09:00:00+09:00'` |

## Returns
The number of seconds elapsed from EPOCH (1970/1/1 00:00:00 UTC) to the specified date and time (or the current date and time) (number)

## Description
Returns the number of seconds elapsed from EPOCH to the current time or the specified date and time. Equivalent to the C `time()` function.

- If all arguments are omitted, the current time is used
- If some arguments are omitted, their values are filled in using the current time in `timezone`
- Values can be outside the normal date range (for example, specifying 13 for the month results in January of the following year)
- Year, month, day, and other values are interpreted as local time. To specify a date and time in UTC or another time zone, use the eighth argument, `timezone` (`GETSECCOUNT(2024,1,1,0,0,0,0,'UTC')`). Daylight saving time for local time is determined according to the rules in effect for the specified date and time

### Date strings
`datetext` can parse the following formats. The weekday in HTTP format can be omitted.

```
Sun, 06 Nov 1994 08:49:37 GMT      RFC 822 / RFC 1123
Sunday, 06-Nov-94 08:49:37 GMT     RFC 850（年が2桁のときは 70-99 が19xx、00-69 が20xx）
Sun Nov  6 08:49:37 1994           C の asctime
2024-01-01T09:00:00+09:00          ISO 8601
```

ISO 8601 can parse the following forms.

| Form | Example |
|----|----|
| Date | `2024-01-01` (time is 00:00:00) |
| Date and time | `2024-01-01T09:30`, `2024-01-01T09:30:15`, `2024-01-01 09:30:15` (`T` can also be lowercase or a space) |
| Fractional seconds | `2024-01-01T09:30:15.123` (fractional seconds are truncated) |
| Time zone | `Z`, `+09:00`, `+0900`, `+09`, `-05:00` |
| Basic format | `20240101`, `20240101T093015Z` |

Nonexistent dates (`2024-02-30`) and out-of-range times (`25:00`) cannot be parsed. `24:00:00` is treated as midnight on the following day, and a second value of `60` is treated as a leap second.

- If the date string ends with a time zone (such as `GMT`, `+0900`, `+09:00`, `-0500`, or `JST` in HTTP format, or `Z` or `+09:00` in ISO 8601), it is parsed using that time zone. The example string with `GMT` returns `784111777` regardless of the time zone of the execution environment
- Date strings without a time zone (such as the asctime format and `2024-01-01T09:00:00`) are parsed as local time
- For an unreadable string, an unrecognized month name, or a nonexistent date, warning W0012 is issued ([GETLASTERROR](GETLASTERROR.md) returns 12) and `-1` is returned. Out-of-range values are handled the same way

## Example
```
// 2006年14月25日 15:56:40 のEPOCH秒を取得し、GETTIMEで日付に変換する例
// （月14 = 翌年2月）
_array = GETTIME(GETSECCOUNT(2006, 14, 25, 0, 15, 56, 40))
"%(_array[1])月%(_array[2])日"
// 結果: "2007年2月25日" のように表示される

// UTCの日時から求める
_sec = GETSECCOUNT(2024, 1, 1, 0, 0, 0, 0, 'UTC')   // 1704067200

// ISO 8601 の文字列から求める
_sec = GETSECCOUNT('2024-01-01T09:00:00+09:00')     // 1704067200
```

## Compatibility
- Available since the initial version of YAYA
- Tc606-1 and later: Added the eighth argument, `timezone`, and ISO 8601 date strings
- Tc606-1: Fixed a bug where time zones in date strings were interpreted as local time, causing a 9-hour discrepancy in Japan time. Negative offsets such as `-0500` and two-digit years in RFC 850 format were also not parsed correctly. Unreadable strings now return `-1` and issue a warning. Also fixed the handling of years from 2100 onward as leap years, and the conversion of dates and times in time zones with daylight saving time according to the current daylight saving rules

## See Also
- GETTIME
- GETTIMEZONE
