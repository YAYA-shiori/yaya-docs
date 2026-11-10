# ERASEVAR

**Category:** メタ操作・特殊関数

## Signature

```
ERASEVAR( name [, name ...] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| name | 要刪除的變數名稱（以字串指定）。可以指定多個。 |

## Returns

沒有傳回值（VOID）。

## Description

刪除變數。變數名稱必須以字串指定。

```
ERASEVAR("i")          // 正しい例：変数 i を削除
ERASEVAR("i","j","k")  // 正しい例：複数の変数を一度に削除
ERASEVAR(i)            // 誤った例：変数名は文字列リテラルで指定すること
```

可用於刪除不需要保留在存檔資料中的全域變數等。

## Compatibility

- YAYA: 自初版起支援
- TC532-1 以後：支援同時刪除多個變數
- AYA: 5.8 以後

## See Also

- ERASE
- EVAL
