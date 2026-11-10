# CVAUTOEX

**Category:** 型取得/変換

## Signature

```
CVAUTOEX(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要轉換的變數 |

## Returns

沒有傳回值（直接轉換變數）

若字串形式的文字可解讀為整數或實數，就進行轉換；否則維持字串。與 CVAUTO 的差異在於，只有在「轉換成字串後的結果與原字串一致」時才會進行轉換。會先嘗試轉換為整數，再嘗試轉換為實數。傳入通用陣列變數時的行為未定義。

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

- YAYA：Tc571-3 以後

## See Also

- CVAUTO
- CVINT
- CVREAL
- CVSTR
- TOAUTO
