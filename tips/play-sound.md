# 音を鳴らす

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### 基礎編

umeiciさん作のSAORI「MCIAudioR」を利用すると便利です。<br>

MIDIデータをロードする→再生する→演奏を止める、という流れになります。<br>
（mciaudior.dllとaya.dllは同じフォルダにおいてください）<br>

(例)mciaudior.dllと同じフォルダにある、fuga.midを再生する場合<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")
FUNCTIONEX("mciaudior.dll", "play")
```

<br>

### 応用編

ゴーストが会話している最中に効果音を流す場合は、

```
\![raise](ユーザー定義イベントの発生)
```

で呼び出します。<br>

まず、mciaudior.dllを呼び出す関数を作成します。<br>

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

実際に曲を呼び出し、再生する場合。<br>

```
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")　// fuga.midをロード
"\0\s[25]\![raise,OnPlayMusic]fuga.midの演奏中です。\e"
```

再生を止める場合は、マウス反応でOnStopMusicを呼び出すようにしてください。
