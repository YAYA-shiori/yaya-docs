# GETFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETFUNCLIST( [prefix] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （省略可）この文字列で始まる関数名のみを返す。省略した場合はすべての関数を返す |

## Returns
- 成功: 関数名の汎用配列
- 失敗: IARRAY

## Description
現在読み込んでいる辞書の関数一覧を返す関数。

`prefix`を指定すると、その文字列で始まる関数名のみがフィルタリングされて返される。省略した場合はすべての関数が返される。

## Example

指定した名前で始まる関数をすべて実行する関数と、正規表現にマッチする関数をすべて実行する関数の例。

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
YAYAの初期バージョンから使用可能

## See Also
- GETVARLIST
- GETSYSTEMFUNCLIST
