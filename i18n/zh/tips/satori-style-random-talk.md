# 写出Satori风格的随机对话

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 在AYA5中轻松写出Satori风格的随机对话

这是＠ちに写的。

词典：[satori_for_aya.dic](http://mistnar.hp.infoseek.co.jp/ukagaka/ayav_text/satori_for_aya.dic)

<span style="color:Red">※这里将OnChoiceSelect的选项直接写成独立函数。请参阅[将选项直接写成独立函数](independent-choice-function.md)。</span>

### 不太容易理解的说明

可以在AYA词典中使用Satori风格的脚本。<br>
不过，本质上当然还是AYA，请不要在这方面产生误解。

### 用法

将aya_aitalk.dic中的

```
OnAiTalk
```

部分的

```
RandomTalk
```

改写为

```
OnAiTalk.Satori
```

，或者追加这段内容即可运行。<br>
请将对话内容写在此词典的

```
RandomTalk.Satori
```

中。<br>
Satori风格的脚本仅在这个函数内有效。

### 支持的标签

```
（サーフィス番号）
：
＠
＞
＿
```

顺带一提，＠和＞的处理完全相同，使用哪个都可以。<br>
像（＿あそぶ）这样写时，效果等同于`\_q[あそぶ,＿あそぶ]`。

其他示例请看下面的"RandomTalk.Satori"。

### 想用玉试试看

```
GET SHIORI/3.0
ID: OnAiTalk.Satori
Sender: CallAIMist
SecurityLevel: local
Charset: Shift_JIS
```

以上，复制粘贴即可。

### 注意

没有进行任何错误修复。<br>
如果无法运行，抱歉。（特别是没有测试＿标签(ﾟ∀ﾟ)
