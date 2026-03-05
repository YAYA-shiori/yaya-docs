# RE_OPTION
**Category:** 正規表現
**Source:** マニュアル/関数/RE_OPTION

## Signature
```
RE_OPTION( オプション文字列 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| オプション文字列 | 設定するPerlCompatible正規表現のオプション文字列（i, s, m, x）。省略した場合は現在の設定を返す |

## Returns
現在有効なオプションを示す文字列（i, s, m, x の組み合わせ）

## Description
Perlコンパチブル正規表現のオプションを設定します。

対応オプション:
- **i**: 大文字小文字を区別しないマッチング
- **m**: 入力を複数行として扱う
- **s**: ワイルドカード（.）が改行文字にもマッチするようにする
- **x**: 正規表現パターン内のコメント（#）と空白を無視する

デフォルト設定: **m のみ**

## Compatibility
- YAYA: Tc534-1以降

## See Also
- RE_MATCH
- RE_SEARCH
- RE_REPLACE
