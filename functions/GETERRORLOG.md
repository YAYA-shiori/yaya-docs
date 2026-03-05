# GETERRORLOG
**Category:** デバッグ
**Source:** マニュアル/関数/GETERRORLOG

## Signature
```
GETERRORLOG()
```

## Parameters
なし

## Returns
エラーログの文字列配列（最大20件、新しいものから順）

## Description
YAYA内部で発生したエラーや警告を含む配列を取得する関数。ログのフォーマットはデバッグツール「Tama」やエラーログ出力機能の出力と同じ形式。

辞書エラーにより緊急ロードが発動した場合でも、緊急機能が動作する前に保持していたエラーログが維持されるため、異常時のエラー出力が可能。

## Example
```
// エラーログをパースしてファイル名・行番号・エラー種別・エラーコード・メッセージに分割する例
_logs = GETERRORLOG()
foreach _logs ; _log
    _log = RE_REPLACE(_log, '(\[.+?\])\s', '$1\t')
    _parts = SPLIT(_log, '\t')
    _filename = _parts[0]
    _lineno   = _parts[1]
    _type     = _parts[2]
    _code     = _parts[3]
    _message  = _parts[4]
endforeach
```

## Compatibility
Tc555-1以降

## See Also
- CLEARERRORLOG
- マニュアル/文法/1.基礎設定
