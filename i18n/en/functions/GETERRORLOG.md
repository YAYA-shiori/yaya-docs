# GETERRORLOG
**Category:** デバッグ

## Signature
```
GETERRORLOG()
```

## Parameters
None

## Returns
An array of error log strings (up to 20 entries, in newest-first order)

## Description

Gets an array of logs for errors and warnings that occurred inside YAYA.

- The error log format is the same as the output from the debugging tool "Tama" and the error log feature (`log` in [Basic Settings](../grammar/01-basic-settings.md)). It has the form `filename(line number) : error E0022 : message`
- If the emergency loading feature for dictionary errors is activated, the error log from before the feature ran is retained. This can be used to output errors when an abnormal condition occurs
- The maximum number of logs can be changed with `maxlognum` in Basic Settings (default: 256). Up to 20 of the most recent errors are returned

## Example

An example that splits an error log into a filename, line number, type, code, and message.

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
- YAYA: Tc555-1 and later

## See Also
- CLEARERRORLOG
- [Basic Settings](../grammar/01-basic-settings.md)
