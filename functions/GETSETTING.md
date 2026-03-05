# GETSETTING
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/GETSETTING

## Signature
```
GETSETTING( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 取得したい情報の識別子（後述の文字列または基礎設定のエントリ名） |

## Returns
- 成功: 要求した情報（文字列）
- 失敗: 空文字列

## Description
動作中の文に設定されている情報を返す関数。

`string`には以下の識別子（文字列）または後方互換のための数値（0〜4）を指定できる。また、基礎設定（マニュアル/文法/1.基礎設定）のエントリ名を指定することも可能。

## Information Types
| 識別子 | 旧数値 | 取得されるデータ | 例 |
|--------|--------|----------------|-----|
| `coreinfo.version` | 0 | YAYAのバージョン番号 | `"Tc522-1"` |
| （数値1）          | 1 | 現在の文字コードID | `0` |
| `coreinfo.path`    | 2 | ディレクトリの絶対パス | `"c:\hogehoge\"` |
| `coreinfo.name`    | 3 | DLL名 | `"YAYA"` |
| `coreinfo.author`  | 4 | DLL作者 | `"umeici/The Maintenance Shop"` |
| `coreinfo.savefile` | — | セーブファイルのパス | `"d:/ghost/konno_yayame/..."` |
| `coreinfo.mode`    | — | 実行モード | `"normal"` または `"emergency"` |

## Compatibility
- YAYA: 初期バージョンから使用可能。`coreinfo.mode`はTc556-2で追加
- AYA: バージョン5.8以降（数値引数0〜4のみ対応）

## See Also
- SETSETTING
- マニュアル/文法/1.基礎設定
