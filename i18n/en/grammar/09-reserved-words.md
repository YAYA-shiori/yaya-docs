# Reserved Words

## Overview

Names reserved by the YAYA system. They cannot be used as user-defined variable names or function names.

## System Functions

All function names listed in the [System Function List](../system/system-functions-index.md) are reserved.

!!! note "Names Consisting of Uppercase Letters and Underscores"
    It is best to avoid names consisting only of uppercase letters and underscores, for future compatibility.

## Control-Flow Keywords

The following control-flow terms are reserved:

```
if  elseif  else  case  when  others  switch
while  for  break  continue  return  foreach
void  parallel
```

`void` and `parallel` are keywords that control function output ([Arrays](05-arrays.md#並列出力)).

## Operators

Reserved operator symbols that cannot be used in variable or function names:

```
( ) [ ] ! ++ -- * / % + - & == != <= >= < > _in_ !_in_ && ||
= := += -= *= /= %= +:= -:= *:= /:= %:= ,=
```

Operator words and symbols also cannot appear as part of a variable or function name.
