# GETFUNCINFO
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCINFO( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 要取得資訊的函式名稱（必填） |

## Returns
- 成功：通用陣列
  - 索引 0：定義函式的檔案完整路徑
  - 索引 1：起始行號
  - 索引 2：結束行號
- 失敗：-1

## Description
取得目前已載入辭典中（使用者）函式資訊的函式。

可以取得函式定義所在的檔案路徑，以及起始和結束行號。此函式適用於偵錯，可動態查詢某個函式定義在哪個檔案、哪個位置。

## Example

以下範例會在 `OnTextDrop` 中接收函式名稱，並顯示該函式定義所在的檔案和行號（偵錯模式時）。

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
- YAYA：Tc558-1 之後

## See Also
- GETFUNCLIST
