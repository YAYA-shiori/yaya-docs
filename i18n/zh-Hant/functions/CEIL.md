# CEIL

**Category:** 数学関数

## Signature

```
CEIL(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 要進位的實數 |

## Returns

成功時：進位後的實數
失敗時：0.0

和 C 語言的 ceil() 函式相同，傳回「大於或等於引數的最小整數」。請注意負數的處理方式。

## Description

將實數的小數部分進位。和 C 語言的 `ceil()` 相同，會傳回「大於或等於引數的整數中最小的值」，因此處理負值時請特別留意。

## Example

```
CEIL(1.75)   // 2.000000 を返す
CEIL(-1.75)  // -1.000000 を返す（-2ではなく切り上げのため）
CEIL(7/3)    // 2.000000 を返す（整数除算のため7/3=2）
CEIL(7.0/3)  // 3.000000 を返す（実数除算）
```

## Compatibility

- YAYA: 初版起即可使用
- AYA: 5.8 版以後

## See Also

- FLOOR
- ROUND
