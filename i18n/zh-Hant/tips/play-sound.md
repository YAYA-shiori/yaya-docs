# 播放音效

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 基礎篇

使用 umeici 製作的 SAORI「MCIAudioR」會很方便。<br>

流程是載入 MIDI 資料 → 播放 → 停止演奏。<br>
（請將 mciaudior.dll 和 aya.dll 放在同一個資料夾。）<br>

（範例）播放與 mciaudior.dll 放在同一個資料夾中的 fuga.mid 時<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")
FUNCTIONEX("mciaudior.dll", "play")
```

<br>

### 應用篇

若要在人格對話時播放音效，請使用

```
\![raise](ユーザー定義イベントの発生)
```

呼叫。<br>

首先，建立呼叫 mciaudior.dll 的函式。<br>

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

實際呼叫並播放曲目時。<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")　// fuga.midをロード
"\0\s[25]\![raise,OnPlayMusic]fuga.midの演奏中です。\e"
```

若要停止播放，請設定成透過滑鼠反應呼叫 OnStopMusic。
