# FREADENCODE

**Category:** ファイル操作

## Signature

```
FREADENCODE(path, size [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPEN 指定的檔案名稱 |
| size | 要讀取的位元組數。指定 0 時會讀取整個檔案 |
| type | 編碼類型。可指定 "base64"、"url" 或 "form"。省略時為 "base64"（詳情請參閱 STRENCODE） |

## Returns

- 成功時：編碼後的字串
- 到達檔案結尾時：-1
- 失敗時：空字串

讀取檔案時同時進行 Base64 或 URL 編碼。若檔案不是以二進位模式開啟，則會套用換行碼轉換。必須先使用 FOPEN 開啟檔案。

## Compatibility

- YAYA：Tc535-1 以後

## See Also

- FREAD
- FREADBIN
- FOPEN
- STRENCODE
