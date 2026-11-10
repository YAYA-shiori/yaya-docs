# 播放声音

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 基础篇

使用 umeici 制作的 SAORI「MCIAudioR」会很方便。<br>

流程是加载 MIDI 数据 → 播放 → 停止演奏。<br>
（请将 mciaudior.dll 和 aya.dll 放在同一个文件夹中）<br>

（示例）播放与 mciaudior.dll 位于同一文件夹中的 fuga.mid<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")
FUNCTIONEX("mciaudior.dll", "play")
```

<br>

### 进阶篇

如果要在人格对话期间播放音效，

```
\![raise](ユーザー定義イベントの発生)
```

可通过上述方式调用。<br>

首先，创建一个用于调用 mciaudior.dll 的函数。<br>

```
OnPlayMusic // （データ再生用の関数）
{
　FUNCTIONEX("mciaudio.dll", "play")
}

OnStopMusic // （再生停止用の関数）
{
　FUNCTIONEX("mciaudio.dll", "stop")
}
```

实际调用并播放曲目时。<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")　// fuga.midをロード
"\0\s[25]\![raise,OnPlayMusic]fuga.midの演奏中です。\e"
```

要停止播放，请设置为通过鼠标响应调用 OnStopMusic。
