# テキストの幅を揃える

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

等幅フォントで使用してください。<br>
指定したバイト数をオーバーすればその分テキストを削ります。<br>
指定したバイト数まで足りない場合は余ったスペースを空白で埋めます。<br>

### 使い方

第一引数(`_argv[0]`)　文字列<br>
第二引数(`_argv[1]`)　揃えるバイト数<br>

```
ARRANGETEXT(文字列,揃えるバイト数)
```

### ARRANGETEXT関数

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
