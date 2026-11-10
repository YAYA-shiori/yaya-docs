# 从 AYA 迁移

将现有的 AYA5 人格迁移到 YAYA。

## 注意事项

### DLL 名称变更

DLL 名称从 `aya5.dll` 变更为 `yaya.dll`。

- 因此，需要将 `aya5.txt` 重命名为 `yaya.txt`
- 存档文件名会变为 `yaya_variable.cfg`，存档数据不会自动迁移

为避免这种情况，提供了相应功能。打开 `aya_shiori3.dic`，在 `load` 函数的 `OnLoad` 前添加以下代码。

```
if FSIZE('yaya_variable.cfg') <= 0 {
	RESTOREVAR('aya5_variable.cfg')
	SAVEVAR('yaya_variable.cfg')
	FDEL('aya5_variable.cfg')
}
```

如果没有修改过 `aya_shiori3.dic`，可以参考[系统词典](../system/yaya-shiori3-dic.md)中的说明，下载并覆盖所需文件，即可轻松完成迁移（如果要使用向前兼容词典，请在 `yaya.txt` 中的 `aya_shiori3.dic` 后添加用于兼容 AYA 的词典。目前的系统词典中，与之对应的是 `compatible.dic`）。

### 系统词典变更

系统词典会有所变更（建议替换）。

- 在 AYA5 的系统词典中，SAORI 的返回值等会将字节值 1 替换为逗号，并将数字转换为数值而非字符串；但 YAYA 的系统词典默认不会进行这些处理
- 系统词典中不再包含部分函数（如 `NAMETOVALUE`）

## 迁移步骤

这里介绍**在 AYA5 中没有修改过 `aya_shiori3.dic` 时**的迁移步骤。以下所有操作均在人格的词典文件夹（`ghost/master/`）中进行。

1. 将 `descript.txt` 中的 `shiori,aya5.dll` 改为 `shiori,yaya.dll`
2. 删除 `aya5.dll`，并放入 `yaya.dll`
3. 将 `aya5.txt` 重命名为 `yaya.txt`
4. 下载[紺野ややめ (Konnoyayame)](http://ms.shillest.net/yayame.xhtml)，将 NAR 文件作为 ZIP 解压，或者安装人格，以便查看其中的文件
5. 参照[系统词典](../system/yaya-shiori3-dic.md)，复制 `system` 文件夹及其下的内容
6. 复制 `system_config.txt`
7. 删除 `yaya.txt` 中的 `dic,aya_shiori3.dic`，并改为 `include, system_config.txt`
8. 打开 `config.dic`，将 `SHIORI3FW.AUTO_DATA_CONVERT` 设为 1，将 `SHIORI3FW.REF_ACCEL` 设为 0

完成以上操作后，大部分迁移相关错误都会得到解决。

## 通过网络发布时

通过网络发布时，`aya5.dll` 和 `aya5.txt` 已经不再需要，因此建议使用包含以下内容的 `delete.txt` 等文件将它们删除。

```
ghost/master/aya5.dll
ghost/master/aya5.txt
```

## 相关内容

- [使用 YAYA 制作人格](./creating-ghost.md)
- [系统词典/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
