# 简写函数、变量和 Sakura Script

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

加入下面这一行后，就可以将之后的 `reference[*]` 缩写为 `Ref[*]`。<br>
函数和 Sakura Script 等也可以同样进行替换。

```
#define Ref reference

OnGhostChanged
{
	"\\0\s[0]%(Ref[0])さんから交代。\e"
}
```

写法为「`#define` 要替换的文本 替换后的文本」。<br>
`#define` 的生效范围是从其下一行开始，到同一词典文件末尾为止。<br>
`#globaldefine` 的生效范围是从其下一行开始，覆盖之后读取的所有词典文件（读取顺序按 yaya.txt/aya.txt 中的记载顺序）。<br>
`#define` 会先于 `#globaldefine` 处理。<br>
请根据用途区分使用。

在 OnTranslate 中使用 REPLACE 函数进行替换时，只会在脚本（对话）即将显示在对话框之前替换脚本；而 `#define` 会在读取词典时直接替换词典内容。<br>

### 注意事项

<span style="color:Red">词典中写入的所有文本都会成为替换对象，因此使用时请尽量缩写为不容易与其他文本重复的内容。</span>
