# YAYA as SAORI

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) 转载

### 概要

这是由摂理氏制作、可将 yaya.dll 作为 SAORI 调用的模块。<br>
可以从 YAYA 以外的 SHIORI 使用 YAYA 的功能。

在默认状态下，只能使用 YAYA 的内置（系统）函数。<br>
通过导入附加模块，可以进一步扩展用途。了解 YAYA 语法的人可以自行创建这些附加模块。<br>

### 下载

- ~~[yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)~~
- [Releases · YAYA-shiori/yaya-as-saori · GitHub](https://github.com/YAYA-shiori/yaya-as-saori/releases)

### 附加模块

- [json解析器 with 类似对象的东西](http://c-lege.hacca.jp/ukgk/ukst.html)
  - 将 json 读取为类似 javascript 对象的形式，并可进行提取元素等操作的模块。
- [calendae](http://gallnuts.webcrow.jp/dump.shtml)
  - 用于历法相关计算的模块。
- [sub-edittext](http://gallnuts.webcrow.jp/dump.shtml)
  - 用于编辑文本文件的模块。
- [ssu.aym](http://rabbitbike.oh.land.to/nicky/log200803.html)
  - 使其执行与 ssu（随 Satori 附带的 SAORI）相同的操作。
- [Reta](http://navy.nm.land.to/post/)
  - 读取文本文件、已安装人格的外壳名称，以及文/Satori/Kawari/美坂的存档数据。

### 说明网站

- [SAORI/YAYA - Satori Wiki](http://soliton.sub.jp/satori/index.php?SAORI%2FYAYA)
  - 关于如何从 Satori 中使用的说明。
- [AYA as SAORI 面向 Satori 的简易说明](http://navy.nm.land.to/post/a_a_s.html)
  - 这是关于 AYA as SAORI 的说明，但也可用于 YAYA as SAORI（不过不包含 YAYA 新增的函数）。

### 演示人格

- [紺野さやめ](http://navy.nm.land.to/post/)
  - 面向 Satori 的演示人格。由于随附的 SAORI 版本较旧，建议替换。

### 自行制作模块

- 与普通词典相同，可以通过在 [yaya.txt](../grammar/01-basic-settings.md) 中追加内容来自由添加。<br>按照惯例，扩展名通常使用“.aym”（※意为 aya module），但使用其他扩展名也不会影响运行。
- SAORI 的参数会在模块内存储于名为 `REQ.ARGS[*]` 的数组中。<br>Argument0 对应 `REQ.ARGS[0]`，后续参数也依此类推。
- SAORI 的返回值会通过在模块内向 RES.RESULT 和名为 `RES.VALUE*` 的变量赋值来返回。<br>单个返回值 Result 会返回到 RES.RESULT，多个返回值 Value\* 则分别返回到各个 `RES.VALUE*` 中。<br>请注意，`RES.VALUE*`**不是数组**。使用系统函数 [EVAL](../functions/EVAL.md) 进行赋值可能会很方便。
- 如果因为参数无效等原因，无法正常执行 SAORI 功能，则会将数值 -1 作为函数的返回值（而不是 SAORI 返回值）返回。<br>当 YAYA as SAORI 系统部分收到 -1 作为返回值时，会将其视为无效调用并报告错误。<br>此时，建议使用 YAYA 的系统函数 [LOGGING](../functions/LOGGING.md)，将发生错误的 SAORI 函数名和错误说明记录到日志中。
- 函数名可以自由设置，但采用“模块名.函数名”这样的组成方式，至少有两个好处。
  - 其一，对于采用这种组成方式的函数名，YAYA as SAORI 提供了加载和卸载模块的机制。<br>调用包含句点、形如模块名.函数名的函数名时，YAYA as SAORI 会记住模块名部分。<br>然后，在首次调用具有相同模块名的函数时，会查找是否存在名为**模块名.Load**的函数；若存在，则执行该函数。<br>此外，卸载 yaya.dll 时，会查找是否存在名为**模块名.Unload**的函数；若存在，则执行该函数。<br>如果需要在整个模块中使用共通的全局变量，就可以利用此机制进行初始化和清理。
  - 其二，像这样在函数名前冠以模块名，可以降低函数名重复的可能性。<br>不同的人可能会创建多个模块并同时使用，当然，一个人也可能分别制作多个模块。<br>考虑到这些情况，采用这样的命名方式可以在一定程度上降低函数名重复的风险。

## 附件

- [yaya_as_saori_2014_01_04.zip](../attachment/yaya_as_saori_2014_01_04.zip)
- [yaya_as_saori_2014_11_08.zip](../attachment/yaya_as_saori_2014_11_08.zip)
- [yaya_as_saori_2014_11_08b.zip](../attachment/yaya_as_saori_2014_11_08b.zip)
- [yaya_as_saori_2015_12_30.zip](../attachment/yaya_as_saori_2015_12_30.zip)
- [yaya_as_saori_2021_06_14-2.zip](../attachment/yaya_as_saori_2021_06_14-2.zip)
- [yaya_as_saori_2021_06_14.zip](../attachment/yaya_as_saori_2021_06_14.zip)
- [yaya_as_saori_2021_06_17.zip](../attachment/yaya_as_saori_2021_06_17.zip)
- [yaya_as_saori_2021_06_24-2.zip](../attachment/yaya_as_saori_2021_06_24-2.zip)
- [yaya_as_saori_2021_06_24.zip](../attachment/yaya_as_saori_2021_06_24.zip)
- [yaya_as_saori_2021_06_25.zip](../attachment/yaya_as_saori_2021_06_25.zip)
- [yaya_as_saori_2021_06_28.zip](../attachment/yaya_as_saori_2021_06_28.zip)
- [yaya_as_saori_2021_06_30.zip](../attachment/yaya_as_saori_2021_06_30.zip)
- [yaya_as_saori_2021_07_10.zip](../attachment/yaya_as_saori_2021_07_10.zip)
- [yaya_as_saori_2021_07_11-2.zip](../attachment/yaya_as_saori_2021_07_11-2.zip)
- [yaya_as_saori_2021_07_11.zip](../attachment/yaya_as_saori_2021_07_11.zip)
- [yaya_as_saori_2021_07_16.zip](../attachment/yaya_as_saori_2021_07_16.zip)
- [yaya_as_saori_2021_08_31.zip](../attachment/yaya_as_saori_2021_08_31.zip)
- [yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)
