# 日付イベント

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

テンプレートゴースト「紺野あやめ」のaya_bootend.dic内にある、GetTimeSlot関数を利用すると楽です。<br>

(例)クリスマスイベントの追加<br>
まず、GetTimeSlot内に以下の文を追加します。<br>

```
elseif month == 12 && day == 25
{
	"クリスマス"
}
```

次に、OnBoot内にクリスマスの日のみ発動するイベントを追加して完了です。

```
elseif _timeslot == "クリスマス"
{
	"\1\s[10]\0\s[0]今日はクリスマスです。\e"
}
```
