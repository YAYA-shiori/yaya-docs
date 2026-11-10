# 600 中的变更点（Tc600-3 及以后）

汇总 Tc600-3 及以后的 YAYA（600 系列）相较于 500 系列（截至 Tc574-1）的规格变更。

!!! note "TL;DR"
    **只需替换 `yaya.dll`，500 系列的词典和存档文件就能照常运行。** 无需重写。开发团队这边也几乎都是不做任何考虑，直接替换。

    只有以下情况需要留意。

    - 词典中存在与 `IHASH` `HASH_KEYS` 等新增系统函数同名的函数或变量 → 函数会被重命名为 `Conflict.名前`，变量则无法使用（[详情](#新しいシステム関数と同じ名前)）
    - 依赖数组元素之间对 VOID 的比较，或依赖类型混杂数组的 `ARRAYDEDUP` → 结果会发生变化（[详情](#既存の辞書に影響しうる変更)）
    - 将在 600 系列中运行过的存档文件恢复到 500 系列 → 包含哈希或嵌套结构的变量会损坏（[详情](#セーブファイルの互換性)）

    新功能（哈希、嵌套数组、JSON / XML / SQLite 等）可在需要时使用。与 500 系列共用的词典可以使用 `#ifdef` 区分编写（[详情](#500-系と共用する辞書)）。

## 概要

| 项目 | 500 系 | 600 系 |
|---|---|---|
| 值类型 | VOID / 整数 / 实数 / 字符串 / 通用数组 | ＋ **哈希**（关联数组） |
| `GETTYPE` / `GETTYPEEX` | 0〜4 | 哈希为 **5** |
| 数组元素 | 仅标量 | 数组和哈希也可以作为元素（**嵌套**） |
| 元素赋值 | 仅 `a[x] = v` | 也可使用 `a[x][y]... = v`（**多维赋值**） |
| foreach | `foreach 表达式 ; 变量` | ＋ `foreach 表达式 ; 键变量, 值变量` |
| 存档文件 | 数组 `a:b:c` | ＋ 哈希 `"k"=v:...`、嵌套 `IARRAY{...}` / `IHASH{...}` |
| 新增系统函数 | ― | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_VALUES](../functions/HASH_VALUES.md) [HASH_SPLIT](../functions/HASH_SPLIT.md) [HASH_EXIST](../functions/HASH_EXIST.md) [HASH_SIZE](../functions/HASH_SIZE.md)、从 Tc601-1 起提供 [FREADJSON](../functions/FREADJSON.md) [FREADXML](../functions/FREADXML.md) [PARSEJSON](../functions/PARSEJSON.md) [PARSEXML](../functions/PARSEXML.md)、从 Tc602-1 起提供 [FWRITEJSON](../functions/FWRITEJSON.md) [FWRITEXML](../functions/FWRITEXML.md) [DUMPJSON](../functions/DUMPJSON.md) [DUMPXML](../functions/DUMPXML.md)、从 Tc602-3 起提供 [PARSEHEADER](../functions/PARSEHEADER.md)、从 Tc602-5 起提供 [FREADYAML](../functions/FREADYAML.md) [FREADTOML](../functions/FREADTOML.md) [PARSEYAML](../functions/PARSEYAML.md) [PARSETOML](../functions/PARSETOML.md) [FWRITEYAML](../functions/FWRITEYAML.md) [FWRITETOML](../functions/FWRITETOML.md) [DUMPYAML](../functions/DUMPYAML.md) [DUMPTOML](../functions/DUMPTOML.md)、从 Tc602-11 起提供 [SQLOPEN](../functions/SQLOPEN.md) [SQLCLOSE](../functions/SQLCLOSE.md) [SQLEXEC](../functions/SQLEXEC.md) [SQLQUERY](../functions/SQLQUERY.md)、从 Tc605-1 起提供 [FREADHTML](../functions/FREADHTML.md) [PARSEHTML](../functions/PARSEHTML.md) |
| 新增警告 | ― | W0024（对哈希使用了 `-` `*` `/` `%`）、从 Tc601-1 起提供 W0025（无法打开文件）・W0026（无法解析 JSON/XML/YAML/TOML）、从 Tc602-1 起提供 W0027（无法转换为 JSON/XML/YAML/TOML）、从 Tc602-11 起提供 W0029（SQLite 处理失败）、从 Tc602-13 起提供 W0030（传入的值多于 SQL 参数数量）、从 Tc604-1 起提供 W0031（在 `embed.lazy, off` 下无法确定 `%` 后的名称） |
| 正则表达式 | DEELX | 从 Tc606-6 起提供 uka_regexp（接近 PCRE2 的语法）。可以通过变量和函数解析模式中的子例程调用（[正则表达式](../grammar/14-regular-expressions.md)） |

语法请参阅 [哈希](../grammar/12-hash.md) 和 [值的嵌套与多维赋值](../grammar/13-nesting.md)。

500 系列中，`a[x][y] = v` 会在加载时导致错误 E0029，因此不存在包含此语法的现有词典。

## 可能影响现有词典的变更

### 数组元素之间的 VOID 比较

比较数组元素时，如果**两者都是 VOID**，现在会将它们视为相等。这与标量之间的 VOID 比较保持一致。

- `(1, 未定义的变量) == (1, 未定义的变量)` 的结果从 0 变为 1
- `ASEARCH(未定义的变量, 数组)` 现在会返回数组中 VOID 元素的位置（500 系列中为 -1）
- `HASH_EXIST`、`ARRAYDEDUP` 以及哈希之间的 `==` 也有相同变化

此变更仅适用于键和值都为 VOID 的情况，整数、实数和字符串的比较不变。

### 向 ARRAYDEDUP 传入混合类型的数组时

在 500 系列中，传入混有整数、实数和字符串的数组时，结果会因排列顺序而异。在 600 系列中，会按照与哈希键相同的规则去除重复项，并按数值 < 字符串的顺序排列。

```
ARRAYDEDUP((10, "9", 9, "a", 1.0, 1, "1"))
// 500 系: 1,1.000000,9,10,9,a
// 600 系: 1.000000,9,10,a
```

`1.0`、`1`、`"1"` 会被视为相同的值，并保留最先出现的值（`1.0`）。仅包含整数、仅包含实数或仅包含字符串的数组，其结果与 500 系列相同。

### 传递给 setter・watcher 的数组

传递给 [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md)（setter）和 [FUNCDECL_READ](../functions/FUNCDECL_READ.md)（watcher）的值为通用数组时，在 500 系中值会损坏（setter 的 `_argv[1]`、`_argv[2]` 变为空，watcher 的 `_argv[1]` 只剩首个元素，直接返回 setter 的返回值时变量会变为空）。

在 600 系中，数组会作为 `_argv` 的元素保持嵌套状态传递。`_argv` 的元素数仍保持不变，setter 为 3，watcher 为 2。

在 500 系中，即使给数组变量设置 setter 或 watcher，也无法正常工作，因此应该不会有实际影响。另外，对下标赋值（`a[0] = v`）时不会调用 setter，这一点与 500 系相同。

### 与新系统函数同名的名称

- 与 `IHASH`、`HASH_KEYS` 等同名的用户自定义函数会被重命名为 `Conflict.名称`，调用会指向系统函数（机制与添加 TOAUTOEX 时相同）
- 不能使用同名的全局变量。从存档文件恢复时会发出警告 W0002

### 对不存在的元素进行复合赋值（Tc602-10 以后）

复合赋值（`+=`、`-=`、`*=`、`/=`、`%=` 及带冒号的变体）的左值为超出通用数组范围的元素或哈希中不存在的键时，现在会像未定义变量一样，按 VOID 进行计算。500 系或 Tc602-9 以前会按空字符串进行计算，因此 `+= 数值` 会变成字符串连接。

```
_c = IHASH()
_c["a"] += 1
_c["a"] += 1     // 500 系・Tc602-9 まで: "11"（文字列）　Tc602-10 以降: 2（整数）

_a = IARRAY
_a[2] += 1       // 500 系・Tc602-9 まで: "1"（文字列）　Tc602-10 以降: 1（整数）
```

- 只有右值为数值的 `+=` 会发生变化。`-=`、`*=`、`/=`、`%=` 会将空字符串也视为数值，因此结果相同。`+= "文字列"` 也相同
- 元素存在且值为空字符串时（`_a[0] = ""` 之后的 `_a[0] += 1`），结果仍与以往一样为 `"1"`
- 简易数组（字符串）中超出范围的元素，原本就按 VOID 进行计算
- 在 Tc602-10 中，读取（`h["none"]` 或超出范围的 `a[9]`）仍会返回空字符串。从 Tc603-1 开始，读取也会返回 VOID（如下）
- 多维赋值时，只有最后一层是处理对象。中间层不存在时（对空的 `_h` 执行 `_h["a"]["b"] += 1`），按照[中间值的行为](../grammar/13-nesting.md#途中の値ごとの動作)改写。`_h["a"]` 在 Tc602-13 以前是字符串 `"1"`，从 Tc603-1 开始则是数组 `(1)`
- `,=` 不变

### 读取不存在的元素（Tc603-1 及以后）

读取通用数组中超出范围的元素、哈希中不存在的键，或对 VOID 使用 `[ ]` 时，现在会像读取未定义变量一样返回 VOID。此前会返回空字符串（简易数组和数值的范围外读取原本就会返回 VOID）。500 系也从 Tc574-8 起采用相同规则（哈希除外）。详情请参阅[范围外的元素](../grammar/05-arrays.md#範囲外の要素)。

```
_h = IHASH()
_h["none"] == 0      // Tc602-13 まで: 0　Tc603-1 以降: 1
_h["none"] + 1       // Tc602-13 まで: "1"（文字列）　Tc603-1 以降: 1（整数）
GETTYPE(_h["none"])  // Tc602-13 まで: 3　Tc603-1 以降: 0
```

`== ""`、if 判断以及与字符串连接的结果都没有变化。

### 向数组中的数组或哈希赋值（Tc603-1 及以后）

使用非范围指定的赋值（`_v[0] = x`、`_v[0] ,= x`、`_v[0] += x` 等）时，如果赋值目标元素是数组或哈希，现在会将右值原样整体替换，而不再展开。此前，如果根元素是数组，右值中的数组会被展开，导致嵌套结构被破坏（即使是 `_v[0] = _v[0]` 也会被破坏）。赋值目标元素为标量时的插入和删除（`_a[1] = (8, 9)`、`_a[1] = IARRAY`）则没有变化。详情请参阅[整体改写内层数组或哈希](../grammar/13-nesting.md#内側の配列やハッシュを丸ごと書き換える)。

```
_v = PARSEJSON('[[1,2],[3,4]]')
_v[0] ,= 5     // Tc602-13 まで: 1,2,5,(3,4)　Tc603-1 以降: (1,2,5),(3,4)
```

## 存档文件的兼容性

- 不包含哈希或嵌套的变量，写出的内容和读取结果都与 500 系相同。可以直接读取 500 系的存档文件
- 包含哈希或嵌套的变量将以新格式保存（参见 [SAVEVAR](../functions/SAVEVAR.md)）
- **注意降级**：在 600 系中保存的文件由 500 系读取时，只有包含哈希或嵌套的变量会损坏（不会崩溃，也不会影响其他变量）。如果在损坏的状态下重新保存，原始内容将丢失

## 与 500 系共用的词典

在 Tc574-2 及之后的 500 系版本，以及 Tc602-2 及之后的 600 系版本中，可以使用 `#ifdef __AYA_SYSTEM_YAYA6__` 或 `#ifdef __AYA_SYSTEM_SYSFUNC_関数名__` 区分面向 600 系的部分。未读取的区段不会进行语法解析，因此即使写入 600 系新增的语法或函数，在 500 系中也不会报错。详情请参阅[预处理](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)。

## 性能

`_a ,= x` 和 `_a[i] = x` 在 500 系中每次都会完整复制数组（在循环中扩展数组时，速度会随着元素数量的平方成比例地变慢）。600 系不会进行这种复制，因此在循环中扩展数组的处理速度大幅提升。

## 相关

- [哈希](../grammar/12-hash.md)
- [值的嵌套与多维赋值](../grammar/13-nesting.md)
- [流程控制（foreach）](../grammar/07-flow-control.md#foreach-ループ)
- [SAVEVAR](../functions/SAVEVAR.md)
- [预处理](../grammar/08-preprocessor.md)
