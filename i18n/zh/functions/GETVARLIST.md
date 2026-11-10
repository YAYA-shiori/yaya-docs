# GETVARLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETVARLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （可选）仅返回以指定字符串开头的变量名。省略时返回所有变量 |

## Returns
- 成功时：变量名组成的通用数组
- 失败时：IARRAY

## Description
返回当前持有的变量列表。指定 `prefix` 时，仅返回以该字符串开头的变量名。

## Example

以下示例展示了清除所有以指定名称开头的变量，以及清除所有匹配正则表达式的变量的函数。

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
- YAYA：从初始版本起即可使用

## See Also
- GETFUNCLIST
