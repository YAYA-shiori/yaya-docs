# GETTYPE
**Category:** 型取得/変換

## Signature
```
GETTYPE( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要检查类型的值、变量或表达式 |

## Returns
- 0：内部错误（失败）
- 1：整数
- 2：浮点数
- 3：字符串
- 4：通用数组
- 5：哈希（Tc600-3 及之后）

## Description
获取指定值的数据类型。

为了保持向后兼容，存在如下行为：“只有一个元素的通用数组会返回其唯一元素的类型”。如果要准确检查只有一个元素的通用数组的类型，建议使用 `GETTYPEEX`。

唯一元素是数组或哈希（[嵌套](../grammar/13-nesting.md)）时，行为也相同，分别返回 4 和 5。

```
GETTYPE(PARSEJSON('[[1,2]]'))     // 4
GETTYPE(PARSEJSON('[{"a":1}]'))   // 5
```

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：5.8 及之后
- Tc600-3：新增哈希类型时返回 5
- Tc602-10：修正了只有一个元素的通用数组在其唯一元素为数组或哈希时返回 0 的问题（改为返回 4 或 5）

## See Also
- GETTYPEEX
- IHASH
