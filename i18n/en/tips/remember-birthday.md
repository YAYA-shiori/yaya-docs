# Remember birthdays

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

<span style="color:Red">※This example writes the OnChoiceSelect choice directly as a standalone function. See [Writing a choice directly as a standalone function](independent-choice-function.md).</span>

### For Mon version 4

- Koki has published a method using InputBox.

<http://homepage2.nifty.com/ko-ki/Birthday.txt>

- A revised version of Koki's Birthday.txt is available below.

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver4.txt](http://couperin.cool.ne.jp/ghost/birthday_ver4.txt)<br>
[Archived copy](http://www.towano.net/ua-ks/index.php?%CA%B8-%C3%C2%C0%B8%C6%FC%A4%F2%B3%D0%A4%A8%A4%EB)
It works correctly, but it contained a syntax error. The comments and warnings have also been corrected, so use this version.<br>

(Example of adding it to a ghost)<br>
Add the script in Birthday.txt above (excluding `\![open,inputbox,OnInputBirthday,-1]`) to a dictionary, create a function for birthday entry (ChoiceBirthdayEntry in this example), and call it from a choice.<br>

```
ChoiceBirthdayEntry
{
　 "\0誕生日を教えてください。\n\n/
　　\w8形式はYYYYMMDDとか、ＹＹＹＹ年ＭＭ月ＤＤ日とか、\n/
　　YYYY/MM/DD等でお願いします。\![open,inputbox,OnInputBirthday,-1]\e"
}
```

### For Mon version 5

The string manipulation function SUBSTR used in this script counts each character as 1 in Mon version 5, whether it is half-width or full-width. Therefore, the relevant part needs to be rewritten.<br>
A sample is available below.

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver5.txt](http://couperin.cool.ne.jp/ghost/birthday_ver5.txt)

## Attached files

- [Birthday_revised_edition.dic](../attachment/Birthday_revised_edition.dic)
