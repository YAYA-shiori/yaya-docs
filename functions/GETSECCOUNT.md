# GETSECCOUNT
**Category:** システム情報
**Source:** マニュアル/関数/GETSECCOUNT

## Signature
```
GETSECCOUNT( [yyyy|datetext [, mm [, dd [, wd [, HH [, MM [, SS]]]]]]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| yyyy | 西暦年（4桁） |
| mm | 月（1〜12） |
| dd | 日 |
| wd | 曜日（0を指定。どんな値でも無視される） |
| HH | 時 |
| MM | 分 |
| SS | 秒 |
| datetext | 代替指定: `'Sun, 06 Nov 1994 08:49:37 GMT'` 形式の日付文字列 |

## Returns
EPOCH（1970/1/1 00:00:00 UTC）から指定日時（または現在日時）までの経過秒数（数値）

## Description
EPOCHから現在時刻または指定日時までの経過秒数を返す関数。C言語の`time()`関数に相当する。

- 引数をすべて省略した場合は現在時刻を使用する
- 一部を省略した場合、省略した値は現在時刻の値で補完される
- 値は通常の日付範囲外でもよい（例: 月に13を指定すると翌年の1月になる）
- 日付文字列にタイムゾーン情報が含まれている場合はそれをパースする

## Example
```
// 2006年14月25日 15:56:40 のEPOCH秒を取得し、GETTIMEで日付に変換する例
// （月14 = 翌年2月）
_array = GETTIME(GETSECCOUNT(2006, 14, 25, 0, 15, 56, 40))
"%(\_array[1])月%(\_array[2])日"
// 結果: "2007年2月25日" のように表示される
```

## Compatibility
YAYAの初期バージョンから使用可能

## See Also
- GETTIME
