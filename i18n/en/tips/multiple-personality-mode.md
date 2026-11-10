# Multiple Personality Mode

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Assume that the mode is stored in the variable mode, and that there are modes 0 and 1.<br>
Write the random talk event OnAiTalk as follows.

Version5

```
OnAiTalk
{
　EVAL("OnAiTalk%mode")
}
```

Version4

```
OnAiTalk
{
　CALLBYNAME("OnAiTalk%mode")
}
```

This lets you separate events by mode as shown below.<br>
Do the same for the other events, and put the dictionaries for each mode into separate dictionary files to finish setting this up.<br>

```
OnAiTalk0
{
　// モード 0
　"\0ユーザーさん大好きっ。\e"
}

OnAiTalk1
{
　// モード 1
　"\0くたばれ腐れユーザーさん。\e"
}
```

(From the notes in "et cetera.")
