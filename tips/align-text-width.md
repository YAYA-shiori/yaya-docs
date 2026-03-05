# テキストの幅を揃える

**Source:** Tips/テキストの幅を揃える

## 概要

等幅フォントを使用する環境で、文字列を指定したバイト数に揃える関数 `ARRANGETEXT` の実装例です。指定バイト数を超える場合はテキストを削り、足りない場合は半角空白で埋めます。

## 使い方

```
ARRANGETEXT(文字列, 揃えるバイト数)
```

- 第一引数: 揃える文字列
- 第二引数: 揃えるバイト数

## コード例

```
ARRANGETEXT
{
    _sb = TOINT(_argv[1])
    _bytes = (GETSTRBYTES(_argv[0], 0))
    if _bytes < _sb {
        // 半角空白で埋める
        _space = (_sb - _bytes)
        _val = _argv[0]
        _lp = 1
        while _lp <= _space {
            _val = _val + ' '
            _lp++
        }
        _val
    }
    elseif _bytes > _sb {
        // 越えていれば削る
        _leng = _sb
        _loop = 0
        _text = _argv[0]
        _byte = 0
        _c = ''
        while _byte < _leng {
            _sub = (SUBSTR((_text), (_loop), 1))
            _c = _c + _sub
            _byte = (GETSTRBYTES(_c, 0))
            _loop++
            if _loop > 200 { break }
        }
        _re = RE_GREP(_c, '.$')
        _re = RE_GETSTR
        if (GETSTRBYTES((_c), 0)) > _leng {
            _c = (RE_REPLACE(_c, '.$', '')) + ' '
            _c
        }
        else { _c }
    }
    else { _argv[0] }
}
```

## 説明

- 文字列が指定バイト数より**短い**場合: `while` ループで半角空白 `' '` を末尾に追加
- 文字列が指定バイト数より**長い**場合: 1文字ずつ取り出してバイト数を計測し、超過した時点で切り捨て。マルチバイト文字の途中で切れる場合は代わりに半角空白を補完
- 文字列が指定バイト数と**同じ**場合: そのまま返す
- `GETSTRBYTES` でバイト数を計測、`RE_GREP` と `RE_REPLACE` で正規表現処理を行う
- 等幅フォント環境でのみ正しく機能する

## 関連項目

- GETSTRBYTES
- SUBSTR
- RE_GREP
- RE_REPLACE
