# 移除 Sakura Script 标签

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Version4/5通用版

这是一个接收包含 Sakura Script 标签的字符串作为参数，并返回移除 Sakura Script 标签后的字符串的函数。

[查看可直接复制粘贴的词典文件-1](../attachment/EraseTag1.txt)

试着展开锚点标签。（**ANCHOR_TOP**到**ANCHOR_END**的部分是新增部分）

[查看可直接复制粘贴的词典文件-2](../attachment/EraseTag2.txt)

### 仅限Version5

如果只想简单地删除标签，用这个就够了。<br>
因为处理得相当粗略，请不要太过依赖它（什么

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

里面写着莫名其妙的正则表达式，不过不用在意（什么<br>
如果不需要将\\\\改回\\（例如之后还要插入 Sakura Script 中使用），请

```
  _text = REPLACE(_text,'\\','\')
```

删掉。

如果要避免匹配转义后的标签，请按以下方式编写。

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'(?<!\\)\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

### 不移除，而是原样显示在对话框中

- [转义 Sakura Script 标签](escape-sakura-tags.md)

## 附件

- [EraseTag1.txt](../attachment/EraseTag1.txt)
- [EraseTag2.txt](../attachment/EraseTag2.txt)
