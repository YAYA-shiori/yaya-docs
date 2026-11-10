# GETTYPEEX
**Category:** 型取得/変換

## Signature
```
GETTYPEEX( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要检查类型的变量名（以字符串形式传入） |

## Returns
- 0：内部错误（失败）
- 1：整数
- 2：实数
- 3：字符串
- 4：通用数组
- 5：哈希（Tc600-3 及之后）

## Description
获取指定变量的数据类型。与 `GETTYPE` 的主要区别在于，参数传入的不是变量本身，而是**以字符串形式表示的变量名**。

对于只有一个元素的通用数组，本函数也会准确返回其类型，因此当 `GETTYPE` 因向后兼容行为而无法正确判定时，应使用本函数。

## Compatibility
- YAYA：Tc537-3 及之后
- Tc600-3：新增哈希类型时返回 5

## See Also
- GETTYPE
- GETVARLIST
