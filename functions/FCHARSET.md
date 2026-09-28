# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | 設定する文字コードID、または文字コードの名前（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。知らない名前なら警告 W0012 を出し、設定を変えない |

## Returns

返り値はありません（VOID）。

## Description

ファイルの読み書きに使用する文字コードを指定します。FOPEN の前に呼び出す必要があります。ファイルごとに文字コードを変更でき、文字コードは FOPEN が呼ばれた時点で決定されます。設定はゴーストの現在のセッション中は維持されますが、終了後にリセットされます。FCHARSET を呼ばない場合のデフォルト文字コードは、基本設定ファイルの charset.file または charset の設定に従います。

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降
- Tc574-8 / Tc603-1: 知らない文字コードの名前を渡すと、警告 W0012 を出して設定を変えないようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also

- FOPEN
- FCLOSE
- FATTRIB
