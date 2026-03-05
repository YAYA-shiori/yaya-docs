# CVAUTOEX

**Category:** 型取得/変換
**Source:** マニュアル/関数/CVAUTOEX

## Signature

```
CVAUTOEX(_var_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 変換対象の変数 |

## Returns

戻り値なし（変数をその場で変換する）

文字列形式のテキストを、整数または実数として解釈できる場合に変換し、それ以外は文字列のまま残す。CVAUTOとの違いは、「文字列に変換した結果が元の文字列と一致する場合のみ変換する」点。整数変換を先に試み、次に実数変換を試みる。汎用配列変数を渡した場合の動作は未定義。

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

- YAYA: TC571-3以降

## See Also

- CVAUTO
- CVINT
- CVREAL
- CVSTR
- TOAUTO
