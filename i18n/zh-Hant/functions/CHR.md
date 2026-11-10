# CHR

**Category:** 文字列操作

## Signature

```
CHR( val [, val ... ] )
```

## Parameters

| 引數 | 說明 |
|-----------|-------------|
| val | UCS-2 字元碼值（數值）。可指定多個 |

## Returns

成功時：轉換後的字元或字串（長度等於引數數量的字串）
失敗時：VOID

## Description

以數值指定 UCS-2 編碼時，會以字串形式傳回對應的 1 個字元。可以指定多個數值，此時會傳回長度等於引數數量的字串（傳入通用陣列時會傳回字串）。UCS-2 編碼在 ASCII 範圍內與 ASCII 編碼相容。

## Example

```
CHR(65)      // "A" を返す
CHR(20282)   // "伺" を返す
```

## Compatibility

- YAYA：自初版起可使用
- AYA：5.8 版以後

## See Also

- CHRCODE
