# 保留字

## 概要

YAYA 系統保留的名稱。不可用於使用者自訂的變數名稱或函式名稱。

## 系統函式

[系統函式一覽](../system/system-functions-index.md) 中列出的所有函式名稱皆為保留名稱。

!!! note "大寫字母＋底線組成的名稱"
    為了確保未來的相容性，最好不要使用僅由大寫字母與底線組成的名稱。

## 控制結構關鍵字

以下控制流程用語為保留字：

```
if  elseif  else  case  when  others  switch
while  for  break  continue  return  foreach
void  parallel
```

`void` 和 `parallel` 是控制函式輸出的關鍵字（[陣列](05-arrays.md#並列出力)）。

## 運算子

不可用於變數名稱或函式名稱的保留運算子符號：

```
( ) [ ] ! ++ -- * / % + - & == != <= >= < > _in_ !_in_ && ||
= := += -= *= /= %= +:= -:= *:= /:= %:= ,=
```
