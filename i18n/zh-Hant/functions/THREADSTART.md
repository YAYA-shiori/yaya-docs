# THREADSTART
**Category:** スレッド

## Signature
```
THREADSTART( name [, arg ... ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 要在另一個執行緒中執行的使用者自訂函式名稱（字串） |
| arg | 傳遞給函式的引數。可省略。傳遞多個引數時，會依序成為 `_argv[0]`、`_argv[1]`、… |

## Returns
執行緒 ID（1 以上的整數）。無法啟動時會傳回負值。

| 值 | 意義 |
|----|------|
| 1 以上 | 已啟動。之後將此 ID 傳遞給 `THREAD*` 函式 |
| -1 | 沒有該名稱的函式（警告 W0035） |
| -2 | 超過可同時執行的數量（32） |
| -3 | 正在處理 unload，無法建立新的執行緒 |
| -4 | OS 無法建立執行緒 |
| -5 | 此建置版本不支援執行緒（Emscripten） |

引數不足或不是字串時，會發出警告 W0008 / W0009 並傳回 -1。

## Description
在另一個執行緒中執行指定的函式。當你想在與 SSP 通訊（`request`）的同時並行執行耗時處理時，可以使用此函式。呼叫端會立刻返回，不會等待執行緒結束。

```
OnBoot
{
	work.done = 0
	work.id = THREADSTART('Work.Heavy', 1000000)
	'計算を始めました'
}

Work.Heavy
{
	_sum = 0
	for _i = 0; _i < _argv[0]; _i++ {
		_sum += _i
	}
	work.sum = _sum     // 結果はグローバル変数に書いておく
	work.done = 1
}

OnSecondChange
{
	if work.done {
		'計算が終わりました: ' + TOSTR(work.sum)
	}
}
```

取得執行緒結果的方式有 3 種。

- 使用 [THREADRESULT](THREADRESULT.md) 取得函式的傳回值
- 將結果寫入全域變數後結束（如上例）。其他執行緒也會共用全域變數
- 使用 [DIRECTSSTP](DIRECTSSTP.md) 通知 SSP。從工作執行緒呼叫時，等待通訊期間不會停止其他處理

### 運作方式
- **全域變數會共用，區域變數則各自獨立**。執行緒中的函式會有自己的區域變數
- 同一時間只會有一個執行緒執行辭典中的函式。工作執行緒會在每個敘述的間隔輪流讓出執行權，**SSP 傳來的 `request` 會優先執行**。即使工作執行緒正在執行，`request` 也只需等到工作執行緒執行完下一個敘述就會返回。此功能並非透過使用多個 CPU 來加快計算
- **等待外部緩慢回應期間，其他執行緒不會停止**。從工作執行緒呼叫的 [REQUESTLIB](REQUESTLIB.md)（SAORI）、[EXECUTE_WAIT](EXECUTE_WAIT.md)、[EXECUTE_CAPTURE](EXECUTE_CAPTURE.md)、[DIRECTSSTP](DIRECTSSTP.md)、[SLEEP](SLEEP.md) 會在等待期間讓出執行權。[THREADJOIN](THREADJOIN.md) 也相同。若在 SSP 的 `request` 中呼叫 `REQUESTLIB` / `EXECUTE_WAIT`，只要有正在執行的工作執行緒，該執行緒也能在等待期間執行（`SLEEP` 在 `request` 中仍會像以往一樣等待）。除了這些等待情況之外，系統函式（例如大型檔案處理）在單次呼叫結束前，無法讓出執行權或中斷
- 最多可同時執行 32 個執行緒。已結束執行緒的紀錄可透過 [THREADCLOSE](THREADCLOSE.md) 捨棄；超過 256 筆時，則會從最舊的紀錄開始刪除
- 執行緒會使用啟動當下的函式。函式定義（中間碼）由 SSP 傳來的 `request` 和所有執行緒共用。計算運算式時的中間值則會在每次呼叫函式時分別保存，因此，**多個執行緒可以同時執行同一個函式**（遞迴呼叫自己也相同）。啟動執行緒時，不會依照辭典大小消耗額外記憶體或時間；不論同時執行多少個執行緒，增加的資源都只有各執行緒本身使用的部分（在有 2 萬個函式、2.5MB 辭典的情況下，啟動約需 2ms，每個工作執行緒增加的記憶體不到 0.1MB）
- `fncdepth` 和 `looplimit` 的值會沿用啟動時的設定

### 限制
- 工作執行緒執行期間，變更辭典或函式的 [DICLOAD](DICLOAD.md)、[DICUNLOAD](DICUNLOAD.md)、[APPEND_RUNTIME_DIC](APPEND_RUNTIME_DIC.md)、[UNDEFFUNC](UNDEFFUNC.md) 會發出警告 W0032 並失敗。[EVAL](EVAL.md) 可以使用
- 工作執行緒發出的警告或錯誤，會立即寫入檔案，但會等到下一個 `request` 才一次傳送給 SSP 或檢查工具（因為 SHIORI 的回呼必須由呼叫 `request` 的執行緒執行）
- 工作執行緒中的 `GETLASTERROR`、`LSO`、`RE_GETSTR` 等會依執行緒個別保存

### unload 與中斷
收到 `unload` 時，會要求所有正在執行的工作執行緒中斷，並等待最多 5 秒讓它們結束。工作執行緒會在下一個敘述的間隔，以和 `return` 相同的方式離開函式（[SLEEP](SLEEP.md) 的等待會立即返回）。若執行緒仍未結束（例如正在執行耗時的系統函式），則會將強制停止作為最後手段，並發出警告 W0034。Windows 以外的平台無法強制停止，因此會放棄仍在通訊等操作中等待的執行緒並繼續處理（正在執行辭典函式的執行緒則會持續等待，直到該函式結束）。

!!! warning "請勿在工作執行緒中使用會長時間停滯的函式"
    強制停止可能會破壞執行緒中途的狀態。請將耗時處理拆成較小的部分，使用 `for` / `while` 分段執行，或在其中穿插 `SLEEP`。如此一來，就能透過 [THREADSTOP](THREADSTOP.md) 或 `unload` 安全地停止執行緒。

## Example
啟動 2 個執行緒，等待兩者結束，並取得傳回值。

```
Work.Add
{
	_argv[0] + _argv[1]
}

Work.Both
{
	_a = THREADSTART('Work.Add', 1, 2)
	_b = THREADSTART('Work.Add', 10, 20)
	_r = THREADJOIN(_a)
	_r = THREADJOIN(_b)
	TOSTR(THREADRESULT(_a)) + ',' + TOSTR(THREADRESULT(_b))   // 3,30
}
```

## Compatibility
- Tc608-1 以後
- Tc608-2：停止複製各執行緒的函式表，改為由所有執行緒共用（在 Tc608-1 中，使用有 2 萬個函式、2.5MB 的辭典時，啟動約需 18ms，每個工作執行緒約需 13MB）。多個執行緒可以同時執行同一個函式

## See Also
- THREADSTATE
- THREADSTOP
- THREADJOIN
- THREADRESULT
- THREADCLOSE
- SLEEP
- DIRECTSSTP
