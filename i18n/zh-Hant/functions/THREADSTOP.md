# THREADSTOP
**Category:** スレッド

## Signature
```
THREADSTOP( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 傳回的執行緒 ID |

## Returns
| 值 | 意義 |
|----|------|
| 1 | 已要求中斷 |
| 0 | 該執行緒已經結束 |
| -1 | 沒有該 ID 的執行緒 |

引數不足或不是整數時，會發出警告 W0008 / W0009 並傳回 -1。

## Description
要求執行緒中斷。此函式會立即返回，不會等待執行緒結束。若要確認執行緒是否結束，請使用 [THREADSTATE](THREADSTATE.md) 或 [THREADJOIN](THREADJOIN.md)。

執行緒會在下一個敘述的間隔（包含 `while` / `for` 每次迴圈的間隔），以和 `return` 相同的方式離開目前的函式，呼叫端函式也會以相同方式離開，然後執行緒便會結束。正在透過 [SLEEP](SLEEP.md) 或 [THREADJOIN](THREADJOIN.md) 等待的執行緒會中止等待並返回。遭中斷的執行緒狀態會變成 2，[THREADRESULT](THREADRESULT.md) 會傳回空值。

執行系統函式的單次呼叫期間（例如大型正規表示式、`REQUESTLIB` 等）不會停止，必須等該次呼叫結束後才會停止。

## Example
```
OnClose
{
	_r = THREADSTOP(work.id)
	_r = THREADJOIN(work.id, 2000)   // 2 秒まで終わりを待つ
}
```

## Compatibility
- Tc608-1 以後

## See Also
- THREADSTART
- THREADSTATE
- THREADJOIN
- THREADCLOSE
