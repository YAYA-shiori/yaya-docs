# GETERRORLOG
**Category:** デバッグ

## Signature
```
GETERRORLOG()
```

## Parameters
無

## Returns
錯誤記錄的字串陣列（最多 20 筆，依新到舊排列）

## Description

取得 YAYA 內部發生的錯誤與警告記錄陣列。

- 錯誤記錄的格式與偵錯工具「玉」及錯誤記錄功能（[基礎設定](../grammar/01-basic-settings.md)的 `log`）輸出的內容相同，格式為 `檔案名稱(行號) : error E0022 : 訊息`
- 發生辭典錯誤而啟動緊急載入功能時，會保留緊急功能啟動前的錯誤記錄。可利用此功能在發生異常時輸出錯誤
- 錯誤記錄的最大筆數可透過基礎設定的 `maxlognum` 變更（預設值：256）。傳回的內容最多為最近的 20 筆錯誤記錄

## Example

以下範例會將錯誤記錄拆解為檔案名稱、行號、類型、代碼和訊息。

```
ErrorList.SPLIT{
	_L=SPLIT(RE_REPLACEEX(_argv[0],'\((\d+|-)\) : ',',$1,'),',',3)
	//("E:\ssp\ghost\Taromati2\ghost\master\dic\system\ERRORLOG.dic","17","error E0041 : 'for'のループ式が異常です.")
	_L[2]=SPLIT(RE_REPLACEEX(_L[2],' *([WEN])(\d+|-)( *: |：)',',$1,$2,'),',',4)
	//("E:\ssp\ghost\Taromati2\ghost\master\dic\system\ERRORLOG.dic","17","error","E","0041","'for'のループ式が異常です.")
	_L
}
ErrorList.Gene{
	ErrorList.filename=IARRAY
	ErrorList.linenum=IARRAY
	ErrorList.type=IARRAY
	ErrorList.typecode=IARRAY
	ErrorList.code=IARRAY
	ErrorList.Info=IARRAY
	_l=GETERRORLOG
	foreach _l;_i{
		_t=ErrorList.SPLIT(_i)
		ErrorList.filename,=_t[0]
		ErrorList.linenum,=TOINT(_t[1])
		ErrorList.type,=_t[2]
		ErrorList.typecode,=_t[3]
		ErrorList.code,=TOINT(_t[4])
		ErrorList.Info,=_t[5]
	}
}
ClearErrorListVar{
	ERASEALLVARBEGINAS('ErrorList.')
}
```

## Compatibility
- YAYA：Tc555-1 之後

## See Also
- CLEARERRORLOG
- [基礎設定](../grammar/01-basic-settings.md)
