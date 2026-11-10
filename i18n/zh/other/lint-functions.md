# LINT 系函数的规格与限制

`LINT.*` 系函数是一组用于调试的函数，可从已加载词典的解析结果（函数内的语句和表达式项）中提取函数与变量的使用位置。它们可作为在 YAYA 词典中构建类似 yayalint 的静态检查功能的基础，但存在以下规格与限制。

## 函数列表

| 函数 | 对象 | 重复项 | 作用域 `{` `}` | 区分读写 | 行 |
|------|------|------|------|------|------|
| [LINT.GetVarRefs](../functions/LINT.GetVarRefs.md) | 变量、函数、块 | 每次出现 | 有（带类型） | 有 | 有 |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | 函数（用户自定义、系统） | 去重、按名称排序 | 无 | - | 无 |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | 用户自定义函数 | 去重、按名称排序 | 无 | - | 无 |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | 全局变量（读写皆包括） | 去重、按名称排序 | 无 | 无 | 无 |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | 全局变量（仅赋值） | 去重、按名称排序 | 无 | - | 无 |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | 局部变量（读写皆包括） | 每次出现 | 有 | 无 | 无 |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | 局部变量（仅赋值） | 每次出现 | 有 | - | 无 |

新建检查功能时，使用 `LINT.GetVarRefs` 即可获得包含其他函数全部信息的结果。

## Tc574-1 中的变更

- 添加了 `LINT.GetVarRefs`。
- `GetGlobalVarLetted` / `GetLocalVarLetted`
  - 现在会将对数组元素的赋值（`_a[0] = 1`、`G_a[0] = 1`）列为对该变量的赋值。
  - 现在会将 `foreach _list ; _v` 中的循环变量 `_v` 列为赋值。
- `GetLocalVarUsedBy`
  - 同一条语句内，赋值目标变量现在会排在最后。由于赋值是在右值求值后进行的，`_z = _z + 1` 会按 `_z`（读取）→ `_z`（赋值）的顺序排列。
- `GetLocalVarUsedBy` / `GetLocalVarLetted`
  - 现在不会列出 `case` 语法内部生成的局部变量（名称以 `_CaSe_ExPr_PrEfIx_` 开头）。

## 限制

### 以词典已加载为前提

分析对象是已成功加载的词典。如果词典因语法错误等原因无法加载，就会进入紧急模式，此时使用 LINT 系函数的词典本身也无法运行。重复定义、语法错误、带括号的未定义函数调用（E0071）等问题，会由 YAYA 本体在加载时作为错误输出。

### 位置信息

- 可通过 `LINT.GetVarRefs` 获取行号。行号以语句为单位。
- 通过 `/` 续行或使用 here document 跨越多行的语句，行号为其**最后一行**的行号。
- 无法获取列号。YAYA 内部也不会保存列号。这是因为加载时会进行行合并、`#define` 替换、注释删除，以及按 `{` `}` `;` 分割。

### 名称的显示方式

- `#define` / `#globaldefine` 会在加载时作为字符串替换，因此显示的是替换后的名称。
- 无法追踪 `EVAL('名称')` 或 `LETTONAME('名称', …)` 这类以字符串指定的名称。
- 执行 LINT 的词典自身的函数和变量也会包含在列表中。请通过前缀等方式将其排除。
- 内嵌表达式 `%(表达式)` 的展开过程中，内部使用的 `TOSTR` 也会作为函数调用包含在结果中（`LINT.GetFuncUsedBy` / `LINT.GetVarRefs`）。无法将其与用户编写的 `TOSTR` 区分开来。

### 区分读取与写入

- 在 `LINT.GetVarRefs` 中，`=` 的赋值目标标记为 `w`，复合赋值（`+=` 等，包括 `++` `--`）的赋值目标标记为 `rw`。
- 对数组元素进行 `=` 赋值（`_a[0] = 1`）时，按 `w` 处理。数组的其他元素会保留，但也允许对未定义变量的元素进行赋值。
- 排序（将赋值目标排在最后）以语句为单位。如果一个表达式包含多个赋值，其顺序可能与实际执行顺序不一致。
- 除 `LINT.GetVarRefs` 外，其他函数都没有读写标记。
  - `GetGlobalVarUsedBy` / `GetGlobalVarLetted` 会去重，因此无法判断“有赋值但从未读取过的全局变量”。
  - 无法逐项将 `GetLocalVarUsedBy` 的结果与 `GetLocalVarLetted` 对照，以判断每项是读取还是赋值。

### 语法信息

- 可通过 `LINT.GetVarRefs` 获取块的类型，以及出现的语法类型（条件表达式、for 的各个部分、case 表达式等）。
- 不会列出不包含变量或函数的语句（`break` / `continue` / 不带表达式的 `return` / `--`、仅输出字面量等）。
- `others` 在内部会转换为 `else`，因此会将“位于 case 块正下方的 else”判定为 `others`。
- `when` 在内部会转换为 `if` / `elseif`，因此会根据是否包含 case 的内部变量来判定。

### 分析范围

- 分支和循环的流程需要在词典侧根据块的类型和深度构建。
- 跨函数分析（参数 `_argv` 的使用方式、全局变量的赋值来源等），需要在词典侧对照各函数的结果。

## 检查构建示例

| 检查 | 可行性 | 方法 |
|------|------|------|
| 未使用的函数 | 可 | 收集 `GETFUNCLIST` 中所有函数对应的 `LINT.GetVarRefs` 的 `func,user`，然后列出从未出现过的函数（排除事件函数等会从外部调用的函数） |
| 未使用的局部变量 | 可 | 按 `{` `}` 作用域查找只有 `w`、没有 `r` / `rw` 的变量 |
| 读取未定义的局部变量 | 可（分支需在词典侧考虑） | 从前向后追踪，查找在该作用域或外层作用域中出现 `w` / `rw` 之前的 `r` / `rw` |
| 未使用的全局变量 | 可 | 收集所有函数中的 `var,global`，然后查找只有 `w` 的变量（无法追踪通过 `EVAL` 等方式读取的变量） |
| 条件表达式中的赋值 | 可 | 查找 `context` 为 `if` / `elseif` / `while` / `switch` / `for-cond`，且 `access` 为 `w` / `rw` 的项目 |
| case 中无效的子句 | 部分可 | 检查 `case` 块正下方（深度+1）是否存在 `when` / `others` 以外的块，或 `context` 不为 `when` 的项目。无法检测不包含变量或函数的记述 |
| 可能拼错的名称 | 可 | 在词典侧计算与 `GETFUNCLIST` / `GETVARLIST` 的编辑距离 |
| 显示行号和列号 | 仅可显示行号 | 无法获取列号 |
