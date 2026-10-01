# 複雑な `_in_` チェック

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

ゴーストのトーク判定など、文字列に何かが含まれているかどうかを
複雑な条件で判定するときに。

（文責：浮子屋）

```
//*****************************************************************************
//	InStrCheck
//	対象文字列の中にチェック文字列が含まれているかどうかを
//	複雑な条件によって判定する
//	argv0:		チェック対象文字列
//	argv1以降:	チェック文字列
//	
//	result:0（チェック失敗）または1（チェック合格）
//	
//	・argv1以降の引数はAND条件となる。
//	・チェック文字列は | で分割可能。この場合はOR条件となる。
//	・チェック文字列の先頭が ! の場合、含まれる、含まれないの判定が逆になる
//	・上記逆転は分割後に評価される
//
//	（例）
//		"hogehemo","hoge","hemo"
//		hogehemo の中に hoge が含まれ AND hemo が含まれるかどうか:結果は1
//		
//		"hogehemo","!hoge","hemo"
//		hogehemo の中に hoge が含まれず AND hemo が含まれるかどうか:結果は0
//		
//		"hogehemo","hoge|pepe"
//		hogehemo の中に hoge が含まれ OR pepe が含まれるかどうか:結果は1
//
//		"hogehemo","hoge|!pepe","!humu"
//		hogehemo の中に hoge が含まれ OR pepe が含まれず、
//		かつ humu が含まれないかどうか:結果は1
//
//		
//*****************************************************************************
InStrCheck
{
	for _i=1 ; _i<_argc ; _i++ {
		_words=SPLIT(_argv[_i],'|')
		_isHit=0
		foreach _words ; _word{
			_onHit=1
			if SUBSTR(_word,0,1) == '!' {
				_word=SUBSTR(_word,1,STRLEN(_word)-1)
				_onHit=0
			}
			if _word _in_ _argv[0] {
				_isHit=_isHit || _onHit
			}else{
				_isHit=_isHit || (1-_onHit)
			}
		}
		if ! _isHit {
			0
			return
		}
	}
	1
	return
}
```
