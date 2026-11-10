# Number Guessing Game

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

A simple number guessing game.<br>
Write the following two functions in a dictionary, then call Choicekazuate.

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

<span style="color:Red">※This example writes the OnChoiceSelect choices directly as independent functions. See [Writing choices directly as independent functions](independent-choice-function.md).</span>
