# EXECUTE_CAPTURE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_CAPTURE( path [, option [, dir [, options ]]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要執行檔案的路徑。與 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同，相對路徑的可靠性較低，因此建議使用絕對路徑。也可以指定 PATH 中的命令名稱 |
| option | 傳遞給程式的引數（可省略）。與 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同 |
| dir | 啟動程序的工作目錄（可省略）。與 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同。省略或指定空字串時，不指定目錄 |
| options | 指定行為的雜湊（可省略）。使用 [IHASH](IHASH.md) 建立。使用下表中的索引鍵。省略索引鍵時會採用預設行為 |

### options 的索引鍵

| 索引鍵 | 值 | 意義 |
|------|----|------|
| stdin | 字串 | 傳遞給程式標準輸入的內容。省略時，不傳遞任何內容，並立即表示輸入結束（不會停止持續等待輸入的程式） |
| stderr | `"separate"` / `"merge"` / `"discard"` | 標準錯誤輸出的處理方式。`"separate"`（預設）會將其與標準輸出分開擷取。`"merge"` 會將其合併至標準輸出（依輸出的順序存入 `stdout`，而 `stderr` 為空）。`"discard"` 則會捨棄 |
| timeout | 整數（毫秒） | 若程式未在此時間內結束，便會終止程式並傳回。0（預設）表示不設限 |
| maxsize | 整數（位元組） | `stdout`、`stderr` 各自的上限。超過時會終止程式並傳回。預設為 16777216（16MiB），可指定的最大值為 1073741824 |
| charset | 字元編碼名稱或數值 | 傳遞 `stdin` 字串，以及將 `stdout`、`stderr` 轉換為字串時使用的字元編碼（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。省略或指定空字串時，使用 OS 預設值（Windows 為 ANSI 代碼頁，POSIX 為 UTF-8）。不影響 path、option、dir |

值為 VOID 的索引鍵會視為未指定。

## Returns

具有下列索引鍵的雜湊。

| 索引鍵 | 值 |
|------|----|
| exitcode | 程式的結束代碼。無法確認程式已結束時（`"failed"`，以及程式結束前發生的 `"timeout"` / `"canceled"` / `"truncated"`）為 -1。在 POSIX 環境中，因訊號而結束時也為 -1 |
| stdout | 標準輸出的內容（字串） |
| stderr | 標準錯誤輸出的內容（字串）。`stderr` 選項為 `"merge"` / `"discard"` 時為空 |
| status | 結束方式。請參閱下表 |

| status | 意義 |
|--------|------|
| ok | 程式已結束（即使結束代碼不是 0，也會是 `"ok"`） |
| timeout | 程式未在 `timeout` 指定的時間內結束，因此將其終止 |
| canceled | 因 [THREADSTOP](THREADSTOP.md) 或 unload 而收到中斷執行緒的要求，因此將程式終止 |
| truncated | `stdout` 或 `stderr` 超過 `maxsize`，因此將程式終止。內容會截斷至 `maxsize` |
| failed | 無法啟動（例如找不到執行檔或工作目錄不存在）。引數或選項不正確時也會傳回 `"failed"` |

發生 `timeout` / `canceled` / `truncated` 時，先前已擷取的輸出也會存入 `stdout` / `stderr`。

## Description

啟動外部程式並等待其結束，擷取標準輸出與標準錯誤輸出。也可以傳遞字串至標準輸入。這個函式相當於其他語言中的 `subprocess.run`（Python）、`Open3.capture3`（Ruby）、`execFileSync`（Node.js）。

```
_r = EXECUTE_CAPTURE('cmd.exe', '/c ver')
if _r['status'] == 'ok' && _r['exitcode'] == 0 {
	_r['stdout']
}
```

以下範例將內容傳遞至標準輸入，並接收結果。

```
_in = 'b' + CHR(13,10) + 'a' + CHR(13,10)
_r = EXECUTE_CAPTURE('sort.exe', '', '', IHASH('stdin', _in))
_r['stdout']       // "a" と "b" が並ぶ
```

以下範例會將標準錯誤輸出合併至標準輸出，並在 10 秒後停止等待。

```
_r = EXECUTE_CAPTURE('tool.exe', '--run', '', IHASH('stderr', 'merge', 'timeout', 10000))
```

### 與 EXECUTE_WAIT 的差異

- **不使用殼層關聯**。無法使用預設應用程式開啟文件或 URL（這些用途請使用 [EXECUTE_WAIT](EXECUTE_WAIT.md) 或 [EXECUTE](EXECUTE.md)）。Windows 會直接啟動執行檔（`CreateProcess`），並傳遞以 `"` 括住 `path` 後接上 `option` 的命令列。也可以啟動 `.bat` / `.cmd`，但請勿在 `option` 中混入來自指令碼外部的字串。POSIX 會將命令傳遞給 `/bin/sh -c`。實際存在的檔案會視為單一名稱；若檔案不存在，則會從 PATH 搜尋殼層命令
- 在 Windows 中不會開啟主控台視窗
- 標準輸出與標準錯誤輸出會透過管線接收，因此部分程式的輸出方式（例如緩衝處理）會與連接至終端機時不同
- 不會轉換換行字元。Windows 程式的輸出會維持 `CRLF`
- 輸出包含 NUL（`\0`）時，字串會在該處結束
- 無法啟動時不會發出警告，而會傳回 `status` 為 `"failed"` 的雜湊

### 等待期間的行為

- 等待期間，[THREADSTART](THREADSTART.md) 的執行緒或來自 SSP 的 `request` 不會停止（與 [EXECUTE_WAIT](EXECUTE_WAIT.md) 相同）
- 執行緒因 [THREADSTOP](THREADSTOP.md) 或 unload 而收到中斷要求時，會先**終止程式**，再以 `"canceled"` 傳回。[EXECUTE_WAIT](EXECUTE_WAIT.md) 即使在 Windows 中也會讓啟動的程式繼續執行，但此函式會將其終止。在 POSIX 中也可以中斷
- 終止程式時，POSIX 會一併終止程式所建立的程序群組（包括由 `sh -c` 啟動的子程序）。Windows 則只會終止啟動的程序，不會終止該程序所啟動的其他程序
- 程式結束後，其他程序有時仍會持續占用標準輸出或標準錯誤輸出（例如透過 `start` 或 `&` 啟動的常駐程式）。此時，輸出中斷後 0.5 秒便會停止讀取，並以 `"ok"` 傳回。之後該程序輸出的內容不會被擷取。即使輸出持續不中斷，經過 `timeout` 指定的時間或收到中斷要求時，也會以 `"timeout"` / `"canceled"` 傳回（程式本身已結束，因此會傳回 `exitcode`）
- 寫入標準輸入與讀取標準輸出、標準錯誤輸出會並行進行，因此即使同時處理大量輸入與大量輸出，程式也不會互相等待

### 錯誤

| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 未指定 path | W0008 | 8 |
| path、dir、options 或選項值的型別不正確 | W0009 | 9 |
| `stderr` / `timeout` / `maxsize` / `charset` 的值不正確 | W0012 | 12 |
| 無法將 `stdin` 轉換為指定的字元編碼 | W0027 | 27 |
| 無法將輸出轉換為字串（該輸出會變成空字串） | W0027 | 27 |
| options 中包含未知索引鍵（為了提醒可能有拼字錯誤而發出警告。其他索引鍵仍有效，執行會繼續） | W0012 | 12 |

即使因 path 等值不正確而發出警告，也會傳回 `status` 為 `"failed"` 的雜湊。

## Compatibility

- Tc608-3: 新增

## See Also

- [EXECUTE_WAIT](EXECUTE_WAIT.md)
- [EXECUTE](EXECUTE.md)
- [IHASH](IHASH.md)
- [THREADSTART](THREADSTART.md)
