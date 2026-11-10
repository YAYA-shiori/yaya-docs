# 記住生日

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

<span style="color:Red">※此處將 OnChoiceSelect 的選項直接寫成獨立函式。請參閱[將選項直接寫成獨立函式](independent-choice-function.md)。</span>

### 文Ver.4的情況

- こーき氏公開了使用 InputBox 的做法。

<http://homepage2.nifty.com/ko-ki/Birthday.txt>

- 以下提供こーき氏的 Birthday.txt 的修訂版。

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver4.txt](http://couperin.cool.ne.jp/ghost/birthday_ver4.txt)<br>
[保存版](http://www.towano.net/ua-ks/index.php?%CA%B8-%C3%C2%C0%B8%C6%FC%A4%F2%B3%D0%A4%A8%A4%EB)
雖然不影響執行，但原檔有語法錯誤。註解掉的注意事項也已修正，請使用這個版本。<br>

（整合至人格時的範例）<br>
將上方 Birthday.txt 中的腳本（「`\![open,inputbox,OnInputBirthday,-1]`」除外）整合至辭典，建立用來輸入生日的函式（此處使用 ChoiceBirthdayEntry），並從選項呼叫該函式。<br>

```
ChoiceBirthdayEntry
{
　 "\0誕生日を教えてください。\n\n/
　　\w8形式はYYYYMMDDとか、ＹＹＹＹ年ＭＭ月ＤＤ日とか、\n/
　　YYYY/MM/DD等でお願いします。\![open,inputbox,OnInputBirthday,-1]\e"
}
```

### 文Ver.5的情況

此處腳本使用的字串操作函式「SUBSTR」，在文 version 5 中，無論半形或全形字元，一個字都會算作 1。因此需要改寫相關部分。<br>
以下提供範例。

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver5.txt](http://couperin.cool.ne.jp/ghost/birthday_ver5.txt)

## 附件

- [Birthday_revised_edition.dic](../attachment/Birthday_revised_edition.dic)
