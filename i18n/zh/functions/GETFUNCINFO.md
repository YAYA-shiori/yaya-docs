# GETFUNCINFO
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCINFO( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 要获取信息的函数名（必填） |

## Returns
- 成功：通用数组
  - 索引 0：定义函数的文件完整路径
  - 索引 1：起始行号
  - 索引 2：结束行号
- 失败：-1

## Description
获取当前已加载词典中的（用户自定义）函数信息的函数。

可以获取函数定义所在文件的路径及其起始行号和结束行号。此函数适用于调试，例如动态查询某个函数定义在哪个文件的什么位置。

## Example

在 `OnTextDrop` 中接收函数名，并显示该函数定义所在的文件和行号的示例（调试模式下）。

```
OnTextDrop{
	//...
	if DebugMode{
		_t=CUTSPACE(reference0)
		//...
		if ISFUNC(_t){
			_info=GETFUNCINFO(_t)
			_path=SPLITPATH(_info[0])
			if _path
				_path=_path[2]+_path[3]
			else
				_path=_info[0]
			"関数「%(_t)」は、\n/
			ファイル「\q[◇%(_path),OnOpenDirOrFile,%(_info[0])]」の%(_info[1])行目から始まります。\n/
			"
		}
		//...
	}
	//...
}
```

## Compatibility
- YAYA：Tc558-1 及以后

## See Also
- GETFUNCLIST
