# GETERRORLOG
**Category:** デバッグ

## Signature
```
GETERRORLOG()
```

## Parameters
なし

## Returns
エラーログの文字列配列（最大20件、新しいものから順）

## Description

YAYA 内部で起きたエラー・警告のログの配列を取得する。

- エラーログの形式は、デバッグツール「玉」やエラーログ機能（[基礎設定](../grammar/01-basic-settings.md)の `log`）で出力されるものと同じ。`ファイル名(行番号) : error E0022 : メッセージ` の形をしている
- 辞書エラーが起きたときの緊急時読み込み機能が作動した場合は、緊急時機能が動作する前のエラーログが維持される。これを使って、異常時にエラーを出力できる
- ログの最大数は、基礎設定の `maxlognum` で変更できる（デフォルト: 256）。返るのは直近のエラーから 20 個まで

## Example

エラーログを、ファイル名・行番号・種別・コード・メッセージに分解する例。

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
Tc555-1以降

## See Also
- CLEARERRORLOG
- [基礎設定](../grammar/01-basic-settings.md)
