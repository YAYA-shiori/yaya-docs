# 音を鳴らす

**Source:** Tips/音を鳴らす

## 概要

YAYAでSAORI「MCIAudioR」（作者: umeici）を使って音声・MIDIを再生する方法を説明します。

## 前提条件

`mciaudior.dll`と`aya.dll`を同じフォルダに配置してください。

## 基本的な使い方

### MIDIの読み込みと再生

```
// MIDIデータの読み込み
FUNCTIONEX("mciaudior.dll", "load", "fuga.mid")

// 再生開始
FUNCTIONEX("mciaudior.dll", "play")
```

### 再生停止

```
FUNCTIONEX("mciaudior.dll", "stop")
```

## 応用: トーク中に音を鳴らす

`\\![raise]`コマンドを使って、ゴーストのトーク中にユーザー定義イベントを発火させ、音を再生させます。

### 関数の作成

```
OnPlayMusic {
    FUNCTIONEX("mciaudio.dll", "play")
}

OnStopMusic {
    FUNCTIONEX("mciaudio.dll", "stop")
}
```

### トーク内での使用

```
SomeTalk {
    // MIDIを読み込んでからトークを開始
    FUNCTIONEX("mciaudio.dll", "load", "bgm.mid")
    "\0\s[0]音楽が流れ始めました。\![raise,OnPlayMusic]\e"
}
```

### 停止

マウス操作など適切なタイミングで`OnStopMusic`を呼び出して再生を停止します。

## 説明

`FUNCTIONEX`はSAORI（外部DLL）を呼び出すための関数です。`mciaudior.dll`はWindows MCI（Media Control Interface）を使って音声を再生するSAORIです。

**最終更新:** 2006-12-09

## 関連項目

- マニュアル/関数/FUNCTIONEX
- Tips/高速化
- other/saori-usage
