# GETFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCLIST( [prefix] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （可省略）仅返回名称以此字符串开头的函数。省略时返回所有函数 |

## Returns
- 成功：包含函数名的通用数组
- 失败：IARRAY

## Description
返回当前已加载词典中的函数列表。

指定 `prefix` 时，只会返回名称以该字符串开头的函数。省略时会返回所有函数。

## Example

执行所有名称以指定字符串开头的函数，以及执行所有名称匹配正则表达式的函数的示例。

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
- YAYA：从初始版本起可用

## See Also
- GETVARLIST
- GETSYSTEMFUNCLIST
