# CLEARERRORLOG

**Category:** デバッグ

## Signature

```
CLEARERRORLOG()
```

## Parameters

なし

## Returns

空の配列

YAYAの内部処理で蓄積されたエラーおよび警告ログを消去する。実行後、GETERRORLOGが返すエラー配列は空になる。

## Description

YAYA 内部で起きたエラー・警告のログを消去する。実行すると、GETERRORLOG で得られるエラー配列が空になる。

## Compatibility

- YAYA: バージョンTc567-2以降

## See Also

- GETERRORLOG
