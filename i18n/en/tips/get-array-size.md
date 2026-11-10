# Get the Number of Array Elements

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

```
i = ("A","B","C")
j = ARRAYSIZE(i)
```

This gives the number of elements, 3, in j.

Also, in Bun5, there is a function called ANY that can extract one random element from an array. (Mikage Sawatari)

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

Gets the number of elements in the passed array.<br>
I use it when using words that users have taught me, for example,<br>
to specify a random number range. (silky)
