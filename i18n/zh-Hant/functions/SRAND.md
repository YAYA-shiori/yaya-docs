# SRAND
**Category:** 数学関数

## Signature
```
SRAND( [seed] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| seed | 隨機數種子值（可接受整數、實數、字串）。省略時會以目前時間隨機初始化 |

## Returns
- 成功時：1
- 失敗時：0

## Description
設定整數隨機數的種子。省略引數時，會以目前時間為基礎初始化種子。

系統辭典中可能會使用 RAND 函式，因此使用 SRAND 時請留意其影響範圍。

## Compatibility
- YAYA：Tc551-1 之後

## See Also
- RAND（亂數產生）
