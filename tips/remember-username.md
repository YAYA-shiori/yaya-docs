# ユーザーの名前を覚える

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

Inputboxを呼び出して入力させる方法が一般的です。<br>

下の二つの関数を作り、ChoiceUsernameEntryを選択肢から呼び出してください。<br>

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

<span style="color:Red">※ここでは、OnChoiceSelectの選択肢をいきなり独立した関数で書いています。[選択肢をいきなり独立した関数で書く](independent-choice-function.md)を参照してください。</span>
<br>
※ここで使用しているEscapeAllTags関数は、はろーYAYAわーるどかSimpleYAYAテンプレートのyaya_shiori3.dic内にあります。この関数が存在してない場合は「username = `reference[0]`」に書き変えてください。

### 応用編

敬称を変える場合の例。<br>

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
