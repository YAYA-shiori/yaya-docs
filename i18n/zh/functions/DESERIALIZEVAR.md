# DESERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
DESERIALIZEVAR( name, text )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| name | 用于恢复的变量名字符串。以 `_` 开头时为局部变量，否则为全局变量。如果变量不存在，则创建变量 |
| text | [SERIALIZEVAR](SERIALIZEVAR.md) 返回格式的字符串 |

## Returns
恢复成功时返回 1。`text` 无法按格式解析或参数无效时返回 0（不对变量进行任何操作）。

## Description
将 `text` 作为 [SAVEVAR](SAVEVAR.md#保存形式) 写入存档文件的值格式进行解析，并存入 `name` 指定的变量。变量原有的值会被替换，类型也由 `text` 的内容决定（整数 / 实数 / 字符串 / 数组 / 哈希）。

与 [LETTONAME](LETTONAME.md) 一样，不会调用为变量设置的 setter / watcher。分隔符以及 setter / watcher / destorier 的设置不会改变。

以下情况会发出警告并返回 0，且不会创建或修改变量。

| 情况 | 警告 |
|------|------|
| 参数不足 | W0008 |
| `name` 或 `text` 不是字符串 | W0009 |
| `name` 是空字符串 | W0010 |
| `name` 不能用作变量名（包含 `,`、与系统函数或保留字同名等） | W0012 |
| `text` 无法按格式解析（空字符串、没有双引号的字符串、没有 `:` 的数组、值只有 `IVOID` 等） | W0026 |

## Example
```
a = (1, "x", 2.5)
_s = SERIALIZEVAR("a")
_r = DESERIALIZEVAR("b", _s)   // b が (1, "x", 2.5) になる。_r は 1

DESERIALIZEVAR("n", "0.5")     // n が実数 0.5 になる
DESERIALIZEVAR("m", "abc")     // 0。警告 W0026
```

恢复到局部变量：

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_r = DESERIALIZEVAR("_y", SERIALIZEVAR("_x"))
// _y は _x と同じ入れ子の配列になる
```

## Compatibility
- Tc607-3 及以上版本

## See Also
- SERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- LETTONAME
- PARSEJSON
