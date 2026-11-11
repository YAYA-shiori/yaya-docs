# LETTONAME
**Category:** メタ操作・特殊関数

## Signature
```
LETTONAME(name, val)
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| name | 表示赋值目标变量名的字符串 |
| val | 要赋的值 |

## Returns
VOID（无返回值）

## Description
将 val 指定的值赋给 name 指定字符串所表示的变量名。用于在运行时动态确定变量名并赋值。例如，需要在运行时合成变量名时可以使用此函数（例如 `shiori3.dic` 中的 reference 变量）。

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
- YAYA：从初始版本起可用
- AYA：5.8 及以上版本可用

## See Also
- ISVAR
