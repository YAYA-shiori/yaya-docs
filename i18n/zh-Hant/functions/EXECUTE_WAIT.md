# EXECUTE_WAIT

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_WAIT( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要執行的檔案或應用程式路徑。相對路徑的可靠性較低，因此建議使用絕對路徑。 |
| option | 傳遞給應用程式的引數（可省略）。例如用來在瀏覽器中開啟 URL。 |
| dir | 啟動之處理程序的工作目錄（可省略）。相對路徑與 FOPEN 等相同，以 DLL 的載入目錄為基準。省略或指定空字串時，不指定工作目錄。YAYA 或 SSP 的目前目錄不會改變。 |

## Returns

- 成功時：已執行程序的結束代碼。若將處理交給已啟動的應用程式等情況下沒有可等待的程序，則為 0
- 失敗時：-1（也包括 dir 指定的目錄不存在，或在 POSIX 環境中因訊號而結束的情況）

## Description

將命令字串傳遞給 OS 的命令處理器，以執行外部應用程式或檔案。與 EXECUTE 不同，此函式會等待應用程式結束後才傳回（同步執行）。相當於 C 語言的 system() 函式。

## Example

```
_val = EXECUTE_WAIT('CL.EXE','HELLOWORLD.C')
```

使用 C 編譯器編譯 HELLOWORLD.C，並等待編譯完成。

從 [THREADSTART](THREADSTART.md) 啟動的執行緒呼叫時，即使正在等待外部應用程式結束，來自 SSP 的 `request` 和其他執行緒也不會停止。在 Windows 中，執行緒收到 [THREADSTOP](THREADSTOP.md) 或 `unload` 的中斷要求時，會停止等待並傳回 -1（已啟動的應用程式會繼續執行）。在 POSIX 環境中則會等待至程式結束。

## Compatibility

- YAYA: TC532-1 以後
- Tc604-1: 新增第 3 個引數 dir（工作目錄）。傳回值改為結束代碼（先前 Windows 成功時傳回 1，POSIX 環境則直接傳回 system() 的傳回值）
- Tc608-1: 等待期間可讓其他執行緒執行（存在 `THREADSTART` 啟動的執行緒時）

## See Also

- EXECUTE
- [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)（擷取標準輸出與標準錯誤輸出。也可以傳遞標準輸入）
- THREADSTART
