# 从 AYA 迁移

将现有的 AYA5 人格迁移到 YAYA。

## 注意事项

### DLL 名称变更

DLL 名称从 `aya5.dll` 变更为 `yaya.dll`。

- 因此，需要将 `aya5.txt` 重命名为 `yaya.txt`
- 存档文件名会变为 `yaya_variable.cfg`，存档数据不会自动迁移
- 如果仍使用 AYA 模板启动过，则将 `aya5_variable.cfg` 重命名为 `yaya_variable.cfg`

为避免这种情况，提供了相应的功能。打开 `aya_shiori3.dic`，在 `load` 函数的 `OnLoad` 之前添加以下代码。

```
if FSIZE('yaya_variable.cfg') <= 0 {
	RESTOREVAR('aya5_variable.cfg')
	SAVEVAR('yaya_variable.cfg')
	FDEL('aya5_variable.cfg')
}
```

如果没有修改过 `aya_shiori3.dic`，可以参考[系统词典](../system/yaya-shiori3-dic.md)中的说明，下载所需文件并覆盖，这样就能轻松完成迁移（如果使用旧版兼容词典，请在 `yaya.txt` 中的 `aya_shiori3.dic` 之后添加用于兼容 AYA 的词典。当前的系统词典中，对应的文件是 `compatible.dic`）。

### 系统词典变更

系统词典会发生变更（建议替换）。

- 在 AYA5 的系统词典中，SAORI 的返回值等会将字节值 1 替换为逗号，并将数字转换为数值而非字符串；而 YAYA 的系统词典默认不会进行这些处理
- 部分函数（如 `NAMETOVALUE`）不包含在系统词典中

## 迁移步骤

这里介绍**未修改过 AYA5 的 `aya_shiori3.dic` 时**的迁移步骤。以下所有操作都在人格的词典文件夹（`ghost/master/`）中进行。

1. 将 `descript.txt` 中的 `shiori,aya5.dll` 改写为 `shiori,yaya.dll`
2. 删除 `aya5.dll`，并放入 `yaya.dll`
3. 将 `aya5.txt` 改名为 `yaya.txt`
4. 下载[紺野ややめ (Konnoyayame)](http://ms.shillest.net/yayame.xhtml)，将 NAR 文件解压为 ZIP，或安装人格，以便查看其中的文件
5. 参考[系统词典](../system/yaya-shiori3-dic.md)，复制 `system` 文件夹下的内容
6. 复制 `system_config.txt`
7. 删除 `yaya.txt` 中的 `dic,aya_shiori3.dic`，改为写入 `include, system_config.txt`
8. 打开 `config.dic`，将 `SHIORI3FW.AUTO_DATA_CONVERT` 设为 1，将 `SHIORI3FW.REF_ACCEL` 设为 0

完成以上操作后，大部分迁移相关错误都能得到解决。

## 网络分发时

网络分发时，`aya5.dll` 和 `aya5.txt` 已经不再需要，因此建议使用包含以下内容的 `delete.txt` 等文件将其删除。

```
ghost/master/aya5.dll
ghost/master/aya5.txt
```

## 相关内容

- [使用 YAYA 制作人格](./creating-ghost.md)
- [系统词典/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
