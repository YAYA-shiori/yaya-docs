# 指定秒数経過後にイベントを実行

**Source:** Tips/指定秒数経過後にイベントを実行

## 概要

YAYA で一定時間経過後にイベントを実行する方法を 2 通り解説します。システム辞書の `SetDelayEvent` 関数を使う方法と、`OnSecondChange` イベントを使って自作する方法があります。

## コード例

### 方法 1: SetDelayEvent 関数を使用

```
30秒待たせるイベント
{
	"\0\s[0]それでは30秒お待ち下さい。\e"
	SHIORI3FW.SetDelayEvent('30秒待った', 30)
}
```

`SetDelayEvent` で指定秒数後に実行するイベント名を登録します。経過時間は `DelayEventTime` で確認できます。

### 方法 2: OnSecondChange を使った自作実装

```
// タイマー開始
OnTimerStart
{
	_sec = _argv[0]
	timer_count = _sec
}

// 毎秒実行（OnSecondChange から呼び出す）
OnTimerCounter
{
	timer_count--
	if timer_count <= 0 {
		OnTimerEnd
	}
}

// タイマー終了時の処理
OnTimerEnd
{
	"\0\s[0]時間になりました。\e"
}
```

## 説明

### 方法 1 の特徴

システム辞書（SHIORI3FW）に組み込まれた `SetDelayEvent` を使うシンプルな方法です。指定したイベント名が、指定秒数後に自動的に呼び出されます。

### 方法 2 の特徴

`OnSecondChange` イベント（毎秒発生）を利用してカウンターを実装します。より柔軟なカスタマイズが可能ですが、複数タイマーを同時計測する場合は追加の工夫が必要です。

## 関連項目

- OnSecondChange
- SHIORI3FW.SetDelayEvent
- GETSECCOUNT
