# 複雑な _in_ チェック

## 概要

ゴーストのトーク判定などで、文字列に何かが含まれているかどうかを複雑な条件で判定するための関数。

`_in_` 演算子は1つの文字列が含まれるかどうかしか調べられないが、この関数を使うと AND・OR・否定を組み合わせた条件をまとめて書ける。

（文責：浮子屋）

## 関数

### InStrCheck

```
InStrCheck(チェック対象文字列, チェック文字列1, チェック文字列2, ...)
```

チェック対象文字列の中にチェック文字列が含まれているかどうかを判定し、条件を満たせば 1、満たさなければ 0 を返す。

- 2つ目以降の引数（チェック文字列）はすべて AND 条件になる
- チェック文字列は `|` で区切れる。区切った場合は OR 条件になる
- チェック文字列の先頭が `!` の場合、「含まれる」「含まれない」の判定が逆になる
- `!` による逆転は、`|` で区切ったあとの各文字列ごとに評価される

## 判定の例

```
// hoge が含まれ、かつ hemo が含まれるか → 1
InStrCheck("hogehemo", "hoge", "hemo")

// hoge が含まれず、かつ hemo が含まれるか → 0
InStrCheck("hogehemo", "!hoge", "hemo")

// hoge が含まれる、または pepe が含まれるか → 1
InStrCheck("hogehemo", "hoge|pepe")

// （hoge が含まれる、または pepe が含まれない）、かつ humu が含まれないか → 1
InStrCheck("hogehemo", "hoge|!pepe", "!humu")
```

## コード

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
//*****************************************************************************
InStrCheck
{
	for _i=1 ; _i<_argc ; _i++ {
		_words=SPLIT(_argv[_i],'|')
		_isHit=0
		foreach _words ; _word {
			_onHit=1
			if SUBSTR(_word,0,1) == '!' {
				_word=SUBSTR(_word,1,STRLEN(_word)-1)
				_onHit=0
			}
			if _word _in_ _argv[0] {
				_isHit=_isHit || _onHit
			}
			else {
				_isHit=_isHit || (1-_onHit)
			}
		}
		if ! _isHit {
			0
			return
		}
	}
	1
}
```

## 使用例

```
OnCommunicate
{
  if InStrCheck(reference[1], "好き|大好き", "!嫌い") {
    "\0\s[1]ありがとう！\e"
  }
}
```

## 関連項目

- [演算（_in_ 演算子）](../grammar/04-arithmetic.md)
- [SPLIT](../functions/SPLIT.md)
- [SUBSTR](../functions/SUBSTR.md)
