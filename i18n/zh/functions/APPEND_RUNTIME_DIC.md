# APPEND_RUNTIME_DIC

**Category:** メタ操作・特殊関数

## Signature

```
APPEND_RUNTIME_DIC(dic_content)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| dic_content | 与词典文件内容等效的字符串。可以包含多行内容和函数定义 |

## Returns

成功时：0
失败时：-1

## Description

这会产生与将 `dic_content` 的内容写入名为 `_RUNTIME_DIC_` 的内存词典相同的效果。可以动态定义新的用户自定义函数等。`dic_content` 可以包含多行内容和函数定义，其行为与从文件读取词典相同。

由 [THREADSTART](THREADSTART.md) 启动的线程运行期间，会输出警告 W0032，不添加任何内容并返回 -1。

## Compatibility

- YAYA：Tc562-1 及之后版本
- Tc608-1：修改为工作线程运行期间无法添加内容

## See Also

- EVAL
- ISEVALUABLE
