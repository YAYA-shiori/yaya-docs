# GETTIME
**Category:** システム情報

## Signature
```
GETTIME( [ sec [, timezone ] ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| sec | (Optional) Integer number of seconds elapsed since EPOCH (1970-01-01 00:00:00 UTC). If omitted, returns the current system time |
| timezone | (Optional) Time zone to use when calculating the date and time. If omitted, uses the OS local time ([Specifying a time zone](#タイムゾーンの指定)) |

## Returns
A generic array with the following structure:

| Index | Value | Details |
|------------|---|------|
| 0 | Year | Gregorian calendar year |
| 1 | Month | Month |
| 2 | Day | Day |
| 3 | Day of week | 0–6 (0 = Sunday) |
| 4 | Hour | 24-hour format |
| 5 | Minute | Minute |
| 6 | Second | Second |
| 7 | Day of year | Number of days elapsed since the start of the year (January 1 is 0) |
| 8 | Daylight saving time flag | 0 = standard time / 1 = daylight saving time |

If `sec` is outside the supported range (approximately ±900 million years), a warning W0012 is issued ([GETLASTERROR](GETLASTERROR.md) returns 12) and `-1` is returned.

## Description
Gets the current date and time information. When `timezone` is omitted, the function behaves like the C `localtime` function.

If `sec` is specified, it is interpreted as the number of seconds elapsed since EPOCH, and the corresponding date and time information is returned. This can be used, for example, to calculate the date 10 days from now by combining it with GETSECCOUNT.

For local time, daylight saving time is determined according to the rules in effect at the time represented by `sec` (not whether it is currently daylight saving time).

### Specifying a time zone
Specify one of the following for `timezone`.

| Value | Meaning |
|------|------|
| Omitted, `""`, `"local"` | OS local time |
| `"UTC"`, `"GMT"`, `"Z"` | UTC |
| `"+09:00"`, `"+0900"`, `"+09"`, `"-5"` | Fixed offset from UTC (hours and minutes; east is positive) |
| `"JST"`, `"EST"`, `"EDT"`, `"CST"`, `"CDT"`, `"MST"`, `"MDT"`, `"PST"`, `"PDT"` | Fixed offset specified by name |
| Integer | Fixed offset from UTC (**seconds**, east is positive; `32400` is `+09:00`). Less than ±24 hours |

When a fixed offset is specified, daylight saving time is not taken into account, and the daylight saving time flag (index 8) is always 0. If the value cannot be interpreted, a warning W0012 is issued (GETLASTERROR returns 12), and the value is treated as local time.

## Example

The current time's `sec` value can be obtained with [GETSECCOUNT](GETSECCOUNT.md). This makes it easy to calculate a time a specified number of days in the future or past.

```
//10日後は何月何日？
_array = GETTIME()
"今は%(_array[0])年%(_array[1])月%(_array[2])日　%(_array[4])時%(_array[5])分%(_array[6])秒／"
--
_array = GETTIME(GETSECCOUNT(_array[0],_array[1],_array[2] + 10,0,_array[4],_array[5],_array[6]))
"10日後は%(_array[0])年%(_array[1])月%(_array[2])日　%(_array[4])時%(_array[5])分%(_array[6])秒\n"
```

```
// UTCでの日時
_utc = GETTIME(GETSECCOUNT(), 'UTC')

// 1970/1/1 00:00:00 UTC は、日本時間（+09:00）では 9時
_jst = GETTIME(0, '+09:00')      // 1970,1,1,4,9,0,0,0,0
```

## Compatibility
- YAYA: Available since the initial release
  - Tc542-1 and later: Day of year (index 7) and daylight saving time flag (index 8) added
  - Tc606-1 and later: `timezone` parameter added
- Tc606-1: Fixed the day-of-year value on Windows, which had counted January 1 as 1, to start at 0 like `localtime`. Also changed the daylight saving time flag and the time in time zones where daylight saving time varies by date to be determined based on `sec` rather than the current time
- AYA 5.8: Only supports calls with no arguments

## See Also
- GETSECCOUNT
- GETTIMEZONE
- GETTICKCOUNT
- GETTYPE
