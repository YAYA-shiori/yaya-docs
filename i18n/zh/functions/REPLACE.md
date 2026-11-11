# REPLACE
**Category:** 文字列操作

## Signature
```
REPLACE( src , before , after [ , count ] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| src | 要转换的字符串 |
| before | 要搜索的子字符串 |
| after | 替换后的子字符串 |
| count | （可省略）替换次数。小于 0 或省略时，替换所有匹配项 |

## Returns
- 成功：替换后的字符串
- 失败：原始 src 字符串（不变）

## Description
替换字符串。所有匹配的原字符串都会被替换。可以通过指定 `count` 限制替换次数。

## Example
```
_tehai = '4m4m5m5m6m6m2p3p3p4p1s1s1s'
_tsumo = '4p'
_dahai = '1s'
_tehai = REPLACE(_tehai, _dahai, _tsumo, 1)
_tehai // '4m4m5m5m6m6m2p3p3p4p4p1s1s'
```

## Compatibility
- YAYA：从初次发布起可用（count 参数于 Tc548-1 添加）
- AYA：5.8 及以上版本可用

## See Also
- RE_REPLACE
- RE_REPLACEEX
