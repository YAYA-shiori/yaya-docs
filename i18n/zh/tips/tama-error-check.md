# 使用玉检查词典错误

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 使用「玉」检查词典错误

使用调试工具「玉」可以轻松检测错误。

- [玉改良项目](https://github.com/nikolat/tama)　可从右侧的Releases下载。
- [「玉」下载站点](http://umeici.onjn.jp/)　可从「tama(debugger for aya)」下载。

### 步骤1

#### 1.启动玉

**启动人格之前**请先启动玉。

#### 2.启动人格

如果没有错误，消息就会以惊人的速度不断滚动。<br>
如果有错误，则会显示红色文字。

#### 3.查看显示的错误

![Image2.png](../attachment/Image2.png)

橙色表示警告，红色表示致命错误。<br>
橙色错误不会妨碍运行，但红色是会导致**人格无法运行的致命错误**，因此需要修复。

```
aya_mouse.dic(8) : error E???? ...
```

最左侧是发生错误的词典文件名，括号内表示错误所在的行号。

### 步骤2

#### 1.结束人格

请**结束所有正在开发的人格等程序**。<br>
「玉」也可以显示运行状况，如果有正在运行的人格，消息就会以惊人的速度不断滚动。

#### 2.将AYA的DLL拖放到玉上

![Image1.png](../attachment/Image1.png)

请拖放DLL，而不是词典文件。

#### 3.查看显示的错误

与步骤1的第3步相同。

### 附：右键菜单说明

**jump to Top**：滚动到最上方。

**jump to Bottom**：滚动到最下方。

**Copy to clipboard**：将内容复制到剪贴板。

**receiVe**：~

显示正在运行的人格的运行状况。<br>
如果想在保持人格运行的同时使用玉进行各种操作，可以取消勾选此项。

**reQuest dialog**：供高级开发者使用的调试功能。通常请勿使用（喂

**Reload(unload and load)**：重新加载。修改词典后想再次检查时，无需反复拖放DLL，使用此菜单即可一次完成。

**Unload**：卸载已加载的AYA。通常无需使用。

**eXit(auto unload)**：退出。点击窗口的×标记也会执行相同操作。

## 附件

- [Image1.png](../attachment/Image1.png)
- [Image2.png](../attachment/Image2.png)
