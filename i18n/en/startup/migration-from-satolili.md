# Migrating from Satori

An explanation mainly for people who have only used Satori as their SHIORI, but would like to try YAYA as well.

## Introduction

### Advantages of switching from Satori to YAYA

YAYA is well suited to programming, so it can make things easier when the parts of a ghost other than its talk have become complicated and difficult to write.

However, this is not a characteristic unique to YAYA; [Kawari](http://www.towano.net/wk_kwr/) is another option. If you do not mind that development has stopped, other SHIORI implementations are also options (although fixes cannot be expected if bugs are found in them). It is best to understand the characteristics of each SHIORI and choose one that seems easy for you to use.

### Common questions about YAYA

#### I heard YAYA is a SHIORI for hardcore science and engineering types...

Several people have said, “I’m more of a humanities person and had only used Satori until now, but YAYA suited me and was easy to use.” In other words, whether YAYA is a good fit has nothing to do with whether you are a science or engineering type; it depends on how well it suits you. You cannot really know until you try it.

#### Can only people who have programmed or used the C language use it?

At least, the person who wrote this has never programmed or used the C language.

#### Isn’t it harder than Satori?

It depends on what kind of ghost you are making. Satori is easier for a simple ghost focused on talk, but for a ghost with complex behavior, Satori can actually be a more difficult SHIORI to understand than YAYA. This is especially true if you use loops or arrays extensively; writing them in Satori can become quite difficult.

#### Is it true that it is slow?

I have not heard that it is particularly slow. It is at least lighter than Satori. If a simple ghost made with YAYA feels slow, it is likely that “Output execution log” or “Retrieve the installed ghost list without limits” is enabled.

A site that may be helpful: [How slow is file I/O? (with an addendum) | Sukuriya](http://nikolat.herokuapp.com/ukagaka/time-file-io/) (the summary at the very bottom)

#### Can only YAYA handle file operations and regular expressions?

Other SHIORI implementations can do this too by using SAORI. For example, if you use YAYA as a SAORI with [YAYA as SAORI](../other/yaya-as-saori.md), you can handle file operations and regular expressions just as you can with YAYA. In other words, you do not need to choose YAYA solely for those features.

#### Can I make a ghost that absolutely cannot be made with Satori?

As mentioned above, most things can be achieved in Satori as well, either by using SAORI or by devising a way to write them. However, there are differences in how easy it is to write the dictionary, how long the code becomes, and how easy the dictionary is to read later.

### Points to note

- Satori automatically added waits, line breaks, scope-switching tags, and so on, but in YAYA you must **write all of these yourself using Sakura Script**. Choices must also always be written in Sakura Script
- In YAYA, write everything other than talk in half-width characters by default
- With Satori, you could get by without a template ghost by preparing `satori.dll` and consulting the manual. With YAYA, it is difficult to create the SHIORI/3.0 configuration script and other components (the mechanisms that make the ghost work) from scratch by yourself, so a template is almost essential. At the very least, it is safer to reuse the SHIORI/3.0 configuration script (called `yaya_shiori3.dic` in the [SimpleYAYA template](../other/simple-yaya-template.md))
- Satori automatically loaded dictionary files with the `.txt` extension and names beginning with `dic`, but YAYA **only loads dictionaries configured in `yaya.txt`**. On the other hand, YAYA can load dictionaries with any extension and lets you place them in any directory
- As with Satori, you can write any event in any dictionary
- You cannot switch dictionary loading on a per-folder basis (the [multiple personality mode](../tips/multiple-personality-mode.md) explains how to make a ghost with multiple personalities, but it does not switch between folders to load)
- Satori could use SAORI-basic as is, but with YAYA, versions earlier than Tc604-1 require a SAORI called `proxy_ex.dll`. You do not need the kind of saori definition you would write in `satori_conf.txt` for Satori (see [Using SAORI](../tips/saori-usage.md) for details)

### Things you should prepare

- **Text editor**: You can use pretty much any editor, but we recommend downloading a text editor listed in [Editor syntax highlighting files](../tips/editor-color-files.md) and the corresponding syntax highlighting file. This makes the code much easier to read. It is even more convenient to configure the editor to apply syntax highlighting automatically when you open files with the `.dic` extension
- **Template ghost**: Choose one that suits you from [Making a ghost with YAYA](creating-ghost.md). As mentioned above, one is almost essential

## Writing a YAYA dictionary

The following may not apply to templates other than [Hello YAYA World (Konnoyayame)](http://ms.shillest.net/yayame.xhtml) and the SimpleYAYA template (especially sections whose titles include “☆”).

We will use the boot event as an example.

### Basics

In Satori, you would write this.

```
＊OnBoot
：いっちばーん。
```

In YAYA, write it as follows.

```
OnBoot
{
	"\0\s[0]いっちばーん。\e"
}
```

There are various symbols whose purpose may not be clear, so we will look at them one by one.

| Symbol | Description |
|------|------|
| `OnBoot` | The name that represents the boot event, written first. This is similar to Satori. In YAYA, this is called a function name. Any event name listed in [CROW/SSP Reference - Shiori](http://crow.aqrs.jp/reference/all/Shiori/index.html) can be used as is in YAYA. Japanese event names such as “起動” (boot), “終了” (shutdown), and “初回” (first time) are specific to Satori, so they will not be called as is if you use them in YAYA |
| `{ }` | After writing the event name, enclose the event’s contents in these two symbols. **When writing a SHIORI Event in YAYA, always use “event name{event contents}”**. If you do not enclose it properly, an error will occur and the ghost will not start |
| `" "` | Strings, such as talk, must always be enclosed in these symbols. **Unlike Satori, text not enclosed in these symbols is treated as a variable or function name**. By the way, if you enclose text in `' '` instead of `" "`, variables inside it will not be expanded. In most cases, use `" "` |
| `\0` | A Sakura Script command meaning “from here on, character 0 (the Sakura side) will speak or change expression.” Text written after this will appear in character 0’s balloon. Use `\1` if you want character 1, the partner character, to speak. In Satori, these two scopes were switched using only “：” |
| `\s[0]` | A Sakura Script command that displays surface 0. In Satori, this was written as （０）. In Satori, the first （０） could be omitted, but in YAYA, if you do not include this, the surface displayed before the talk will remain on screen |
| `\e` | A Sakura Script command that marks the end of talk. It does not seem to cause any particular problems if you omit it, but it is safer to include it at the end of the talk |

Unlike Satori, waits are not added automatically. If you want to add them, use Sakura Script. Sakura Script is also used by SHIORI implementations other than YAYA, so this manual will not explain it in detail. There are many other commands as well, so use a reference site to learn the ones you “want to try using,” “a little at a time,” along with YAYA (trying to learn everything at once will make your head explode).

- [CROW Reference - SakuraScript](http://crow.aqrs.jp/reference/crow/SakuraScript/index.html)
- [Disc-2 SakuraScript List](http://disc2.s56.xrea.com/manual/list_sakura_script.htm)

As long as you follow the rules for writing code, such as writing the event name first and enclosing the contents in `{ }`, you can write it like this:

```
OnBoot {
"\0\s[0]いっちばーん。\e"
}
```

or like this.

```
OnBoot { "\0\s[0]いっちばーん。\e" }
```

You can include or omit whitespace and line breaks between `OnBoot` and `{`, for example. You can also use tabs. Choose a style that is easy for you to read and write.

```
OnBoot{"\0\s[0]いっちばーん。\e"}
```

By default, spaces, tabs, and line breaks outside `" "` are ignored, so you can also write something like this.

```
OnBoot
	{

		"\0\s[0]いっちばーん。\e"

							}
```

In other words,

```
【ここ】OnBoot【ここ】{【ここ】"\0\s[0]いっちばーん。\e"【ここ】}【ここ】
```

you can put any amount of whitespace (half-width spaces, full-width spaces, or tabs) or line breaks where 【ここ】 appears. YAYA uses this feature to let you arrange dictionaries freely. This is one reason people say that dictionaries are easier to follow than Satori dictionaries.

### Insert line breaks

In Satori, you wrote it like this.

```
＊OnBoot
：改行
します。
```

In Satori, line breaks in the dictionary became line breaks in the talk as-is, but **in YAYA, unless you use Sakura Script to insert line breaks, they will not appear as line breaks when displayed in the balloon**. Insert `\n` where you want a line break.

```
OnBoot
{
	"\0\s[0]改行\nします。\e"
}
```

If you think, “This is hard to read because there are no line breaks in the dictionary,” you can write it like this.

```
OnBoot
{
	"\0\s[0]改行\n/
	します。\e"
}
```

As shown here, you can insert a line break by putting `/` at the end of a line. Use it wherever you like.

```
OnBoot
{
	"\0\s[0]/
	改行\n/
	します。/
	\e"
}
```

Bad example:

```
OnBoot
{
	"\0\s[0]改行\n
	します。\e"
}
```

**Be careful: if you insert a line break inside a section enclosed by `" "` or `' '` without putting `/` at the end of the line, an error will occur.**

### Select words or sentences at random

In Satori, if you wrote many entries for the same event, one was selected at random from among them.

```
＊OnBoot
：こんにちはー。

＊OnBoot
：おっすー。

＊OnBoot
：やっほー。
```

However, doing this in YAYA will cause an error and prevent startup. **In YAYA, you cannot write two or more events with the same event name.** Instead, put `" "`-enclosed strings inside `{ }`, with each string on a separate line, as shown here.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e"
	"\0\s[0]おっすー。\e"
	"\0\s[0]やっほー。\e"
}
```

**In YAYA, if there are multiple strings enclosed in `" "` or `' '` inside `{ }`, one of them is selected at random.**

You can also put them all on one line by separating them with `;` instead of line breaks.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e" ; "\0\s[0]おっすー。\e" ; "\0\s[0]やっほー。\e"
}
```

If you find it tedious to write `\0\s[0]` and `\e` repeatedly, you can write it like this.

```
OnBoot
{
	"\0\s[0]"
	--
	"こんにちはー。"
	"おっすー。"
	"やっほー。"
	--
	"\e"
}
```

**When you separate strings with `--`, one string enclosed in `" "` or `' '` is selected at random from each section, and the selected strings are joined together and displayed.**

This may be a little difficult to understand, so here is an example.

```
てんき
{
	"きょうは"  //←<1>この2つのどっちかが選ばれる
	"明日は"    //←<2>
	--
	"晴れ"      //←(1)この4つの中のどれかが選ばれる
	"雨"        //←(2)
	"曇り"      //←(3)
	"雷"        //←(4)
	--
	"です。"    //←1コしかないので必ずコレが選ばれる
}
```

Written this way,

- “Today will be rainy.”
- “Tomorrow will be cloudy.”
- “Today will be sunny.”
- “Tomorrow will be stormy.”
- “Tomorrow will be sunny.”

and similar sentences are generated at random each time they are called.

Because the selection is random, the same word can be selected consecutively. You might wonder, “Can’t I avoid duplicates like in Satori?” You can.

```
OnBoot : nonoverlap
{
	"\0\s[0]"
	--
	"こんにちはー。"
	"おっすー。"
	"やっほー。"
	--
	"\e"
}
```

Add ` : nonoverlap` after the event name. The same sentence will not be selected consecutively. To select items in order from the top, use ` : sequential` ([Function selection methods](../grammar/02-functions.md#選択方式)).

In Satori, you can call a group of words written elsewhere in a talk by writing it as follows.

```
＊
：（季節）はいいね～
：どの季節でも言ってるジャン

＠季節
春
夏
秋
冬
```

The equivalent in YAYA looks like this.

```
Talk
{
	"\0\s[0]%(季節)はいいね～\w9\1\s[10]どの季節でも言ってるジャン\e"
}

季節
{
	"春"
	"夏"
	"秋"
	"冬"
}
```

Writing `%(季節)` or `%季節` in a talk calls the function named “季節” ([Expanding embedded elements in strings](../grammar/06-string-embedding.md)).

In Satori, a group of words was written as “＠季節,” while a passage of text that could contain line breaks was written as “＊季節.” In **YAYA, words and passages are not distinguished, so both are written as “季節{ }”**. SHIORI events such as `OnBoot` and groups of words are both written as “functions,” so their syntax is exactly the same.

Of course, you can also write the weather talk above as follows.

```
Talk
{
	"\0\s[0]"
	--
	"春"
	"夏"
	"秋"
	"冬"
	--
	"はいいね～\w9\1\s[10]どの季節でも言ってるジャン\e"
}
```

If you want to use the word group “season” in other talks too, the method described first is better.

### Variables

Variables, familiar from Satori as well. Many people may have used them for the user name, number of launches, uptime, and affection level. Satori had only one type of variable, but YAYA has several. First, let’s explain those.

#### Strings and numbers

YAYA variables can be either strings or numbers (strictly speaking, there are three types: integers, real numbers, and strings).

```
変数 = 1
```

With this assignment, the variable contains the number `1`.

```
変数 = "1"
```

When you assign a value enclosed in `" "` or `' '` like this, the variable contains the string `"1"`.

Unlike Satori, full-width numerals such as “１”, “２”, and “３” cannot be numbers and are treated as strings. **String variables cannot be compared or calculated as numbers.** For example, adding the numbers `1` and `2` gives the result `3`, but adding the strings `"1"` and `"2"` joins them together into `"12"`. Be aware that there are many other differences as well.

You can change a variable from a string to a number, or vice versa, whenever you like, so there is no need to worry. Change it depending on how you intend to use it.

- Make a variable a string variable: `変数 = TOSTR(変数)`
- Make a variable a numeric variable: `変数 = TOINT(変数)`

There is also [TOAUTO](../functions/TOAUTO.md), which automatically determines whether a value is an integer, real number, or string and converts it.

#### Differences Between Global and Local Variables

Prefix a name with `_` to make it a local variable; without the prefix, it is a global variable.

```
_変数名
変数名
```

Roughly speaking, a local variable is “something used temporarily that disappears soon,” while a global variable is “something that remains indefinitely unless deleted.” All Satori variables are global variables. In YAYA, it is recommended that you use local variables for everything except variables that need to persist, such as the user's name or affection level.

As for how long local variables can be used, they “can only be used within the current `{ }` and in deeper nested scopes. Their lifetime ends when execution leaves the relevant `{ }`” (from [Values and Variables](../grammar/03-values-and-variables.md#スコープとライフタイム)).

Since this is difficult to explain in words, here is an example.

```
ローカル変数テスト {
	{
		_変数 = 1
	}
	結果 = _変数
}
```

Written this way, `_変数` disappears when it moves from a deeper scope to a shallower one, so `結果` will also be empty. However,

```
ローカル変数テスト {
	_変数 = ""
	{
		_変数 = 1
	}
	結果 = _変数
}
```

this way, `_変数` is created in the shallower scope first, then moves from a shallower scope → a deeper scope → a shallower scope… so it remains even when execution moves from a deeper scope to a shallower one, and `結果` will be 1. The key is whether the scope where `_変数` is first created is the same as, or shallower than, the scope of `結果 = _変数`.

In other words, if you want a local variable to last longer, write a line such as `_○○ = ""` at the shallowest scope first.

#### Assigning Variables

Here is an example of setting a flag after giving someone a present. The present flag is set to the number 1.

Satori:

```
＊プレゼントした
＄プレゼントフラグ＝１
：わーいありがとう！
```

YAYA:

```
プレゼントした
{
	プレゼントフラグ = 1

	"\0\s[0]わーいありがとう！\e"
}
```

The differences from Satori are as follows.

- Do not prefix the name with “＄”
- Write all talks, calculations, and so on inside `{ }` (writing them outside `{ }` causes an error)
- Write all calculation symbols such as `=` and numbers such as `1` in **half-width characters**

If you are used to writing calculations and numbers in half-width characters in Satori, this may feel easier.

```
【ここ】プレゼントフラグ【ここ】=【ここ】1【ここ】
```

You can put spaces or tabs in place of 【ここ】. Many people put half-width spaces on both sides of operators to make the code easier to read.

To assign a string, do as follows. This puts the text “bouquet” into the variable “present.”

Satori:

```
＊プレゼントした
＄プレゼント【タブ】花束
：わーいありがとう！
```

YAYA:

```
プレゼントした
{
	プレゼント = "花束"

	"\0\s[0]わーいありがとう！\e"
}
```

If the value is not a number, be sure to enclose it in `" "` or `' '`, just as when writing a talk. You cannot write it as “プレゼント【タブ】"花束"” like you can in Satori. You must assign it using `=`.

```
プレゼントした
{
	プレゼント = 花束

	"\0\s[0]わーいありがとう！\e"
}
```

If you accidentally write it this way, the value of “プレゼント” will be empty. The reason is that **in YAYA, `花束` without `"花束"` is treated as a variable named “花束.”** As a result, it is interpreted as “put the value of the variable ‘花束’ into the variable ‘プレゼント’,” but since the variable “花束” does not exist, its value is empty.

In Satori, this would be equivalent to writing the following.

```
＊プレゼントした
＄プレゼント【タブ】（花束）
：わーいありがとう！
```

This is the reverse of how Satori works, so it may be a little confusing at first.

#### Calculating with Variables

Satori:

```
＊好感度アップ
＄好感度＝（好感度）＋１
：ユーザーさんだいすき！
```

YAYA:

```
好感度アップ
{
	好感度 = 好感度 + 1

	"\0\s[0]ユーザーさんだいすき！\e"
}
```

This is also simple. In Satori, the variable on the right side had to be written with `（ ）`, as in `＄好感度＝（好感度）＋１`, but YAYA does not require anything around it. As mentioned above, any text not enclosed in `" "` or `' '` is treated as a variable or function name (or as a number if it consists only of half-width digits).

YAYA also lets you write this in a shorter form.

```
好感度アップ
{
	好感度++

	"\0\s[0]ユーザーさんだいすき！\e"
}
```

`好感度++` means “increase 好感度 by 1” and is equivalent to `好感度 = 好感度 + 1`. `好感度--` (two half-width minus signs) decreases it by 1. `好感度 += 2` is equivalent to `好感度 = 好感度 + 2`, and `好感度 -= 2` is equivalent to `好感度 = 好感度 - 2`. For explanations of other calculation symbols available in YAYA, see [Arithmetic](../grammar/04-arithmetic.md).

As in Satori, you can also add strings together.

```
プレゼント = "花" + "束"
```

When written this way, the value of the variable `プレゼント` becomes `"花束"`.

Of course, you can also use variables in a talk.

```
プレゼントした
{
	プレゼント = "花束"

	"\0\s[0]わーい\w6%(プレゼント)だー！\w9\w9ありがとう！\e"
}
```

The balloon displays “わーい花束だー！ ありがとう！” The syntax is exactly the same as when using the word groups described above in a talk. This is the same in both Satori and YAYA.

To check whether a variable has been saved correctly, close the ghost and open the save data file (`yaya_variable.cfg`) in a text editor. In the example above, if you see a line like this,

```
プレゼント,"花束",",",
```

the save was successful. For a numeric variable, the number stored in the variable is not enclosed in `" "`, as shown here.

```
プレゼントフラグ,1,",",
```

For details about the save format, see [SAVEVAR](../functions/SAVEVAR.md#保存形式).

### Conditional branching

An example of a response to being poked. The `OnMouseDoubleClick` event is specified so that when character 0 (the Sakura side) is poked, “0” is put in `Reference3`. So, let’s write a dictionary that checks whether 0 is in `Reference3` and then jumps to “response to character 0 being poked.”

Satori:

```
＊OnMouseDoubleClick
＞0番さんがつつかれた【タブ】（R3）＝＝０

＊0番さんがつつかれた
：（７）つつくなっ！
```

YAYA:

```
OnMouseDoubleClick {
	if reference[3] == 0 {
		0番さんがつつかれた
	}
}

0番さんがつつかれた {
	"\0\s[7]つつくなっ！\e"
}
```

The new feature here is `if`. `if` means that if the condition expression that follows it (in this case, `reference[3] == 0`) is true, the contents of the next `{ }` are executed.

```
OnMouseDoubleClick {
	if reference[3] == 0 {
		"\0\s[7]つつくなっ！\e"
	}
}
```

Of course, you can also write a talk directly inside `{ }` like this. Choose the syntax as needed.

You can also use `else` together with `if` to do the following.

```
OnMouseDoubleClick {
	if reference[3] == 0 {
		"\0\s[7]つつくなっ！\e"
	}
	else {
		"\0\s[7]あたし以外の子もつつくなっ！\e"
	}
}
```

If `if 条件式 { }` does not match, the contents of the following `else { }` are executed. In this example, if a character other than character 0 is poked, the contents of `else { }` are executed. Note that `else` can only be used after `if`; writing `else` on its own causes an error.

To have the ghost talk only when character 0 is poked “on the head,” write this:

```
OnMouseDoubleClick {
	if reference[3] == 0 && reference[4] == "Head" {
		"\0\s[7]頭を叩くなっ！\e"
	}
}
```

You can list two or more condition expressions. Apart from the difference between half-width and full-width characters, the symbols `==` and `&&` are used exactly the same way as in Satori. Be sure to put a space or tab between `if` and `reference[3] == 0`.

By the way, poking responses in Satori were probably written like this.

```
＊0Headつつかれ
：（７）頭を叩くなっ！

＊1つつかれ
：やめれ！
```

Can’t you do something similar in YAYA? For those of you wondering, here is how to write it.

```
OnMouseDoubleClick {
	EVAL( "%(reference[3])%(reference[4])つつかれ" )
}

0Headつつかれ {
	"\0\s[7]頭を叩くなっ！\e"
}

1つつかれ {
	"\1\s[10]やめれ！\e"
}
```

Normally, if you write only `"%(reference[3])%(reference[4])つつかれ"`, the ghost will say “0Headつつかれ” when its head at index 0 is poked. Wrapping it in `EVAL( )` makes “0Headつつかれ” a function name.

This [EVAL](../functions/EVAL.md) function is useful in many situations besides branches where you can “write a standalone function directly.”

### How to write R0, S0, and A0 in YAYA

Write everything using half-width characters.

| Satori | YAYA | Notes |
|------|------|------|
| `Ｒ０` `Ｒ１` `Ｒ２` … | `reference[0]` `reference[1]` `reference[2]` … | Older templates used `reference0` `reference1` `reference2` … (you can also write them this way in newer templates, depending on the settings) |
| `Ｓ０` `Ｓ１` `Ｓ２` … | `valueex0` `valueex1` `valueex2` … | For information on using SAORI, see the “SAORI” section below |
| `Ａ０` `Ａ１` `Ａ２` … | `_argv[0]` `_argv[1]` `_argv[2]` … | As indicated by the `_` at the beginning, these are local variables |

### Things like ssu

“Conditional branching,” “comparison,” and “calculation” are done in different ways, but you can do almost everything else in the same way using YAYA system functions. See the [System Function List](../system/system-functions-index.md).

If you find it hard to find what you want to use, there is also the [YAYA System Function Reference](http://navy.nm.land.to/post/y_sysfn.html) (external site).

### SAORI

#### Usage

Satori:

```
（mciaudio,load,鳥の詩.mp3）（mciaudio,play）
```

YAYA:

```
FUNCTIONEX( 'mciaudio.dll' , 'load' , '鳥の詩.mp3' )
FUNCTIONEX( 'mciaudio.dll' , 'play' )
```

Unlike in Satori, you do not need to configure the SAORI to use in advance. Specify the relative path to the SAORI from `yaya.dll` directly.

By the way, if `mciaudio.dll` and `鳥の詩.mp3` are not in the same directory as `yaya.dll`, but in the `saori` directory one level below it, write it as follows.

```
FUNCTIONEX( 'saori\mciaudio.dll' , 'load' , '鳥の詩.mp3' )
```

You can also run it using `SAORI` instead of `FUNCTIONEX` (a system dictionary function and an alias for `FUNCTIONEX`). If either works for you, use `FUNCTIONEX`.

#### Return value Result

When you use the SAORI execution function, the result is returned as is. If you want to display the return value directly in the balloon, you can also embed it in a talk as follows (but note that the arguments to the SAORI execution function must be enclosed in `' '`, not `" "`. You cannot write `" "` inside `" "`).

```
"\0\s[0]クリップボードにある文字を取り出します。\n「%(FUNCTIONEX( 'saori\textcopy.dll' , 'コピーする文字' ))」\e"
```

You can also save it to a variable first and then use it.

```
変数 = FUNCTIONEX( 'saori\textpaste.dll' )
```

If you do not want the Result to be displayed directly in the balloon, assign it to an appropriate local variable.

#### Return value Value[n]

As mentioned above, what you wrote as `Ｓ０` `Ｓ１` `Ｓ２` … in Satori should be written as `valueex0` `valueex1` `valueex2` … in YAYA.

See the following pages for details.

- [Playing sounds](../tips/play-sound.md)
- [Using SAORI](../tips/saori-usage.md)

### ☆Display the current time

Refer to the time variables (`year` `month` `day` `weekday` `hour` `minute` `second`) in [system dictionary/yaya_shiori3.dic](../system/yaya-shiori3-dic.md). Memory usage and sender header variables can also be viewed here.

```
時間をおしえる
{
	"\0\s[0]ただいま%(hour)時%(minute)分%(second)秒で～す。\e"
}
```

If you prefer writing in Japanese, as you can with Satori, you can also use a template as a reference and write it yourself.

```
年　{ GETTIME[0] }
月　{ GETTIME[1] }
日　{ GETTIME[2] }
分　{ GETTIME[5] }
秒　{ GETTIME[6] }

時間をおしえる
{
	"\0\s[0]ただいま%(時)時%(分)分%(秒)秒で～す。\e"
}
```

For how to display the day of the week using kanji, see [Determine the day of the week](../tips/detect-weekday.md) (this is already included in the SimpleYAYA template).

### ☆Timer (＄○○タイマ【タブ】seconds)

- [Run an event after the specified number of seconds](../tips/execute-after-seconds.md)

### replace.txt

You can do the same thing with `#define`. However, `#define` is a powerful feature that transforms all text exactly as written in the dictionary before SHIORI performs calculations and other operations. Be careful not to make mistakes such as transforming important strings. For details on how to use it, see [Shorten functions, variables, and Sakura Script](../tips/shorthand-writing.md).

For example, with the following entry,

```
#define @r reference
```

you can write `@r[0]` as a shorthand for `reference[0]`.

### ☆replace_after.txt

You can do this with the `OnTranslate` or `OnTranslateInternal` event. If you want to use this for automatic waits, `OnTranslateInternal` is recommended (`OnTranslate` would also transform, for example, the contents of headlines).

Example of automatically adding waits to talk:

```
OnTranslateInternal
{
	_text = _argv[0]
	_text = REPLACE(_text, "…", "…\w3")
	_text = REPLACE(_text, "、", "、\w5")
	_text = REPLACE(_text, "。", "。\w9")
	_text
}
```

### Add responses to shell clipping and overlap

- [Clipping and overlap responses in the style of Satori](../tips/collision-response-satolili-style.md)

### Disable dangerous symbols such as Φ

As with Satori, there are symbols in YAYA that you cannot write directly in talk. In Satori, you disabled a symbol by placing “Φ” before it. In YAYA, use the [CHR](../functions/CHR.md) function to write it.

Refer to sites like the following to find the symbol’s upper 3 bits (the symbol on the horizontal axis of the table) and upper 4 bits (the vertical axis).

- [[psl] ASCII code table](http://www.psl.ne.jp/perl/pdojo00b.html)
- [Character code table](http://winofsql.jp/VA003334/CprogBase040109013756.htm)

```
CHR(0x(上位3ビット)(上位4ビット))
```

Write it as shown. For example, `1` becomes `CHR(0x31)`. Be sure to use half-width characters.

Example of writing `"` inside `" "`:

```
記号表示テスト
{
	"\0\s[0]記号「%(CHR(0x22))」をバルーンに表示\e"
}
```

For double quotes, starting with Tc569-8, you can also write two of them in a row as `""` ([Values and variables](../grammar/03-values-and-variables.md#文字列)).

### Comments

Just change `＃` to `//`.

Satori:

```
＃ 起動イベント
＊OnBoot
：こんにちはー。
```

YAYA:

```
// 起動イベント
OnBoot
{
	"\0\s[0]こんにちはー。\e"
}
```

You can also add comments in places like the following. In other words, everything to the right of `//` is commented out.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e"// 起動トーク
}
```

You can also comment out text by enclosing it in `/*` and `*/`. This lets you comment out multiple lines at once, so it is easier when there are many lines. The drawback is that it can be a little difficult to tell which text is commented out.

```
/*
起動イベント
一番最初に起動したとき呼ばれる
*/
OnBoot
{
	"\0\s[0]こんにちはー。\e"
}
```

YAYA makes it easier than Satori to add comments, so they are convenient to use freely. Add plenty of comments so that when you look back later, you can quickly remember what each part does.

## Common questions from people who migrated from Satori to YAYA

### The ghost does not do anything at all when I start it!

Unlike Satori, in YAYA, even a single mistake in the dictionary syntax can prevent the ghost from running. Check which part of the dictionary has an error.

- [Check dictionary errors using Tama](../tips/tama-error-check.md)

You can also check by viewing the execution log. Add the line `log, ayame.log` to `yaya.txt`, which is in the same directory as `yaya.dll`, then start the ghost and open the resulting `ayame.log` in a text editor.

### Where is satori_savedata.txt (save data)?

Global variables are saved in `yaya_variable.cfg` (the file name may differ depending on the template).

### I got an alias error. What is it?

Is `descript.txt` still set to `shiori,satori.dll`?

### Other questions

Also see [Troubleshooting](../other/troubleshooting.md).

## Related

- [Basics/Variables](../basic/variables.md)
- [Grammar/7. Flow control](../grammar/07-flow-control.md)
- [Troubleshooting](../other/troubleshooting.md)
