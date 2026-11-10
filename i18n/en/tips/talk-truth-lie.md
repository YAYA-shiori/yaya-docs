# Truths and Lies About Statements

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

This page collects easily misunderstood points and miscellaneous tips about using statements.<br>
Although this is titled “Truths and Lies,” it has all turned out to be lies (sweat).

Some of these points may change as the statements themselves are improved.<br>
Remember that they apply only to statements **as they are now**.

#### It makes little difference whether you use local or global variables

<span style="font-size:24px"><span style="color:#cc0000">×</span></span> - False

Use these two types deliberately for different purposes.<br>
If you leave global variables around, they are saved as-is, increasing the size of the save file. Also, needlessly increasing the number of variables that are retained indefinitely can make processing progressively slower.

Make active use of local variables.

#### Frequently using ERASEVAR reduces memory usage

<span style="font-size:24px"><span style="color:#cc0000">×</span></span> - False

In the current implementation, ERASEVAR only marks a variable as “deleted”; it still occupies memory.<br>
Unless there is a particular reason, calling ERASEVAR frequently has little effect. In fact, it can make things considerably slower because the variables to delete have to be searched for each time.<br>
It is better to use local variables actively so that there is no need to delete them in the first place.

However, using ERASEVAR on global variables just before shutdown is useful for preventing the save file from growing too large (???`_variable.cfg`).

#### Using arrays makes things slower

<span style="font-size:24px"><span style="color:#cc0000">×</span></span> - False

**Generic arrays** are fast enough.<br>
Depending on the situation, using a generic array for references can even be faster than creating a large number of variables.

However, simple arrays are slower.<br>
Use IARRAY and similar functions to ensure that you are using a generic array.

#### Using the feedback operator to pass values to functions is faster

<span style="font-size:24px"><span style="color:#cc0000">×</span></span> - Mostly false

Unlike pass-by-reference in C++ and similar languages, the current implementation achieves this by assigning the calculation result back to the variable. Using the feedback operator may therefore be slower.

Unless you really need to do this, don't overthink it; just pass the value normally.

――pona@bugtra

#### Enclosing an if statement's condition in "()" makes it slower

<span style="font-size:24px"><span style="color:#cc0000">×</span></span> - False

"()" are discarded when the dictionary finishes loading, so whether they are present makes no difference. Their presence or absence also does not affect internal memory usage.

You can decide based on what you are used to or what looks better.

――yukaya

#### You cannot use Japanese function names

<span style="font-size:24px"><span style="color:#cc0000">×</span></span> - False

You can. Many people simply do not use them out of habit.<br>
You can use Japanese (two-byte characters such as kanji and hiragana) for both function names and variable names.<br>
The following are not allowed:

- Starting with half-width digits - they may be mistaken for numbers
- Starting with an underscore - this conflicts with local variables
- A name that could conflict with a system function written entirely in half-width uppercase English letters - this will not cause an error, but it is best not to use such a name
- A name containing half-width operators such as +−＊／ - it may be mistaken for a calculation expression
