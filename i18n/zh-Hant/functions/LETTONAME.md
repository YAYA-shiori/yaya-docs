# LETTONAME
**Category:** メタ操作・特殊関数

## Signature
```
LETTONAME(name, val)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 表示要指派目標的變數名稱之字串 |
| val | 要指派的值 |

## Returns
VOID（沒有傳回值）

## Description
將 val 指定的值指派給 name 指定字串所表示的變數名稱。用於在執行時動態決定變數名稱並指派值。

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
- YAYA：初始版本起即可使用
- AYA：5.8 版起即可使用

## See Also
- ISVAR
