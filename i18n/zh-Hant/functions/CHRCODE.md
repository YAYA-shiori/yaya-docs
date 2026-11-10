# CHRCODE

**Category:** 文字列操作

## Signature

```
CHRCODE( string [ , pos ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 包含要取得字元碼之字元的文字 |
| pos | （可省略）要取得字元碼的字元位置（從 0 開始）。省略時為 0 |

## Returns

成功時：表示字元碼的數值
失敗時：0

傳回 UCS-2 字元碼。ASCII 字元（半形英數字）與 ASCII 碼相容。

## Example

```
CHRCODE('A')      // 65 を返す
CHRCODE('ABC', 2) // 67（文字'C'）を返す
CHRCODE('伺')     // 20282 を返す
```

## Compatibility

- YAYA: 初版起即可使用
- AYA: 5.8 版以後

## See Also

- CHR
