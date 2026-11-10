# Align Text Width

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Use a monospaced font.<br>
If the text exceeds the specified number of bytes, the excess is removed.<br>
If the text is shorter than the specified number of bytes, the remaining space is filled with spaces.<br>

### Usage

First argument (`_argv[0]`): string<br>
Second argument (`_argv[1]`): number of bytes to align to<br>

```
ARRANGETEXT(文字列,揃えるバイト数)
```

### ARRANGETEXT Function

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
