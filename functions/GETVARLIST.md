# GETVARLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETVARLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （省略可）指定した文字列で始まる変数名のみを返す。省略時は全変数を返す |

## Returns
- 成功時: 変数名の汎用配列
- 失敗時: IARRAY

## Description
現在保持している変数のリストを返す。`prefix` を指定すると、その文字列で始まる変数名のみが返される。

## Example

指定した名前で始まる変数をすべて消去する関数と、正規表現にマッチする変数をすべて消去する関数の例。

```
ERASEALLVARBEGINAS {
	_L= GETVARLIST(_argv[0])
	foreach _L;_V {
		ERASEVAR(_V)
	}
}

ERASEALLVARINRE {
	_L= GETVARLIST
	foreach _L;_V {
		if RE_GREP(_V,_argv[0])
			ERASEVAR(_V)
	}
}
```

## Compatibility
- YAYA: 初期から利用可能

## See Also
- GETFUNCLIST
