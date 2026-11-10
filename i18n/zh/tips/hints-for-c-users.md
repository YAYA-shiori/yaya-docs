# 给 C 语言使用者的提示

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 这篇文章是什么？

AYA是一种 SHIORI，具有以类 C 的方式组织的语法、简单（层次较浅）的规格，<br>
以及强大的编程能力等特点，因此 C 系语言的使用者即使几乎不看手册，<br>
也能直接上手使用。

然而，这些特点反过来也可能成为意想不到的陷阱。

总之，这些是我过去的失败记录。<br>
其中大部分只要认真阅读手册就能避免……

（撰写：浮子屋）

<span style="color:Red">※以下内容写于 AYA5。部分项目可能不适用于 YAYA。</span>

## 最基础的基础

- 函数的返回值会从此前输出的候选项中选出。
- 因此，如果因为某种错误而将空字符串加入候选项，就可能偶尔什么也不说，变成难以发现的错误。<span style="color:Red">请注意。</span>
- 为了避免这种情况，可以有效利用 void 或输出确定符 --。
- 从 Tc573-1 开始，可以使用带参数的 return，因此能够采用与 C 相同的写法。带参数的 return 会替换此前的输出候选项，因此返回空字符串之类的错误应该会大幅减少。

## 字符串展开

- "" 会展开字符串中的变量和函数。
- 习惯了 C 语言后，可能会不由自主地想用 " 编写字符串字面量，但最好记住 ' 才表示字符串。<span style="color:Red">请注意。</span>
- 不过，从内部处理来看，不包含 % 的字符串在生成中间代码时似乎会作为字面量处理，与 ' 的效果相同。
- "abc%(hemo)efg" 与写成 'abc'+EVAL('hemo')+'efg' 的效果（大概）几乎相同。
- 因此，对于「从大量候选项中择一」之类的函数，展开所有候选项是没有意义的。
- 可以等候选项确定后，再用 EVAL 展开嵌入内容。[性能优化](optimization.md)
- 除非有特殊理由，否则应使用 %() 明确指定范围。仅使用 % 进行最长名称匹配展开的开销较大。
- "abc%hemoefg" 在生成中间代码时大概会变成 'abc'+"%hemoefg"，运行时必须解析 "%hemoefg"。

## 变量与运算

- 变量分为全局变量和局部变量。以 _ 开头的变量是局部变量。
- 全局变量会在 SHIORI 加载和卸载时保存到文件或从文件读取。
- 因此，对于不需要保存的全局变量，最好用 ERASEVAR 删除。
- 变量的初始值是空字符串，不是「0 或空字符串」。<span style="color:Red">请注意。</span>
- 字符与数值进行运算时，加法的结果是字符串，其他运算的结果则为空字符串。
- 因此，如果数式中混入不存在的变量，结果会是字符串或空字符串。<span style="color:Red">请注意。</span>
- 对于会不断递增的变量，如果没有先将其初始化为数值，可能会导致意想不到的错误。
- 例如，代码 i++ 会根据上述逻辑变成类似 "11111" 的字符串。<span style="color:Red">请注意。</span>
- 如果不确定变量是否已初始化为数值，也可以用 CVINT 强制将其转换为数值。
- 局部变量的作用域是&color(Red){「在当前以及更深层的{ }内有效」};。
- 上述规格有时会导致意想不到的错误。请看下面的代码示例。<span style="color:Red">尤其需要注意。</span>

```
hogehoge{
  // ここに _sum=0 が必要。無いとこの関数の結果は空文字
  for _i=0 ; _i<10 ; _i++ {
    _sum+=_i
  }
  _sum
}
```

- 使用比较运算 == 比较数值和字符串时，结果为假。
- 使用比较运算 == 比较未定义变量和 '' 时，结果为真。

## 流程控制

- C 语言中的 else if 对应 elseif。
- 与 C 语言中的 switch 类似的结构不是 switch，而是 case ～ when。
- 使用 for `_i` = 1; `_i` < 11; `_i`++ 这样的写法时，如果写成 i 而不是 `_i`，大多会陷入无限循环并卡死。
- 因此，如果循环卡死了，就仔细检查是否漏写了 _。很容易忘记，<span style="color:Red">请注意。</span>

## 人格模板（aya_shiori3.dic）

- OnAiTalk 是 AYA 特有的事件。它由 OnSecondChange 触发，每隔 aitalkinterval 秒从 aya_shiori3.dic 发出通知。
- 连锁由人格自身词典中 OnAiTalk 内的条件分支，以及模板一侧的 ChainTalk 实现。
- 因此，随意改写人格自身词典中的 OnAiTalk 会破坏连锁机制。
- res_reference0 看起来像普通变量，但为其赋值会使模板在请求响应中加入 Reference?:。
- 也就是说，为其赋值会触发交流。<span style="color:Red">请注意。</span>
- ghostexlist / ghostexcount 基于本体的 otherghostname 通知，因此有时并不准确。
- On_otherghostname 和 On_hwnd 不在 aya_shiori3.dic 中，而是在人格自身的 `*_string.dic` 中。
- 使用自定义事件时，如果事件名不以「On」开头，就会自动调用名称前加上「`On_`」的函数。
- SAORI 的返回值会转换为适当的类型后返回。字符串中的字节值 1 会变成逗号。
- 此时的优先顺序为 CVINT→CVREAL→字符串。

## 其他

- SAORI 会在首次使用时加载，并在 SHIORI 卸载时卸载。
- 也就是说，SSP 启用了人格缓存时，由于 SHIORI 会被缓存，即使人格结束，SAORI 也可能不会卸载，<span style="color:Red">请注意。</span>[确保在人格启动和结束时执行操作](reliable-boot-shutdown.md)
- 人格结束时需要终止的 SAORI，必须使用 UNLOADLIB 明确终止（也可以使用 SHIORI3FW.SaoriUnloadAll）
- 如果习惯了 C 语言的思维方式，可能很难意识到函数名或变量名可以在运行时通过 EVAL 动态拼接。
- 如果想根据某个变量的值调用对应的函数，可以使用 EVAL("`func_`%(`_var`)") 这一语法。[直接将选项写成独立函数](independent-choice-function.md)
- 如果某个变量的值是包含 %() 的字符串，并且之后想要展开它，可以使用 EVAL(CHR(0x22)+`_var`+CHR(0x22)) 这一语法。[性能优化](optimization.md)
