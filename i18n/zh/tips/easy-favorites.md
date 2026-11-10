# 让收藏夹更容易编写

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

适合那些不想每次都写CHR(1)CHR(2)之类内容的人！<br>
**???需要修改`_string.dic`。**

### 方法

那么，首先添加一个函数。

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

先把它添加到任意位置。

接下来，修改收藏夹菜单本身的写法。<br>
这里以On_sakura.recommendsites为例，实际使用时也可以选择其他项目。

```
On_sakura.recommendsites
{
    "/
    ごにょごにょ%(CHR(1))http://go.nyo/%(CHR(1))%(CHR(2))/
    "
}
```

原来的写法是这样……但编辑起来非常麻烦，看得眼花缭乱。<br>
因此，可以改写为：

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

|是分隔符。<br>
可以在它的左右适当添加半角空格或制表符，让内容看起来更清晰。

`_EX`部分可以使用任意名称，但请不要忘记加上: array。

示例中使用了' '括起字符串，不过改用" "也完全没问题。<br>
如果要使用变量等内容，或者网站名称中含有'而需要避免冲突，请使用" "。

Emily/Phase4等人格中也使用了这种写法。<br>
如果不明白，也可以参考那些人格。

―― ぽな@ばぐとら
