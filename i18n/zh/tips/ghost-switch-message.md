# 更改人格切换消息

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

- 人格A说了包含「お料理」这句台词的内容
- 人格A说了包含「薬」这句台词的内容
- 其他情况

分别作出不同反应时。

```
OnGhostChanged
{
 　if reference0 == "ゴーストA" // （ここでゴースト名を指定）
 　{
 　　if "お料理" _in_ reference1 // （ここでキーワード「お料理」を指定）
 　　{
       "(文章1)"
 　　}
 　　elseif "薬" _in_ reference1 // （ここでキーワード「薬」を指定）
 　　{
 　　  "(文章2)"
 　　}
 　　else // （キーワード「お料理」がなかったときの反応）
 　　{
 　　  "(文章3)"
 　　}
 　}
}
```

如果要添加到现有词典中，请使用 elseif，而不是 if。

如果想增加用于改变反应的关键词，请增加第二个 elseif 部分。
