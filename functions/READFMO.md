# READFMO
**Category:** システム情報
**Source:** マニュアル/関数/READFMO

> **【Windows専用】** この関数はWindows用にコンパイルされたyayaでしか動作しません。

## Signature
```
READFMO( [ name ] [ , charset ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | （省略可）FMOの識別子。省略時は "Sakura" |
| charset | （省略可）文字エンコーディング。省略時はOSのデフォルト。Tc569-13で追加。 |

## Returns
- 成功: FMOの内容を文字列として返す
- 失敗: VOID（何も返さない）

## Description
ファイルマッピングオブジェクト（FMO）の内容を文字列として取得します。FMOの先頭4バイトはサイズを表す符号なし整数であり、読み取り時にはその4バイトが除去されます。FMO内にnullバイト（0x00）が存在する場合の動作は未定義です。

## Compatibility
- YAYA: バージョンTc524-1で導入
