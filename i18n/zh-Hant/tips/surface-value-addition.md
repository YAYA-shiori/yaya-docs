# Surface 值加算

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 手動嵌入 Surface 指示的方法

- 例如，想要將 dressmode 這個變數的 100 倍加到 surface 編號上時，

請將下方的函式新增至辭典中。<br>
不過，使用時必須將 `\s[n]` 改成 %sf(n)。<br>

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

可應用於不使用 OnSurfaceChange 的換裝模式等情況。

- 應用篇

如果睡衣造型的 surface 編號是一般 surface 編號加上 100，<br>
且想要在凌晨 23 時到早上 5 時之間自動換裝。<br>

```
sf
{
	_surface = _argv[0]
	if hour >= 23 || hour =< 4 { _surface += 100 }
	"\s[%_surface]"
}
```

（轉載自 et cetera. 的留言板）

### 自動轉換指令碼的方法

保持 Sakura Script 原樣並加算 Surface 值的函式。

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

範例中使用了「SurfaceMode」這個變數；修改標示為「//ここが変換部」那一行的運算式，就能實現各種不同的效果。

從 OnTranslate 等事件中呼叫此函式。<br>

```
OnTranslate
{
  reference0 = sfcnv(reference0);
  reference0
}
```

摘自人格「[染井吉野](https://hironet.jp/ukagaka/#yoshino)」的辭典。
