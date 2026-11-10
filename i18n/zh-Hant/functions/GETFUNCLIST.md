# GETFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCLIST( [prefix] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （可省略）只傳回名稱以此字串開頭的函式。省略時會傳回所有函式 |

## Returns
- 成功：函式名稱的通用陣列
- 失敗：IARRAY

## Description
傳回目前已載入辭典的函式清單。

指定 `prefix` 時，只會傳回名稱以該字串開頭的函式。省略時會傳回所有函式。

## Example

以下範例會呼叫所有名稱以指定字串開頭的函式，以及所有符合正規表示式的函式。

```
CALLALLFUNCTIONBEGINAS {
	_L= GETFUNCLIST(_argv[0])
	foreach _L;_V {
		EVAL(_V)
	}
}

CALLALLFUNCTIONINRE {
	_L= GETFUNCLIST
	foreach _L;_V {
		if RE_GREP(_V,_argv[0])
			EVAL(_V)
	}
}
```

## Compatibility
- YAYA：從初期版本起即可使用

## See Also
- GETVARLIST
- GETSYSTEMFUNCLIST
