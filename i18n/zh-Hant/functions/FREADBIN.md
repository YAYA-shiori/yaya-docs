# FREADBIN

**Category:** ファイル操作

## Signature

```
FREADBIN( path , size [ , char ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 開啟的檔案名稱 |
| size | 要讀取的位元組數。指定 0 時會讀取整個檔案 |
| char | 取代空位元組（0x00）的字元（省略時使用空格） |

## Returns

- 成功時：讀取到的資料字串
- 到達檔案結尾時：-1
- 失敗時：空字串

不進行字元編碼轉換，直接讀取二進位資料。為避免行尾轉換，建議事先以 FOPEN 指定二進位模式。空位元組（0x00）會以指定的字元取代（這是 YAYA 不允許字串中包含位元組值 0 的限制所致）。若未以二進位存取模式開啟 FOPEN，則會進行換行字元轉換。

## Compatibility

- YAYA：Tc516-901 以後
- 注意：直到 Tc540-3 為止，存在因轉型錯誤導致 0x80 以上的位元組被誤轉換為 0xFF80 範圍值的錯誤

## See Also

- FREAD
- FWRITEBIN
