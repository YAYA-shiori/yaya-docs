# GETERRORLOG
**Category:** デバッグ

## Signature
```
GETERRORLOG()
```

## Parameters
无

## Returns
错误日志字符串数组（最多 20 条，按时间从新到旧排列）

## Description

获取 YAYA 内部发生的错误和警告日志数组。

- 错误日志的格式与调试工具「玉」及错误日志功能（[基础设置](../grammar/01-basic-settings.md)中的 `log`）输出的内容相同。格式为 `文件名(行号) : error E0022 : 消息`
- 发生词典错误并启用紧急加载功能时，会保留紧急功能运行前的错误日志。可利用这一点在发生异常时输出错误
- 最大日志数可以通过基础设置中的 `maxlognum` 更改（默认值：256）。返回最近的 20 条错误日志

## Example

将错误日志拆分为文件名、行号、类型、代码和消息的示例。

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
- YAYA：Tc555-1 及以后

## See Also
- CLEARERRORLOG
- [基础设置](../grammar/01-basic-settings.md)
