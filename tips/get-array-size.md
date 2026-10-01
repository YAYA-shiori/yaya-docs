# 配列の要素数を取得

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

```
i = ("A","B","C")
j = ARRAYSIZE(i)
```

で j に要素数の 3 が得られます．

また，文5には，ANYという関数があり，配列の要素のうちランダムな１つを取り出すことが出来ます．(沢渡 みかげ)

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

渡された配列の要素数を取得します。<br>
私の場合は、ユーザーさんから教わった単語を使う時に、<br>
乱数の範囲指定とかに使ったりしてます。(silky)
