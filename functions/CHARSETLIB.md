# CHARSETLIB

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIB(code)
CHARSETLIB()
CHARSETLIB
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | （省略可）文字コードIDまたは文字コードを表すテキストで文字エンコーディングを指定する（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。知らない名前なら警告 W0012 を出し、設定を変えない |

## Returns

引数なしの場合：現在のDLL文字コード設定を文字列で返す
引数ありの場合：VOID（何も返さない）

外部ライブラリとのやり取りに使用する文字コードを設定する。LOADLIBの前に呼び出す必要がある。デフォルトのエンコーディングは設定ファイルの charset.extension エントリ（未指定の場合は charset）から取得される。

CHARSETLIBはすべての外部ライブラリにグローバルに適用されるが、CHARSETLIBEXはライブラリごとの設定が可能。

## Compatibility

- YAYA: 初版から利用可能。引数省略はTc531以降でサポート
- AYA: バージョン5.8以降
- Tc574-8 / Tc603-1: 知らない文字コードの名前を渡すと、警告 W0012 を出して設定を変えないようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also

- CHARSETLIBEX
- CHARSETIDTOTEXT
