# 猜数字游戏

> 转引自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

一个简单的猜数字游戏。<br>
将下面两个函数写入词典，然后调用Choicekazuate。

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

<span style="color:Red">※这里直接将OnChoiceSelect的选项写成了独立函数。请参阅[直接将选项写成独立函数](independent-choice-function.md)。</span>
