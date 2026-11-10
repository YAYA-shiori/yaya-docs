# Remembering the User's Name

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

A common way to do this is to call an Inputbox and have the user enter their name.<br>

Create the following two functions, and call ChoiceUsernameEntry from a choice.<br>

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

<span style="color:Red">※Here, the OnChoiceSelect choice is written directly as an independent function. See [Writing a choice directly as an independent function](independent-choice-function.md).</span>
<br>
※The EscapeAllTags function used here is in yaya_shiori3.dic in the Hello YAYA World or SimpleYAYA template. If this function is not available, change it to “username = `reference[0]`”.

### Advanced

Example of changing the honorific.<br>

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
