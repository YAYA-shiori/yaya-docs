# LETTONAME
**Category:** メタ操作・特殊関数

## Signature
```
LETTONAME(name, val)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | String representing the name of the destination variable |
| val | Value to assign |

## Returns
VOID (no return value)

## Description
Assigns the value specified by val to the variable whose name is specified by the string name. Use this when you need to determine a variable name dynamically at runtime and assign a value to it. For example, it can be used when composing a variable name at runtime, such as for the reference variables in `shiori3.dic`.

## Example
```
// ループを使った動的変数代入
for _i = 0 ; _i < 5 ; _i ++ {
    LETTONAME('var' + _i , _i + 100)
}
// var0〜var4にそれぞれ100〜104が代入される

// 配列の代入（正しい書き方）
LETTONAME(_varname, ('abc', 12))

// 配列変数を経由した代入（正しい書き方）
_array = ('abc', 12)
LETTONAME(_varname, _array)

// 誤った書き方（最初の値しか代入されない）
LETTONAME(_varname, 'abc', 12)
```

## Compatibility
- YAYA: Available since the initial version
- AYA: Available from version 5.8

## See Also
- ISVAR
