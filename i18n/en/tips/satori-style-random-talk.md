# Writing Random Talk the Satori Way

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## Try writing random talk the Satori way, easily (@AYA5)

Written by @chini.

Dictionary: [satori_for_aya.dic](http://mistnar.hp.infoseek.co.jp/ukagaka/ayav_text/satori_for_aya.dic)

<span style="color:Red">※Here, the choices for OnChoiceSelect are written directly as independent functions. See [Writing choices directly as independent functions](independent-choice-function.md).</span>

### An unclear explanation

You can also use Satori-style scripts in an AYA dictionary.<br>
However, it is still basically AYA, of course, so be careful not to get confused about that.

### How to use it

In aya_aitalk.dic, replace or add to the

```
OnAiTalk
```

part:

```
RandomTalk
```

Change it to

```
OnAiTalk.Satori
```

and it will work.<br>
Write talks and similar content in this dictionary's

```
RandomTalk.Satori
```

function.<br>
Satori-style scripts are valid only within this function.

### Supported tags

```
（サーフィス番号）
：
＠
＞
＿
```

By the way, @ and > perform exactly the same operation, so either one is fine.<br>
Writing something like （＿あそぶ） is equivalent to `\_q[あそぶ,＿あそぶ]`.

For other examples, take a look at "RandomTalk.Satori" below.

### Try it with Tama!

```
GET SHIORI/3.0
ID: OnAiTalk.Satori
Sender: CallAIMist
SecurityLevel: local
Charset: Shift_JIS
```

That's it—copy and paste.

### Notes

I haven't done any bug fixing.<br>
Sorry if it doesn't work. (I haven't tried the ＿ tag in particular (ﾟ∀ﾟ)
