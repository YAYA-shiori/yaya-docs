# 转义 Sakura Script 标签

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

- 适用于不删除标签，而是让它原样显示在对话框中的情况。例如「`\s[]`0」会转换为「\\`\s[0]`」。
- 基本上，在对话框中显示「不知道里面装着什么」的变量时，最好使用此函数，以免出错。

### 转义所有 Sakura Script

- 使用 Hello YAYA World 或 SimpleYAYA 模板中的 [Escape～函数](../system/yaya-optional-dic.md)

```
EscapeAllTags( エスケープしたい文字列 )
```

#### 使用示例

```
OnGhostChanged
{
_name = EscapeAllTags( reference[0] )
"%(_name)さんから交代したよ～。\e"
}
```

这样一来，即使是从名为「青い`\105`のノート」的人格切换而来，对话框中也会原样显示「青い`\105`のノートさんから交代したよ～。」。

### 只转义危险的 Sakura Script

- 使用 Hello YAYA World 或 SimpleYAYA 模板中的 [Escape～函数](../system/yaya-optional-dic.md)

```
EscapeDangerousTags( エスケープしたい文字列 )
```

只转义 vanishbymyself 等执行后会造成麻烦的 Sakura Script。
例如，在执行从别处找到的带有 Sakura Script 的对话时使用。

### 不想转义，而是想删除

- [删除 Sakura Script 标签](remove-sakura-tags.md)
