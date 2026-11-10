# What to Do When You Have a Problem

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Development-related questions are handled at the Ukagaka Development Forum<http://ghost.sakura.tv/fluxbb/viewforum.php?id=4>
.

### The ghost is running slowly

Have you left logging enabled?<br>
Review the talk settings file aya.txt once more.<br>

Alternatively, have you set “Get the list of installed ghosts” in `***_shiori3.dic`?<br>
Try reducing the maximum number to retrieve. If you do not use the ghost list at all, setting it to 0 is fine.<br>

### Choices can sometimes be selected and sometimes cannot

You may have forgotten to close a {} somewhere.<br>

### After selecting a choice, the ghost only says “1.”

If you are using Talk Ver5.0 to a version earlier than Ver5.2, the function specified in OnChoiceSelect may contain one or more of the following characters.

```
(　)　[　]　!　++　--　*　/　%　+　-　&　==　!=　<=　>=　<　>　_in_　!_in_
&&　||　=　:=　+=　-=　*=　/=　%=　+:=　-:=　*:=　/:=　%:=　,=
```

If you modify the function name so that it does not contain any of the characters above, it may work normally.<br>
(From [:::et cetera. - bbs](http://umeici.hp.infoseek.co.jp/bbs2.html)).

### Mysterious “0” or “1” appears in talk

When assigning a variable, did you mean to write “i = 1” but write “i == 1” instead?

### Random talk has stopped

You may have deleted OnSecondChange.<br>
If it is deleted, OnAiTalk will not be called.<br>
If OnSecondChange does nothing, write it as follows:<br>

```
OnSecondChange{}
```

(Reposted from the notes on [SatisFactory](http://www5d.biglobe.ne.jp/~satis/))<br>

### Does not start correctly

A syntax error in the script is the most likely cause.<br>
For YAYA Ver.5, you can find most syntax errors by using the syntax checker “Tama” on the YAYA Ver.5 release page.

[Checking dictionary errors with Tama](../tips/tama-error-check.md)

Examples of common mistakes.

- Forgetting to close ' ' or " "
- Including ' inside ' ', or " inside " "
  - %(CHR(0x22)) = " / %(CHR(0x27)) = '. Use these as needed.
- Writing elseif as else if
- Starting with elseif without writing if
- Too many or too few ( ) or { }
  - Look for a text editor that can check matching parentheses.
- Uppercase and lowercase letters in variable and function names
- Trying to use a variable that has never been used before
  - Referencing a variable that has never been used does not cause an error.
- Incorrect character encoding for the dictionary
  - This applies only if you are using a UTF-8 dictionary. Naturally, if you write it in ShiftJIS, you will be left struggling with a flood of mysterious errors. The reverse is also true.

### “Invalid argument type” error for all specific functions in a dictionary

When using a function, if you pass a string argument where a numeric argument is required, or vice versa, an error may occur even for functions that are written correctly.

Even if there is a possibility that “an argument that is neither numeric nor a string” will be passed, it may still cause an error. Make use of TOINT and TOSTR.<br>

- Example

```
i = TOSTR( i )
REPLACE( i , "abc" , "bca" )
```

### Freezing when running SAORI

There may be a problem with how the path is written.<br>
Use "saori\\`\xxx`.dll" or "saori`\xxx`.dll", not "saori/xxx.dll".

### How can I write “]” inside SakuraScript's []?

Enclose the entire string in "". <br>
Write any " inside a pair of " as "".

```
_txt=REPLACE(テキスト,'"','""')
_txt='"' + _txt + '"'
"\![open,input,ID,-1,%(_txt)]"
```

A function that is easy to use is provided.

```
ESCAPE_TEXT
{
	_r = _argv[0]
	if RE_SEARCH(_r,'["\[\]]') >= 0 {
		'"' + REPLACE(_r,'"','""') + '"'
	}
	else {
		_r
	}
}
```

Write this somewhere, then

```
ESCAPE_TEXT(テキスト)
```

and it should work correctly.

### When distributing a ghost, you don't know which files to delete

If any of the following files are in ghost`\master`, remove them.
(The string represented by \*\*\* varies depending on the ghost's settings.)

```
***_variable.cfg　（セーブデータ）
***.log　（AYA/YAYA実行ログ）
ssp_shiori_log.txt （SSP実行ログ）
「profile」フォルダまるごと
「var」フォルダまるごと
tama.exe
aycencode.exe
暗号化前の***.dic （※辞書の暗号化をしている場合）
```
