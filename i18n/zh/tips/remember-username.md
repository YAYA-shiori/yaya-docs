# 记住用户的名字

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

常见做法是调用 Inputbox 让用户输入。<br>

创建下面两个函数，并从选项中调用 ChoiceUsernameEntry。<br>

```
 ChoiceUsernameEntry
 {
 "\0お名前、教えてください。\![open,inputbox,OnInputUsername,-1]\e"
 }

 OnInputUsername
 {
 username = EscapeAllTags(reference[0]) //さくらスクリプトが混入していた時の対処策
 	if username == ""
	{
	//空打ちされた時の対処策
	//ここでは「名無し」という仮名を代入しています
	username = '名無し'
	"\0教えてくれないの？\n\w9じゃあ勝手に%usernameって呼んじゃうね。\e"
	}
	else
	{
	 "\0じゃあこれから、\w5%usernameって呼ぶね。\e"
	}
 }
```

<span style="color:Red">※这里直接将 OnChoiceSelect 的选项写成了独立函数。请参阅[将选项直接写成独立函数](independent-choice-function.md)。</span>
<br>
※这里使用的 EscapeAllTags 函数位于「はろーYAYAわーるど」或 SimpleYAYA 模板的 yaya_shiori3.dic 中。如果不存在此函数，请将其改写为「username = `reference[0]`」。

### 进阶篇

更改敬称的示例。<br>

```
 ChoiceUsernameEntry
 {
 "\0お名前、教えてください。\![open,inputbox,OnInputUsername,-1]\e"
 }
```

```
 OnInputUsername
 {
 inputted_name = reference[0]
 "/
 \0呼び方は、どうするの？\n\n[half]/
 \![*]\q[ちゃん,Oninputted_name1]\n/
 \![*]\q[さん,Oninputted_name2]\e"
 }
 
 //ちゃん
 Oninputted_name1
 {
 "/
 \0「%inputted_nameちゃん」でいい？\n\n[half]/
 \![*]\q[いいよ,Oninputted_name1_determination]\n/
 \![*]\q[まちがい,ChoiceUsernameEntry]\e"
 }
 
 Oninputted_name1_determination
 {
 username = "%inputted_nameちゃん"
 "\0じゃあこれから、\w5%usernameってよぶね。\e"
 }
 
 //さん
 Oninputted_name2
 {
 "/
 \0「%inputted_nameさん」でいい？\n\n[half]/
 \![*]\q[いいよ,Oninputted_name2_determination]\n/
 \![*]\q[まちがい,ChoiceUsernameEntry]\e"
 }
 
 Oninputted_name2_determination
 {
 username = "%inputted_nameさん"
 "\0じゃあこれから、\w5%usernameって呼ぶね。\e"
 }
```
