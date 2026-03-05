# メニューを横一ライン反転

**Source:** Tips/メニューを横一ライン反転

## 概要

メニュー選択肢をバルーンの幅いっぱいに反転表示させることで、選択しやすくする実装方法を説明しています。メニュー項目の後ろに半角空白を補完して、指定バイト数まで埋める `MENUITEM` 関数を定義します。

## コード例

### MENUITEM 関数の定義

```
MENUITEM
{
    _menuitem = _argv[0]
    for _i = GETSTRBYTES(_menuitem) ; _i < 48 ; _i++
    {
        _menuitem += " "
    }
    _menuitem
}
```

メニュー項目の後ろにスペースを補完して48バイトに揃えます。バルーンの幅に合わせて `48` の値を調整してください。

### 実装方法1: 文字列埋め込み（AYA5.7 fix3 以降）

`%(...)` 演算子を使った手抜き構文:

```
OpenMenu
{
    "\0\s[0]"
    --
    "はい、なんでしょうか？"
    --
    "\n\n/
    \q[%(MENUITEM('なんか話して')),AITALK]\n/
    \q[%(MENUITEM('しゃべり頻度を変えて')),TALKINTERVAL]\n/
    \q[%(MENUITEM('コミュニケート')),COMMUNICATEOPEN]\n/
    \q[%(MENUITEM('AIについて')),ABOUTAYA]\n/
    \q[%(MENUITEM('なんでもない')),CANCEL]\e"
}
```

### 実装方法2: セミコロン使用版

```
OpenMenu
{
    "\0\s[0]"
    --
    "はい、なんでしょうか？"
    --
    "\n\n/
    \q[";--;MENUITEM("なんか話して");--;",AITALK]\n/
    \q[";--;MENUITEM("しゃべり頻度を変えて");--;",TALKINTERVAL]\n/
    \q[";--;MENUITEM("コミュニケート");--;",COMMUNICATEOPEN]\n/
    \q[";--;MENUITEM("AIについて");--;",ABOUTAYA]\n/
    \q[";--;MENUITEM("なんでもない");--;",CANCEL]\e"
}
```

### 実装方法3: セミコロン非使用版

```
OpenMenu
{
    "\0\s[0]"
    --
    "はい、なんでしょうか？"
    --
    "\n\n/
    \q["
    --
    MENUITEM("なんか話して")
    --
    ",AITALK]\n/
    \q["
    --
    MENUITEM("しゃべり頻度を変えて")
    --
    ",TALKINTERVAL]\n/
    \q["
    --
    MENUITEM("コミュニケート")
    --
    ",COMMUNICATEOPEN]\n/
    \q["
    --
    MENUITEM("AIについて")
    --
    ",ABOUTAYA]\n/
    \q["
    --
    MENUITEM("なんでもない")
    --
    ",CANCEL]\e"
}
```

## 説明

- `GETSTRBYTES` でメニュー項目のバイト数を計測し、`48` バイトに満たない分を半角空白で補完する
- 変数や関数の結果を連結したい場合は方法2または方法3を使用すること
- `48` の値はバルーンのサイズに合わせて調整する

## 関連項目

- GETSTRBYTES
