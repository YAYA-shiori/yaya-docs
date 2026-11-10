# 對齊文字寬度

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

請使用等寬字型。<br>
若超過指定的位元組數，會刪除超出的文字。<br>
若未達指定的位元組數，會以空格填補剩餘部分。<br>

### 使用方式

第一個引數(`_argv[0]`)　字串<br>
第二個引數(`_argv[1]`)　要對齊的位元組數<br>

```
ARRANGETEXT(文字列,揃えるバイト数)
```

### ARRANGETEXT 函式

```
 ARRANGETEXT
 {
 _sb=TOINT(_argv[1])
 _bytes=(GETSTRBYTES(_argv[0],0))
	if _bytes < _sb {
	// 半角空白で埋める
	_space=(_sb-_bytes)
	_val=_argv[0]
	_lp=1
		while _lp <= _space {
		_val=_val+' '
		_lp++
		}
	_val
	}
	elseif _bytes > _sb {
	// 越えていれば削る
	_leng=_sb
	_loop=0
	_text=_argv[0]
	_byte=0
	_c=''
		while _byte<_leng {
			_sub=(SUBSTR((_text),(_loop),1))
			_c=_c+_sub
			_byte=(GETSTRBYTES(_c,0))
			_loop++
				if _loop>200 {break}
		}
	_re=RE_GREP(_c,'.$')
	_re=RE_GETSTR
			if (GETSTRBYTES((_c),0))>_leng {
				_c=(RE_REPLACE(_c,'.$',''))+' '
				_c
			}
			else {_c}
	}
	else {_argv[0]}
 }
```
