# 誕生日を覚える

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

<span style="color:Red">※ここでは、OnChoiceSelectの選択肢をいきなり独立した関数で書いています。[選択肢をいきなり独立した関数で書く](independent-choice-function.md)を参照してください。</span>

### 文Ver.4の場合

- InputBoxを使ったやり方を、こーき氏が公開しています。

<http://homepage2.nifty.com/ko-ki/Birthday.txt>

- こーき氏のBirthday.txtを改訂したものを、下記に上げておきます。

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver4.txt](http://couperin.cool.ne.jp/ghost/birthday_ver4.txt)<br>
[保管版](http://www.towano.net/ua-ks/index.php?%CA%B8-%C3%C2%C0%B8%C6%FC%A4%F2%B3%D0%A4%A8%A4%EB)
動作に支障はありませんが、構文ミスがありました。コメントアウトされている注意事項も直っていますので、こちらをお使い下さい。<br>

(ゴーストに組み込む時の例)<br>
上のBirthday.txt内にあるスクリプト（「`\![open,inputbox,OnInputBirthday,-1]`」は除く）を辞書に組み込み、誕生日入力用の関数（今回はChoiceBirthdayEntry）を作成し、選択肢から呼び出してください。<br>

```
ChoiceBirthdayEntry
{
　 "\0誕生日を教えてください。\n\n/
　　\w8形式はYYYYMMDDとか、ＹＹＹＹ年ＭＭ月ＤＤ日とか、\n/
　　YYYY/MM/DD等でお願いします。\![open,inputbox,OnInputBirthday,-1]\e"
}
```

### 文Ver.5の場合

ここのスクリプトで使われている、文字列操作関数「SUBSTR」は、文version 5では半角でも全角でも、ひとつの文字は1と数えます。そのため、該当部分を書き直す必要があります。<br>
下記にサンプルを上げておきます。

[http://couperinjp.hp.infoseek.co.jp/ghost/birthday_ver5.txt](http://couperin.cool.ne.jp/ghost/birthday_ver5.txt)

## 添付ファイル

- [Birthday_revised_edition.dic](../attachment/Birthday_revised_edition.dic)
