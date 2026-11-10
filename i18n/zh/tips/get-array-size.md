# 获取数组的元素个数

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

```
i = ("A","B","C")
j = ARRAYSIZE(i)
```

这样就能在 j 中获得元素个数 3。

另外，文5中有一个名为 ANY 的函数，可以从数组元素中随机取出一个。(沢渡 みかげ)

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

获取传入数组的元素个数。<br>
我会在使用用户告诉我的单词时，<br>
用它来指定随机数的范围等。(silky)
