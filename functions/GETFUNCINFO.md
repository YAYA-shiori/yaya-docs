# GETFUNCINFO
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCINFO( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 情報を取得したい関数名（必須） |

## Returns
- 成功: 汎用配列
  - インデックス0: 関数が定義されているファイルのフルパス
  - インデックス1: 開始行番号
  - インデックス2: 終了行番号
- 失敗: -1

## Description
現在読み込んでいる辞書の（ユーザー）関数の情報を取得する関数。

関数が定義されているファイルのパスと、その開始・終了行番号を取得できる。デバッグ用途で、ある関数がどのファイルのどこに定義されているかを動的に調べる際に有用。

## Example

`OnTextDrop` で関数名を受け取り、その関数が定義されているファイルと行を表示する例（デバッグモード時）。

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
- YAYA: Tc558-1 以降

## See Also
- GETFUNCLIST
