# CEIL

**Category:** 数学関数
**Source:** マニュアル/関数/CEIL

## Signature

```
CEIL(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 切り上げを行う実数 |

## Returns

成功時：切り上げ後の実数
失敗時：0.0

C言語のceil()関数と同様に「引数以上の最小の整数」を返す。負数の扱いに注意が必要。

## Example

```
CEIL(1.75)   // 2.000000 を返す
CEIL(-1.75)  // -1.000000 を返す（-2ではなく切り上げのため）
CEIL(7/3)    // 2.000000 を返す（整数除算のため7/3=2）
CEIL(7.0/3)  // 3.000000 を返す（実数除算）
```

## Compatibility

- YAYA: 初版から利用可能
- AYA: バージョン5.8以降

## See Also

- FLOOR
- ROUND
