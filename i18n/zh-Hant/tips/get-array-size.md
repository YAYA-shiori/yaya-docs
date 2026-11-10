# 取得陣列元素數量

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

```
i = ("A","B","C")
j = ARRAYSIZE(i)
```

如此一來，j 就會取得元素數量 3。

此外，文5有一個名為 ANY 的函式，可以從陣列元素中隨機取出一個。（沢渡 みかげ）

---

```
dim_enum
{
	if _argv[0] != "" {
		len = STRLEN(_argv[0])
		i = 0
		j = 1
		c = ""
		while i < len {
			c = SUBSTR(_argv[0],i,1)
			if c == "," {
				j++
			}
			i++
		}
	}
	else {
		_argv[0] = ""
		j = 0
	}
	j
}
```

取得傳入陣列的元素數量。<br>
我會在使用從使用者那裡學到的單字時，<br>
用它來指定亂數的範圍等。（silky）
