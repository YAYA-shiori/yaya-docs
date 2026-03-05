# LETTONAME
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/LETTONAME

## Signature
```
LETTONAME(name, val)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 代入先の変数名を表す文字列 |
| val | 代入する値 |

## Returns
VOID（戻り値なし）

## Description
nameで指定された文字列の変数名に、valで指定された値を代入します。実行時に変数名を動的に決定して値を代入する際に使用します。

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
- YAYA: 初期バージョンより使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- ISVAR
