# LICENSE
**Category:** メタ操作・特殊関数

## Signature
```
LICENSE()
LICENSE
```

## Parameters
無

## Returns
包含 YAYA 授權文字的通用陣列。各個項目以換行分隔。

## Description
傳回 YAYA 的授權文字。除了 YAYA 本體的授權文字，也包含所內含函式庫（MT19937、parson、TinyXML-2、SQLite）的授權文字。

## Compatibility
- YAYA: Tc530-1 以上即可使用
- Tc601-1: 新增 parson 與 TinyXML-2 的授權文字
- Tc602-11: 新增 SQLite（公有領域）的說明

## See Also
- LETTONAME
- LINT.GetFuncUsedBy
