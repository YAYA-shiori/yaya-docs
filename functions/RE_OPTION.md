# RE_OPTION
**Category:** 正規表現

## Signature
```
RE_OPTION( オプション文字列 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| オプション文字列 | 設定する Perl 互換の正規表現オプション文字列（i, s, m, x）。省略した場合は現在の設定を返す |

## Returns
現在有効なオプションを示す文字列（i, s, m, x の組み合わせ）

## Description
Perl 互換の正規表現オプションを設定します。

対応オプション:
- **i**: 大文字小文字を区別しないマッチング
- **m**: 入力を複数行として扱う
- **s**: ワイルドカード（.）が改行文字にもマッチするようにする
- **x**: 正規表現パターン内のコメント（#）と空白を無視する

既定ではオプションなし（`RE_OPTION("")` でも同じ状態に戻る）。引数なしで呼ぶと、現在のオプションを文字列で返す。

オプションはパターンの中でも指定できる（`(?i)abc` など）。詳しくは [正規表現](../grammar/14-regular-expressions.md#オプション) を参照。

## Compatibility
- YAYA: Tc534-1以降

## See Also
- RE_MATCH
- RE_SEARCH
- RE_REPLACE
- [正規表現](../grammar/14-regular-expressions.md)
