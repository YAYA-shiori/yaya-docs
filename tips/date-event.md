# 日付イベント

**Source:** Tips/日付イベント

## 概要

特定の日付にのみ発動するイベント（クリスマス、誕生日など）を実装する方法です。テンプレートゴースト「紺野あやめ」に含まれる `aya_bootend.dic` の `GetTimeSlot` 関数を活用します。

## コード例

### ステップ 1: GetTimeSlot 関数に月日の判定を追加

`aya_bootend.dic` 内の `GetTimeSlot` 関数に条件を追記します。

```
elseif month == 12 && day == 25
{
	"クリスマス"
}
```

### ステップ 2: OnBoot 内でイベント発動条件を設定

```
OnBoot
{
	_timeslot = GetTimeSlot

	elseif _timeslot == "クリスマス"
	{
		"\1\s[10]\0\s[0]今日はクリスマスです。\e"
	}
}
```

## 説明

### 動作の仕組み

1. `GetTimeSlot` 関数が現在の月日を判定して時間帯・日付の名前を返す
2. `OnBoot` イベントで `GetTimeSlot` の戻り値を確認する
3. 戻り値が "クリスマス" であれば対応するセリフを実行する

### 他の日付イベントへの応用

同じ方法で様々な日付イベントを追加できます。

```
// バレンタイン
elseif month == 2 && day == 14
{
	"バレンタイン"
}

// お正月
elseif month == 1 && day == 1
{
	"元旦"
}
```

### 注意

`aya_bootend.dic` は「紺野あやめ」テンプレートに付属のファイルです。別のテンプレートを使用している場合は、`GetTimeSlot` の実装を自分で追加するか、直接 `month` と `day` 変数で判定してください。

## 関連項目

- GETTIME
- month（システム変数）
- day（システム変数）
