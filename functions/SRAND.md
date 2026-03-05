# SRAND
**Category:** 数学関数
**Source:** マニュアル/関数/SRAND

## Signature
```
SRAND( [seed] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| seed | 乱数のシード値（整数・実数・文字列を受け付ける）。省略時は現在時刻でランダムに初期化 |

## Returns
- 成功時: 1
- 失敗時: 0

## Description
整数乱数のシードを設定します。引数を省略した場合は現在時刻を基にシードを初期化します。

システム辞書内で RAND 関数が使用されている場合があるため、SRAND を使用する際は影響範囲に注意してください。

## Compatibility
- YAYA: Tc551-1以降

## See Also
- RAND（乱数生成）
