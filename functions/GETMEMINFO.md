# GETMEMINFO
**Category:** システム情報
**Source:** マニュアル/関数/GETMEMINFO

## Signature
```
GETMEMINFO()
```

## Parameters
なし（引数はありません）

## Returns
動作環境のメモリ情報を格納した汎用配列（5要素）:

| インデックス | 内容 |
|------------|------|
| 0 | 物理メモリ使用率 |
| 1 | 物理メモリ総量 |
| 2 | 物理メモリ空き容量 |
| 3 | 仮想メモリ＋物理メモリの総量 |
| 4 | 仮想メモリ＋物理メモリの空き容量 |

## Description
動作環境のメモリ情報を取得する関数。

## Compatibility
- YAYA: 初期バージョンから使用可能
- AYA: バージョン5.8以降
