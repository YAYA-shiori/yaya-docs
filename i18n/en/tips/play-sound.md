# Play sounds

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Basics

The SAORI “MCIAudioR” by umeici is useful.<br>

The process is: load the MIDI data → play it → stop playback.<br>
(Place mciaudior.dll and aya.dll in the same folder.)<br>

(Example) To play fuga.mid in the same folder as mciaudior.dll:<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")
FUNCTIONEX("mciaudior.dll", "play")
```

<br>

### Advanced

To play sound effects while the ghost is talking, call it using

```
\![raise](ユーザー定義イベントの発生)
```

.<br>

First, create functions that call mciaudior.dll.<br>

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

To load and play a song:<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")　// fuga.midをロード
"\0\s[25]\![raise,OnPlayMusic]fuga.midの演奏中です。\e"
```

To stop playback, set up a mouse reaction to call OnStopMusic.
