# サーフェス値加算

**Source:** Tips/サーフェス値加算

## 概要

サーフェス番号に値を加算する方法を説明しています。時間帯や服装モードなどの変数に応じてサーフェス番号を動的に変更するために使用します。`OnSurfaceChange` を使わずにサーフェス切り替えを実現できます。

## コード例

### 方法1: sf 関数（手動でサーフェス命令を埋め込む）

服装モード変数 `dressmode` の値に応じてサーフェス番号に100単位で加算する例:

```
sf
{
    _surface = _argv[0]
    if TOSTRING2(dressmode) == "" {
        dressmode = 0
    }
    _surface = _surface + dressmode*100
    "\s[%_surface]"
}
```

時間帯に応じてサーフェスを変更する例（23時〜4時はパジャマモード）:

```
sf
{
    _surface = _argv[0]
    if hour >= 23 || hour =< 4 { _surface += 100 }
    "\s[%_surface]"
}
```

### 方法2: sfcnv 関数（既存スクリプトを自動変換）

`OnTranslate` を経由して、スクリプト内のすべてのサーフェス参照を自動変換する方法:

```
sfcnv
{
    _script = _argv[0];
    _script = REPLACE(_script,"\\",CHR(1));

    _count = RE_GREP(_script,"\\s\[(\d+)\]");
    _grep = RE_GETSTR;
    foreach _grep;_string {
        _count = RE_GREP(_string,"\d+");
        _surface = TOINT(RE_GETSTR[0]);
        if ((_surface < 10)||(19 < _surface)) {
            _surface += SurfaceMode * 500;
            _script = REPLACE(_script,_string,"\s[%(_surface)]");
        }
    }

    _script = REPLACE(_script,CHR(1),"\\");
    _script;
}

OnTranslate
{
    reference0 = sfcnv(reference0);
    reference0
}
```

## 説明

- **方法1** は個別のセリフに `%(sf(サーフェス番号))` のように組み込んで使用する
- **方法2** は `OnTranslate` を使ってすべてのスクリプトを自動変換するため、既存コードを変更せずに使える
- `sfcnv` では `\s[0]`〜`\s[19]` の範囲は変換せず、それ以外のサーフェスのみ加算する設計になっている

## 関連項目

- OnTranslate
- RE_GREP
- RE_REPLACE
- REPLACE
