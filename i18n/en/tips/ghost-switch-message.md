# Change Ghost-Switch Messages

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Use different reactions depending on whether:

- Ghost A said a sentence containing “お料理”
- Ghost A said a sentence containing “薬”
- Something else

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

When adding this to an existing dictionary, use elseif instead of if.

To add more keywords that trigger different reactions, add more elseif clauses after the second one.
