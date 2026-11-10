# Plain-text Talk Support Library “Ayariris EX”

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Tired of writing wait tags every time?

Does writing things like `\s[]` take too much time?

Find it hard to revise text later when you write it in Sakura Script?

…Then this is for you.

### Overview

> "`\u\s[10]\0\s[2]`…`\w5`…`\w5`…`\w5`…`\w5`…`\w5\w9\w9\1`What the heck, `\w5`with that stupid-looking face. `\w9\w9\0\s[7]\n\n`Your battery is about to give out, so `\w9\n`please don't leave the computer in hibernation!`\w9\n`You'll turn stupid!`\w9\w9\1\n\n`…`\w5`…`\w5`Like I was ever smart to begin with. `\w9\w9\0\s[26]\n\n`…`\w5`…`\w5`…`\w5`…`\w5\e`"

A dictionary like this…

```
<<"
ま０５：分かりました！分かりましたよ！２０年モノのパソコンがどうなるのか！
し１０：スクラップやのうて？
ま　　：付喪神っていう便利な言葉が、世の中にはあるんですよ！
し１１：…まあ、ゴーストにはなったがな？
">>
```

becomes this.

**Even after installing it, talks written as a single line of ordinary Sakura Script pass through as-is (or you can adjust things like waits at punctuation).**

**Sakura Script within the text is executed as-is. If you want to make fine adjustments, or call a feature other than simple speech partway through, write the Sakura Script directly.**

### Real-world examples

<http://ssp.shillest.net/ghost.html>

- the "MobileMaster"
- Traffic☆Train
- Mary's Telephone

<http://ms.shillest.net/>

- The Daughter Who Doesn't Quite Inspire Moe
- Trouble☆Bugtrack

### Preparation

1. Please overwrite yaya.dll and the "system dictionary," as this makes extensive use of the latest system dictionary and the latest YAYA features.
1. Save [aya_lilith_ex.dic](http://ms.shillest.net/ghost/mobilemaster/ghost/master/aya_lilith_ex.dic) and [aya_lilith_ex_config.dic](http://ms.shillest.net/ghost/mobilemaster/ghost/master/aya_lilith_ex_config.dic), and place them under ghost/master.
1. Add the following after **include, system_config.txt** in yaya.txt:
dic, aya_lilith_ex.dic<br>
dic, aya_lilith_ex_config.dic<br>
Please add these lines.

Open **aya_lilith_ex_config.dic**, and set **あやりりすEXヘッダ0** and **あやりりすEXヘッダ1** appropriately. The instructions are in comments in the dictionary, but normally, you can list multiple one-character candidates you want to use and enclose them in square brackets, as in [まマ].

※Advanced: Regular expressions can be used in this section. Try experimenting if you want to use two or more characters.

### Usage

This uses the multiline text notation feature (here documents), added in a relatively recent version of YAYA.

Text enclosed in " " is

```
<<"
">>
```

Text enclosed in ' ' is

```
<<'
'>>
```

equivalent to the above. The only difference between these two notations is that the latter can be written continuously across multiple lines.

Basically, use this feature to write text as follows.

```
<<"
ま０５：分かりました！分かりましたよ！２０年モノのパソコンがどうなるのか！
し１０：スクラップやのうて？
ま　　：付喪神っていう便利な言葉が、世の中にはあるんですよ！
し１１：…まあ、ゴーストにはなったがな？
">>
```

Set the first character, "ま" or "し", to the character configured in aya_lilith_ex_config.dic.

The full-width numbers that follow are surface numbers (expression IDs). Half-width numbers also work.

Punctuation and waits at line breaks are inserted automatically as appropriate. Usually, write the text as-is.

If you want to do anything special, you can use Sakura Script directly. As before, you can also use it alongside single-line text containing conventional Sakura Script.

### Syntax

```
ま０５：てすとてすと
```

The part before 「：」 defines the expression or other options, and the part after it is the text to speak.

The basic form is: one character you have set, followed by a surface number, then a colon and the text. Surface numbers (expression IDs) can be entered in either half-width or full-width characters, but it is easier to type them in full-width characters while Japanese input mode is on.

```
ま０５「かぎかっこでもいけるよ」
```

You can also enclose the text in quotation marks, but make sure to close them.

```
ま消：きゃー消えちゃった―
```

If you write 「消」 instead of a number, the window disappears (the character is hidden).

```
ま　：さっきの表情のままね
```

If you leave it blank, the previous expression is kept. Spaces are ignored, whether full-width or half-width.

```
二人：バルス！
```

Writing 「二人」 makes both characters speak at the same time.

```
ま０７し１１二人：バルス！
```

You can also combine multiple options this way. In the example above, the two characters change to expressions 7 and 11, respectively, and then speak at the same time.

```
待ち無しま０５：あまり待たない
待ちゼロま０５：ぜんぜん待たない
待ち多めま０５：ふつうより長めに待つ
```

You can control the wait time before speaking starts, for example, when you want to add an immediate retort or show a character thinking for a while. Note that **a suitable wait time is added by default even if you don't specify one**.

```
クリック待ちま０７：クリック待ってる
```

Writing クリック待ち makes the balloon wait for a click before speaking.

```
改行無しま０５：改行しないよ
```

Writing 改行無し lets you change only the expression without starting a new line after the previous text.

```
改行多めま０８：改行しまくり！
```

Adds a few extra line breaks, for example, to separate paragraphs.

```
ま００：（ユーザ）さん！
```

Inserts the user's name within the text. This applies only to the spoken text after ：.

```
ま０５：（チョコ｜菓子パン｜ケーキ）食べよう！
```

Write strings separated by ｜ and enclose them in parentheses to select one at random.

```
＃コメントなので無視
```

Lines beginning with ＃ are completely ignored.

```
＠設定：パッシブモード
＠設定：クイックセクション
＠設定：タイムアウト1000「時間切れ」
```

Lines beginning with 「＠設定：」 specify options related to the following talk. The examples above are, respectively,

- Passive mode (ignore everything except mouse reactions)
- Quick section (display all text instantly, ignoring all waits)
- Timeout (wait for the following number of milliseconds, then call the function whose name is enclosed in 「」)

respectively.

```
＠メニュー：さんぷる１｜Sample1Execute
＠半分メニュー：さんぷる２｜さんぷる２実行
＠改行多めメニュー：さんぷる３｜OnTest3Exec｜R0
＠クリック待ちメニュー：さんぷる４｜さんぷる4実行
```

Lines beginning with 「＠～メニュー：」 display a menu.<br>
A half menu displays two items side by side in each row of a standard-size balloon.<br>
Adding “more line breaks” makes each line break one and a half lines high. Use it to separate choices, for example.<br>
Adding “wait for click” puts the script into click-wait mode (`\x`) immediately after displaying the menu.

The remainder is separated by ｜. The first item is the text to display, and the second and subsequent items are the function/event to execute.

Also, **menus automatically use a quick section**, so they are displayed all at once without any waits.

### Automatic Chain Talk and Random Selection

```
ま０５：ちぇいんてすと。
し１０：うまくいくやろか。
=====
ま０５：ちぇいん2-Aにきたよ。
し１０：成功やね。
-----
ま０５：ちぇいん2-Bにきたよ。
し１０：ここはランダムや。
```

Separating sections with ===== (5 or more = signs) creates chain talk, while separating them with ----- (5 or more - signs) creates random selection.

For example, in the case above, after speaking up to the first =====, the talk ends for the time being. The next time it is time to speak random talk, one of the second and third talks is spoken.

### FAQ

**Why EX?**: There used to be an event-processing support library called “Ayariris,” but it still had too many dependencies to separate it out... There are also other libraries for explaining terminology.

**Why did you write this?**: I’m glad to get ideas from places like Twitter, but converting every single entry in the format Ra “mumble” Te “mumble” into Sakura Script is **extremely tedious**...

**I want to do dubious things in bulk in the development version.**: “MobileMaster” and Traffic☆Train are currently being used as the debugging front line.

**I want to be able to write things like choices and eventually reach Satori’s level...**: For that kind of complicated stuff, just write Sakura Script...
