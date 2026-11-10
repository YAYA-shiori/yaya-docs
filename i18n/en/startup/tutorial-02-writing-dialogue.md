# Tutorial 2: Writing Dialogue

## Open the folder containing the dictionary files

With the template ghost running, click the “Open” button at the bottom of the development palette. Select “GHOST” to open a folder containing yaya.dll and various other files. Files in that folder with the “.dic” extension are YAYA dictionary files.

These dictionary files describe “what the ghost says and does.” You will now edit them little by little to make a ghost.

## Take a look at the dictionary

First, open the main dictionary, `dic_main.dic`, in a text editor. Around line 150, you should find something like this:

```
//起動
OnBoot
{
	"\1\s[10]\0\s[0]こんにちは。\e"
}
```

This is the line the ghost says when it starts. If this is your first time seeing it, you probably won't know what anything means except the text “こんにちは。”, so let's work out what each of the mysterious symbols means.

| Element | Description |
|------|------|
| `OnBoot` | The function name. In this example, it is the name of the SHIORI Event called when the ghost starts. In other words, it means “what follows in `{ }` is the event that occurs when the ghost starts.” If you change it to `OnClose`, it means “the event that occurs when the ghost exits.” |
| `{ }` | The contents of the function. After writing the function name, enclose the contents in these two symbols to make “function name{function contents}.” |
| `" "` | Talk and Sakura Script must always be enclosed in these symbols. Text that is not enclosed in `" "` or `' '` will be treated as a variable name or function name, not as talk. (The difference between `" "` and `' '`, and the meaning of variable names, will be explained later.) |
| `\0` | A Sakura Script command meaning “from here on, character 0 (the main character, also called the Sakura side) will speak or change expression.” The text that follows is displayed in character 0's balloon. Text written after `\1` is displayed in the balloon of character 1, the companion character (also called the Unyuu side). |
| `\s[0]` | A Sakura Script command that displays surface 0. A surface is a type of character illustration. Changing the number, as in `\s[1]` or `\s[2]`, changes the expression to a sad face or a smile (however, the default shell in this template only has illustrations for surfaces 0 and 10, so writing `\s[1]` or `\s[2]` will not change anything). |
| `\e` | A Sakura Script command that marks the end of talk. It seems to be fine if you leave it out, but just in case, add it at the end of the talk. It is almost like a good-luck charm. |

For details about events such as OnBoot, see the [CROW/SSP Reference](http://crow.aqrs.jp/reference/all/Shiori/index.html). In general, all SHIORI Events described in this reference can be written in the same way as OnBoot.

### About Sakura Script

Sakura Script is used by SHIORI engines other than YAYA as well, so this manual will not explain it in any more detail. There are many other commands, so learn the ones you want to try out little by little from the reference sites (if you try to learn everything at once, your head will explode).

- [CROW Reference - SakuraScript](http://crow.aqrs.jp/reference/crow/SakuraScript/index.html)
- [UKADOC Project Sakura Script List](https://ssp.shillest.net/ukadoc/manual/list_sakura_script.html)
- [Disc-2 SakuraScript List](http://disc2.s56.xrea.com/manual/list_sakura_script.htm) (The information is a little out of date.)

You can practice writing Sakura Script by writing talk in “Script Input” in the development palette and sending it.

![Sending `\0\s[0]やっほー！\e` using Script Input](../attachment/img_tutorial_02_001.png)
If it sends without any apparent problems, write it in the dictionary and check that it speaks correctly (to check the talk in the OnBoot event, exit the ghost and start it again).

## Try writing different kinds of talk

### Choose talk at random

Having the same greeting every time the ghost starts is boring, so let's increase the number of greetings to three.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e"
	"\0\s[0]おっすー。\e"
	"\0\s[0]やっほー。\e"
}
```

**If there are multiple strings enclosed in `" "` or `' '` inside `{ }`, YAYA randomly selects just one of them.**

If you want to put everything on one line, separate the strings with `;` instead of line breaks.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e" ; "\0\s[0]おっすー。\e" ; "\0\s[0]やっほー。\e"
}
```

If it's tedious to write `\0\s[0]` and `\e` over and over, you can write it like this:

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

**When you separate parts with `--`, one string enclosed in `" "` or `' '` is randomly selected from each part, and the selected strings are joined together and displayed.**

You can also write this on one line by separating it with `;` (though it's hard to read).

```
OnBoot
{
	"\0\s[0]" ; -- ; "こんにちはー。" ; "おっすー。" ; "やっほー。" ; -- ; "\e"
}
```

!!! warning "`--` syntax"
    Write `--` on a line by itself, or separate it from the preceding and following text with `;`. Writing `"こんにちは。" -- "おっすー。"` without `;` or a line break will cause an error.

Here is another example.

```
OnBoot
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

This produces talk such as:

- “きょうは雨です。”
- “明日は曇りです。”
- “きょうは晴れです。”
- “明日は雷です。”
- “明日は晴れです。”

This creates random talk each time, giving you more variations.

However, since this is truly random, the same word may be selected repeatedly. To avoid that, add ` : nonoverlap` after the function name. The same sentence will not be selected twice in a row.

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

To select them in order from top to bottom, add ` : sequential`. For details, see [Function Selection Methods](../grammar/02-functions.md#選択方式).

### Creating an Original Function

What we wrote above,

```
OnBoot
{
	"\0\s[0]きょうは"
	"\0\s[0]明日は"
	--
	"晴れ"
	"雨"
	"曇り"
	"雷"
	--
	"です。\e"
}
```

can be rewritten as follows.

```
OnBoot
{
	"\0\s[0]きょうは"
	"\0\s[0]明日は"
	--
	天気一覧
	--
	"です。\e"
}

天気一覧
{
	"晴れ"
	"雨"
	"曇り"
	"雷"
}
```

You can also create an independent original function and call it in your script. One benefit of writing it this way is that

```
OnBoot
{
	"\0\s[0]きょうは"
	"\0\s[0]明日は"
	--
	天気一覧
	--
	"です。\e"
}

OnGhostChanged
{
	"\0\s[0]昨日は"
	--
	天気一覧
	--
	"だったよ。\e"
}

天気一覧
{
	"晴れ"
	"雨"
	"曇り"
	"雷"
}
```

you can reuse it by calling it from multiple functions.

```
OnBoot
{
	"\0\s[0]きょうは%(天気一覧)です。\e"
}

天気一覧
{
	"晴れ"
	"雨"
	"曇り"
	"雷"
}
```

To call a function from within `" "`, write it as `%(関数名)` ([Expanding embedded elements in strings](../grammar/06-string-embedding.md)).

### Things to Keep in Mind When Creating Original Functions

Function names (such as 「天気一覧」 in the example above) can be in English or Japanese, but you must follow these rules.

- Function names must not start with a half-width digit (`5test` is not allowed, but `test5` and `te5st` are allowed)
- Function names must not start with `_` (it could be mistaken for a local variable)
- Function names must not contain any of the following characters: space　`!`　`"`　`#`　`$`　`%`　`&`　`(`　`)`　`*`　`+`　`,`　`-`　`/`　`:`　`;`　`<`　`=`　`>`　`?`　`@`　`[`　`]`　`` ` ``　`{`　`|`　`}`
- And so on

For details, see [Defining and Executing User-Defined Functions](../grammar/02-functions.md#ユーザー関数の定義と実行).

## Making Dictionaries Easier to Read

### Adding Spaces and Line Breaks

As long as you follow the syntax rules—write the function name first and enclose its contents in `{ }`—

```
OnBoot {
	"\1\s[10]\0\s[0]こんにちは。\e"
}
```

you can write it this way,

```
OnBoot { "\1\s[10]\0\s[0]こんにちは。\e" }
```

or this way,

```
OnBoot{"\1\s[10]\0\s[0]こんにちは。\e"}
```

as well. You can add or omit spaces and line breaks between `OnBoot` and `{`, for example. Tabs are also allowed. Format your code in whichever way is easiest for you to read and write.

In general, spaces, tabs, and line breaks outside `" "` are ignored, so you can also write it like this.

```
OnBoot
	{

		"\1\s[10]\0\s[0]こんにちは。\e"

							}
```

In other words,

```
【ここ】OnBoot【ここ】{【ここ】"\0\s[0]いっちばーん。\e"【ここ】}【ここ】
```

you can put any number of spaces (half-width or full-width), tabs, or line breaks where 【here】 appears. YAYA dictionaries can be formatted neatly and made easier to read by using this feature.

### Comments

Comments prevent the specified parts from being loaded as dictionary content. They are useful when you want to add a note or annotation, or temporarily set aside part of a dictionary you have written. To comment out a line, simply put `//` at the beginning of the line.

```
// 起動イベント
OnBoot
{
	"\0\s[0]こんにちはー。\e"
}
```

You can also put it in a position like this. In other words, everything from `//` to the end of the line is commented out.

```
OnBoot
{
	"\0\s[0]こんにちはー。\e"// 起動トーク
}
```

You can also comment out text by enclosing it in `/*` and `*/`. This makes it easy to comment out multiple lines at once, so it is more convenient when there are many lines. The drawback is that it can be hard to tell which part is commented out.

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

Add plenty of notes so that when you look back at the dictionary later, you can quickly remember what each part does.

### Things You Must Not Do

Be careful: the following mistakes cause errors and prevent the ghost from running at all.

```
OnBoot
{
	"\0\s[0]改行\n
	します。\e"
}
```

A line break inside a string enclosed in `" "` or `' '` causes an error. To insert a line break in this situation, put `/` at the end of the line.

```
OnBoot
{
	"\0\s[0]改行\n/
	します。\e"
}
```

Also, starting with YAYA Tc535-1, you can use a [here document](../grammar/03-values-and-variables.md#ヒアドキュメント).

You must not write two or more functions with the same name, as in the example below. Make sure there is only one.

```
//起動
OnBoot
{
	"\1\s[10]\0\s[0]こんにちは。\e"
}

OnBoot
{
	"\1\s[10]\0\s[0]やっほー！\e"
}
```

As long as you follow these rules, it does not matter which dictionary file or location you write a function in (however, you should avoid writing in the system dictionary `yaya_shiori3.dic` whenever possible).

## The Ghost Is Not Working at All! Is This an Error? What Should I Do?

Stay calm and investigate the cause of the error.

### Investigating on Your Own

Your ghost was working properly before, so the error must be in a dictionary you wrote afterward. Carefully check the parts of the dictionary that you edited yourself. A common cause is a missing closing bracket.

If you still cannot find the cause, temporarily comment out suspicious sections and restart the ghost. If it starts normally, you have found the cause.

### Using the YAYA Debugging Tool

The “Tama” tool you prepared earlier. For details, see [Checking for Dictionary Errors with Tama](../tips/tama-error-check.md).

### View the execution log

Open `yaya.txt` in the same directory as yaya.dll. It contains an entry like this:

```
//log, ayame.log	// ログを指定されたファイルに記録
```

Delete the leftmost `//` and save the file, overwriting it, so it looks like this:

```
log, ayame.log	// ログを指定されたファイルに記録
```

Start the ghost again, and `ayame.log` will be generated. Open it to view the log.

### View the script log

This is useful when you want to know what Sakura Script is being sent to the ghost. To use it, right-click the ghost in SSP → Functions → Script Log.

## Next step

- [Tutorial 3: Try using variables](./tutorial-03-variables.md)

## Previous step

- [Tutorial 1: Preparation](./tutorial-01-preparation.md)
