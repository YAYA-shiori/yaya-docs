# GETMEMINFO
**Category:** システム情報

## Signature
```
GETMEMINFO()
```

## Parameters
無（沒有引數）

## Returns
包含執行環境記憶體資訊的通用陣列（5 個元素）：

| 索引 | 內容 |
|------------|------|
| 0 | 實體記憶體使用率 |
| 1 | 實體記憶體總量 |
| 2 | 實體記憶體可用容量 |
| 3 | 虛擬記憶體＋實體記憶體總量 |
| 4 | 虛擬記憶體＋實體記憶體可用容量 |

## Description
取得執行環境記憶體資訊的函式。

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 版以後
