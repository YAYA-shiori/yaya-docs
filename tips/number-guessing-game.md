# 数当てゲーム

**Source:** Tips/数当てゲーム

## 概要

0〜99 の範囲の数字を当てるシンプルなゲームの実装例です。`RAND` による乱数生成と `inputbox` による入力受付を組み合わせて実現します。

## コード例

```
Choicekazuate
{
	Kazuate_a = RAND
	"\0\s[5]数当てゲーム開始ー。\n/
	私がイメージする0～99までの数を当ててみてね。
	\![open,inputbox,OnInputKazuate_b,-1]\e"
}
```

```
OnInputKazuate_b
{
	Kazuate_b = reference0
	if Kazuate_b == Kazuate_a
	{
		"\0\s[6]正解！私がイメージしたのは%Kazuate_aでした～\e"
	}
	elseif Kazuate_b > Kazuate_a
	{
		"\0\s[5]答えよりも大きいよ。\n/
		さぁ、もう一度数を予想してみて。
		\![open,inputbox,OnInputKazuate_b,-1]\e"
	}
	elseif Kazuate_b < Kazuate_a
	{
		"\0\s[5]答えよりも小さいよ。\n/
		さぁ、もう一度数を予想してみて。
		\![open,inputbox,OnInputKazuate_b,-1]\e"
	}
}
```

## 説明

### 関数の役割

| 関数 | 役割 |
|------|------|
| `Choicekazuate` | ゲーム開始。乱数を生成して inputbox を開く |
| `OnInputKazuate_b` | ユーザーの入力値と答えを比較して結果を返す |

### 実装のポイント

- `RAND` で 0〜99 の乱数を生成し `Kazuate_a` に保存する
- `\![open,inputbox,OnInputKazuate_b,-1]` でユーザー入力を受け付ける
- `reference0` でユーザーが入力した値を取得する
- 正解・大きい・小さいの 3 分岐で結果を返す
- 不正解の場合は再帰的に inputbox を開いてゲームを継続する

### 呼び出し方

選択肢やトークから `Choicekazuate` を呼び出すことでゲームが始まります。「選択肢をいきなり独立した関数で書く」の手法と組み合わせると便利です。

## 関連項目

- RAND
- Tips/選択肢をいきなり独立した関数で書く
