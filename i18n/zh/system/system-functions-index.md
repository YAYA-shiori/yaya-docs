# 系统函数一览

## 概要

YAYA 内置的系统函数一览。详细信息请参阅各函数的页面（`functions/` 目录）。

## 已更名的函数

旧版资料或脚本中出现的旧名称与当前名称的对应关系。旧名称的函数已不存在。

| 旧名 | 新名 | 更名或替换的版本 |
|------|------|------|
| TONUMBER | [CVINT](../functions/CVINT.md) | v4 |
| TONUMBER2 | [TOINT](../functions/TOINT.md) | v4 |
| TOSTRING | [CVSTR](../functions/CVSTR.md) | v4 |
| TOSTRING2 | [TOSTR](../functions/TOSTR.md) | v4 |
| ERASEVARIABLE | [ERASEVAR](../functions/ERASEVAR.md) | v4 |
| ISFUNCTION | [ISFUNC](../functions/ISFUNC.md) | v4 |
| SETSEPARATOR | [SETDELIM](../functions/SETDELIM.md) | v4 |
| BINSTRTONUM | [BINSTRTOI](../functions/BINSTRTOI.md) | v4 |
| HEXSTRTONUM | [HEXSTRTOI](../functions/HEXSTRTOI.md) | v4 |
| ISINTEGER / ISREAL | [GETTYPE](../functions/GETTYPE.md) | v4（旧版的表述为「相当」） |
| GETSTRURLENCODE | [STRENCODE](../functions/STRENCODE.md) | Tc532-1 |
| GETSTRURLDECODE | [STRDECODE](../functions/STRDECODE.md) | Tc532-1 |

## A-C

| 函数 | 说明 |
|------|------|
| [ACOS](../functions/ACOS.md) | 返回反余弦（弧度） |
| [ANY](../functions/ANY.md) | 从数组中随机选择 1 个元素 |
| [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) | 动态追加到运行时词典 |
| [ARRAYDEDUP](../functions/ARRAYDEDUP.md) | 删除数组中的重复元素 |
| [ARRAYSIZE](../functions/ARRAYSIZE.md) | 返回数组的元素个数 |
| [ASEARCH](../functions/ASEARCH.md) | 搜索数组并返回第一个匹配项的索引 |
| [ASEARCHEX](../functions/ASEARCHEX.md) | 搜索数组并返回所有匹配项的索引 |
| [ASIN](../functions/ASIN.md) | 返回反正弦（弧度） |
| [ASORT](../functions/ASORT.md) | 对数组进行排序 |
| [ATAN](../functions/ATAN.md) | 返回反正切（弧度） |
| [BINSTRTOI](../functions/BINSTRTOI.md) | 将二进制字符串转换为整数 |
| [BITWISE_AND](../functions/BITWISE_AND.md) | 按位与 |
| [BITWISE_NOT](../functions/BITWISE_NOT.md) | 按位取反 |
| [BITWISE_OR](../functions/BITWISE_OR.md) | 按位或 |
| [BITWISE_SHIFT](../functions/BITWISE_SHIFT.md) | 按位移位 |
| [BITWISE_XOR](../functions/BITWISE_XOR.md) | 按位异或 |
| [CEIL](../functions/CEIL.md) | 向上取整 |
| [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md) | 将字符编码 ID 转换为文本 |
| [CHARSETLIB](../functions/CHARSETLIB.md) | 设置外部库的字符编码 |
| [CHARSETLIBEX](../functions/CHARSETLIBEX.md) | 设置指定外部库的字符编码 |
| [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md) | 将字符编码文本转换为 ID |
| [CHR](../functions/CHR.md) | 将 UCS-2 代码转换为字符 |
| [CHRCODE](../functions/CHRCODE.md) | 返回字符的 UCS-2 代码 |
| [CLEARERRORLOG](../functions/CLEARERRORLOG.md) | 清除错误日志 |
| [COS](../functions/COS.md) | 返回余弦 |
| [COSH](../functions/COSH.md) | 返回双曲余弦 |
| [CUTSPACE](../functions/CUTSPACE.md) | 删除前后的空格和制表符 |
| [CVAUTO](../functions/CVAUTO.md) | 自动将字符串转换为适当的类型 |
| [CVAUTOEX](../functions/CVAUTOEX.md) | CVAUTO 的扩展版 |
| [CVINT](../functions/CVINT.md) | 将变量转换为整数类型 |
| [CVREAL](../functions/CVREAL.md) | 将变量转换为实数类型 |
| [CVSTR](../functions/CVSTR.md) | 将变量转换为字符串类型 |

## D-F

| 函数 | 说明 |
|------|------|
| [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) | 从 SERIALIZEVAR 的字符串中还原变量（Tc607-3 及以后） |
| [DICLOAD](../functions/DICLOAD.md) | 读取词典文件 |
| [DICUNLOAD](../functions/DICUNLOAD.md) | 卸载词典文件 |
| [DIRECTSSTP](../functions/DIRECTSSTP.md) | 通过 DirectSSTP 向人格发送请求 |
| [DUMPJSON](../functions/DUMPJSON.md) | 将值转换为 JSON 字符串（Tc602-1 及以后） |
| [DUMPTOML](../functions/DUMPTOML.md) | 将哈希转换为 TOML 字符串（Tc602-5 及以后） |
| [DUMPVAR](../functions/DUMPVAR.md) | 转储变量 |
| [DUMPXML](../functions/DUMPXML.md) | 将元素哈希转换为 XML 字符串（Tc602-1 及以后） |
| [DUMPYAML](../functions/DUMPYAML.md) | 将值转换为 YAML 字符串（Tc602-5 及以后） |
| [ERASE](../functions/ERASE.md) | 从字符串中删除子字符串 |
| [ERASEVAR](../functions/ERASEVAR.md) | 删除变量 |
| [EVAL](../functions/EVAL.md) | 将字符串作为表达式或语句序列进行求值 |
| [EXECUTE](../functions/EXECUTE.md) | 执行外部程序 |
| [EXECUTE_CAPTURE](../functions/EXECUTE_CAPTURE.md) | 执行外部程序并传入标准输入，捕获标准输出和标准错误输出（Tc608-3 及以后） |
| [EXECUTE_WAIT](../functions/EXECUTE_WAIT.md) | 执行外部程序并等待其完成 |
| [FATTRIB](../functions/FATTRIB.md) | 获取或设置文件属性 |
| [FCHARSET](../functions/FCHARSET.md) | 设置文件的字符编码 |
| [FCLOSE](../functions/FCLOSE.md) | 关闭文件 |
| [FCOPY](../functions/FCOPY.md) | 复制文件 |
| [FDEL](../functions/FDEL.md) | 删除文件 |
| [FDIGEST](../functions/FDIGEST.md) | 计算文件的哈希值 |
| [FENUM](../functions/FENUM.md) | 枚举文件和目录 |
| [FLOOR](../functions/FLOOR.md) | 向下取整 |
| [FMOVE](../functions/FMOVE.md) | 移动文件 |
| [FOPEN](../functions/FOPEN.md) | 打开文件 |
| [FREAD](../functions/FREAD.md) | 从文件中读取 |
| [FREADBIN](../functions/FREADBIN.md) | 以二进制形式读取文件 |
| [FREADENCODE](../functions/FREADENCODE.md) | 在转换编码的同时读取 |
| [FREADHTML](../functions/FREADHTML.md) | 一次性读取整个 HTML 文件并转换为哈希（Tc605-1 及以后） |
| [FREADJSON](../functions/FREADJSON.md) | 一次性读取整个 JSON 文件并转换为哈希或数组（Tc601-1 及以后） |
| [FREADTOML](../functions/FREADTOML.md) | 一次性读取整个 TOML 文件并转换为哈希（Tc602-5 及以后） |
| [FREADXML](../functions/FREADXML.md) | 一次性读取整个 XML 文件并转换为哈希（Tc601-1 及以后） |
| [FREADYAML](../functions/FREADYAML.md) | 一次性读取整个 YAML 文件并转换为哈希或数组（Tc602-5 及以后） |
| [FRENAME](../functions/FRENAME.md) | 重命名文件 |
| [FSEEK](../functions/FSEEK.md) | 移动文件指针 |
| [FSIZE](../functions/FSIZE.md) | 返回文件大小 |
| [FSTATUS](../functions/FSTATUS.md) | 返回文件 I/O 操作的状态 |
| [FTELL](../functions/FTELL.md) | 返回文件指针的位置 |
| [FUNCDECL_ERASE](../functions/FUNCDECL_ERASE.md) | 删除动态函数声明 |
| [FUNCDECL_READ](../functions/FUNCDECL_READ.md) | 读取动态函数声明 |
| [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md) | 写出动态函数声明 |
| [FUNCTIONEX](../functions/FUNCTIONEX.md) | 调用外部库函数 |
| [FWRITE](../functions/FWRITE.md) | 写入文件 |
| [FWRITE2](../functions/FWRITE2.md) | 写入文件（附带换行） |
| [FWRITEBIN](../functions/FWRITEBIN.md) | 以二进制形式写入文件 |
| [FWRITEDECODE](../functions/FWRITEDECODE.md) | 在转换解码的同时写入 |
| [FWRITEJSON](../functions/FWRITEJSON.md) | 将值转换为 JSON 并写入文件（Tc602-1 及以后） |
| [FWRITETOML](../functions/FWRITETOML.md) | 将哈希转换为 TOML 并写入文件（Tc602-5 及以后） |
| [FWRITEXML](../functions/FWRITEXML.md) | 将元素哈希转换为 XML 并写入文件（Tc602-1 及以后） |
| [FWRITEYAML](../functions/FWRITEYAML.md) | 将值转换为 YAML 并写入文件（Tc602-5 及以后） |

## G-I

| 函数 | 说明 |
|------|------|
| [GETCALLSTACK](../functions/GETCALLSTACK.md) | 获取调用栈 |
| [GETDELIM](../functions/GETDELIM.md) | 获取当前分隔符 |
| [GETENV](../functions/GETENV.md) | 获取环境变量 |
| [GETERRORLOG](../functions/GETERRORLOG.md) | 获取错误日志 |
| [GETFUNCINFO](../functions/GETFUNCINFO.md) | 获取函数信息 |
| [GETFUNCLIST](../functions/GETFUNCLIST.md) | 获取用户自定义函数列表 |
| [GETLASTERROR](../functions/GETLASTERROR.md) | 获取最后的错误代码 |
| [GETMEMINFO](../functions/GETMEMINFO.md) | 获取内存信息 |
| [GETSECCOUNT](../functions/GETSECCOUNT.md) | 获取秒数计数 |
| [GETSETTING](../functions/GETSETTING.md) | 获取设置值 |
| [GETSTRBYTES](../functions/GETSTRBYTES.md) | 返回字符串的字节数 |
| [GETSYSTEMFUNCLIST](../functions/GETSYSTEMFUNCLIST.md) | 获取系统函数列表 |
| [GETTICKCOUNT](../functions/GETTICKCOUNT.md) | 获取滴答计数 |
| [GETTIME](../functions/GETTIME.md) | 获取当前时间 |
| [GETTIMEZONE](../functions/GETTIMEZONE.md) | 获取本地时区信息 |
| [GETTYPE](../functions/GETTYPE.md) | 返回变量的类型 |
| [GETTYPEEX](../functions/GETTYPEEX.md) | 详细返回变量的类型 |
| [GETVARLIST](../functions/GETVARLIST.md) | 获取全局变量列表 |
| [HAN2ZEN](../functions/HAN2ZEN.md) | 将半角字符转换为全角字符 |
| [HASH_EXIST](../functions/HASH_EXIST.md) | 检查哈希中是否存在键（Tc600-3及以后） |
| [HASH_KEYS](../functions/HASH_KEYS.md) | 以数组形式返回哈希的键（Tc600-3及以后） |
| [HASH_SIZE](../functions/HASH_SIZE.md) | 返回哈希的元素数（Tc600-3及以后） |
| [HASH_SPLIT](../functions/HASH_SPLIT.md) | 分割字符串并创建哈希（Tc600-3及以后） |
| [HASH_VALUES](../functions/HASH_VALUES.md) | 以数组形式返回哈希的值（Tc600-3及以后） |
| [HEXSTRTOI](../functions/HEXSTRTOI.md) | 将十六进制字符串转换为整数 |
| [IARRAY](../functions/IARRAY.md) | 通用数组的初始值 |
| [IHASH](../functions/IHASH.md) | 创建哈希（Tc600-3及以后） |
| [INSERT](../functions/INSERT.md) | 在字符串中插入字符串 |
| [ISEVALUABLE](../functions/ISEVALUABLE.md) | 检查是否可以通过 EVAL 求值 |
| [ISFUNC](../functions/ISFUNC.md) | 检查函数是否存在 |
| [ISGLOBALDEFINE](../functions/ISGLOBALDEFINE.md) | 检查全局定义是否存在 |
| [ISINTSTR](../functions/ISINTSTR.md) | 检查是否为整数字符串 |
| [ISREALSTR](../functions/ISREALSTR.md) | 检查是否为实数字符串 |
| [ISVAR](../functions/ISVAR.md) | 检查变量是否存在 |

## J-P

| 函数 | 说明 |
|------|------|
| [LETTONAME](../functions/LETTONAME.md) | 动态指定变量名并赋值 |
| [LICENSE](../functions/LICENSE.md) | 显示许可证信息 |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | 获取函数的使用位置（LINT） |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | 获取全局变量的赋值位置（LINT） |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | 获取全局变量的使用位置（LINT） |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | 获取局部变量的赋值位置（LINT） |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | 获取局部变量的使用位置（LINT） |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | 获取用户自定义函数的使用位置（LINT） |
| [LINT.GetVarRefs](../functions/LINT.GetVarRefs.md) | 按出现位置获取变量、函数的出现位置及其所在代码块（LINT） |
| [LOADLIB](../functions/LOADLIB.md) | 加载外部库 |
| [LOG](../functions/LOG.md) | 返回自然对数 |
| [LOG10](../functions/LOG10.md) | 返回常用对数 |
| [LOGGING](../functions/LOGGING.md) | 输出到日志 |
| [LSO](../functions/LSO.md) | 返回最后选中的选项的索引 |
| [MKDIR](../functions/MKDIR.md) | 创建目录 |
| [OUTPUTNUM](../functions/OUTPUTNUM.md) | 设置数值的输出格式 |
| [PARSEHEADER](../functions/PARSEHEADER.md) | 将类似 HTTP、SHIORI 的标头转换为哈希或数组（Tc602-3及以后） |
| [PARSEHTML](../functions/PARSEHTML.md) | 将 HTML 字符串转换为哈希（Tc605-1及以后） |
| [PARSEJSON](../functions/PARSEJSON.md) | 将 JSON 字符串转换为哈希或数组（Tc601-1及以后） |
| [PARSETOML](../functions/PARSETOML.md) | 将 TOML 字符串转换为哈希（Tc602-5及以后） |
| [PARSEXML](../functions/PARSEXML.md) | 将 XML 字符串转换为哈希（Tc601-1及以后） |
| [PARSEYAML](../functions/PARSEYAML.md) | 将 YAML 字符串转换为哈希或数组（Tc602-5及以后） |
| [POW](../functions/POW.md) | 返回幂 |
| [PROCESSGLOBALDEFINE](../functions/PROCESSGLOBALDEFINE.md) | 处理全局定义 |

## Q-S

| 函数 | 说明 |
|------|------|
| [RAND](../functions/RAND.md) | 生成随机数 |
| [READFMO](../functions/READFMO.md) | 从 FMO 读取数据 |
| [REPLACE](../functions/REPLACE.md) | 替换字符串 |
| [REQUESTLIB](../functions/REQUESTLIB.md) | 向外部库发送请求 |
| [RESTOREVAR](../functions/RESTOREVAR.md) | 恢复变量 |
| [RE_ASEARCH](../functions/RE_ASEARCH.md) | 使用正则表达式搜索数组 |
| [RE_ASEARCHEX](../functions/RE_ASEARCHEX.md) | 使用正则表达式搜索数组（完全匹配） |
| [RE_GETLEN](../functions/RE_GETLEN.md) | 返回正则表达式匹配的长度 |
| [RE_GETPOS](../functions/RE_GETPOS.md) | 返回正则表达式匹配的位置 |
| [RE_GETSTR](../functions/RE_GETSTR.md) | 返回正则表达式匹配的字符串 |
| [RE_GREP](../functions/RE_GREP.md) | 使用正则表达式进行筛选 |
| [RE_MATCH](../functions/RE_MATCH.md) | 检查正则表达式是否匹配 |
| [RE_OPTION](../functions/RE_OPTION.md) | 设置正则表达式选项 |
| [RE_REPLACE](../functions/RE_REPLACE.md) | 使用正则表达式进行替换 |
| [RE_REPLACEEX](../functions/RE_REPLACEEX.md) | 使用正则表达式进行替换（扩展） |
| [RE_SEARCH](../functions/RE_SEARCH.md) | 使用正则表达式搜索 |
| [RE_SPLIT](../functions/RE_SPLIT.md) | 使用正则表达式分割 |
| [RMDIR](../functions/RMDIR.md) | 删除目录 |
| [ROUND](../functions/ROUND.md) | 四舍五入 |
| [SAVEVAR](../functions/SAVEVAR.md) | 保存变量 |
| [SERIALIZEVAR](../functions/SERIALIZEVAR.md) | 将变量值转换为存档文件格式的字符串（Tc607-3及以后） |
| [SETDELIM](../functions/SETDELIM.md) | 设置分隔符 |
| [SETGLOBALDEFINE](../functions/SETGLOBALDEFINE.md) | 设置全局定义 |
| [SETLASTERROR](../functions/SETLASTERROR.md) | 设置最后的错误代码 |
| [SETSETTING](../functions/SETSETTING.md) | 更改设置值 |
| [SETTAMAHWND](../functions/SETTAMAHWND.md) | 设置玉窗口句柄 |
| [SIN](../functions/SIN.md) | 返回正弦值 |
| [SINH](../functions/SINH.md) | 返回双曲正弦值 |
| [SLEEP](../functions/SLEEP.md) | 暂停处理 |
| [SPLIT](../functions/SPLIT.md) | 分割字符串并返回数组 |
| [SPLITPATH](../functions/SPLITPATH.md) | 分解路径 |
| [SQLCLOSE](../functions/SQLCLOSE.md) | 关闭 SQLite 数据库（Tc602-11及以后） |
| [SQLEXEC](../functions/SQLEXEC.md) | 执行 SQL（Tc602-11及以后） |
| [SQLOPEN](../functions/SQLOPEN.md) | 打开 SQLite 数据库（Tc602-11及以后） |
| [SQLQUERY](../functions/SQLQUERY.md) | 执行 SQL 并返回结果行（Tc602-11及以后） |
| [SQRT](../functions/SQRT.md) | 返回平方根 |
| [SRAND](../functions/SRAND.md) | 设置随机数种子 |
| [STRDECODE](../functions/STRDECODE.md) | 解码字符串 |
| [STRDIGEST](../functions/STRDIGEST.md) | 计算字符串的哈希值 |
| [STRENCODE](../functions/STRENCODE.md) | 编码字符串 |
| [STRFORM](../functions/STRFORM.md) | 生成格式化字符串 |
| [STRLEN](../functions/STRLEN.md) | 返回字符串的长度 |
| [STRSTR](../functions/STRSTR.md) | 搜索字符串 |
| [SUBSTR](../functions/SUBSTR.md) | 获取子字符串 |

## T-Z

| 函数 | 说明 |
|------|------|
| [TAN](../functions/TAN.md) | 返回正切值 |
| [TANH](../functions/TANH.md) | 返回双曲正切值 |
| [THREADCLOSE](../functions/THREADCLOSE.md) | 丢弃线程记录（Tc608-1及以后） |
| [THREADJOIN](../functions/THREADJOIN.md) | 等待线程结束（Tc608-1及以后） |
| [THREADRESULT](../functions/THREADRESULT.md) | 返回已结束线程中函数的返回值（Tc608-1及以后） |
| [THREADSTART](../functions/THREADSTART.md) | 在其他线程中执行函数（Tc608-1及以后） |
| [THREADSTATE](../functions/THREADSTATE.md) | 返回线程状态（Tc608-1及以后） |
| [THREADSTOP](../functions/THREADSTOP.md) | 请求中断线程（Tc608-1及以后） |
| [TOAUTO](../functions/TOAUTO.md) | 自动将值转换为适当的类型 |
| [TOAUTOEX](../functions/TOAUTOEX.md) | TOAUTO的扩展版 |
| [TOBINSTR](../functions/TOBINSTR.md) | 将整数转换为二进制字符串 |
| [TOHEXSTR](../functions/TOHEXSTR.md) | 将整数转换为十六进制字符串 |
| [TOINT](../functions/TOINT.md) | 将值转换为整数 |
| [TOLOWER](../functions/TOLOWER.md) | 将字符串转换为小写 |
| [TOREAL](../functions/TOREAL.md) | 将值转换为实数 |
| [TOSTR](../functions/TOSTR.md) | 将值转换为字符串 |
| [TOUPPER](../functions/TOUPPER.md) | 将字符串转换为大写 |
| [TRANSLATE](../functions/TRANSLATE.md) | 转换字符串 |
| [UNDEFFUNC](../functions/UNDEFFUNC.md) | 删除函数定义 |
| [UNDEFGLOBALDEFINE](../functions/UNDEFGLOBALDEFINE.md) | 删除全局定义 |
| [UNLOADLIB](../functions/UNLOADLIB.md) | 卸载外部库 |
| [ZEN2HAN](../functions/ZEN2HAN.md) | 将全角字符转换为半角字符 |
