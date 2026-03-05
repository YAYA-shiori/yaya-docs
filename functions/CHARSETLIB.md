# CHARSETLIB

**Category:** 外部ライブラリ
**Source:** マニュアル/関数/CHARSETLIB

## Signature

```
CHARSETLIB(code)
CHARSETLIB()
CHARSETLIB
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | （省略可）文字コードIDまたは文字コードを表すテキストで文字エンコーディングを指定する |

## Returns

引数なしの場合：現在のDLL文字コード設定を文字列で返す
引数ありの場合：VOID（何も返さない）

外部ライブラリとのやり取りに使用する文字コードを設定する。LOADLIBの前に呼び出す必要がある。デフォルトのエンコーディングは設定ファイルの charset.extension エントリ（未指定の場合は charset）から取得される。

CHARSETLIBはすべての外部ライブラリにグローバルに適用されるが、CHARSETLIBEXはライブラリごとの設定が可能。

## Compatibility

- YAYA: 初版から利用可能。引数省略はTc531以降でサポート
- AYA: バージョン5.8以降

## See Also

- CHARSETLIBEX
- CHARSETIDTOTEXT
