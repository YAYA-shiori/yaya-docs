# サーフェス値加算

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### 手動でサーフィス指示を埋め込む方法

- 例えば、dressmodeという代数の100倍の値を、surface番号に追加したい場合、

下の関数を、辞書のなかに追加してください。<br>
ただし、これを使うときは、`\s[n]`を%sf(n)に直す必要があります。<br>

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

OnSurfaceChangeを使わない着替えモード、などに応用できます。

- 応用編

パジャマ姿のsurfaceが、通常surfaceに100を足した数字で、<br>
夜中の23時から朝の5時まで自動的に着替えさせたい場合。<br>

```
sf
{
	_surface = _argv[0]
	if hour >= 23 || hour =< 4 { _surface += 100 }
	"\s[%_surface]"
}
```

（et cetera.の掲示板から転記しました）

### 自動でスクリプトを変換する方法

さくらスクリプトはそのままでサーフィス加算を行う関数。

```
sfcnv
{
  _script = _argv[0];
  _script = REPLACE(_script,"\\",CHR(1));
  
  //_countは捨て変数(余分な出力をしないための措置)
  //YAYAの場合は、RE_GREPの戻りをvoidに突っ込む方がスマートです。
  //その場合、void RE_GREP～のような感じになります(=は不要です)。
  
  _count = RE_GREP(_script,"\\s\[(\d+)\]");
  _grep = RE_GETSTR;
  foreach _grep;_string {
    _count = RE_GREP(_string,"\d+");
    _surface = TOINT(RE_GETSTR[0]);
    if ((_surface < 10)||(19 < _surface)) {	//\1側は変換しない(必要に応じて範囲は変えてください)
       _surface += SurfaceMode * 500; //ここが変換部。この例ではSurfaceModeと言う変数に500を掛けてサーフェス番号に加算している
       _script = REPLACE(_script,_string,"\s[%(_surface)]");
    }
  }
  
  _script = REPLACE(_script,CHR(1),"\\");
  _script;
}
```

例では「SurfaceMode」という変数を使っていますが、「//ここが変換部」と書いてある行の式をいじるといろいろできます。

これをOnTranslateなどから呼び出す。<br>

```
OnTranslate
{
  reference0 = sfcnv(reference0);
  reference0
}
```

ゴースト「[そめいよしの](https://hironet.jp/ukagaka/#yoshino)」の辞書より。
