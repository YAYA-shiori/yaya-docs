# SPLIT
**Category:** 文字列操作
**Source:** マニュアル/関数/SPLIT

## Signature
```
SPLIT(src, delim [, max])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 分割対象の文字列（数値変数はTOSTRで変換してから渡すことを推奨） |
| delim | 区切り文字列 |
| max | 最大分割数（省略時または0で完全分割） |

## Returns
- 成功時: 分割した文字列要素を含む汎用配列
- 失敗時: 空の配列

## Description
文字列を分割して汎用配列として返します。正規表現処理を行わないため、RE_SPLIT よりも高速です。

`max` を指定した場合、その数で分割を打ち切り、残りの部分は最後の要素にまとめられます。

## Example
```
_array = SPLIT("A//B//C//D//E", "//", 3)
// 結果: ("A", "B", "C//D//E")
```

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降

## See Also
- RE_SPLIT（正規表現を使った分割）
