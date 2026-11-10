# Surface Value Addition

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### How to embed surface instructions manually

- For example, if you want to add a value 100 times that of the dressmode variable to the surface number,

Add the following function to a dictionary.<br>
However, when using this, you need to change `\s[n]` to %sf(n).<br>

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

This can be used for things like a changing mode that does not use OnSurfaceChange.

- Advanced application

If the surface for pajamas is the normal surface number plus 100, and you want the ghost to change automatically from 11 p.m. to 5 a.m.<br>
In this case:<br>

```
sf
{
	_surface = _argv[0]
	if hour >= 23 || hour =< 4 { _surface += 100 }
	"\s[%_surface]"
}
```

(Reposted from the et cetera. bulletin board)

### How to convert scripts automatically

A function that adds to the surface number while leaving Sakura Script as is.

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

The example uses a variable called "SurfaceMode," but you can do various things by modifying the expression on the line marked "//ここが変換部".

Call this from OnTranslate or another event.<br>

```
OnTranslate
{
  reference0 = sfcnv(reference0);
  reference0
}
```

From the dictionary of the ghost "[Somei Yoshino](https://hironet.jp/ukagaka/#yoshino)".
