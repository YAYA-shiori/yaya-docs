# LETTONAME
**Category:** メタ操作・特殊関数

## Signature
```
LETTONAME(name, val)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | String representing the name of the variable to assign to |
| val | Value to assign |

## Returns
VOID (no return value)

## Description
Assigns the value specified by val to the variable whose name is given by name. Use this function to determine a variable name dynamically at runtime and assign a value to it.

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
- YAYA: Available from the initial version
- AYA: Available from version 5.8 onward

## See Also
- ISVAR
