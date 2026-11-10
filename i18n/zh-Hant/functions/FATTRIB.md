# FATTRIB

**Category:** ファイル操作

## Signature

```
FATTRIB( path )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要取得各種資訊的檔案或目錄路徑。可指定完整路徑。若為相對路徑，則以 DLL 的 load 傳入的位置為基準 |

## Returns

傳回包含 11 個元素的通用陣列。若失敗則傳回 `-1`。

| 索引 | 內容 |
|-------------|------|
| `[0]` | 可封存（僅限 Windows）= 1，其他 = 0 |
| `[1]` | 已壓縮（僅限 Windows）= 1，其他 = 0 |
| `[2]` | 目錄 = 1，其他 = 0 |
| `[3]` | 隱藏檔案（僅限 Windows）= 1，其他 = 0 |
| `[4]` | 一般檔案 = 1，其他 = 0 |
| `[5]` | 離線檔案（僅限 Windows）= 1，其他 = 0 |
| `[6]` | 唯讀（僅限 Windows）= 1，其他 = 0 |
| `[7]` | 系統檔案（僅限 Windows）= 1，其他 = 0 |
| `[8]` | 暫存檔案（僅限 Windows）= 1，其他 = 0 |
| `[9]` | 檔案建立日期時間。UNIX 上為 inode 更新日期時間 |
| `[10]` | 檔案最後更新日期時間 |

日期時間的單位為自 1970/1/1 0 時起算的秒數（epoch）。若要轉換為一般日期資訊，可使用 `GETTIME(_attrib[10])`。

## Description

取得檔案或目錄的各種資訊。也可以指定完整路徑。若為相對路徑，則以 DLL 的 load 傳入的位置（多數情況下為 DLL 所在位置）為基準。

## Example

```
_attrib = FATTRIB('hoge.txt')
_attrib[10]          // 最終更新日時（エポック秒）
GETTIME(_attrib[10]) // 読みやすい形式に変換
```

## Compatibility

- YAYA：自初版起支援
- AYA：5.8 以後（但 5.8 以前的版本無法使用 [9]～[10]）

## See Also

- FSIZE
- GETTIME
