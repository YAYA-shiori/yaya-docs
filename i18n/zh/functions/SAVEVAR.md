# SAVEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SAVEVAR( [path] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 保存目标文件名（省略时为 DLL 名 + "_variable.cfg"，例如：yaya_variable.cfg） |

## Returns
无（VOID）

## Description
保存变量。执行的处理与卸载时相同。

也可以将保存目标文件指定为任意路径。

## 保存格式

每行写出一个变量，格式如下。

```
変数名,値,"デリミタ",watcher|setter|destorier
```

值的格式如下。

| 类型 | 格式 | 示例 |
|---|---|---|
| 整数 | 原样 | `5` |
| 实数 | 使用能够还原原值的小数位数（不使用指数形式）。无穷大和 NaN 写作 `inf` `-inf` `nan`（Tc574-8 / Tc603-1 及以上版本） | `2.5`、`0.0000001` |
| 字符串 | `"..."`（对 `"` 和控制字符进行转义） | `"abc"` |
| 通用数组 | 用 `:` 分隔元素。只有一个元素时末尾加上 `:IARRAY`，为空时写作 `IARRAY:IARRAY` | `1:"b":2.5` |
| 哈希（Tc600-3 及以上版本） | 用 `:` 分隔 `键=值`。只有一个元素时末尾加上 `:IHASH=IHASH`，为空时写作 `IHASH=IHASH:IHASH=IHASH` | `"a"=1:"b"="x"` |
| 元素、键或值为 VOID | `IVOID` | `"v"=IVOID` |
| 嵌套元素（Tc600-3 及以上版本） | 将数组或哈希的格式用 `IARRAY{...}` / `IHASH{...}` 包围 | `"l"=IARRAY{1:2}` |

Tc600-3 及以上版本中的哈希和嵌套示例:

```
h,"a"=1:"l"=IARRAY{1:2}:"n"=IHASH{"x"=1:"y"="s"},",",
v,IHASH{"k"=1:IHASH=IHASH}:IARRAY,",",
e,"e"=IHASH{IHASH=IHASH:IHASH=IHASH}:"ea"=IARRAY{IARRAY:IARRAY},",",
```

嵌套结构的内部也会按照相同规则写出，因此无论嵌套多少层，都可以还原为原值。

不包含哈希或嵌套结构的变量，其格式与 Tc600-3 之前相同。使用旧版本读取由 Tc600-3 及以上版本保存的文件时，只有包含哈希或嵌套结构的变量会损坏（[600 中的变更](../other/changes-600.md#セーブファイルの互換性)）。

## Compatibility
- YAYA: 初始版本起支持
- AYA: 5.8 及以上版本
- Tc600-3: 支持保存哈希和嵌套值
- Tc574-8 / Tc603-1: 实数改为以能够还原原值的小数位数保存（此前会四舍五入到小数点后 6 位，且无法读回无穷大和 NaN）

## See Also
- RESTOREVAR
- SERIALIZEVAR
- DESERIALIZEVAR
