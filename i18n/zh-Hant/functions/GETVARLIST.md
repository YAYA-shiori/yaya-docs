# GETVARLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETVARLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （可省略）只傳回以指定字串開頭的變數名稱。省略時傳回所有變數 |

## Returns
- 成功時：變數名稱的通用陣列
- 失敗時：IARRAY

## Description
傳回目前持有的變數清單。指定 `prefix` 時，只會傳回以該字串開頭的變數名稱。

## Example

以下範例分別示範清除所有以指定名稱開頭的變數，以及清除所有符合正規表示式的變數之函式。

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
- YAYA：從初期版本起即可使用

## See Also
- GETFUNCLIST
