# 记住生日

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

<span style="color:Red">※这里直接将 OnChoiceSelect 的选项写成了独立函数。请参阅[将选项直接写成独立函数](independent-choice-function.md)。</span>

### 文 Ver.4 的情况

- こーき氏公开了使用 InputBox 的方法。

<http://homepage2.nifty.com/ko-ki/Birthday.txt>

- 下面提供的是对 こーき氏的 Birthday.txt 进行修订后的版本。

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver4.txt](http://couperin.cool.ne.jp/ghost/birthday_ver4.txt)<br>
[存档版](http://www.towano.net/ua-ks/index.php?%CA%B8-%C3%C2%C0%B8%C6%FC%A4%F2%B3%D0%A4%A8%A4%EB)
虽然不影响运行，但其中有语法错误。注释掉的注意事项也已修正，请使用这个版本。<br>

（整合到人格中的示例）<br>
将上面的 Birthday.txt 中的脚本（不包括「`\![open,inputbox,OnInputBirthday,-1]`」）整合到词典中，创建用于输入生日的函数（此处为 ChoiceBirthdayEntry），然后从选项中调用该函数。<br>

```
ChoiceBirthdayEntry
{
　 "\0誕生日を教えてください。\n\n/
　　\w8形式はYYYYMMDDとか、ＹＹＹＹ年ＭＭ月ＤＤ日とか、\n/
　　YYYY/MM/DD等でお願いします。\![open,inputbox,OnInputBirthday,-1]\e"
}
```

### 文 Ver.5 的情况

这里脚本中使用的字符串操作函数「SUBSTR」，在文 version 5 中，无论半角还是全角，一个字符都按 1 计算。因此，需要改写相应部分。<br>
下面提供了示例。

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver5.txt](http://couperin.cool.ne.jp/ghost/birthday_ver5.txt)

## 附件

- [Birthday_revised_edition.dic](../attachment/Birthday_revised_edition.dic)
