# GETSYSTEMFUNCLIST
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/GETSYSTEMFUNCLIST

## Signature
```
GETSYSTEMFUNCLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （省略可）指定した文字列で始まるシステム関数名のみを返す。省略時は全システム関数を返す |

## Returns
- 成功時: システム関数名の汎用配列
- 失敗時: IARRAY

## Description
システム関数のリストを返す。`prefix` を指定すると、その文字列で始まるシステム関数名のみが返される。省略した場合は全システム関数のリストが返される。

## Compatibility
- YAYA: Tc557-1以降

## See Also
- GETVARLIST
- GETFUNCLIST
