# 曜日を判別

**Source:** Tips/曜日を判別

## 概要

YAYA で現在の曜日を判別し、トークネタの変更や機能制限など様々な用途に応用する 3 つの実装パターンを紹介します。`weekday` 変数（0 = 日曜日、6 = 土曜日）を使用します。

## コード例

### 方法 1: 条件分岐による基本実装

```
GetWeekdayName
{
	if weekday == 0 {
		"日"
	}
	elseif weekday == 1 {
		"月"
	}
	elseif weekday == 2 {
		"火"
	}
	elseif weekday == 3 {
		"水"
	}
	elseif weekday == 4 {
		"木"
	}
	elseif weekday == 5 {
		"金"
	}
	elseif weekday == 6 {
		"土"
	}
}
```

### 方法 2: 汎用配列による実装

```
GetWeekdayName
{
	_days = IARRAY
	_days ,= "日"
	_days ,= "月"
	_days ,= "火"
	_days ,= "水"
	_days ,= "木"
	_days ,= "金"
	_days ,= "土"

	_days[weekday]
}
```

### 方法 3: 簡易配列による実装

```
GetWeekdayName
{
	_days = "日,月,火,水,木,金,土"
	SPLIT(_days, ",")[weekday]
}
```

## 説明

### weekday 変数

YAYA のシステム変数 `weekday` は現在の曜日を 0〜6 の整数で返します。

| 値 | 曜日 |
|----|------|
| 0 | 日曜日 |
| 1 | 月曜日 |
| 2 | 火曜日 |
| 3 | 水曜日 |
| 4 | 木曜日 |
| 5 | 金曜日 |
| 6 | 土曜日 |

### 各方法の比較

| 方法 | 特徴 |
|------|------|
| 条件分岐 | わかりやすく、各曜日で異なる処理を書きやすい |
| 汎用配列 | 簡潔。月の異名など他の用途にも応用しやすい |
| 簡易配列 | 最も短く書けるが、汎用配列より低速 |

### 活用例

- 曜日によってトークネタを変える
- 平日・休日で機能を制限する
- 特定曜日にのみイベントを発動させる

```
// 活用例: 曜日に応じた挨拶
OnBoot
{
	if weekday == 0 || weekday == 6 {
		"\0今日はお休みですね。\e"
	}
	else {
		"\0今日もお仕事ですか？\e"
	}
}
```

## 関連項目

- GETTIME
- weekday（システム変数）
- SPLIT
- IARRAY
