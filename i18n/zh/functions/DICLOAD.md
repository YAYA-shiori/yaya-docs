# DICLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICLOAD( filename [, code] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | 要读取的词典文件名 |
| code | 字符编码 ID 或字符编码名称（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。省略、为空字符串或为 `default` 时，遵循基本设置文件中的设置。如果是未知名称，则发出警告 W0012，不读取任何内容并返回 1 |

## Returns

- `0`：成功
- `1`：失败

## Description

动态读取指定的词典文件。

注意事项：

- 如果词典存在问题，则会报错，且不会进行任何更改。
- 读取的词典要到下一次请求调用时才会生效；当前正在执行的函数会受到保护。
- 字符串嵌入元素的[范围指定展开](../grammar/06-string-embedding.md#範囲付き展開)在 DICLOAD 之后不会生效。可以考虑使用能立即识别已读取词典内容的 EVAL。
- 可以使用 DICUNLOAD 卸载已读取的词典，但存在限制。
- 通过 [THREADSTART](THREADSTART.md) 启动的线程运行期间，会发出警告 W0032，不读取任何内容并返回 1。

## Compatibility

- YAYA：Tc556-1 及更高版本
- Tc608-1：改为在线程运行期间无法读取词典
- Tc574-8 / Tc603-1：修复了以数值形式传入字符编码 ID 时被忽略的问题。传入未知字符编码名称时，改为发出警告 W0012 并返回失败（此前会根据基本设置文件中的设置读取）

## See Also

- DICUNLOAD
- EVAL
