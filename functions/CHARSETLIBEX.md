# CHARSETLIBEX

**Category:** 外部ライブラリ
**Source:** マニュアル/関数/CHARSETLIBEX

## Signature

```
CHARSETLIBEX(path, code)
CHARSETLIBEX(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | DLLファイルの場所。YAYAのディレクトリからの相対パス、または絶対パスで指定する |
| code | （省略可）文字コードIDまたは文字コードを表すテキスト識別子 |

## Returns

codeを省略した場合：指定したDLLの現在の文字コード設定を文字列で返す
codeを指定した場合：VOID（何も返さない）

外部ライブラリとのやり取りに使用する文字コードを個別に指定する。Tc530-2以降、LOADLIBの前に呼び出すことで有効になり、「初期化中」に設定可能。デフォルトのエンコーディングは設定ファイルの charset.extension エントリ（未指定の場合は charset）から取得される。

## Compatibility

- YAYA: 初版から利用可能。引数省略機能はTc531以降

## See Also

- CHARSETLIB
- CHARSETTEXTTOID
