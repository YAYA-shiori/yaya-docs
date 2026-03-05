# LOGGING
**Category:** デバッグ
**Source:** マニュアル/関数/LOGGING

## Signature
```
LOGGING(var)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | ログに書き込む値。任意の型を指定可能 |

## Returns
VOID（戻り値なし）

## Description
指定した値をログファイルに書き込み、同時にデバッグツール「玉」にも表示します。任意のデータ型を受け付けます。

単純配列は各値をカンマで結合した形式で出力されます。

## Compatibility
- YAYA: 初期バージョンより使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- GETERRORLOG
- CLEARERRORLOG
- GETLASTERROR
- SETLASTERROR
