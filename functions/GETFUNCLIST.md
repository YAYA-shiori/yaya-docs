# GETFUNCLIST
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/GETFUNCLIST

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
```
// すべての関数を列挙する例
_funclist = GETFUNCLIST()
foreach _funclist ; _func
    "%(\_func)"
endforeach

// "On"で始まる関数のみを取得する例
_on_funcs = GETFUNCLIST('On')

// RE_GREPで特定パターンの関数をフィルタリングする例
_all = GETFUNCLIST()
_filtered = RE_GREP(_all, '^On.*Event$')
```

## Compatibility
YAYAの初期バージョンから使用可能

## See Also
- GETVARLIST
- GETSYSTEMFUNCLIST
