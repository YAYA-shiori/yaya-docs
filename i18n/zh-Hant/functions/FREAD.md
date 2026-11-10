# FREAD

**Category:** ファイル操作

## Signature

```
FREAD(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 指定之檔案的相對路徑（相對於 yaya.dll 的路徑） |

## Returns

- 成功時：讀取到的一行字串（會移除 CR、LF 等行尾字元）。從 FCHARSET 指定的字元編碼轉換為 YAYA 的內部編碼
- 到達檔案結尾時：-1
- 失敗時：空字串

必須事先使用 FOPEN 開啟檔案。

## Description

從檔案讀取一行。

- 執行 `FREAD` 前，必須先使用 `FOPEN` 開啟檔案
- 字元編碼會從 `FCHARSET` 指定的編碼轉換為 YAYA 內部使用的字元編碼
- 會移除行尾的換行字元（CR、LF）

### 注意

若為了偵測 EOF 而撰寫如下程式碼，當檔案中存在「只有 `-1` 的一行」時，可能會將其誤認為 EOF，並停止讀取。

```
_line = FREAD(_filename);
if(_line == -1) { break; }
```

可如下修改以避免此情況。

```
_line = FREAD(_filename);
if(GETTYPE(_line) == 1 && _line == -1) { break; }
```

EOF 的 `-1` 是整數值，而從檔案讀取的 `"-1"` 是字串，因此請使用 [GETTYPE](GETTYPE.md) 檢查值的種類，只有在值是「整數值 `-1`」時才將其視為 EOF。

## Compatibility

- YAYA：從首次發布起即可使用
- AYA：版本 5.8 以後

## See Also

- FWRITE
- FREADBIN
- FOPEN
- FREADENCODE
- FWRITE2
- FCHARSET
