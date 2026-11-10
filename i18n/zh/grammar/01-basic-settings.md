# 基础设置

## 概要

YAYA 的默认 DLL 文件名为 `yaya.dll`，主文件名 `yaya` 可以自由更改为其他名称。

要运行 YAYA，需要一个称为“基础设置文件”的文件。基础设置文件的文件名为“主文件名.txt”，默认情况下为 `yaya.txt`。如果将 DLL 文件名更改为 `hoge.dll`，则基础设置文件的文件名为 `hoge.txt`。

基础设置文件是文本文件，会使用运行所在 OS 的默认字符编码进行解码。如果需要考虑国际化，为避免多字节字符编码相关的问题，基础设置文件应仅使用 ASCII 编码编写。

如果没有设置文件，或者没有任何要读取的词典，则会以[外壳模式](#シェルモード)运行（Tc574-7 / Tc602-12 及之后版本。在此之前，如果没有设置文件，会因错误 E0005 而停止运行）。

## 设置示例

```
// dics
dic, basis.dic
dic, control./*doc*/ayc

// option parameters
charset, UTF-8
charset.dic, Shift_JIS
charset.setting, Shift_JIS
charset.output, UTF-8
charset.file, Shift_JIS
charset.save, UTF-8
charset.extension, Shift_JIS

msglang, english
log, executelog.txt
iolog, off
fncdepth, 16
```

设置时，用逗号分隔命令和参数。空行（只有换行符的行）、`//` 之后的内容，以及用 `/*` 和 `*/` 括起来的区域都会被视为注释。

## 读取时发生词典错误后的行为

从 Tc555-1 起，读取时发生词典错误后，会先尝试使用紧急用基础设置文件重新读取。

紧急用基础设置文件的文件名为“主文件名_emerg.txt”，默认情况下为 `yaya_emerg.txt`。更改 DLL 名称时的行为也与普通基础设置文件相同。

如果仍然发生错误，request 函数将不返回任何内容（NULL）。

发生问题时，可以通过 [GETERRORLOG](../functions/GETERRORLOG.md) 获取错误日志。

使用 `yaya_emerg.txt` 进入的紧急模式不会变为[外壳模式](#シェルモード)。如果没有 `yaya_emerg.txt`，则会像以往一样停止运行。

## 设置项

### charset, name

设置默认字符编码。指定以下保留值之一。如果未指定，则按 Shift_JIS 处理。

- `Shift_JIS` / `ShiftJIS` / `SJIS`：Shift JIS 编码
- `UTF-8`：UTF-8
- `default`：运行所在 OS 的默认字符编码

以下以 `charset.` 开头的设置为单独设置。必须写在通过 `charset` 进行整体设置之后。

### charset.dic

词典的字符编码。

### charset.setting

基础设置文件本身的字符编码。

### charset.output

request 函数输入和输出所用的字符编码。

### charset.log

日志文件和玉的输出所用的字符编码（Tc569-15 及之后版本）。

### charset.file

文件输入和输出所用的字符编码。

### charset.save

全局变量存档文件输入和输出所用的字符编码。

### charset.save.old

读取未指定字符编码的旧格式存档文件时所用的字符编码。

### charset.extension

外部 DLL（SAORI 等）输入和输出所用的字符编码。

### dic, filename ( , charset )

加载词典文件 `filename`。词典文件是编写了 YAYA 脚本的程序源文件，YAYA 根据其中编写的程序内容运行。可以指定并加载任意数量的词典文件。

`filename` 使用相对于 load 指定路径位置的相对路径。

标准词典文件是使用 `charset` 指定的字符编码编写的纯文本文件。此外，还可以加载按照一定规则进行扰码处理的加密文件。

在文件名后以逗号分隔添加字符编码后，指定的文件将使用该字符编码读取。

### dicif, filename ( , charset )

与 `dic` 相同，但指定的文件不存在时会忽略该文件（Tc571-2 及之后版本）。

### dicdir, dirname ( , charset )

将指定目录下的所有文件作为词典读取（Tc556-1 及之后版本）。除指定的是目录之外，其余与 `dic` 相同。

!!! warning "读取顺序"
    文件的读取顺序不固定。因此，定义 `globaldefine` 等内容时，可能会因读取顺序而发生问题。定义 `globaldefine` 时，务必将定义所在的词典安排在靠前的位置读取。

如果 `dicdir` 指定的目录中有名为 `_loading_order_override.txt` 或 `_loading_order.txt` 的文件，其行为与写入了 `includeEX,(目录)/_loading_order.txt` 相同。会按 `_loading_order_override.txt` → `_loading_order.txt` 的顺序检查文件是否存在，并且只对先找到的文件执行 `includeEX`（Tc571-2 及之后版本）。

如果没有指定 `dic`，或者 `dicif` 指定的文件全部不存在、`dicdir` 指定的目录为空等，导致没有任何要读取的词典，则会以[外壳模式](#シェルモード)运行（Tc574-7 / Tc602-12 及之后版本）。

### msglang, language

!!! note "通常无需指定"
    通常即使不特别指定，错误消息的语言也会自动切换（Tc573-5 及之后版本）。

选择日志中记录的错误消息等内容所用的语言。指定以下保留值之一。如果未指定，则按 `japanese` 处理。

- `japanese`
- `english`
- `chinese-simplified`
- `chinese-traditional`
- `german`
- `korean`

此设置是为兼容旧版本而保留的。请改用下面的 `messagetxt`。

### messagetxt, filename ( , charset )

!!! note "通常无需指定"
    通常即使不特别指定，错误消息的语言也会自动切换（Tc573-5 及以后）。

读取记录到日志中的错误消息等内容所使用的语言文件。例如，可以这样写。省略 `charset` 时，将使用 UTF-8（带 BOM）（Tc557 及以后）。

```
messagetxt,messagetxt/japanese.txt
messagetxt,messagetxt/english.txt
messagetxt,messagetxt/chinese-simplified.txt
messagetxt,messagetxt/chinese-traditional.txt
messagetxt,messagetxt/german.txt
messagetxt,messagetxt/korean.txt
```

语言文件名可在 [yaya-shiori 的 messagetxt](https://github.com/ponapalt/yaya-shiori/tree/500/messagetxt) 中查看。

Tc570-1 及以后，在 Windows 上，语言文件会嵌入 DLL 中，因此无需分发语言文件本身。保留 `messagetxt` 中填写文件名的规格，是为了兼容 Windows 以外的环境。

### basepath, directory

将读取词典等内容时作为基准的目录重新设定为任意位置。不设定时，通常使用与 `yaya.dll` 相同的目录（Tc557 及以后）。

### include, filename

从其他文件读取基础设置文件的内容。指定文件中的内容也会作为有效的基础设置处理。

### includeEX, filename

基本上与 `include` 执行相同的处理，但如果 `filename` 中指定的文件名包含目录名，则会先临时将当前目录切换到该目录，再执行 `include` 处理（Tc559 及以后）。

### log, logfilename

将运行日志记录到文件 `logfilename` 中。日志将使用 `charset.log` 中指定的字符编码写入。`logfilename` 应指定相对于 load 中指定路径位置的相对路径。

### iolog, [on|off]

设置是否将执行 load、unload、request 时的输入输出字符串及处理时间记录到日志中。指定 `on` 时会记录。默认值为 `on`，不需要时请设为 `off`。即使指定 `off`，若采用将玉拖放到程序上以启动的方式，也会强制设为 `on`。

### iolog.filter.keyword, [忽略判定字符串]

如果 request 字符串中包含指定的忽略判定字符串，则不将该 request 的 I/O 记录到日志中（也不会输出到玉）。可以指定多个。旧定义名为 `ignoreiolog`。

例：不记录 `OnSecondChange` 和 `OnMouse` 系列事件

```
ignoreiolog, ID: OnSecondChange //OnSecondChange無視
iolog.filter.keyword, OnMouse        //OnMouse系無視
```

由于基础设置文件的格式规则，忽略判定字符串前后的空格以及注释 `//` 之后的内容都会被忽略。

### iolog.filter.keyword.delete, [字符串]

删除上述设置。这是面向 [SETSETTING](../functions/SETSETTING.md) 的写法，直接写在定义文件中意义不大。

### iolog.filter.keyword.regex, [忽略判定字符串：正则表达式]

`iolog.filter.keyword` 的正则表达式版本。

### iolog.filter.keyword.regex.delete, [字符串]

删除上述设置。这是面向 [SETSETTING](../functions/SETSETTING.md) 的写法，直接写在定义文件中意义不大。

### iolog.filter.mode, [模式]

针对上述 `iolog.filter.keyword` 等设置的判定条件，切换为“不输出符合条件的内容”或“只输出符合条件的内容”。未定义时，采用“不输出符合条件的内容”模式。

```
iolog.filter.mode,allowlist
iolog.filter.mode,whitelist
```

切换为只输出符合条件内容的模式。

```
iolog.filter.mode,denylist
iolog.filter.mode,blacklist
```

切换为不输出符合条件内容的模式。

### fncdepth, [depth]

以数值指定函数调用的最大深度。默认值为 32。最小值为 2；指定小于此值或无效的值时，也会按 2 处理。设为 0 时不检查深度上限（Tc556-1 及以后）。

达到上限时会调用 [shiori.OnCallLimit](../system/shiori-OnCallLimit.md)。

除深度上限外，Tc607-4 及以后，当 YAYA 运行所在的线程剩余堆栈较少时（大约低于 128KB），也会像达到上限时一样停止调用并调用 `shiori.OnCallLimit`。被停止调用的值会变为空。即使将 `fncdepth` 设为 0 或较大的值，也不会再因耗尽堆栈而导致整个 baseware 崩溃。停止时的调用深度会随 baseware 线程的堆栈大小而变化（1MB 堆栈时为数百层）。截至 Tc607-3，将其设为 0 且调用深度过大时，整个 baseware 会崩溃。

### looplimit, [count]

以数值指定循环次数上限。默认值为 1000000（Tc574-10 / Tc606-4 及以后；此前为 10000）。设为 0 时不检查上限，但程序会持续运行，导致冻结。对 `foreach` 无效（Tc564-1 及以后）。

达到上限时会调用 [shiori.OnLoopLimit](../system/shiori-OnLoopLimit.md)。

### save.encode, [on|off]

加密存档文件。所谓“加密”并不复杂，最多只能让内容稍微难以看懂。设为 `on` 后，存档文件会一直保持加密状态，直到将其删除。更改设置时请务必谨慎。

### save.auto, [on|off]

切换自动保存存档文件功能的开启/关闭。开启时，会定期备份，并在退出时自动保存变量。关闭时，除非明确调用保存函数，否则不会保存。默认开启。

### embed.lazy, [on|off]

在运行时查找不带括号的字符串 `%` 嵌入名称（默认值：`on`）。设为 `off` 时，则在加载词典时确定（Tc604-1 以后。[详情](06-string-embedding.md#名前を読み込み時に確定する)）。

### maxlognum, [count]

设置可通过 [GETERRORLOG](../functions/GETERRORLOG.md) 获取的日志最大数量。默认值为 256 个元素。

## 外壳模式

Tc574-7 / Tc602-12 以后。如果没有设置文件，或没有任何要加载的词典，YAYA 会像只加载了以下词典一样运行。

```c
load { }
unload { }
request { EVAL(_argv[0]) }
```

直接对传入 request 的字符串执行 [EVAL](../functions/EVAL.md)，并返回其结果。除了单个表达式，也可以写用 `;` 或换行分隔的一系列语句，以及控制语句。无需准备完整人格或词典，就能快速检查 YAYA 表达式和函数的运行情况。

| request 的输入 | 返回值 |
|---------------|------|
| `1+2` | `3` |
| `_a = 3; _a * 5` | `15` |
| `'hello' + ' world'` | `hello world` |
| `X = 10` | 空字符串（全局变量 `X` 中存入 10） |
| `X` | `10` |

- 全局变量在同一会话期间会保持不变
- 没有设置文件时，不会自动保存或恢复变量（`yaya_variable.cfg`）。如果有设置文件，但未指定词典，则遵循 `save.auto` 等设置
- 进入外壳模式时，日志中会出现注记 N0002
- 如果 `dic` 指定的词典文件不存在、词典中有语法错误，或 `include` 的目标不存在等，则不会进入外壳模式
- SHIORI 请求也会直接执行 EVAL，因此此模式并非用于作为人格使用。它面向这样的用法：使用 YAYA 的可执行文件版本（`yaya.exe`），先 `load` 一个空目录，再通过 `request` 发送表达式
