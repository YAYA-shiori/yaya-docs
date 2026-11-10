# CVAUTOEX

**Category:** 型取得/変換

## Signature

```
CVAUTOEX(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The variable to convert |

## Returns

No return value (converts the variable in place)

Converts text in string form if it can be interpreted as an integer or real number; otherwise, it remains a string. Unlike CVAUTO, this function converts only if converting the string back produces the original string. It first attempts integer conversion, then real number conversion. Behavior is undefined if a generic array variable is passed.

## Example

```
// 文字列のまま残る例
_val = '3.14'
CVAUTOEX(_val)
GETTYPE(_val)  // "3" を出力（文字列型）

// 実数に変換される例
_val = '3.140000'
CVAUTOEX(_val)
GETTYPE(_val)  // "2" を出力（実数型）
```

## Compatibility

- YAYA: Tc571-3 and later

## See Also

- CVAUTO
- CVINT
- CVREAL
- CVSTR
- TOAUTO
