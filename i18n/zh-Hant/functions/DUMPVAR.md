# DUMPVAR

**Category:** デバッグ

## Signature

```
DUMPVAR()
```

## Parameters

無

## Returns

沒有傳回值（VOID）。

## Description

將變數傾印至記錄檔。執行時會將當下所有變數的狀態寫入預設記錄檔（通常是 ayame.log）。這是用來檢查指令碼執行期間特定時間點的變數狀態的除錯工具。

## 輸出格式

每行會以 `[編號] 變數名稱 = 值` 的形式寫入一個變數。值會標示型別。

| 型別 | 格式 |
|---|---|
| 整數・實數・字串 | `(int)5`、`(double)2.500000`、`(string)abc` |
| VOID | `(nop/void)` |
| 通用陣列 | 接在 `(array) : ` 後面，元素之間以空白分隔 |
| 雜湊（Tc600-4 以後） | 接在 `(hash) : ` 後面，`鍵=值` 之間以空白分隔 |
| 巢狀元素（Tc600-4 以後） | 陣列以 `(array)[ ... ]` 括住，雜湊以 `(hash){ ... }` 括住 |

```
[0] count = (int)3
[1] list = (array) : (int)1 (string)p
[2] h = (hash) : (string)a=(int)1 (string)l=(array)[ (int)1 (int)2 ] (string)n=(hash){ (string)x=(double)2.500000 }
```

## Compatibility

- YAYA：Tc529-2 以後
- Tc600-4：改為輸出雜湊和巢狀值（此前雜湊會顯示為 `(unknown type)`，巢狀元素會顯示為 `(?UNKNOWN)`）
