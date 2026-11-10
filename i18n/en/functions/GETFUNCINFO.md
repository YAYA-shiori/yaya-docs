# GETFUNCINFO
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCINFO( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | The name of the function whose information to retrieve (required) |

## Returns
- On success: A generic array
  - Index 0: Full path of the file where the function is defined
  - Index 1: Starting line number
  - Index 2: Ending line number
- On failure: -1

## Description
Gets information about a (user-defined) function in the currently loaded dictionary.

You can retrieve the path of the file where the function is defined, as well as its starting and ending line numbers. This is useful for debugging when you need to dynamically find which file and location a function is defined in.

## Example

An example that receives a function name in `OnTextDrop` and displays the file and line where the function is defined (in debug mode).

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
- YAYA: Tc558-1 and later

## See Also
- GETFUNCLIST
