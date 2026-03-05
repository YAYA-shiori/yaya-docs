# FCHARSET

**Category:** ファイル操作
**Source:** マニュアル/関数/FCHARSET

## Signature

```
FCHARSET( code )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | 設定する文字コードID |

## Returns

返り値はありません（VOID）。

## Description

ファイルの読み書きに使用する文字コードを指定します。FOPEN の前に呼び出す必要があります。ファイルごとに文字コードを変更でき、文字コードは FOPEN が呼ばれた時点で決定されます。設定はゴーストの現在のセッション中は維持されますが、終了後にリセットされます。FCHARSET を呼ばない場合のデフォルト文字コードは、基本設定ファイルの charset.file または charset の設定に従います。

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- FOPEN
- FCLOSE
- FATTRIB
