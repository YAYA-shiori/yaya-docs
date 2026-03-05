# PROCESSGLOBALDEFINE
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/PROCESSGLOBALDEFINE

## Signature
```
PROCESSGLOBALDEFINE(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | プリプロセス処理を行いたい文字列 |

## Returns
- 成功: グローバル定義を適用した後の処理済み文字列
- 失敗: -1

## Description
`#globaldefine` で定義したプリプロセス処理（文字列置き換え処理）と同様の処理を行います。プリプロセッサ機能の詳細については、マニュアル/文法/8.プリプロセスを参照してください。

## Compatibility
- YAYA: バージョンTc559-1から使用可能

## See Also
- マニュアル/文法/8.プリプロセス
