# Optimization

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## Optimization tuning

**Warning!** In most cases, there is no problem at all even if you do not apply the changes described here.<br>
Use them with care, as they may cause unexpected problems.

### Introduction

Optimization tuning for AYAv5, for those who don't mind being a guinea pig!<br>
Ideal for impatient people.

### Speeding up startup

AYA-based ghosts often share the drawback of slow startup, which may be a source of frustration for many. This section covers simple tuning for faster startup.

#### Startup is slow in an environment with many ghosts installed

These days, the total number of ghosts can easily reach four digits, and many environments probably have hundreds installed.
...That's all well and good, but the amount of ghost information sent from the baseware has also grown enormous, creating the troublesome problem of AYA taking a long time to parse it.

#### Simple tips

**Risk level**: ★★☆☆☆

The solution is simple: take some of the #define entries near the beginning of aya_shiori3.dic and

```
#define IGLIST_MAX 0
#define REQUEST_LINES_LIMIT 30
```

change them to something like this.

**IGLIST_MAX**: AYA has a feature that searches internally for information about installed ghosts without relying on the baseware. This setting indicates whether to enable it: 0 disables it, and -1 means unlimited. If you do not need it, disabling it is perfectly fine.

**REQUEST_LINES_LIMIT**: Communication between the baseware and a ghost takes place in strings spanning multiple lines. This setting limits the number of lines to parse, based on the idea of avoiding delays when parsing large amounts of notifications.

Note that changing these settings can cause problems for ghosts that need to handle information about installed ghosts/balloons, and so on.

#### Tips for those who want to try a little more

**Risk level**: ★★★★☆

...So, for those who still can't stand it, here's a tip. Disable ghost information retrieval itself.

Around line 600 onward in aya_shiori3.dic, you should find something called On_installedghostname. Comment out all of it.

```
/*On_installedghostname
{
    (ごにょごにょ)
}*/
```

Something like this.

### Random talk is slow to appear

At last, your masterpiece is complete! It even has hundreds of random talks!!<br>
...But it's slow...

This is an optimization tip for a somewhat unusual situation.

This is an extended version of a tip that umeici mentioned on the support forum or in a diary. It became possible with the latest version of AYA.

#### Speeding things up with single quotes

**Risk level**: ★★★★☆

You probably write your random talks in aya_aitalk.dic.

```
RandomTalk
{
   "ごにょごにょ"
}
```

Something like this.

You enclose the text in " " and write Sakura Script out directly, but newer versions of AYA also allow ' ' in addition to " ".

Before explaining why that matters, let's look at an example of the change.<br>
If you just want to use it right away without worrying about the details, copy and paste this.

```
RandomTalk
{
    TOSTR(EVAL(CHR(0x22)+RandomTalkEx()+CHR(0x22)))
}

RandomTalkEx
{
    'ごにょごにょ'
}
```

That's it: just rename the original RandomTalk to something else (here, RandomTalkEx), change the quotes around the text to ' ', and add a RandomTalk with that unusual command.((The outer TOSTR probably isn't necessary, but I've left it in just in case. If it bothers you, feel free to remove it.))

...Now, let's explain how it works.

In the new versions of AYA5, ' ' means **do not expand %()**.<br>
For details, see the AYA manual. When you enclose text in ' ', the feature that lets you insert variables, functions, and expressions by writing things like %hogehoge or %(hogehoge) is entirely disabled.

With the original " " form, AYA has to parse all the embedded expressions and evaluate them. With ' ', the enclosed part is treated as a plain string, so almost no processing is needed.

Recall how AYA behaves: everything inside a function is evaluated, and then one of the results is selected at random (or one is selected according to the options).

...Leaving aside that complicated explanation, the point is that **if you write hundreds of random talks, the %() processing must also be done hundreds of times**, so you can imagine why it gets slow.((People who know the details of AYA's actual internal processing may have objections, but this explanation is intended to be easy to understand.))

That covers the part renamed to RandomTalkEx, but as things stand, the contents of %() will not be inserted correctly. The solution is:

```
TOSTR(EVAL(CHR(0x22)+RandomTalkEx()+CHR(0x22)))
```

TOSTR is a command that means "treat this as a string," but it is not important here. **The key is EVAL and what is inside its parentheses**.

EVAL is a command that means "execute the contents passed in parentheses as an AYA script." And CHR(0x22) means ".

...You can probably see what's happening. The script that EVAL executes becomes:

```
" + RandomTalkExの結果 + "
```

This creates an expression that performs the %() expansion.<br>
Instead of having to process %() hundreds of times, the part enclosed by EVAL only needs to be processed once. That's the trick that makes it faster.

### For those who want to go even further

Optimization techniques that cannot be used as-is with other ghosts have been implemented in various ways in Emily/Phase4 at

<http://ssp.shillest.net/ghost.html>

The dictionaries are pretty messy, so they are not the best examples to follow, but they may give you something to talk about (wry smile).
