# GETVARLIST
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/GETVARLIST

## Signature
```
GETVARLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | （省略可）指定した文字列で始まる変数名のみを返す。省略時は全変数を返す |

## Returns
- 成功時: 変数名の汎用配列
- 失敗時: IARRAY

## Description
現在保持している変数のリストを返す。`prefix` を指定すると、その文字列で始まる変数名のみが返される。

## Example
```
// 指定したプレフィックスを持つ全変数を削除する関数
ERASEALLVARBEGINAS
{
    _prefix = _argv[0]
    _varlist = GETVARLIST(_prefix)
    foreach _varlist ; _v
    {
        ERASEVAR(_v)
    }
}

// 正規表現にマッチする全変数を削除する関数
ERASEALLVARINRE
{
    _varlist = GETVARLIST
    foreach _varlist ; _v
    {
        if RE_MATCH(_v, _argv[0])
        {
            ERASEVAR(_v)
        }
    }
}
```

## Compatibility
- YAYA: 初期から利用可能

## See Also
- GETFUNCLIST
