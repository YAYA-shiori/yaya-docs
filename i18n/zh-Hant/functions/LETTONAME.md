# LETTONAME
**Category:** メタ操作・特殊関数

## Signature
```
LETTONAME(name, val)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 表示指派目標變數名稱的字串 |
| val | 要指派的值 |

## Returns
VOID（沒有傳回值）

## Description
將 val 指定的值指派給 name 所指定字串表示的變數名稱。用於在執行時動態決定變數名稱並指派值，例如在執行時組合變數名稱時使用（例：`shiori3.dic` 中的 reference 變數）。

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
- YAYA：自初期版本起可使用
- AYA：5.8 版以後可使用

## See Also
- ISVAR
