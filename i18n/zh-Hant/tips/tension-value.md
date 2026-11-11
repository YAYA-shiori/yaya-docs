# 提高或降低緊張度（情緒值）

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

這篇舊版文章（適用於文 Ver.4）已將函式名稱改寫為目前使用的名稱（`SETDELIM` `TOINT` `CHR`）。

根據對話內容提高或降低緊張度（情緒值），<br>
藉此改變角色反應的方法如下。<br>
以下範例中，變數 `tention` 代表情緒值。

```
#define :tention+  %(CHR(1))
#define :tention-  %(CHR(1))-

TalkScript
{
	if tention > 10
	{
		"ハイテンション！"
		"舞い上がってお茶こぼした…\e:tention-5"
	}
	elseif tention > 5
	{
		"普通テンション"
		"阪神勝ったー！\e:tention+5"
	}
	else
	{
		"鬱"
	}
}

OnTalk
{
	_script = TalkScript
	SETDELIM(_script, CHR(1))
	_lastindex = ARRAYSIZE(_script) - 1
	if _lastindex > 0 {
		tention += TOINT(_script[_lastindex])
		_lastlen = STRLEN(_script[_lastindex])
		_eraseindex = STRLEN(_script) - _lastlen - 1
		_erasesize = _lastlen + 1
		_script = ERASE(_script, _eraseindex, _erasesize)
	}
	_script
}
```

請在對話時呼叫 `OnTalk`。<br>
（摘自 et cetera. 的隨筆）

## 原理

`#define` 會取代辭典的原始文字，因此 `\e:tention-5` 在載入時會變成 `\e` 後面接著控制字元 `CHR(1)` 和 `-5` 的字串。`OnTalk` 會以 `CHR(1)` 分割這個字串，將最後一個元素（`-5`）轉換為數值並加到 `tention`，然後移除分隔符及其後的內容，再輸出。

- [SETDELIM](../functions/SETDELIM.md)
- [TOINT](../functions/TOINT.md)
- [ERASE](../functions/ERASE.md)
- [#define](../grammar/08-preprocessor.md#define)
