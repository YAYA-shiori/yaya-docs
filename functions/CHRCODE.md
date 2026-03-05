# CHRCODE

**Category:** 文字列操作
**Source:** マニュアル/関数/CHRCODE

## Signature

```
CHRCODE( string [ , pos ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 文字コードを取得したい文字を含むテキスト |
| pos | （省略可）文字コードを取得する文字位置（0始まり）。省略時は0 |

## Returns

成功時：文字コードを表す数値
失敗時：0

UCS-2の文字コードを返す。ASCII文字（半角英数字）についてはASCIIコードと互換性がある。

## Example

```
CHRCODE('A')      // 65 を返す
CHRCODE('ABC', 2) // 67（文字'C'）を返す
CHRCODE('伺')     // 20282 を返す
```

## Compatibility

- YAYA: 初版から利用可能
- AYA: バージョン5.8以降

## See Also

- CHR
