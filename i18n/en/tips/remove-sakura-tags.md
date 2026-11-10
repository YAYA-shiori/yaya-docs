# Remove SAKURA Script Tags

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Version 4/5 shared version

This function takes a string containing SAKURA Script tags as an argument and returns the string with the SAKURA Script tags removed.

[View the dictionary file that you can copy and paste as-is-1](../attachment/EraseTag1.txt)

Try expanding anchor tags. (The part between **ANCHOR_TOP** and **ANCHOR_END** is the added part.)

[View the dictionary file that you can copy and paste as-is-2](../attachment/EraseTag2.txt)

### Version 5 only

If all you want to do is simply remove tags, this will do the job.<br>
It's very rough, so don't rely on it too much (what

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

There's a mysterious regular expression here, but don't worry about it (what<br>
If you don't need to convert \\\\ to \\ (for example, if you plan to insert it into Sakura Script again later),

```
  _text = REPLACE(_text,'\\','\')
```

remove this line.

To prevent it from matching escaped tags, use the following.

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'(?<!\\)\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

### Display tags in the balloon as-is instead of removing them

- [Escape SAKURA Script tags](escape-sakura-tags.md)

## Attachments

- [EraseTag1.txt](../attachment/EraseTag1.txt)
- [EraseTag2.txt](../attachment/EraseTag2.txt)
