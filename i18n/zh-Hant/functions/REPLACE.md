# REPLACE
**Category:** 文字列操作

## Signature
```
REPLACE( src , before , after [ , count ] )
```

## Parameters
| 引數 | 說明 |
|-----------|-------------|
| src | 要轉換的字串 |
| before | 要搜尋的子字串 |
| after | 取代後的子字串 |
| count | （可省略）取代次數。若小於 0 或省略，則會取代所有符合項目 |

## Returns
- 成功：取代後的字串
- 失敗：原始 src 字串（未變更）

## Description
取代字串。所有符合的原字串都會被取代。指定 `count` 即可限制取代次數。

## Example
```
_tehai = '4m4m5m5m6m6m2p3p3p4p1s1s1s'
_tsumo = '4p'
_dahai = '1s'
_tehai = REPLACE(_tehai, _dahai, _tsumo, 1)
_tehai // '4m4m5m5m6m6m2p3p3p4p4p1s1s'
```

## Compatibility
- YAYA：自初次發行起即可使用（count 參數於 Tc548-1 新增）
- AYA：自版本 5.8 起即可使用
