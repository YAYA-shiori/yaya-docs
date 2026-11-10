# 保留字

## 概述

YAYA 系统中保留的名称。不能用作用户定义的变量名或函数名。

## 系统函数

[系统函数一览](../system/system-functions-index.md) 中列出的所有函数名均为保留名称。

!!! note "仅由大写字母和下划线组成的名称"
    为了兼容未来版本，最好不要使用仅由大写字母和下划线组成的名称。

## 控制结构关键字

以下控制流术语为保留字：

```
if  elseif  else  case  when  others  switch
while  for  break  continue  return  foreach
void  parallel
```

`void` 和 `parallel` 是控制函数输出的关键字（[数组](05-arrays.md#並列出力)）。

## 运算符

不能用于变量名或函数名的保留运算符符号：

```
( ) [ ] ! ++ -- * / % + - & == != <= >= < > _in_ !_in_ && ||
= := += -= *= /= %= +:= -:= *:= /:= %:= ,=
```
