# Reserved Words

## Overview

Names reserved by the YAYA system. They cannot be used as user-defined variable names or function names.

## System Functions

All function names listed in the [System Function List](../system/system-functions-index.md) are reserved.

!!! note "Names with uppercase letters and underscores"
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

Reserved operator symbols that cannot be used in variable names or function names:

```
( ) [ ] ! ++ -- * / % + - & == != <= >= < > _in_ !_in_ && ||
= := += -= *= /= %= +:= -:= *:= /:= %:= ,=
```
