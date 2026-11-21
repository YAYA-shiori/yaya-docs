# 速查表

这是将 YAYA 的写法汇总到一页的速查表。详细说明请参阅各项对应的链接。

## YAYA 的基本概念

- 词典是**函数的集合**。以 `名前 { ... }` 的形式定义函数，使用 `OnBoot` 等事件名时，该函数就是对应事件的响应。
- 函数中的**表达式和字符串逐行成为“输出候选项”**。调用函数时，会从候选项中随机选择一个并返回。赋值（`_a = 1`）等语句不会成为候选项。
- 字符串用 `"..."` 括起来。Sakura Script 也是字符串，因此必须用引号括起来。
- 变量具有类型（整数、实数、字符串、数组、哈希），无需声明。名称以 `_` 开头的是局部变量。
- 函数外不能编写语句或变量，只有 `#define` 等预处理指令可以写在外面。
- `if` `while` 的条件表达式可以用括号括起来，也可以不加括号（`if (_a == 1)` 和 `if _a == 1` 相同）。`for` `foreach` 的整个头部也可以用 `( )` 括起来（Tc603-6 及以后版本；此前会报错）。
- 符号使用半角字符（不能使用全角的 `（` 或 `＋`）。

## 函数的写法

```
OnBoot
{
  _name = "さくら"
  "\0\s[0]こんにちは、%(_name)さん。\e"
  "\0\s[0]起動しましたね。\e"
}
```

- 上例中，`"\0\s[0]こんにちは…"` 和 `"\0\s[0]起動しましたね。\e"` 中的一个会被随机返回（`_name = …` 不会成为候选项）。
- **每行一个**候选项。像 `"a" "b"` 这样在一行中并列书写会报错。`"a" / "b"` 中的 `/` 是除法运算符，不是候选项的分隔符。
- 在单独一行写 `--`，会将前后的候选项分成不同的组，从每组中各选一个并连接起来（参见[函数](../grammar/02-functions.md)）。
- `{` 可以与函数名写在同一行，也可以写在下一行。
- 注释有 `// 行末まで` 和 `/* 複数行 */` 两种。
- 在一行中编写多个语句时，用 `;` 分隔（`_a = 1 ; _b = 2`）。

### 参数和返回值

| 写法 | 含义 |
|--------|------|
| `Func(1, "a")` | 带参数调用。没有参数时只写 `Func` 即可 |
| `_argv[0]` `_argv[1]` | 接收到的参数（从 0 开始） |
| `_argc` | 参数的数量 |
| `Func(&_v)` | 按引用传递变量。在 `Func` 中执行 `_argv[0] = 99` 会改变 `_v` |
| `return` | 在此结束函数。从此前的候选项中返回一个 |
| `return 式` | **丢弃**此前的所有候选项，返回表达式的值（Tc573-1 及以后版本） |

### 候选项的选择方式

在函数名后用 `:` 指定（`Seq : sequential`）。

| 指定值 | 行为 |
|------|------|
| （无） | 从候选项中随机选择一个 |
| `nonoverlap` | 不连续选择与上次相同的候选项 |
| `sequential` | 从上到下依次返回，到末尾后重新开始 |
| `array` | 将所有候选项组成通用数组并返回 |
| `void` | 执行内部内容，但不返回任何值 |
| `all` | 将所有候选项连接成一个字符串并返回（Tc567-1 及以后版本） |
| `last` | 返回最后一个候选项（Tc567-1 及以后版本） |

除了选择方式，还可以指定以下修饰符。

| 指定值 | 行为 |
|------|------|
| `_pool` | 将内层块（包括 `if` 的内容）中的候选项展开，与外层候选项以相同概率选择 |
| `_pool_nonoverlap` `_pool_sequential` | 对展开后的全部候选项使用不重复或顺序选择方式 |
| `melt_` | 如果选中的输出是通用数组，则将其元素展开并加入外层块的候选项 |

```
OnTest : _pool
{
  "x"
  {
    "y"
    "z"
  }
}
```

- 不使用 `_pool` 时，内层的 `{ }` 整体算作一个候选项（`x` 的概率为 1/2，`y` 和 `z` 各为 1/4）。使用 `_pool` 后，`x` `y` `z` 的概率各为 1/3。
- 如果 `if` 的条件为假，其内部的候选项不会被加入。可以使用 `if 条件 { "b" "c" }` 实现“仅在条件为真时增加候选项”。
- `while` `for` `foreach` 中的候选项每次循环加入一个。
- 像 `nonoverlap : {` 这样指定了选择方式的块不会被展开，仍作为一个候选项。

详情参见[函数](../grammar/02-functions.md)。

## 值和类型

| 类型 | 写法 | 示例 |
|------|--------|----|
| 整数 | 10 进制、`0b`（2 进制）、`0x`（16 进制）。64 位 | `10` `0b1010` `0xa` |
| 实数 | 带小数点 | `3.14` |
| 字符串 | `"..."`（展开）、`'...'`（不展开） | `"a%(_x)"` `'a%(_x)'` |
| 多行字符串 | `<<"` … `">>`（展开）、`<<'` … `'>>`（不展开） | |
| 通用数组 | `(1, "a", 2.5)` | [数组](../grammar/05-arrays.md) |
| 简易数组 | 以逗号分隔的字符串 `"a,b,c"` | 同上 |
| 哈希 | `IHASH("キー", 値, …)`（Tc600-3 及以后版本） | [哈希](../grammar/12-hash.md) |
| VOID | 未定义的变量、超出范围的元素 | 用作字符串时为空，用作数值时为 0 |

- 字符串中的 `"` 需要连续写两个（`"1""2"` → `1"2`）。
- 使用 [GETTYPE](../functions/GETTYPE.md) 查询类型（VOID 为 0，整数为 1，实数为 2，字符串为 3，通用数组为 4，哈希为 5）。
- 实数转换为字符串时，小数点后保留 6 位（`3.0/4*100` → `75.000000`）。
- 整数之间的除法会截去小数部分（`4/3` → `1`）。将其中一个操作数改为实数，结果就是实数。

## 变量

| 写法 | 含义 |
|--------|------|
| `_a = 1` | 局部变量。仅在该函数及其内层块中有效。退出块后消失 |
| `a = 1` | 全局变量。可从任何函数使用。退出时自动保存，下次启动时恢复 |
| `ERASEVAR("a")` | 删除全局变量 |
| `_a++` `_a--` `_a += 2` | 加法、减法和复合赋值（还有 `-=` `*=` `/=` `%=`） |

- 未定义的变量在计算中为 0，用作字符串时为空字符串（`UNDEF + 1` 为 `1`）。
- 不能使用以数字开头的名称，也不能使用与保留字或函数名相同的名称（参见[保留字](../grammar/09-reserved-words.md)）。

## 运算符

按优先级从高到低排列（[算术运算](../grammar/04-arithmetic.md)）。

| 类型 | 运算符 |
|------|--------|
| 括号和下标 | `( )` `[ ]` |
| 否定 | `!` |
| 自增自减 | `++` `--` |
| 乘除 | `*` `/` `%` |
| 加减 | `+` `-` |
| 比较 | `==` `!=` `>=` `<=` `>` `<` `_in_` `!_in_` |
| 逻辑 | `&&` `\|\|` |
| 赋值 | `=` `+=` `-=` `*=` `/=` `%=` `,=` |
| 逗号（创建数组） | `,` |

- `0` 为假，非 0 为真。比较结果为 `1` 或 `0`。
- `"or" _in_ "World"` 在右侧字符串包含左侧字符串时结果为 `1`。
- `+` 在任一操作数为字符串时表示**连接**（`"5" + 1` 的结果为 `"51"`）。`*` 按数值计算（`"5" * 2` 的结果为 `10`）。
- `==` 区分大小写（`"abc" == "ABC"` 的结果为 `0`）。
- 没有三元运算符（`? :`）。

## 控制结构

```
if _a < 3
{
  "小"
}
elseif _a < 10
{
  "中"
}
else
{
  "大"
}
```

| 要实现的功能 | 写法 |
|--------------|--------|
| 二分支或多分支 | `if` / `elseif` / `else`（除嵌套的 `if` 外，只有一条语句时可省略 `{ }`） |
| 按值分支 | `case 式 { when 値 { … } when 値1, 値2 { … } others { … } }` |
| 按位置选择 | `switch 式 { 候補0 候補1 … }`（每行一个候选项，从 0 开始） |
| 按条件重复 | `while 条件 { … }` |
| 按次数重复 | `for _i = 0 ; _i < 10 ; _i++ { … }`（三个部分均为必填。Tc603-6 及以后版本可以用 `( )` 包围整个头部） |
| 依次遍历数组 | `foreach 配列 ; _v { … }` |
| 遍历键和值 | `foreach 配列またはハッシュ ; _k, _v { … }`（Tc600-3 及以后版本） |
| 退出循环或进入下一次循环 | `break` / `continue` |

```
case _name
{
  when "さくら" { "さくらだね" }
  when "うにゅう", "うに" { "うにゅうだね" }
  others { "だれ？" }
}
```

- `case` 的 `when` 中**只能写字面量**（不能使用变量或表达式）。范围写作 `3-5` 或 `"a"-"d"`。
- `when` 和 `others` 写在 `case 式` 后面的 `{ }` 中。如果不加 `{` 就接着写 `when`，加载时会报错（E0051）。
- 循环的重复次数有上限（默认为 1000000 次，由 `looplimit` 设置）。超过上限时会调用 `OnLoopLimit`。
- `while 1` 是无限循环，请务必编写 `break`。

## 字符串嵌入

| 写法 | 含义 |
|--------|------|
| `"%(_a)"` `"%(1+2)"` | 计算表达式并嵌入结果（带范围的展开） |
| `"%_a"` | 按名称的最长匹配进行嵌入。由于在运行时查找名称，速度较慢 |
| `'%(_a)'` | 使用单引号时不展开 |

详见[字符串嵌入](../grammar/06-string-embedding.md)。

## 数组

```
_a = (10, 20, 30)
_a[1]            // 20
_a[0,1]          // 範囲（10,20）
_a ,= 40         // 末尾に追加
_a = ("先頭", _a) // 先頭に追加
_a + "!"         // 全要素に演算（10!,20!,…）
ARRAYSIZE(_a)    // 要素数
```

- 范围外的元素为 VOID（`GETTYPE(_a[9])` 的结果为 0）。
- 简易数组保持字符串形式，通过下标读写（`_s = "a,b,c"` → `_s[1]` 的结果为 `b`）。分隔符可像 `_s[1,"|"]` 这样指定。
- 获取数组元素数量使用 [ARRAYSIZE](../functions/ARRAYSIZE.md)，搜索使用 [ASEARCH](../functions/ASEARCH.md)，排序使用 [ASORT](../functions/ASORT.md)，分割使用 [SPLIT](../functions/SPLIT.md)。

## 哈希（Tc600-3 及以后版本）

```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]        // さくら
_h["age"] += 1    // 複合代入も使える
_h["none"]        // VOID（キーが無い）
foreach _h ; _k, _v { … }
```

- 哈希必须事先用 `IHASH()` 创建。
- 元素按键排序，而非按插入顺序排列。
- 元素中也可以存放数组或哈希（[值的嵌套](../grammar/13-nesting.md)）。

## 预处理器

| 写法 | 含义 |
|--------|------|
| `#define 前 後` | 替换该文件中此行之后的字符串 |
| `#globaldefine 前 後` | 在此后加载的所有词典中进行替换 |
| `#ifdef 名前` … `#else` … `#endif` | 如果名称已定义则加载（Tc574-2 / Tc602-2 及以后版本） |
| `__AYA_SYSTEM_YAYA6__` | 600 系列中已定义（用于与 500 系列共用的词典） |
| `__AYA_SYSTEM_FILE__` `__AYA_SYSTEM_LINE__` `__AYA_SYSTEM_FUNC__` | 分别替换为文件名、行号和函数名 |

详见[预处理器](../grammar/08-preprocessor.md)。

## 配置文件（yaya.txt）

```
dic, basis.dic
charset, UTF-8
log, executelog.txt
```

| 配置项 | 含义 |
|------|------|
| `dic, ファイル` | 加载词典（`dicif` 仅在文件存在时加载，`dicdir` 加载文件夹内的所有词典） |
| `charset, UTF-8` | 字符编码（也可通过 `charset.dic` 等按用途分别指定） |
| `log, ファイル` | 输出执行日志 |
| `fncdepth, 数` | 函数调用深度的上限（默认为 32。0 表示深度不受限制，但剩余栈空间不足时会停止） |
| `looplimit, 数` | 循环次数的上限（默认为 1000000） |
| `embed.lazy, off` | 在加载时确定 `"%名前"` 的名称（默认值 on 表示在运行时查找） |

- 配置文件的名称是在 DLL 名称后加上 `.txt`（`yaya.txt`）。可以使用 `//` 和 `/* */` 编写注释。
- 如果没有配置文件，或没有任何要加载的词典，就会进入**shell 模式**。该模式会直接对发送的表达式执行 `EVAL` 并返回结果，因此可用于验证表达式的行为（[基础设置](../grammar/01-basic-settings.md#シェルモード)）。

详见[基础设置](../grammar/01-basic-settings.md)。

## 常用函数

完整列表参见[系统函数列表](../system/system-functions-index.md)。

| 用途 | 函数 |
|------|------|
| 查看或转换类型 | [GETTYPE](../functions/GETTYPE.md) [CVINT](../functions/CVINT.md) [CVSTR](../functions/CVSTR.md) [CVREAL](../functions/CVREAL.md) |
| 数组 | [ARRAYSIZE](../functions/ARRAYSIZE.md) [ASEARCH](../functions/ASEARCH.md) [ASORT](../functions/ASORT.md) [SPLIT](../functions/SPLIT.md) |
| 哈希 | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_EXIST](../functions/HASH_EXIST.md) |
| 字符串 | [STRLEN](../functions/STRLEN.md) [SUBSTR](../functions/SUBSTR.md) [STRSTR](../functions/STRSTR.md) [REPLACE](../functions/REPLACE.md) |
| 从字符串执行表达式 | [EVAL](../functions/EVAL.md) |
| 删除变量 | [ERASEVAR](../functions/ERASEVAR.md) |
| 将变量转换为字符串或从字符串还原 | [SERIALIZEVAR](../functions/SERIALIZEVAR.md) [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) |
| 随机数 | [RAND](../functions/RAND.md) |
| 在其他线程中运行耗时处理 | [THREADSTART](../functions/THREADSTART.md) [THREADSTATE](../functions/THREADSTATE.md) [THREADJOIN](../functions/THREADJOIN.md) [THREADRESULT](../functions/THREADRESULT.md) [THREADSTOP](../functions/THREADSTOP.md) [THREADCLOSE](../functions/THREADCLOSE.md) |
| 文件 | [FOPEN](../functions/FOPEN.md) [FREAD](../functions/FREAD.md) [FCLOSE](../functions/FCLOSE.md) |
| 读取 JSON | [PARSEJSON](../functions/PARSEJSON.md) [FREADJSON](../functions/FREADJSON.md) [FREADJSONL](../functions/FREADJSONL.md)（每行一个 JSON 的文件） |

## 相关内容

- [人格的制作方法](creating-ghost.md)
- [从 Satori 迁移](migration-from-satolili.md)
- [从 AYA 迁移](migration-from-aya.md)
