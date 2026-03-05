# UNDEFGLOBALDEFINE
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/UNDEFGLOBALDEFINE

## Signature
```
UNDEFGLOBALDEFINE( definename )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| definename | `#globaldefine` で宣言したディレクティブ名 |

## Returns
- 0: 成功
- 1: 失敗

## Description
`#globaldefine` で宣言されたディレクティブを無効化・削除する。

`#globaldefine` で定義されたテキストを辞書ファイルに直接挿入することはできない。クォートで囲んでいてもプリプロセッサが適用されてしまうため、回避するには対象文字列を分割して記述する（例: `"TEST_" + "DEF"` のように連結する）。

## Compatibility
- YAYA: Tc561-1 以降

## See Also
- DICUNLOAD
- SETGLOBALDEFINE
- ISGLOBALDEFINE
- PROCESSGLOBALDEFINE
