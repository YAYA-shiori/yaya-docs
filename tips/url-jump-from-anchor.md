# アンカータグからURLジャンプ

**Source:** Tips/アンカータグからURLジャンプ

## 概要

アンカータグをクリックしたときに、IDが `http://` で始まる場合はブラウザでURLを開く機能の実装方法。RSSの記事タイトルをクリックしてURLジャンプする場合などにも使える。

## アンカータグの記法

```
\_a[URL]表示文字列\_a/
```

## コード例

### OnAnchorSelect / OnAnchorSelectEx

```
OnAnchorSelect
{
  _id = reference[0]
  // アンカーのIDの冒頭に「http://～」があればWebサイトを開く
  if RE_MATCH(_id, 'http://.+') {
    _url = AYATEMPLATE.EscapeText(_id)
    "\C\j[%(_url)] \e"
  // それ以外はIDと同じ名前のイベントへジャンプ
  } elseif ISFUNC(_id) {
    EVAL(_id)
  }
}

OnAnchorSelectEx
{
  _id = reference[1]
  // アンカーのIDの冒頭に「http://～」があればWebサイトを開く
  if RE_MATCH(_id, 'http://.+') {
    _url = AYATEMPLATE.EscapeText(_id)
    "\C\j[%(_url)] \e"
  // それ以外はIDと同じ名前のイベントへジャンプ
  } elseif ISFUNC(_id) {
    EVAL(_id)
  }
}
```

### URLエスケープ用ヘルパー関数

```
AYATEMPLATE.EscapeText
{
  _r = _argv[0]
  if RE_SEARCH(_r,'[,"\[\]]') {
    '"' + REPLACE(_r,'"','""') + '"'
  }
  else {
    _r
  }
}
```

### 使用例

```
sample
{
  "\1\s[10]\0\s[0]/
  文Wikiを開きます。\n\n/
  \_a[http://emily.shillest.net/ayaya/?FrontPage]ここをクリック\_a/
  \e"
}
```

## 説明

- `\C` タグを使うとSSP環境ではバルーン表示のままURLジャンプが可能
- 他のベースウェアではバルーンが空白表示されてからジャンプする
- ツールチップと組み合わせることで、クリック前にジャンプ先URLをユーザーに表示できる

## 関連項目

- マニュアル/関数/RE_MATCH
- マニュアル/関数/ISFUNC
- マニュアル/関数/EVAL
