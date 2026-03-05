# 日数計算

**Source:** Tips/日数計算

## 概要

YAYA で 2 つの日付の間の日数差・時間差を計算する方法を解説します。通日（ユリウス通日）を利用した `J_DATE` 関数と、日数・時間差を返す `DateTimeCalc` 関数が紹介されています。

作成者: せきやひろし

## コード例

### J_DATE 関数（通日を取得）

年・月・日を指定してその日付の通日を取得します。

```
J_DATE
{
	_y = TOINT(_argv[0])
	_m = TOINT(_argv[1])
	_d = TOINT(_argv[2])

	if _m <= 2 {
		_y--
		_m += 12
	}

	_jd = TOINT(365.25 * (_y + 4716)) + TOINT(30.6001 * (_m + 1)) + _d - 1524

	_jd
}
```

### DateTimeCalc 関数（日数と時間差を計算）

比較元と比較先の日付・時間を入力し、日数差と時間差を返します。

```
DateTimeCalc
{
	// 比較元日付（配列で受け取る）
	_from_date = _argv[0]
	_from_year  = _from_date[0]
	_from_month = _from_date[1]
	_from_day   = _from_date[2]
	_from_hour  = _from_date[3]
	_from_min   = _from_date[4]
	_from_sec   = _from_date[5]

	// 比較先日付（配列で受け取る）
	_to_date = _argv[1]
	_to_year  = _to_date[0]
	_to_month = _to_date[1]
	_to_day   = _to_date[2]
	_to_hour  = _to_date[3]
	_to_min   = _to_date[4]
	_to_sec   = _to_date[5]

	// 通日の差
	_day_diff = J_DATE(_to_year, _to_month, _to_day) - J_DATE(_from_year, _from_month, _from_day)

	// 秒単位に変換して差を計算
	_from_seconds = _from_hour * 3600 + _from_min * 60 + _from_sec
	_to_seconds   = _to_hour   * 3600 + _to_min   * 60 + _to_sec
	_time_diff = _to_seconds - _from_seconds

	_result = IARRAY
	_result ,= _day_diff
	_result ,= _time_diff
	_result
}
```

## 説明

### J_DATE 関数の仕組み

通日（Julian Day Number）を計算することで、異なる日付同士の差を単純な引き算で求められます。グレゴリオ暦に対応しており、月が 1 月・2 月の場合は年と月を補正してから計算します。

### DateTimeCalc 関数の使い方

引数は日付情報を格納した配列を 2 つ渡します。戻り値は日数差と秒数差の配列です。

```
// 使用例
_from = IARRAY
_from ,= 2024  // 年
_from ,= 1     // 月
_from ,= 1     // 日
_from ,= 0     // 時
_from ,= 0     // 分
_from ,= 0     // 秒

_to = GETTIME  // 現在時刻

_result = DateTimeCalc(_from, _to)
_days = _result[0]   // 日数差
_secs = _result[1]   // 時間差（秒）
```

### YAYA 標準関数による代替

より簡単な方法として、以下の関数でも日数計算が可能です。

- `GETTIME` — 現在の日時を取得する
- `GETSECCOUNT` — UNIX タイムスタンプ（エポック秒）を取得して差を計算する

## 関連項目

- GETTIME
- GETSECCOUNT
- TOINT
