# 猜數字遊戲

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

簡單的猜數字遊戲。<br>
請將以下兩個函式寫入辭典，然後呼叫Choicekazuate。

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

<span style="color:Red">※此處將OnChoiceSelect的選項直接寫成獨立函式。請參閱[將選項直接寫成獨立函式](independent-choice-function.md)。</span>
