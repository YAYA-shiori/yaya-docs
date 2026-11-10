# Tips for C Language Users

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## What Is This Article?

AYA is a SHIORI with a C-like, well-organized syntax, a simple (thin-layered) design, and<br>
powerful programming capabilities. This makes it possible for people familiar with C-family languages to use it<br>
with hardly any need to consult the manual.

However, these very features can also lead to unexpected pitfalls.

In short, this is a collection of notes about my past mistakes.<br>
Most of them could have been avoided by reading the manual carefully, but...

(Author: Ukiko-ya)

<span style="color:Red">※The following text is about AYA5. Some items may not apply to YAYA.</span>

## The Basics

- A function's return value is selected from the candidates output up to that point.
- Therefore, if an empty string accidentally becomes one of the candidates, it can cause a hard-to-find bug, such as occasionally not saying anything at all. <span style="color:Red">Take care.</span>
- To prevent this, you can make effective use of void or the output-commit operator --.
- Starting with Tc573-1, return statements with arguments became available, allowing you to write them as you do in C. A return statement with an argument replaces the previous output candidates, so bugs that cause an empty string to be returned should become much less common.

## String Expansion

- "" expands variables and functions within a string.
- If you are used to C, you may be tempted to write string literals using ", but it is better to remember that ' denotes a string. <span style="color:Red">Take care.</span>
- However, internally, strings that do not contain % seem to be treated as literals, equivalent to ', when the intermediate code is generated.
- "abc%(hemo)efg" is (probably) almost the same as writing 'abc'+EVAL('hemo')+'efg'.
- Therefore, for a function that "selects one from many candidates," expanding every candidate is wasteful.
- Once the candidate has been selected, you can use EVAL to expand the embedded text.[Optimization](optimization.md)
- Unless there is a special reason not to, you should explicitly specify the range with %(). Name expansion using longest match with % alone is expensive.
- "abc%hemoefg" is probably converted to 'abc'+"%hemoefg" when the intermediate code is generated, and "%hemoefg" must then be resolved at runtime.

## Variables and Operations

- There are global and local variables. Local variables are variables that begin with _.
- Global variables are saved to a file when SHIORI is loaded or unloaded, and read from the file when SHIORI is loaded.
- Therefore, global variables that do not need to be saved should be deleted with ERASEVAR.
- The initial value of a variable is an empty string. It is not "0 or an empty string." <span style="color:Red">Take care.</span>
- When a string and a number are used in an operation, the result is a string for addition, and an empty string for any other operation.
- Therefore, if an undefined variable is included in a formula, the result will be a string or an empty string. <span style="color:Red">Take care.</span>
- Variables that are incremented should be initialized to a number first to avoid unexpected errors.
- For example, code such as i++ will become a string like "11111" according to the logic above. <span style="color:Red">Take care.</span>
- If you are unsure whether a variable has been initialized to a number, you can also force it to be a number with CVINT.
- The scope of a local variable is &color(Red){“valid only in the current { } and any nested { }”};.
- The behavior described above can cause unexpected errors. See the following code example. <span style="color:Red">Take particular care.</span>

```
hogehoge{
  // ここに _sum=0 が必要。無いとこの関数の結果は空文字
  for _i=0 ; _i<10 ; _i++ {
    _sum+=_i
  }
  _sum
}
```

- When a number and a string are compared using the comparison operator ==, the result is false.
- When an undefined variable and '' are compared using the comparison operator ==, the result is true.

## Flow Control

- The equivalent of C's else if is elseif.
- The equivalent of C's switch is not switch, but case ～ when.
- In a notation such as for `_i` = 1; `_i` < 11; `_i`++, writing i instead of `_i` will usually cause an infinite loop and freeze things.
- So if a loop freezes, check carefully for _ characters. They are easy to forget, so <span style="color:Red">take care.</span>

## Ghost Template (aya_shiori3.dic)

- OnAiTalk is an AYA-specific event. It is sent every aitalkinterval seconds from aya_shiori3.dic, triggered by OnSecondChange.
- Chaining is done by the conditional branching inside OnAiTalk in the ghost's dictionary, together with ChainTalk on the template side.
- Therefore, carelessly rewriting OnAiTalk in the ghost's dictionary will break the chaining mechanism.
- res_reference0 looks like an ordinary variable, but assigning it a value causes the template to include Reference?: in the request response.
- In other words, assigning it a value triggers communication. <span style="color:Red">Take care.</span>
- ghostexlist / ghostexcount are based on the baseware's otherghostname notification, so they may not be accurate.
- On_otherghostname and On_hwnd are in the ghost's `*_string.dic`, not aya_shiori3.dic.
- When using a custom event whose name does not start with “On”, a function name with “`On_`” added automatically is called.
- SAORI return values are converted to the appropriate types before being returned. Byte value 1 in a string becomes a comma.
- The conversion priority in that case is CVINT→CVREAL→string.

## Other

- SAORI is loaded the first time it is used, and unloaded when SHIORI is unloaded.
- In other words, if the ghost cache is enabled in SSP, SHIORI is cached, so <span style="color:Red">be aware</span> that SAORI may not be unloaded even after the ghost exits.[Make Sure Something Happens When a Ghost Starts and Exits](reliable-boot-shutdown.md)
- SAORI that need to be terminated when a ghost exits must be explicitly terminated with UNLOADLIB (SHIORI3FW.SaoriUnloadAll can also be used)
- If you think in C, it can be difficult to realize that function and variable names can be dynamically assembled at runtime using EVAL.
- If you want to call a function based on the value of a variable, the syntax EVAL("`func_`%(`_var`)") is useful.[Writing Choices as Separate Functions Right Away](independent-choice-function.md)
- If a variable contains a string with %(), and you want to expand it later, the syntax EVAL(CHR(0x22)+`_var`+CHR(0x22)) is useful.[Optimization](optimization.md)
