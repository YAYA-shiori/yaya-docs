# 讓お気愛選單更容易撰寫

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

這則技巧適合那些覺得每次都要寫CHR(1)CHR(2)之類，實在很煩人的人。<br>
**???需要修改`_string.dic`。**

### 方法

首先，新增函式。

```
LinkMenuConvert
{
    _text = ''
    _data = IARRAY
    for _i = 0 ; _i < _argc ; _i++ {
        _data = (RE_SPLIT(_argv[_i],'[ \t]*\|[ \t]*'),'','') //ダミー
        _text += "%(_data[0])%(CHR(1))%(_data[1])%(CHR(1))%(_data[2])%(CHR(1))%(CHR(2))"
    }
    _text;
}
```

先把這段加到任何位置。

接著，修改お気愛選單的撰寫方式。<br>
以下以On_sakura.recommendsites為例，實際上使用哪個都可以。

```
On_sakura.recommendsites
{
    "/
    ごにょごにょ%(CHR(1))http://go.nyo/%(CHR(1))%(CHR(2))/
    "
}
```

原本是這樣……但編輯起來非常麻煩，看得眼花撩亂。<br>
因此，改寫如下：

```
On_sakura.recommendsites
{
   LinkMenuConvert(On_sakura.recommendsites_EX)
}
 
On_sakura.recommendsites_EX : array
{
   'ごにょごにょ  | http://go.nyo/ | '
   'ほげほげ      | http://ho.ge/  | '
   "ふがふが      | http://fu.ga/  | "
}
```

| 是分隔符號。<br>
可以在左右適當加入半形空格或定位字元，讓內容更容易閱讀。

`_EX`部分可以使用任意名稱，但別忘了加上: array。

範例使用' '括住字串，但改用" "也完全沒問題。<br>
如果要使用變數等內容，或是網站名稱中包含'而需要避開，請使用" "。

Emily/Phase4等人格都有使用這種寫法。<br>
如果不清楚，也可以參考那些人格。

―― ぽな@ばぐとら
