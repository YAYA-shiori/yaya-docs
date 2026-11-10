# SAVEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SAVEVAR( [path] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 儲存目的地檔名（省略時為 DLL 名稱 + "_variable.cfg"，例如：yaya_variable.cfg） |

## Returns
無（VOID）

## Description
儲存變數。這項處理等同於 unload 時執行的處理。

也可以將儲存目的地檔案指定為任意路徑。

## 儲存格式

每個變數各用一行，以下列格式寫出。

```
変数名,値,"デリミタ",watcher|setter|destorier
```

值的格式如下。

| 型 | 書式 | 例 |
|---|---|---|
| 整數 | 原樣 | `5` |
| 實數 | 使用可還原原始值位數的小數（不使用指數表示法）。無限大和 NaN 分別表示為 `inf`、`-inf`、`nan`（Tc574-8 / Tc603-1 以後） | `2.5`、`0.0000001` |
| 字串 | `"..."`（`"` 和控制字元會跳脫處理） | `"abc"` |
| 通用陣列 | 以 `:` 分隔元素。若只有一個元素，末尾加上 `:IARRAY`；若為空，則為 `IARRAY:IARRAY` | `1:"b":2.5` |
| 雜湊（Tc600-3 以後） | 以 `:` 分隔 `鍵=值`。若只有一個元素，末尾加上 `:IHASH=IHASH`；若為空，則為 `IHASH=IHASH:IHASH=IHASH` | `"a"=1:"b"="x"` |
| 元素、鍵或值為 VOID | `IVOID` | `"v"=IVOID` |
| 巢狀元素（Tc600-3 以後） | 將陣列或雜湊的格式以 `IARRAY{...}` / `IHASH{...}` 包起來 | `"l"=IARRAY{1:2}` |

Tc600-3 以後的雜湊與巢狀範例:

```
h,"a"=1:"l"=IARRAY{1:2}:"n"=IHASH{"x"=1:"y"="s"},",",
v,IHASH{"k"=1:IHASH=IHASH}:IARRAY,",",
e,"e"=IHASH{IHASH=IHASH:IHASH=IHASH}:"ea"=IARRAY{IARRAY:IARRAY},",",
```

巢狀結構的內層也會依照相同規則寫出，因此無論巢狀幾層，都能還原成原本的值。

不包含雜湊或巢狀結構的變數，其格式與 Tc600-3 以前相同。使用 Tc600-3 以後的版本儲存的檔案若由舊版讀取，只有包含雜湊或巢狀結構的變數會變得不正確（[600 的變更點](../other/changes-600.md#セーブファイルの互換性)）。

## Compatibility
- YAYA: 自初始版本起支援
- AYA: 5.8 以後
- Tc600-3: 支援儲存雜湊與巢狀值
- Tc574-8 / Tc603-1: 改為以可還原原始值的位數儲存實數（在此之前會四捨五入至小數點後 6 位，無限大和 NaN 無法讀回）

## See Also
- RESTOREVAR
- SERIALIZEVAR
- DESERIALIZEVAR
