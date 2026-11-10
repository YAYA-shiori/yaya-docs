# Migrating from Satori

An explanation mainly for people who have only used Satori as their SHIORI and want to try YAYA as well.

## Introduction

### Advantages of switching from Satori to YAYA

YAYA is well suited to programming tasks, so it can make things easier when parts of a ghost other than its talk have become complicated and tedious to write.

However, this is not a characteristic unique to YAYA; [Kawari](http://www.towano.net/wk_kwr/) is another option. If you do not mind that development has stopped, other SHIORI implementations are also options (although you cannot expect fixes even if bugs are found). It is best to understand the characteristics of each SHIORI and choose one that seems easy for you to use.

### Common questions about YAYA

#### I heard that YAYA is a SHIORI for hardcore science and engineering types...

Several people have said, “I’m from the humanities and had only used Satori until now, but YAYA felt right for me and was easy to use.” In other words, whether YAYA is a good fit has nothing to do with whether you are a science or engineering type; it depends on how well it suits you. You cannot tell until you try it.

#### Can only people who have programmed or used C use it?

At least, the person who wrote this has never programmed or used C.

#### It’s harder than Satori, right?

It depends on what kind of ghost you are making. For a simple ghost centered on talk, Satori is easier. However, for a ghost with complex behavior, Satori can actually be a more difficult SHIORI to understand than YAYA. This is especially true if you make extensive use of loops or arrays; writing them in Satori is likely to become difficult.

#### Is it true that it’s slow?

I have not heard that it is particularly slow. At least, it is lighter than Satori. If a simple YAYA ghost seems slow, there is a good chance that “Enable execution log output” or “Retrieve the installed ghost list without limits” is enabled.

This site may be helpful: [How slow is file reading and writing? (with an additional note) | Sukuriya](http://nikolat.herokuapp.com/ukagaka/time-file-io/) (summary at the very bottom)

#### Can only YAYA handle file operations and regular expressions?

You can do those things with other SHIORI implementations by using SAORI. For example, if you use YAYA as a SAORI with [YAYA as SAORI](../other/yaya-as-saori.md), you can handle file operations and regular expressions just as you can in YAYA. In other words, you do not need to choose YAYA solely for those features.

#### Does it let you make ghosts that absolutely cannot be made with Satori?

As mentioned above, you can achieve most things in Satori too, by using SAORI or refining how you write things. However, there are differences in how easy it is to write dictionaries, how long the descriptions become, and how easy those dictionaries are to read later.

### Points to note

- Satori automatically inserted waits, line breaks, scope-switching tags, and so on, but in YAYA you **write all of these yourself using Sakura Script**. Choices must also always be written in Sakura Script
- In YAYA, you generally write everything except talk using half-width characters
- With Satori, you could get by without a template ghost by preparing `satori.dll` and consulting the manual. With YAYA, it is difficult to create the SHIORI/3.0 configuration script and other parts (the mechanisms that make a ghost work) from scratch yourself, so a template is nearly essential. At the very least, it is safer to reuse the SHIORI/3.0 configuration script (called `yaya_shiori3.dic` in the [SimpleYAYA template](../other/simple-yaya-template.md))
- Satori automatically loaded dictionary files with the `.txt` extension and filenames beginning with `dic`, but YAYA **only loads dictionaries configured in `yaya.txt`**. In return, it can load dictionaries with any extension, and you can place dictionaries in any directory
- As with Satori, you can write any event in any dictionary
- You cannot switch dictionary loading by folder (how to set up multiple personalities is described in [Multiple Personality Mode](../tips/multiple-personality-mode.md), but it does not use a method that switches the loading folder)
- Satori could use SAORI-basic directly, but versions of YAYA earlier than Tc604-1 require the SAORI named `proxy_ex.dll` to use it. You do not need a saori definition like the one you wrote in `satori_conf.txt` for Satori (see [Using SAORI](../tips/saori-usage.md) for details)

### Things you should prepare

- **Text editor**: Basically, any editor will do, but it is recommended that you download a text editor listed in [Editor syntax highlighting files](../tips/editor-color-files.md) and the corresponding syntax highlighting file. The text is much easier to read. It is even more convenient to configure the editor to automatically apply syntax highlighting when opening files with the `.dic` extension
- **Template ghost**: Choose one that suits you from [Creating a ghost with YAYA](creating-ghost.md). As mentioned above, it is nearly essential

## Trying out YAYA dictionaries

The following may not apply to templates other than [Hello YAYA World (Konnoyayame)](http://ms.shillest.net/yayame.xhtml) and the SimpleYAYA template (especially for items whose titles include “☆”).

Here is an example using the startup event.

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

There are various symbols that may not make much sense at first, so let’s look at them one by one.

| Symbol | Description |
|------|------|
| `OnBoot` | The name written first, representing the startup event. This part is the same as in Satori. In YAYA, this is called a function name. Any event name listed in [CROW・SSP Reference - Shiori](http://crow.aqrs.jp/reference/all/Shiori/index.html) can be written as is in YAYA. Japanese event names such as “起動” (startup), “終了” (shutdown), and “初回” (first time) are event names specific to Satori, so writing them in YAYA will not call them as is |
| `{ }` | After writing the event name, enclose the event contents in these two symbols. **When writing a SHIORI Event in YAYA, always use “event name{event contents}”.** If you do not enclose the contents correctly, an error occurs and the ghost will not start |
| `" "` | Always enclose strings, such as talk, in these symbols. **Unlike Satori, any text not enclosed in them is assumed to be a variable name or function name.** By the way, if you enclose text in `' '` instead of `" "`, variables inside it will not be expanded. Usually, `" "` is fine |
| `\0` | Sakura Script meaning “from this point on, character 0 (the Sakura side) speaks or changes expression.” Text written after this is displayed in character 0’s balloon. Use `\1` if you want character 1, the partner character, to speak. In Satori, these two switches were handled using only “：” |
| `\s[0]` | Sakura Script that displays surface 0. In Satori, you would write (０). In Satori, the first (０) could be omitted, but in YAYA, unless you include this, the surface displayed before the talk will remain on screen |
| `\e` | Sakura Script indicating the end of the talk. It does not seem to cause any particular problem if you omit it, but it is a good idea to include it at the end of the talk, just in case |

Unlike Satori, waits are not inserted automatically. If you want to add them, use Sakura Script. Sakura Script is also used by SHIORI implementations other than YAYA, so this manual does not explain it in detail. There are many other scripts as well, so learn the ones you “actually want to try” from the reference sites, “a little at a time,” along with YAYA (trying to learn everything at once will make your head explode).

- [CROW Reference - SakuraScript](http://crow.aqrs.jp/reference/crow/SakuraScript/index.html)
- [Disc-2 SakuraScript List](http://disc2.s56.xrea.com/manual/list_sakura_script.htm)

As long as you follow the writing rules, such as writing the event name first and enclosing the contents in `{ }`, you can also write it like this:

```
OnBoot {
"\0\s[0]いっちばーん。\e"
}
```

Or you can write it like this.

```
OnBoot { "\0\s[0]いっちばーん。\e" }
```

Spaces and line breaks between `OnBoot` and `{`, for example, are optional. You can also use tabs. Choose a style that is easy for you to read and write.

```
OnBoot{"\0\s[0]いっちばーん。\e"}
```

Basically, spaces, tabs, and line breaks outside `" "` are ignored, so you can also write something like this.

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

means that you can put any amount of whitespace (half-width spaces, full-width spaces, or tabs) or line breaks where 【ここ】 appears. YAYA uses this feature to let you format dictionaries freely. This is one reason people say that dictionaries are easier to read than in Satori.

### Adding line breaks

In Satori, you wrote this:

```
＊OnBoot
：改行
します。
```

In Satori, line breaks in a dictionary became line breaks in the talk as they were, but **in YAYA, unless you use Sakura Script to add line breaks, they will not appear as line breaks when displayed in the balloon**. Insert `\n` where you want a line break.

```
OnBoot
{
	"\0\s[0]改行\nします。\e"
}
```

If you think, “This is hard to understand because the dictionary itself has no line break,” write it as follows:

```
OnBoot
{
	"\0\s[0]改行\n/
	します。\e"
}
```

You can add a line break by putting `/` at the end of a line like this. Put it wherever you like.

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

**Be careful: if you add a line break inside a section enclosed in `" "` or `' '` without putting `/` at the end of the line, an error will occur.**

### Randomly selecting words or sentences

In Satori, if you wrote the same event many times, one of them was selected at random.

```
＊OnBoot
：こんにちはー。

＊OnBoot
：おっすー。

＊OnBoot
：やっほー。
```

However, doing this in YAYA causes an error and prevents startup. **YAYA does not allow you to write two or more events with the same event name.** Instead, list `" "` sections on separate lines inside `{ }`, as follows.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e"
	"\0\s[0]おっすー。\e"
	"\0\s[0]やっほー。\e"
}
```

**If there are multiple strings enclosed in `" "` or `' '` inside `{ }`, YAYA randomly selects just one of them.**

You can also put them all on one line by separating them with `;` instead of line breaks.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e" ; "\0\s[0]おっすー。\e" ; "\0\s[0]やっほー。\e"
}
```

If you find it tedious to write `\0\s[0]` and `\e` repeatedly, you can write it as follows:

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

**When you separate sections with `--`, one string enclosed in `" "` or `' '` is randomly selected from each section, and the selected strings are joined together and displayed.**

This may be a little hard to understand, so here is an example.

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

Writing it this way produces sentences such as:

- “It’s sunny today.”
- “It will be cloudy tomorrow.”
- “It’s sunny today.”
- “There will be a thunderstorm tomorrow.”
- “It will be sunny tomorrow.”

Each time it is called, a sentence is generated at random.

Because the selection is random, the same word may be selected consecutively. You may be wondering, “Can I prevent duplicates, like in Satori?” You can.

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

Add ` : nonoverlap` after the event name. The same sentence will not be selected consecutively. To select items in order, use ` : sequential` ([Function selection methods](../grammar/02-functions.md#選択方式)).

In Satori, you can call a group of words written elsewhere into a talk by writing it as follows.

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

To do the same thing in YAYA, write it as follows.

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

In Satori, a group of words was written as “＠季節,” while a sentence with line breaks was written as “＊季節.” **YAYA does not distinguish between words and sentences, so write “季節{ }” for either words or sentences.** SHIORI events such as `OnBoot` and groups of words are both written as “functions,” so they are written in exactly the same way.

Of course, you can also write it as follows, as in the weather talk example above.

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

If you want to use the group of words “季節” in another talk as well, the first method is better.

### Variables

Variables are also familiar from Satori. Many people may have used them for the user's name, the number of startups, startup time, or affection level. Satori had only one kind of variable, but YAYA has several. First, here is an explanation of those.

#### Strings and numbers

YAYA variables can be either strings or numbers (more precisely, there are three types: integers, real numbers, and strings).

```
変数 = 1
```

When you assign it this way, the variable contains the number `1`.

```
変数 = "1"
```

When you assign it enclosed in `" "` or `' '` like this, the variable contains the string `"1"`.

Unlike Satori, full-width “１”, “２”, “３”... cannot be numbers and are treated as strings. **String variables cannot be compared or used in calculations as numbers.** For example, adding the numbers `1` and `2` produces `3`, but adding the strings `"1"` and `"2"` joins 1 and 2 to produce `"12"`. There are other differences as well, so be careful.

You can change a variable between a string and a number whenever you like, so there is no need to worry. Change it according to how you use it.

- Make a variable a string variable: `変数 = TOSTR(変数)`
- Make a variable a numeric variable: `変数 = TOINT(変数)`

There is also [TOAUTO](../functions/TOAUTO.md), which automatically determines whether a value is an integer, real number, or string and converts it accordingly.

#### Differences Between Global and Local Variables

Adding `_` to the beginning of a name makes it a local variable; without it, it is a global variable.

```
_変数名
変数名
```

Roughly speaking, a local variable is “something used temporarily that disappears soon,” while a global variable is “something that remains until it is deleted.” All Satori variables are global variables. In YAYA, we recommend using local variables except for variables that need to persist, such as the user's name and affection level.

As for how long a local variable can be used: “It can be used only within the current `{ }` and in deeper nested scopes. Its lifetime ends when it exits the relevant `{ }`” (from [Values and Variables](../grammar/03-values-and-variables.md#スコープとライフタイム)).

This is difficult to explain in words, so here is an example.

```
ローカル変数テスト {
	{
		_変数 = 1
	}
	結果 = _変数
}
```

Written this way, `_変数` disappears when it moves from a deeper scope to a shallower one, so `結果` is empty. However,

```
ローカル変数テスト {
	_変数 = ""
	{
		_変数 = 1
	}
	結果 = _変数
}
```

this way, `_変数` is created first in the shallower scope, then moves from a shallower scope to a deeper scope and back to a shallower one, so it remains even after moving from a deeper scope to a shallower one, and `結果` contains 1. The key is whether the scope where `_変数` is first created is at the same level as `結果 = _変数` or shallower.

In other words, if you want a local variable to live longer, write a line such as `_○○ = ""` first, in the shallowest scope.

#### Assigning Variables

Here is an example of setting a flag after giving a present. The present flag is set to the number 1.

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

- Do not add “＄” to the beginning
- Write all talk and calculations inside `{ }` (writing them outside `{ }` results in an error)
- Write all calculation symbols, such as `=`, and numbers, such as `1`, in **half-width characters**

If you are used to writing calculation expressions and numbers in half-width characters in Satori, this may feel easier.

```
【ここ】プレゼントフラグ【ここ】=【ここ】1【ここ】
```

You can put spaces or tabs in place of 【ここ】. Many people add half-width spaces to the left and right of operators to make the code easier to read.

To assign a string, write it as follows. This puts the string “bouquet” into the variable “present.”

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

If the value is not a number, always enclose it in `" "` or `' '`, just as when writing talk. You cannot write it like Satori's “プレゼント【タブ】"花束"”. You must assign it with `=`.

```
プレゼントした
{
	プレゼント = 花束

	"\0\s[0]わーいありがとう！\e"
}
```

If you accidentally write it this way, “プレゼント” will be empty. This is because **in YAYA, writing `花束` without `"花束"` makes it “a variable named 花束.”** So it is interpreted as “put the contents of the variable named 花束 into the variable named プレゼント.” Since there is no variable named 花束, its contents are empty.

In Satori, this would be like writing the following.

```
＊プレゼントした
＄プレゼント【タブ】（花束）
：わーいありがとう！
```

This is the opposite of how Satori works, so it may be a little confusing at first.

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

This is also simple. In Satori, the variable on the right had to be written with `（ ）`, as in `＄好感度＝（好感度）＋１`, but YAYA requires no such notation. As mentioned earlier, strings that are not enclosed in `" "` or `' '` are treated as variable or function names (or as numbers if they contain only half-width digits).

YAYA also lets you write this in abbreviated form.

```
好感度アップ
{
	好感度++

	"\0\s[0]ユーザーさんだいすき！\e"
}
```

`好感度++` means “increase 好感度 by 1” and is equivalent to `好感度 = 好感度 + 1`. `好感度--` (two half-width minus signs) decreases it by 1. `好感度 += 2` is equivalent to `好感度 = 好感度 + 2`, and `好感度 -= 2` is equivalent to `好感度 = 好感度 - 2`. For explanations of the other calculation symbols available in YAYA, see [Arithmetic](../grammar/04-arithmetic.md).

As in Satori, you can also add strings together.

```
プレゼント = "花" + "束"
```

When written this way, the contents of the variable `プレゼント` become `"花束"`.

You can, of course, also use variables in talk.

```
プレゼントした
{
	プレゼント = "花束"

	"\0\s[0]わーい\w6%(プレゼント)だー！\w9\w9ありがとう！\e"
}
```

The balloon displays “わーい花束だー！ ありがとう！”. The way to write this is exactly the same as when using the word groups described above in talk. This is one area where Satori and YAYA work the same way.

To check whether a variable has been saved correctly, exit the ghost and open the save data file (`yaya_variable.cfg`) in a text editor. In the example above, you should find a line like this:

```
プレゼント,"花束",",",
```

If you do, the save was successful. For a numeric variable, the number stored in the variable is not enclosed in `" "`, as shown here:

```
プレゼントフラグ,1,",",
```

For details about the save format, see [SAVEVAR](../functions/SAVEVAR.md#保存形式).

### Branching

Example of a reaction to being poked. According to the `OnMouseDoubleClick` event specification, when character 0 (the Sakura side) is poked, "0" is placed in `Reference3`. So, let's write a dictionary that checks whether 0 is in `Reference3` and then jumps to the "character 0 was poked" talk.

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

Here is a new element, `if`. `if` means that if the condition expression that follows it (in this case, `reference[3] == 0`) is true, the contents of the following `{ }` are executed.

```
OnMouseDoubleClick {
	if reference[3] == 0 {
		"\0\s[7]つつくなっ！\e"
	}
}
```

Of course, you can also write the talk directly inside `{ }` like this. Choose the notation as needed.

You can also do the following by using `else` together with `if`.

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

If the condition in `if 条件式 { }` is not met, the contents of the following `else { }` are executed. In this example, if a character other than character 0 is poked, the contents of `else { }` are executed. Note that `else` can only be used after `if`; writing `else` by itself will cause an error.

If you want the talk to play only when character 0 is poked "on the head," write this:

```
OnMouseDoubleClick {
	if reference[3] == 0 && reference[4] == "Head" {
		"\0\s[7]頭を叩くなっ！\e"
	}
}
```

You can list two or more condition expressions. The symbols `==` and `&&` are used exactly as in Satori; the only difference is whether they are half-width or full-width. Be sure to put a space or tab between `if` and `reference[3] == 0`.

By the way, this is how you would have written a poke reaction in Satori:

```
＊0Headつつかれ
：（７）頭を叩くなっ！

＊1つつかれ
：やめれ！
```

Can YAYA do something similar? Here's how.

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

Normally, if you write only `"%(reference[3])%(reference[4])つつかれ"`, the ghost will say "0Headつつかれ" when character 0 is poked on the head. By wrapping it in `EVAL( )`, "0Headつつかれ" becomes a function name.

This [EVAL](../functions/EVAL.md) is a useful function that can help in many situations, not just in branching where you can "write an independent function on the fly."

### How to write R0, S0, and A0 in YAYA

Write everything in half-width characters.

| Satori | YAYA | Notes |
|------|------|------|
| `Ｒ０` `Ｒ１` `Ｒ２` … | `reference[0]` `reference[1]` `reference[2]` … | Older templates used `reference0` `reference1` `reference2` … (You can also write this way with newer templates, depending on the settings.) |
| `Ｓ０` `Ｓ１` `Ｓ２` … | `valueex0` `valueex1` `valueex2` … | See the "SAORI" section below for how to use SAORI. |
| `Ａ０` `Ａ１` `Ａ２` … | `_argv[0]` `_argv[1]` `_argv[2]` … | As indicated by the leading `_`, these are local variables. |

### Things like ssu

"Conditional branching," "comparison," and "calculation" are done in different ways, but other than that, you can do almost the same things using YAYA system functions. See the [system function list](../system/system-functions-index.md).

### SAORI

#### How to use

Satori:

```
（mciaudio,load,鳥の詩.mp3）（mciaudio,play）
```

YAYA:

```
FUNCTIONEX( 'mciaudio.dll' , 'load' , '鳥の詩.mp3' )
FUNCTIONEX( 'mciaudio.dll' , 'play' )
```

Unlike in Satori, you do not need to configure the SAORI to use in advance. Specify the relative path to the SAORI as seen from `yaya.dll` directly.

By the way, if `mciaudio.dll` and `鳥の詩.mp3` are in the `saori` directory one level below, rather than in the same directory as `yaya.dll`, write this:

```
FUNCTIONEX( 'saori\mciaudio.dll' , 'load' , '鳥の詩.mp3' )
```

You can also execute it using `SAORI` instead of `FUNCTIONEX` (a system dictionary function and an alias for `FUNCTIONEX`). If either works, use `FUNCTIONEX`.

#### Return value Result

The SAORI execution function returns the result directly. If you want to display the return value in the balloon as-is, you can also embed it directly in a talk as follows (but note that the arguments of the SAORI execution function must be enclosed in `' '`, not `" "`. You cannot write `" "` inside `" "`).

```
"\0\s[0]クリップボードにある文字を取り出します。\n「%(FUNCTIONEX( 'saori\textcopy.dll' , 'コピーする文字' ))」\e"
```

You can also save it in a variable first and use it.

```
変数 = FUNCTIONEX( 'saori\textpaste.dll' )
```

If you do not want Result to be displayed directly in the balloon, assign it to an appropriate local variable.

#### Return value Value[n]

As mentioned above, what you wrote as `Ｓ０` `Ｓ１` `Ｓ２` … in Satori should be written as `valueex0` `valueex1` `valueex2` ….

See the following pages for details.

- [Playing sounds](../tips/play-sound.md)
- [How to use SAORI](../tips/saori-usage.md)

### ☆Display the current time

Refer to the time variables (`year` `month` `day` `weekday` `hour` `minute` `second`) in [system dictionary/yaya_shiori3.dic](../system/yaya-shiori3-dic.md). You can also find memory usage and sender header variables here.

```
時間をおしえる
{
	"\0\s[0]ただいま%(hour)時%(minute)分%(second)秒で～す。\e"
}
```

If you "don't like it unless you can write it in Japanese like Satori," you can also refer to the template and write it yourself.

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

For how to display the day of the week using kanji, see [Determine the day of the week](../tips/detect-weekday.md) (already included in the SimpleYAYA template).

### ☆Timer (＄○○timer【Tab】number of seconds)

- [Run an event after the specified number of seconds](../tips/execute-after-seconds.md)

### replace.txt

You can do the same thing with `#define`. However, `#define` is powerful because it replaces “all the strings exactly as written in the dictionary” before SHIORI performs calculations and other operations. Be careful not to make mistakes such as replacing important strings. For detailed usage, see [Shortening functions, variables, and Sakura Script](../tips/shorthand-writing.md).

For example, if you write the following,

```
#define @r reference
```

you can write `@r[0]` as a shorter form of what you previously wrote as `reference[0]`.

### ☆replace_after.txt

You can do this in the `OnTranslate` or `OnTranslateInternal` event. If you want to use it for automatic waits and similar purposes, `OnTranslateInternal` is recommended (`OnTranslate` may also transform, for example, the contents of headlines).

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

### Adding shell collision and overlap reactions

- [Collision and overlap reactions in the style of Satori](../tips/collision-response-satolili-style.md)

### Disabling dangerous symbols such as Φ

As with Satori, YAYA also has symbols that cannot be written directly in talk. In Satori, these were disabled by placing “Φ” before the symbol. In YAYA, write them using the [CHR](../functions/CHR.md) function.

Refer to sites like the following to find the upper 3 bits (the symbols on the horizontal axis of the table) and upper 4 bits (the vertical axis) of the symbol you want to write.

- [[psl] ASCII Code List](http://www.psl.ne.jp/perl/pdojo00b.html)
- [Character Code Table](http://winofsql.jp/VA003334/CprogBase040109013756.htm)

```
CHR(0x(上位3ビット)(上位4ビット))
```

Write it as shown. For example, `1` becomes `CHR(0x31)`. Always use half-width characters.

Example of writing `"` inside `" "`:

```
記号表示テスト
{
	"\0\s[0]記号「%(CHR(0x22))」をバルーンに表示\e"
}
```

For double quotation marks, you can also write two of them in succession as `""` in Tc569-8 and later ([Values and Variables](../grammar/03-values-and-variables.md#文字列)).

### Commenting out

Simply change `＃` to `//`.

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

You can also put comments in positions like the following. In other words, everything to the right of `//` is commented out.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e"// 起動トーク
}
```

You can also comment out text by enclosing it in `/*` and `*/`. This lets you enclose multiple lines at once, so it is easier when there are many lines. One drawback is that it can be a little difficult to tell where the comment starts and ends.

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

YAYA makes it easier to add comments than Satori, so they are convenient to use freely. Add plenty of comments so that when you look back later, you can quickly remember what each part does.

## Common questions from people migrating from Satori to YAYA

### The ghost does not do anything when I start it!

Unlike Satori, in YAYA, the ghost will not run if even one character in the dictionary is written incorrectly. Check which part is incorrect.

- [Checking dictionary errors using Tama](../tips/tama-error-check.md)

You can also check the execution log. Add the line `log, ayame.log` to `yaya.txt`, which is in the same directory as `yaya.dll`, then start the ghost and open the resulting `ayame.log` in a text editor.

### Where is satori_savedata.txt (save data)?

Global variables are saved in `yaya_variable.cfg` (the file name may differ depending on the template).

### I got an alias error. What is this?

Is `descript.txt` still set to `shiori,satori.dll`?

### Other questions

See [Troubleshooting](../other/troubleshooting.md) as well.

## Related

- [Basics/Variables](../basic/variables.md)
- [Grammar/7. Flow Control](../grammar/07-flow-control.md)
- [Troubleshooting](../other/troubleshooting.md)
