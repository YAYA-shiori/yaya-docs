# CHARSETLIBEX

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIBEX(path, code)
CHARSETLIBEX(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | DLLファイルの場所。YAYAのディレクトリからの相対パス、または絶対パスで指定する |
| code | （省略可）文字コードIDまたは文字コードを表すテキスト識別子（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。知らない名前なら警告 W0012 を出し、設定を変えない |

## Returns

codeを省略した場合：指定したDLLの現在の文字コード設定を文字列で返す
codeを指定した場合：VOID（何も返さない）

外部ライブラリとのやり取りに使用する文字コードを個別に指定する。Tc530-2以降、LOADLIBの前に呼び出すことで有効になり、「初期化中」に設定可能。デフォルトのエンコーディングは設定ファイルの charset.extension エントリ（未指定の場合は charset）から取得される。ただし POSIX 環境のSAORI-basic（Tc604-1以降）のデフォルトは UTF-8。

## Compatibility

- YAYA: 初版から利用可能。引数省略機能はTc531以降
- Tc574-8 / Tc603-1: 知らない文字コードの名前を渡すと、警告 W0012 を出して設定を変えないようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also

- CHARSETLIB
- CHARSETTEXTTOID
