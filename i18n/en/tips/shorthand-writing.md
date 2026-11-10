# Shortening Functions, Variables, and Sakura Script

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Adding the following line lets you write `reference[*]` in the shorter form `Ref[*]` from that point on.<br>
Functions and Sakura Script can be replaced in the same way.

```
#define Ref reference

OnGhostChanged
{
	"\\0\s[0]%(Ref[0])さんから交代。\e"
}
```

The format is “`#define` text to replace replacement text”.<br>
The scope of `#define` extends from the following line to the end of the same dictionary file.<br>
The scope of `#globaldefine` extends from the following line to all subsequently loaded dictionary files (in the order specified in yaya.txt/aya.txt).<br>
`#define` is processed before `#globaldefine`.<br>
Use each as appropriate.

When you perform replacement with the REPLACE function inside OnTranslate, only the script is replaced just before the script (talk) is displayed in the balloon. With `#define`, the dictionary itself is replaced when it is loaded.<br>

### Notes

<span style="color:Red">All text written in the dictionary is subject to replacement, so if you use this, choose text that is unlikely to conflict with other text.</span>
