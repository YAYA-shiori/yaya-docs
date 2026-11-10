# DICLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICLOAD( filename [, code] )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| filename | 要加载的词典文件名 |
| code | 字符编码 ID 或字符编码名称（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。省略、为空字符串或为 `default` 时，遵循基本设置文件中的设置。如果名称未知，则发出警告 W0012，不加载任何内容并返回 1 |

## Returns

- `0`：成功
- `1`：失败

## Description

动态加载指定的词典文件。

注意事项：

- 如果词典存在问题，则会发生错误，不会进行任何修改。
- 加载的词典要到下一次请求调用时才生效，当前正在执行的函数会受到保护。
- 字符串嵌入元素的作用域展开语法在 DICLOAD 之后无法使用。请考虑使用能立即识别已加载词典内容的 EVAL。
- 加载的词典可以通过 DICUNLOAD 卸载，但存在限制。
- 通过 [THREADSTART](THREADSTART.md) 启动的线程运行期间，会发出警告 W0032，不加载任何内容并返回 1。

## Compatibility

- YAYA: Tc556-1 及以上版本
- Tc608-1：改为在工作线程运行期间无法加载
- Tc574-8 / Tc603-1：修复了传入数值字符编码 ID 时被忽略的问题。现在传入未知字符编码名称时会发出警告 W0012 并失败（此前会按基本设置文件中的设置加载）

## See Also

- DICUNLOAD
- EVAL
