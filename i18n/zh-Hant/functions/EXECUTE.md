# EXECUTE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要啟動的檔案或應用程式路徑。相對路徑的可靠性較低，因此建議使用絕對路徑。 |
| option | 傳遞給應用程式的引數（可省略）。用於以瀏覽器開啟 URL 等情況。 |
| dir | 啟動程序的工作目錄（可省略）。相對路徑與 FOPEN 等相同，以 DLL 的載入目錄為基準。省略或指定空字串時，不會設定目錄。YAYA 或 SSP 的目前目錄不會改變。 |

## Returns

- 成功時：大於或等於 0 的整數（依作業系統而異。Windows 中為 ShellExecute 的傳回值，POSIX 環境中為 0）
- 失敗時：-1（也包括 dir 指定的目錄不存在的情況）

## Description

將命令字串傳遞給命令處理器，以啟動外部應用程式或檔案。這是改良自 C 語言 system() 函式的功能，會在不等待應用程式結束的情況下傳回。

## Example

```
_val = EXECUTE('IEXPLORE.EXE','http://www.yahoo.co.jp/')
```

以 Internet Explorer 開啟 Yahoo 首頁。

## Compatibility

- YAYA：從初版開始支援
- Tc604-1：新增第 3 個引數 dir（工作目錄）。新增 POSIX 環境支援（之前一律傳回 -1）

## See Also

- EXECUTE_WAIT
- [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)
