# OUTPUTNUM
**Category:** メタ操作・特殊関数

## Signature
```
OUTPUTNUM(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 調べる対象の関数名（文字列） |

## Returns
対象関数が出力する選択候補数（整数）

## Description
指定した関数が出力する選択候補数を返します。対象関数を空の引数リストで呼び出すことで、出力候補数を取得します。関数の択一選択の仕組みについては[関数の選択方式](../grammar/02-functions.md#選択方式)を参照してください。

## Compatibility
- YAYA: バージョンTc569-1以降で使用可能

## See Also
- [関数の選択方式](../grammar/02-functions.md#選択方式)
