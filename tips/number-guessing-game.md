# 数当てゲーム

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

簡単な数当てゲーム。<br>
下の二つの関数を辞書に書き、Choicekazuateを呼び出してください。

```
Choicekazuate
{
	Kazuate_a = RAND
	"\0\s[5]数当てゲーム開始ー。\n/
	私がイメージする0～99までの数を当ててみてね。 \![open,inputbox,OnInputKazuate_b,-1]\e"
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
		さぁ、もう一度数を予想してみて。\![open,inputbox,OnInputKazuate_b,-1]\e"
	}
	elseif Kazuate_b < Kazuate_a
	{
		"\0\s[5]答えよりも小さいよ。\n/
		さぁ、もう一度数を予想してみて。\![open,inputbox,OnInputKazuate_b,-1]\e"
	}
}
```

<span style="color:Red">※ここでは、OnChoiceSelectの選択肢をいきなり独立した関数で書いています。[選択肢をいきなり独立した関数で書く](independent-choice-function.md)を参照してください。</span>
