# 预处理

## 概述

读取词典文件时执行的预处理器命令。

## #define

直接对词典文件的原始文本执行字符串替换：

```
#define before after
```

从声明之后开始，应用于该文件直到末尾的所有文本。替换按声明顺序执行，因此应先写需要优先转换的内容。

## #globaldefine

与 `#define` 类似，但作用范围更广：

```
#globaldefine before after
```

对之后读取的所有词典文件都有效。将其放在第一个词典文件的开头时，会影响整个项目。

**处理顺序：** 先执行 `#define` 的替换，然后执行 `#globaldefine` 的替换：

```
#globaldefine tea green
#define tea milk
"teacup"
```

结果: `"milkcup"` （`#define` 优先）

## \_\_AYA\_SYSTEM\_FILE\_\_

YAYA Tc543-1 及之后的版本可用。返回当前文件相对于 DLL 的路径：

```
"__AYA_SYSTEM_FILE__"
```

示例：输出 `"aya_aitalk.txt"`

## \_\_AYA\_SYSTEM\_LINE\_\_

Tc543-1 及之后的版本可用。使用与 `__AYA_SYSTEM_FILE__` 相同的机制，返回正在执行的文件的当前行号。

## \_\_AYA\_SYSTEM\_FUNC\_\_

Tc574-2 及之后的版本（600 系列为 Tc602-2 及之后）可用。在函数中书写时，会替换为该函数的名称：

```
OnTest
{
	LOGGING("__AYA_SYSTEM_FUNC__: called")
}
```

示例：输出 `"OnTest: called"`

- 只会替换函数的 `{` `}` 内部。不会包含附加到函数名上的防止重复选项（如 `:nonoverlap`）
- 即使包含在 `#define` 替换后的字符串中，也会被替换，因此可用于日志输出宏
- 在通过 [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) 添加的函数中也可使用

## #ifdef / #ifndef / #elifdef / #elifndef / #else / #endif

Tc574-2 及之后的版本（600 系列为 Tc602-2 及之后）可用。根据名称是否已定义，切换是否读取词典的一部分：

```
#ifdef 名前
（名前が定義されていれば読み込む）
#elifdef 別の名前
（最初の名前が未定義で、別の名前が定義されていれば読み込む）
#else
（どれにも当てはまらなければ読み込む）
#endif
```

- `#ifndef` / `#elifndef` 表示“如果未定义”
- `#elifdef` / `#elifndef` / `#else` 可以省略。`#elifdef` / `#elifndef` 可以写任意多个
- 可以嵌套
- 会忽略行首空白，因此可以缩进。也可以在函数中使用
- 行末可以写 `//` 注释
- 不能写条件表达式（没有 `#if`）

不会解析未读取区间内的行的语法。调用不存在的系统函数，或写入该 YAYA 不认识的语法，也不会报错。区间内的 `#define` / `#globaldefine` 也不会被登记。

不过，注释（`/* */`）、通过行末的 `/` 连接行、以及文档字符串会先行处理。写在文档字符串中的 `#endif` 等不会作为预处理器命令处理。

### 判定对象的名称

| 名称 | 定义条件 |
|---|---|
| `#define` 的名称 | 在该文件中、该行之前定义 |
| `#globaldefine` 的名称 | 在此之前读取的词典文件中定义（如果是同一文件，则在该行之前定义） |
| `__AYA_SYSTEM_YAYA5__` | 500 系列的 YAYA |
| `__AYA_SYSTEM_YAYA6__` | 600 系列的 YAYA |
| `__AYA_SYSTEM_SYSFUNC_関数名__` | 存在该系统函数（例如：`__AYA_SYSTEM_SYSFUNC_FREADJSON__`） |
| `__AYA_SYSTEM_FILE__` / `__AYA_SYSTEM_LINE__` / `__AYA_SYSTEM_FUNC__` | 始终定义 |

`__AYA_SYSTEM_YAYA5__` / `__AYA_SYSTEM_YAYA6__` / `__AYA_SYSTEM_SYSFUNC_関数名__` 是仅用于 `#ifdef` 系列判定的名称，不会替换词典中的字符串。

`#globaldefine` 会受到读取顺序的影响。之后读取的词典文件中的 `#globaldefine` 不可见。

### 500 系列和 600 系列共用的词典

使用 600 系列新增的语法或函数时，在 500 系列中会在读取时出错（调用未知函数会出现 E0071 等错误）。使用 `#ifdef` 区分写法后，两者都不会报错：

```
#ifdef __AYA_SYSTEM_YAYA6__
LoadConfig
{
	FREADJSON('config.json')
}
#else
LoadConfig
{
	// 500 系向けの代わりの処理
}
#endif
```

根据特定系统函数是否存在来区分写法时，请使用 `__AYA_SYSTEM_SYSFUNC_関数名__`。这样即使今后的版本中新增函数，也可以继续直接使用：

```
#ifdef __AYA_SYSTEM_SYSFUNC_DUMPJSON__
	_s = DUMPJSON(_data)
#else
	_s = ''
#endif
```

不认识 `#ifdef` 的旧版 YAYA（Tc574-1 以前、Tc602-1 以前）会将 `#ifdef` 等行报为错误 E0076，并解析区间内的所有内容。发布共用词典时，请注明所需的 YAYA 版本。

## #error / #warning

Tc574-2 及之后的版本（600 系列为 Tc602-2 及之后）可用。在读取时输出错误或警告：

```
#ifndef __AYA_SYSTEM_YAYA6__
#error この辞書は YAYA 600 系（Tc602-2 以降）が必要です
#endif
```

- `#error` 会输出错误 E0104。由于会导致词典错误，因此会以紧急模式读取
- `#warning` 会输出警告 W0028。读取会继续
- 后面写的字符串会接在消息后输出（不包括行末的 `//` 注释）
- 对于因 `#ifdef` 等而未读取的区间，不会执行任何操作

## 错误

| 编号 | 内容 |
|---|---|
| E0074 | `#ifdef` 系列缺少名称、名称多于一个，或 `#else` / `#endif` 后面存在字符串 |
| E0101 | 没有对应的 `#ifdef` / `#ifndef` 的 `#elifdef` / `#elifndef` / `#else` / `#endif` |
| E0102 | `#else` 后面出现了 `#elifdef` / `#elifndef` / `#else` |
| E0103 | `#ifdef` / `#ifndef` 未用 `#endif` 关闭（显示最内层 `#ifdef` 所在的行） |
| E0104 | `#error` |
| W0028 | `#warning` |
