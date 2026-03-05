# ISGLOBALDEFINE
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/ISGLOBALDEFINE

## Signature
```
ISGLOBALDEFINE( define )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| define | `#globaldefine` で定義されているか確認する名前 |

## Returns
- 1: 定義が存在する
- 0: 定義が存在しない

## Description
`#globaldefine` ディレクティブで定義された名前が存在するかどうかを確認する。

## Compatibility
- YAYA: Tc562-1以降

## See Also
- SETGLOBALDEFINE
