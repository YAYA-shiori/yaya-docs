# CHR

**Category:** 文字列操作
**Source:** マニュアル/関数/CHR

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

ASCII範囲のコードはASCIIエンコーディングとの互換性を持つ。

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
