# Making Favorites Easier to Write

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

For anyone thinking, “I can't be bothered to write CHR(1)CHR(2) every time!”<br>
**???Modifying `_string.dic` is required.**

### Method

First, let's add a function.

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

Add this anywhere.

Next, change how you write the Favorites menu itself.<br>
The example uses On_sakura.recommendsites, but you can use any menu.

```
On_sakura.recommendsites
{
    "/
    ごにょごにょ%(CHR(1))http://go.nyo/%(CHR(1))%(CHR(2))/
    "
}
```

This is what it looks like originally... but editing it is very tedious and hard on the eyes.<br>
So, rewrite it like this:

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

 | is the delimiter.<br>
You can add half-width spaces or tabs on either side as you like to make it easier to read.

You can give `_EX` any name you like, but don't forget to add : array.

The examples are enclosed in ' ', but using " " works just as well.<br>
Use " " if you want to use variables or need to avoid an apostrophe in a site name.

This is used in Emily/Phase4 and others.<br>
If you're unsure, refer to those as well.

―― Pona@Bugtra
