# RESTOREVAR
**Category:** メタ操作・特殊関数

## Signature
```
RESTOREVAR( [ path ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | （可省略）還原來源的檔案名稱。省略時會使用預設檔案名稱（DLL 名稱 + "_variable.cfg"，例如：yaya_variable.cfg） |

## Returns
VOID（沒有傳回值）

## Description
從檔案載入（還原）變數。處理方式與載入時執行的處理相同。可以從指定的檔案還原變數。

檔案格式請參閱 [SAVEVAR](SAVEVAR.md#保存形式)。Tc600-3 之後也可以還原雜湊和巢狀值。以 Tc600-3 之前的版本儲存的檔案也可以直接讀取。

## Compatibility
- YAYA：從初始版本起即可使用
- Tc600-3：開始支援還原雜湊和巢狀值

## See Also
- SAVEVAR
- SERIALIZEVAR
- DESERIALIZEVAR
