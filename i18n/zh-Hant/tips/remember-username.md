# 記住使用者名稱

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

一般會使用 Inputbox 呼叫輸入框，讓使用者輸入。<br>

請建立以下兩個函式，並從選項呼叫 ChoiceUsernameEntry。<br>

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

<span style="color:Red">※此處將 OnChoiceSelect 的選項直接寫成獨立函式。請參閱[將選項直接寫成獨立函式](independent-choice-function.md)。</span>
<br>
※此處使用的 EscapeAllTags 函式位於 はろーYAYAわーるど 或 SimpleYAYA 範本的 yaya_shiori3.dic 中。若沒有這個函式，請改寫為「username = `reference[0]`」。

### 應用篇

以下是變更敬稱的範例。<br>

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
