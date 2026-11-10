# 对齐文本宽度

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/)转载

请在等宽字体中使用。<br>
如果超过指定字节数，则会删去超出的部分。<br>
如果不足指定字节数，则会用空格填补剩余部分。<br>

### 用法

第一个参数（`_argv[0]`）　字符串<br>
第二个参数（`_argv[1]`）　要对齐的字节数<br>

```
ARRANGETEXT(文字列,揃えるバイト数)
```

### ARRANGETEXT 函数

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
