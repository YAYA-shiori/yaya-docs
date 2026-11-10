# YAYA 手册

这是一本汇总了伺か（ukagaka）的 SHIORI「YAYA」用法与规格的手册。这里也收集了有关 YAYA 及其前身 AYA 的信息和 Tips。

我们力求让没有编程经验的人也能看懂。如果发现难以理解的地方或错误，请随时通过[整备班BTS](https://bts.shillest.net/)（报告表单）告诉我们。熟悉 GitHub 的用户也可以提交 [Issues](https://github.com/YAYA-shiori/yaya-docs/issues) 或 Pull Request。

> 我们为 AI 智能体准备了查找指南 [llms.txt](https://yaya-shiori.github.io/yaya-docs/llms.txt)。每个页面的 Markdown 原稿都可以通过与仓库中相同的路径加上 `.md` 获取（例如：`https://yaya-shiori.github.io/yaya-docs/startup/cheatsheet.md`）。

## 下载

- [下载（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [更新日志](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)

## YAYA v6（俗称 Tc600 系列）

- 这是在合并 [steve green](https://github.com/steve02081504) 的开发分支、调整兼容性后，作为大幅强化版发布的版本。
- 在保持与 500 系列高度兼容的同时，还对变量灵活性、高速头部解析、XML/JSON 等解析器、数据库（SQLite）等进行了大幅改进。
- 想先大致了解一下 → [YAYA 6 登场](other/yaya6-launch.md)
- 想从 YAYA Tc5xx-x 迁移到 Tc6xx-x（从 v5 系列迁移到 v6 系列）→ [600 中的变更](other/changes-600.md)（只需替换 `yaya.dll`，词典和存档文件都可以照常运行。需要注意的只有函数名冲突等少数几点）

## 初次使用

- YAYA 和 AYA 是什么？→ [关于 YAYA](other/yaya.md)
- 想大致了解 YAYA 的写法 → [速查表](startup/cheatsheet.md)
- 想第一次制作人格？→ [如何制作人格](startup/creating-ghost.md)
- 以前用 AYA 制作人格，想迁移到 YAYA → [从 AYA 迁移](startup/migration-from-aya.md)
- 想从 Satori 迁移到 YAYA → [从 Satori 迁移](startup/migration-from-satolili.md)

## 查找资料

- 没有编程经验！→ [基础](basic/)
- 想了解 YAYA 的语法 → [语法](grammar/)、[速查表](startup/cheatsheet.md)
- 有哪些内置（系统）函数？→ [按用途分类的函数列表](functions/)
- 想按名称查找函数 → [系统函数列表](system/system-functions-index.md)
- 想调查或处理错误 → [错误处理函数](system/error-handling-functions.md)

也可以通过页面顶部的搜索框进行查找。

## 系统词典与模板

- 关于系统词典 → [yaya_shiori3.dic](system/yaya-shiori3-dic.md)、[yaya_optional.dic](system/yaya-optional-dic.md)
- 关于模板人格 → [如何制作人格](startup/creating-ghost.md)、[简单的 YAYA 模板](other/simple-yaya-template.md)
- 想轻松编写对话 → [talklib](other/talklib.md)
- SHIORI 以外的用法 → [将 YAYA 用作 SAORI](other/yaya-as-saori.md)、[将 YAYA 用作 MAKOTO](other/yaya-as-makoto.md)、[将 YAYA 用作插件](other/yaya-as-plugin.md)

## 遇到问题时

- 想了解各种实用技巧 → [Tips](tips/)
- 制作过程中遇到问题 → [故障排除](other/troubleshooting.md)
- 如果仍无法解决，或者怀疑是 YAYA 的缺陷 → 请到[整备班BTS](https://bts.shillest.net/)（报告表单）提问。熟悉 GitHub 的用户也可以提交 [yaya-shiori 的 Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) 或 Pull Request
- 在[开发信息搜索](http://ukadev.shillest.net/)中搜索，也许能找到答案

## 相关工具

- [紺野ややめ (Konnoyayame)](https://github.com/YAYA-shiori/konnoyayame) — YAYA 的模板人格
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 用于检查词典错误和调试的工具
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — 使用 GitHub Actions 检查词典的 CI 工具
- [ukagaka-doc-mcp](https://github.com/finelagusaz/ukagaka-doc-mcp) - 用于在 AI 开发中自动查找伺か相关规格的工具
