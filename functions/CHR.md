# CHR

**Category:** 文字列操作

## Signature

```
CHR( val [, val ... ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | UCS-2の文字コード値（数値）。複数指定可能 |

## Returns

成功時：変換された文字または文字列（引数の数に等しい長さの文字列）
失敗時：VOID

## Description

UCS-2 コードを数値で指定すると、対応する 1 文字を文字列で返す。数値は複数指定でき、その場合は引数の数だけの長さの文字列を返す（汎用配列を渡せば文字列が返る）。UCS-2 コードは ASCII の範囲では ASCII コードと互換性がある。

## Example

```
CHR(65)      // "A" を返す
CHR(20282)   // "伺" を返す
```

## Compatibility

- YAYA: 初版から利用可能
- AYA: バージョン5.8以降

## See Also

- CHRCODE
