# ツールチップ

**Source:** Tips/ツールチップ

## 概要

Windowsにおいて、マウスポインタの下に適宜表示される小さな説明窓のこと。YAYA/SSP では2種類のツールチップを実装できます。改行には `\n` を使用します。

## コード例

### 1. シェルツールチップ（SSP 2.1.58 以降）

シェルキャラクターの上に表示されるツールチップ。ヒット領域ごとにテキストを定義します。

```
On_tooltip
{
    AYATEMPLATE.MouseEventExec('tooltip')
}

tooltip0Bust
{
    'ここにテキスト'
}

tooltip1Bust
{
    'ここにテキスト'
}

AYATEMPLATE.MouseEventExec
{
    _fname = _argv[0] + TOSTR(reference[3]) + TOSTR(reference[4])
    if ISFUNC(_fname) {
        EVAL(_fname)
        return
    }

    _fname = _argv[0] + TOSTR(reference[3])
    if ISFUNC(_fname) {
        EVAL(_fname)
        return
    }
}
```

- `tooltip[キャラクター番号][ヒット識別子]` : 特定領域のツールチップ
- `tooltip[キャラクター番号]` : 未定義領域のデフォルトツールチップ

### 2. バルーンツールチップ（SSP 2.1.62 以降）

バルーンのメニュー選択肢の上に表示されるツールチップ。

#### 方法A: 選択ID（`reference[1]`）による指定

```
menu {
    "\1\s[10]\0\s[0]/
    \q[何か話して,Talking]\n/
    \q[自己紹介,Profile]\n/
    \q[閉じる,CloseBalloon]\n/
    \e"
}

On_balloon_tooltip {
    if ISFUNC( "BalloonTooltip_%(reference[1])" ) {
        EVAL( "BalloonTooltip_%(reference[1])" )
    }
}

BalloonTooltip_Talking      { "お話します" }
BalloonTooltip_Profile      { "わたしのこと" }
BalloonTooltip_CloseBalloon { "バルーンを閉じます\n（放置しても閉じます）" }
```

#### 方法B: ラベルテキスト（`reference[0]`）による指定

```
On_balloon_tooltip {
    if ISFUNC( "BalloonTooltip_%(reference[0])" ) {
        EVAL( "BalloonTooltip_%(reference[0])" )
    }
}

BalloonTooltip_何か話して { "お話します" }
BalloonTooltip_自己紹介   { "わたしのこと" }
BalloonTooltip_閉じる     { "バルーンを閉じます\n（放置しても閉じます）" }
```

> **注意:** ラベルに `!`, `@`, `[`, `]` などの特殊文字が含まれる場合は、文字の除去や全角への変換などのワークアラウンドが必要です。

### 3. URLのツールチップ表示

選択肢がURLの場合に移動先を表示する応用例:

```
On_balloon_tooltip {
    if ISFUNC( "BalloonTooltip_%(reference[0])" ) {
        EVAL( "BalloonTooltip_%(reference[0])" )
    }
    else {
        if RE_MATCH( reference[0], 'http://.+' ) {
            "以下のURLをブラウザで開きます\n%(reference[0])"
        }
    }
}
```

## 説明

| 種別 | 互換性 | 表示位置 | イベント |
|------|--------|----------|----------|
| シェルツールチップ | SSP 2.1.58+ | シェルキャラクターの上 | `On_tooltip` |
| バルーンツールチップ | SSP 2.1.62+ | バルーンメニューの上 | `On_balloon_tooltip` |

## 関連項目

- ISFUNC
- EVAL
- RE_MATCH
