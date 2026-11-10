# HASH_VALUES
**Category:** ハッシュ操作

## Signature
```
HASH_VALUES( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | 哈希 |

## Returns
值组成的通用数组。按键的顺序排列。

## Description
以通用数组的形式返回哈希的值。排列顺序与 [HASH_KEYS](HASH_KEYS.md) 的键顺序相同。

值为数组时，会将该数组作为一个元素包含在返回值中（形成嵌套数组）。因此，返回值的元素数与哈希的元素数相同。

参数不是哈希时，会发出警告 W0009。

## Example
```
_h = IHASH("a", 1)
_h["b"] = (1, 2)
_v = HASH_VALUES(_h)
ARRAYSIZE(_v)   // 2
_v[1]           // 配列 (1,2)
TOSTR(_v)       // "1,1,2"
```

## Compatibility
- YAYA: Tc600-3及之后

## See Also
- HASH_KEYS
- IHASH
- [值的嵌套与多维赋值](../grammar/13-nesting.md)
