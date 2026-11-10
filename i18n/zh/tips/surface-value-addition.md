# 增加 Surface 值

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 手动嵌入 Surface 指令的方法

- 例如，想把名为 dressmode 的变量值乘以 100 后加到 surface 编号上时，

请将下面的函数添加到词典中。<br>
不过，使用此函数时，需要将 `\s[n]` 改为 %sf(n)。<br>

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

可以将此方法应用于不使用 OnSurfaceChange 的换装模式等。

- 应用篇

睡衣造型的 surface 编号比通常的 surface 编号大 100，<br>
如果想在夜间 23 点到早上 5 点之间自动换装。<br>

```
sf
{
	_surface = _argv[0]
	if hour >= 23 || hour =< 4 { _surface += 100 }
	"\s[%_surface]"
}
```

（转载自 et cetera. 的论坛）

### 自动转换脚本的方法

无需修改 Sakura Script 即可增加 Surface 值的函数。

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

示例中使用了名为「SurfaceMode」的变量，修改标注为「//这里是转换部分」的那一行中的表达式，还可以实现各种效果。

从 OnTranslate 等事件中调用此函数。<br>

```
OnTranslate
{
  reference0 = sfcnv(reference0);
  reference0
}
```

摘自人格「[そめいよしの](https://hironet.jp/ukagaka/#yoshino)」的词典。
