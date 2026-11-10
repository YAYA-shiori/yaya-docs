# LSO
**Category:** メタ操作・特殊関数

## Signature
```
LSO
LSO()
```

## Parameters
无

## Returns
表示上一次选择操作所选位置的数值。

## Description

是 "last Selection Order" 的缩写。以表示位置的数值返回最近一次选择的结果。

```
request
{
    _i = foo
    LSO
}

foo
{
    "earth"
    "moon"
    "sun"
}
```

如果向 `_i` 赋值 `"sun"`，则 `LSO` 为 2（从0开始计数）。所有发生择一选择的情况都会生效。因此必须在相关处理完成后立即获取该值，否则就没有意义。

### 注意获取的位置

如果以下代码是为了获取 `ANY` 的选择结果，那么这是错误的。此处的 `LSO` 获取的是 `{ }` 的选择结果。因此 `res` 始终为0。

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
    }
    res = LSO
}
```

修改如下即可按预期工作。

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
        res = LSO
    }
}
```

### 存在输出确定符时

存在输出确定符（`--`）时，`LSO` 会对所有可能的组合生效。

```
request
{
    {
        "1"
        "2"
        "3"
        --
        "A"
        "B"
    }
    _i = LSO
}
```

例如，上述函数中的 `{ }` 部分会输出 `"1A"` `"2A"` `"3A"` `"1B"` `"2B"` `"3B"` 中的一种。`LSO` 的取值范围也与此一致，为0～5。各个值与上述排列顺序对应。

## Compatibility
- YAYA：从早期版本起可用
- AYA：5.8版以后可用

## See Also
- ANY
