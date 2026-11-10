# YAYA 6 登场

<div class="y6-hero" markdown>

![YAYA 6——迄今为止最聪明的 YAYA。](../assets/yaya6/hero.svg)

</div>

<div class="y6-lead" markdown>

**YAYA 6（Tc600 系列）现已正式发布。**

使用哈希和嵌套结构自由组合值，直接读写 JSON、XML、YAML、TOML；用 SQLite 储存回忆；即使通过循环不断扩展数组，速度也不会变慢。迄今为止最聪明的 YAYA，来到了你的人格身边。

当然，**使用 500 系列编写的词典基本上可以原样运行。**

</div>

<div class="y6-cta" markdown>

[下载（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases) [从 500 系列迁移的指南](changes-600.md)

</div>

!!! note "注意"
    本页面是以庆祝气氛为主的介绍页面，为了营造氛围，省略了不少细节。准确的规格请参阅[600 中的变更](changes-600.md)和各参考文档。

<div class="y6-stats" markdown>

- **6** 种值类型（新增哈希）
- 可读写 **4** 种结构化数据格式
- **1** 个内置数据库（SQLite）
- **1/5000** 扩展数组时的复制次数（理论值）

</div>

## 亮点

### 🗝️ 将哈希，握在手中

YAYA 6 终于获得了原生的**哈希（关联数组）**。通过名称获取值，仅此而已，就能让人格的记忆变得如此清晰。

```
OnMouseDoubleClick
{
    if GETTYPE(nadenade) != 5 {
        nadenade = IHASH()          // ハッシュは IHASH で作る（GETTYPE は 5）
    }
    nadenade[reference[4]] += 1     // 当たり判定の名前ごとに数える

    _n = nadenade[reference[4]]
    "\0\s[0]%(reference[4])を触られたの、これで%(_n)回目だよ。\e"
}
```

`nadenade` 会以哈希的形式保存到存档文件中，因此下次启动时也会记得。只要写成 `foreach _h ; _k, _v { ... }`，就可以同时获取键和值并进行遍历。

→ [哈希](../grammar/12-hash.md)

### 🧩 自由组合值的结构

500 系列的数组元素只能是数值或字符串。在 YAYA 6 中，数组中可以包含数组，哈希中可以包含数组，数组中也可以包含哈希——无论怎样组合，都可以进行**嵌套**。而且只要连接 `[ ]`，就可以直接读写任意深处的值（**多维赋值**）。

```
_ghost = IHASH()
_ghost["sakura"] = IHASH("name", "さくら")
_ghost["sakura"]["surface"] = (0, 5, 7)
_ghost["kero"] = IHASH("name", "うにゅう")
_ghost["kero"]["surface"] = (10, 11)

_ghost["sakura"]["surface"] ,= 8       // 奥の配列に追加
_ghost["kero"]["name"] = "けろちゃん"    // 奥の値を直接書き換え
_ghost["sakura"]["surface"][0]         // 0

foreach _ghost ; _id, _g {
    // _g["name"] で名前、_g["surface"] で表情の一覧
}
```

- 不仅 `=`，`+=` 和 `,=` 也可以直接用于深层的值
- 可以保持嵌套结构**保存到存档文件**，也可以按原有结构写出为 JSON 等格式
- 使用 `DUMPVAR` 即可一目了然地查看内容

中间层的哈希不会自动创建，因此通常要像上面的例子一样，先用 `IHASH()` 创建。

→ [值的嵌套与多维赋值](../grammar/13-nesting.md)

### 🌐 多格式解析

![在 JSON、XML、YAML、TOML、SQLite、HTML 与 YAYA 6 的哈希之间转换的示意图](../assets/yaya6/formats.svg)

JSON、XML、YAML 和 TOML，读取后都会变成嵌套的哈希和数组。修改后也可以直接写回。无论是设置文件，还是其他工具或 SAORI 输出的数据，都不再需要用 `STRSTR` 和 `SUBSTR` 将内容切碎。

```
_conf = FREADJSON("config.json")
_name = _conf["user"]["name"]
_conf["boot"] += 1
FWRITEJSON("config.json", _conf, "UTF-8", 1)   // 整形して書き戻す
```

也可以读取 HTML（仅支持读取）。即使是缺少结束标签的损坏 HTML，也会按照与浏览器相同的规则补全并转换为标签树，因此可以轻松提取网页中需要的部分。

```
_h = PARSEHTML(_raw)
_body = _h["children"][1]                // <body>
foreach _body["children"]; _e {
    // _e["name"]（タグ名）、_e["attr"]（属性）、_e["text"]（テキスト）
}
```

此外，`PARSEHEADER` 可以瞬间将 SHIORI、SSTP、HTTP 等「`键: 值`」格式的字符串拆解为哈希。

```
_r = PARSEHEADER(_raw)
_r["start"]               // 1 行目（"HTTP/1.1 200 OK" など）
_r["header"]["Charset"]   // ヘッダの値
_r["body"]                // 空行より後ろ
```

### 🧠 让人格拥有长期记忆

内置了 SQLite。打开数据库后，就可以用 SQL 随意储存和回忆数据。即使是数万条对话记录，也不必再担心。

```
OnLoad
{
    SQLOPEN("memory.db")
    SQLEXEC("memory.db", "CREATE TABLE IF NOT EXISTS said(word TEXT)")
}

Remember
{
    SQLEXEC("memory.db", "INSERT INTO said VALUES(?)", _argv[0])
}

OnKuchiguse
{
    _sql = "SELECT word, count(*) AS n FROM said GROUP BY word ORDER BY n DESC LIMIT 1"
    _top = SQLQUERY("memory.db", _sql)
    "\0\s[0]あなたの口ぐせは「%(_top[0]['word'])」だね。\e"
}
```

查询结果中的每一行都会直接以「列名 → 值」的哈希形式返回。

→ [SQLOPEN](../functions/SQLOPEN.md)・[SQLEXEC](../functions/SQLEXEC.md)・[SQLQUERY](../functions/SQLQUERY.md)

### ⚡ 扩展数组也不会变慢

![将数组扩展到 1 万个元素的循环中，元素复制次数的理论值。YAYA 5 约为 5000 万次，YAYA 6 约为 1 万次](../assets/yaya6/bench.svg)

在 500 系列中，每次执行 `_a ,= x` 或 `_a[i] = x` 时，都会复制整个数组。元素越多，每次操作所需的时间也越长，因此在循环中扩展数组时，速度会随着元素数量的平方而下降。YAYA 6 不再进行这种复制。创建大型数组的词典，应该能明显感受到这一变化。

## 基准测试

这是与 YAYA 5 的比较（自行调查）。

| 项目 | YAYA 5（Tc574） | YAYA 6（Tc603） |
|---|---|---|
| 值类型的种类 | 5 | **6** |
| `GETTYPE` 返回的最大值 | 4 | **5** |
| 可用作数组元素的内容 | 仅标量 | **数组和哈希也可以** |
| `a[x][y] = v` | 读取错误 | **可用** |
| foreach 可接收的变量 | 1 | **2**（键和值） |
| 可读写的结构化数据格式 | 0 | **4**（JSON / XML / YAML / TOML） |
| 内置数据库 | 无 | **SQLite** |
| 扩展 1 万个元素的数组时的复制次数（理论值） | 约 5,000 万次 | **约 1 万次** |
| 500 系列的存档文件 | ― | **可以直接读取** |

## 演进历程

![从 Tc600-3 到 Tc603-1 的主要新增功能年表](../assets/yaya6/timeline.svg)

YAYA 600 系列从 Tc600-3 的哈希和嵌套结构起步，随着不断发布新版本，功能也逐渐增强。到了 Tc603-1，它成为了首个正式版。

## 安全性与兼容性

即使功能增强，也不会让你的词典无法继续使用。

- **500 系列的词典几乎可以原样运行。** 除极少数情况外，500 系列中原有功能的行为都不会改变（变更内容请参阅下方的“已知限制事项”）。多维赋值 `a[x][y] = v` 在 500 系列中会导致读取错误，因此也不会改变现有词典的含义
- **500 系列的存档文件可以直接读取。** 不包含哈希或嵌套结构的变量，其写出的内容也与 500 系列相同
- **即使与新函数重名也没有问题。** 与 `IHASH` 等名称相同的用户函数会自动重命名为 `Conflict.名称`
- **也可以编写同时兼容两个系列的词典。** 使用 `#ifdef __AYA_SYSTEM_YAYA6__` 区分面向 600 系列的部分后，在 500 系列中也不会报错（[预处理](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)）

### 已知限制事项

- **请注意降级。** 使用 600 系列保存的存档文件若由 500 系列读取，其中包含哈希或嵌套结构的变量会损坏。若在损坏的状态下重新保存，将无法恢复
- 不能使用与新系统函数同名的全局变量
- 读取不存在的元素、比较 VOID 与 VOID 等方面，有一些细节行为发生了变化。虽然这不会影响大多数词典，但完整列表请参阅[600 系列中的变更](changes-600.md#既存の辞書に影響しうる変更)

## 模型卡片

<div class="y6-card" markdown>

| 项目 | 内容 |
|---|---|
| 名称 | YAYA 6（Tc600 系列） |
| 类型 | SHIORI（也可作为 [SAORI](yaya-as-saori.md)、[MAKOTO](yaya-as-makoto.md) 和[插件](yaya-as-plugin.md)运行） |
| 开发 | YAYA 整备班、[steve green 先生](https://github.com/steve02081504) |
| 架构 | 用 C++ 编写的字符串处理 DLL |
| 语法 | 类似 C 语言 |
| 训练数据 | 无。**你编写的词典就是全部** |
| 参数数量 | 与 `_argv` 中的参数数量相同 |
| 上下文长度 | 只受可用内存限制 |
| 幻觉 | 不会说出词典中没有写的内容 |
| 许可证 | BSD 3-Clause |
| 费用 | 免费（输入和输出均免费） |

</div>

## 致谢

YAYA 6 基于 [steve green 先生](https://github.com/steve02081504) 的开发分支，并在调整与 500 系列的兼容性后诞生。在此感谢多年来一直使用 YAYA 编写词典的所有人格作者。

## 开始使用

### 如果你准备制作人格：紺野ややめ + 伺か Vibe Coding 工具箱

模板人格 **[紺野ややめ](https://github.com/YAYA-shiori/konnoyayame)** 已预装 600 系列的 YAYA。修改后，它就可以成为你自己的个性化人格。

此外，它还附带了用于与 AI 编码代理（Claude Code、Codex、GitHub Copilot 等）协作开发的 **Vibe Coding 工具箱**（开发套件）。从检查词典到在 SSP 中确认运行情况，代理都可以提供帮助。YAYA 6 的新功能也可以通过向代理提出要求，迅速加入词典。

1. 从 [Releases](https://github.com/YAYA-shiori/konnoyayame/releases) 下载 `konnoyayame.nar`，并安装到 SSP
2. 如果要手动修改，请编辑 `ghost/master/dic/normal/` 中的词典（词典结构见 [GHOST.md](https://github.com/YAYA-shiori/konnoyayame/blob/master/GHOST.md)）
3. 如果要与 AI 一起修改，请在人格文件夹中启动代理，并让它“进行设置”（准备事项见 [DEVKIT-GUIDE.md](https://github.com/YAYA-shiori/konnoyayame/blob/master/DEVKIT-GUIDE.md)）

该工具箱是在 Windows 和 Claude Code 的组合环境下制作并验证运行的。

### 如果要将手头的人格升级到 YAYA 6

1. 从 [GitHub Releases](https://github.com/YAYA-shiori/yaya-shiori/releases) 下载最新版
2. 替换人格中的 `yaya.dll`（以防万一，请先备份人格）
3. 大致浏览一下[600 系列中的变更](changes-600.md)
4. 试着在词典中写入 `IHASH()`

即使不是基于紺野ややめ制作的人格，也可以只安装 Vibe Coding 工具箱（[向其他 YAYA 人格安装开发套件](https://github.com/YAYA-shiori/konnoyayame/blob/master/DEVKIT-GUIDE.md#別の-yaya-ゴーストに開発キットを入れる)）。

## 发现问题时

如果发现行为与 500 系列不同，或程序没有按编写内容运行，请通过[整备班 BTS](https://bts.shillest.net/)（报告表单）告知我们。熟悉 GitHub 的用户也可以通过 [yaya-shiori 的 Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) 或 Pull Request 提交反馈。

## 相关

- [600 中的变更](changes-600.md)
- [哈希](../grammar/12-hash.md)
- [值的嵌套与多维赋值](../grammar/13-nesting.md)
- [预处理](../grammar/08-preprocessor.md)
- [关于 YAYA](yaya.md)

<div class="y6-byline" markdown>

---

YAYA 6 的兼容性保障、调试、文稿与图示：**[Claudia](https://ponadocs.shillest.net/claudia/)**

</div>
