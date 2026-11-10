# 教程 1：准备

## 下载所需内容

- **[SSP](http://ssp.shillest.net/)（最新版本）**：目前主流的 baseware。功能丰富、运行轻快，并且仍在持续更新；如果没有特别偏好的话，建议使用它。本教程也以使用该 baseware 为前提进行说明。
- **yaya.dll（最新版本）**：YAYA 的 SHIORI 本体。可从 [yaya-shiori 的发布页面](https://github.com/YAYA-shiori/yaya-shiori/releases)获取。
- **[模板人格](creating-ghost.md)**：有多种类型，这里将使用 [SimpleYAYA 模板](../other/simple-yaya-template.md)进行说明。请将其安装到上面准备好的最新版本 SSP 中。

大多数情况下，人格附带的 yaya.dll 都比较旧。请将其替换为上面下载的最新版本（位置为“（ssp.exe 所在文件夹）\ghost\（模板人格的文件夹名称）\ghost\master”）。

## 准备便于开发的环境

### SSP 开发面板

首先启动 SSP，右键单击人格 → 设置 → 本体设置 → 常规 → 勾选“启用开发者功能”（虽然会弹出警告对话框，但可以放心确认）。

接下来，右键单击 → 功能 → 打开开发面板。这里提供了各种便于人格开发的调试功能。开发期间建议一直保持面板打开。

![SSP 的开发面板](../attachment/img_tutorial_01_002.png)

### YAYA 调试工具

下载[调试器“玉”](http://umeici.onjn.jp/)，并解压到方便使用的位置。参考：[使用玉检查词典错误](../tips/tama-error-check.md)

## 准备文本编辑器和 YAYA 语法高亮设置（仅供有需要的人）

使用 Windows 自带的记事本也能制作人格，但设置 YAYA 语法高亮后，词典会更易于阅读。请从[编辑器语法高亮文件](../tips/editor-color-files.md)中选择喜欢的文件。使用 JmEditor 时，显示效果如下。

![JmEditor 中的语法高亮示例](../attachment/img_tutorial_01_001.png)

## 设置文件关联

将“.dic”（词典）、“.log”（运行日志）和“.cfg”（存档数据）这 3 种扩展名设置为双击后即可使用文本编辑器打开。文件关联的设置方法因操作系统而异，这里不作说明。请自行通过搜索网站等方式查找。

如果准备了设置好 YAYA 语法高亮的文本编辑器，请将“.dic”文件关联到该编辑器。

## 下一步

- [教程 2：试着编写对话](./tutorial-02-writing-dialogue.md)

## 相关内容

- [SimpleYAYA 模板](../other/simple-yaya-template.md)
- [遇到问题时的处理方法](../other/troubleshooting.md)
