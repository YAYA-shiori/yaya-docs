# 关于 YAYA

## YAYA、AYA 是什么

- 读作“YAYA”。它是用于处理字符串的 DLL。
- 它是名为 SHIORI（栞，しおり）的基础组件之一，负责掌管人格（让角色出现在桌面上的软件，即运行在 [SSP](http://ssp.shillest.net/) 等 baseware 上的角色）的头脑。
- 除此之外，SHIORI 还有 [里々](https://ukatech.shillest.net/satori-docs/)、[华和梨](https://ukatech.shillest.net/kawari-docs/)、结奈等。
- 想从 Satori 转过来的话，请参阅 [从 Satori 迁移](../startup/migration-from-satolili.md)。

## 设计理念

- 它的特点是采用类似 C 语言的写法。接触过编程的人或许能很快上手。
- 为了让没有编程经验的人也能使用，本手册还准备了[基础知识](../basic/)。
- 由于 YAYA 是作为通用语言设计的，因此用途不限于 SHIORI。有关 SHIORI 以外的用法，请参阅以下页面。
  - [作为 SAORI 的 YAYA](yaya-as-saori.md)
  - [作为 MAKOTO 的 YAYA](yaya-as-makoto.md)
  - [作为插件的 YAYA](yaya-as-plugin.md)
- 也有人通过替换系统词典，将其用作 SAORI。
- 除了人格之外，也并非不能将它用作通用的字符串处理内嵌语言。有关作为通用语言 DLL 的 YAYA，请参阅[作为 WindowsDLL 的 YAYA](../grammar/10-yaya-as-windows-dll.md)。
- 发布的二进制文件是适用于 Windows 的 `yaya.dll`。源代码也可以在 Linux、FreeBSD 和 macOS 上构建，并且已确认可以运行（但只发布 Windows 版本）。如果发现有无法运行的地方，请告知我们。

## 什么是“作为通用语言设计的”

- `yaya.dll` 单独并不具备任何作为 SHIORI 使用的功能。它只是 DLL 格式符合 SHIORI 规范的通用语言 DLL。
- 因此，需要使用一系列名为“系统词典”的 YAYA 脚本文件，使其作为 SHIORI 运行。
- 本手册的[语法](../grammar/)和[系统函数](../functions/)介绍的是作为通用语言的 YAYA。作为 SHIORI 时的运行方式，则在[系统词典](../system/)页面中介绍。
- 因此，如果将本手册的语法部分作为“用作人格的 SHIORI”时的参考，可能会觉得不太对劲（“根本没有 request 函数啊！”“On〜 事件什么时候调用？”）。
- 想要深入了解“作为人格 SHIORI 的 YAYA”时，也建议一并阅读 [yaya_shiori3.dic](../system/yaya-shiori3-dic.md) 页面。

## YAYA 与 AYA 的区别

- AYA 是 umeici 制作的 SHIORI。最后一个版本是 5.8，可以从 [::: et cetera.](http://umeici.onjn.jp/) 获取。
- YAYA 以 umeici 的 AYA Ver.5 为原型，由 YAYA 开发团队（整备班）接手并进行了改造和发展。
- YAYA 有 500 系（Tc5xx-x）和 600 系（Tc6xx-x，即 YAYA 6）。600 系新增了哈希、嵌套数组、JSON・XML 等的读写以及 SQLite。500 系的词典只需替换 `yaya.dll`，基本上就能原样运行。详情请参阅 [YAYA 6 上线](yaya6-launch.md)和 [600 中的变更](changes-600.md)。

### 应该选哪个？

为方便在 AYA 和 YAYA 之间犹豫不决的人做选择，这里提供一个简单的比较。

|  | 新功能・更新 | 稳定性 |
|---|---|---|
| AYA | △ AYA 已停止更新。 | ○ AYA 5.8 发布至今已有很长时间，但依然稳定。 |
| YAYA | ○ YAYA 开发团队持续添加新功能并进行更新。 | △ 由于更新频繁，不同版本的运行方式可能有所不同。更新时请确认变更记录。 |

简单来说……

- 如果现有的人格使用 AYA 运行，且对功能没有特别的不满，继续使用 AYA 就没有问题。
- 如果要从头制作人格，或想不断尝试新功能，请使用 YAYA。想从 AYA 转过来的话，请参阅[从 AYA 迁移](../startup/migration-from-aya.md)。

本手册主要介绍 YAYA 相关信息。

## 发布与相关工具

- [下载（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [更新记录](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)
- [紺野ややめ](https://github.com/YAYA-shiori/konnoyayame) — YAYA 模板人格
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 用于检查词典错误和调试的工具
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — 使用 GitHub Actions 检查词典的 CI 工具

## 本手册的结构

| 想了解的内容 | 页面 |
|---|---|
| 想快速了解 YAYA 的写法 | [速查表](../startup/cheatsheet.md) |
| 想第一次制作人格 | [如何制作人格](../startup/creating-ghost.md)、[教程](../startup/tutorial-01-preparation.md) |
| 没有编程经验 | [基础知识](../basic/) |
| 想了解语法 | [语法](../grammar/) |
| 想查询内置函数 | [按用途分类的函数列表](../functions/)、[系统函数列表](../system/system-functions-index.md) |
| 想了解系统词典 | [yaya_shiori3.dic](../system/yaya-shiori3-dic.md)、[yaya_optional.dic](../system/yaya-optional-dic.md) |
| 想了解各种技巧 | [Tips](../tips/) |
| 遇到问题时 | [故障排除](troubleshooting.md) |
