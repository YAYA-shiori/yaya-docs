# ホイール反応を自然なものにする

**Source:** Tips/ホイール反応を自然なものにする

## 概要

マウスホイール操作でゴーストのトークが複数回連続で発生する問題を、一定間隔の時間判定を加えることで解決する手法です。

マウスの種類や設定によっては、一回ホイールを回しただけで2〜3回連続してトークが発生してしまう場合があります。`systemuptime` を使って前回の反応からの経過時間を計測し、一定時間（デフォルト1秒）以上経過した場合にのみ反応するようにします。

## コード例

### 基本実装（改善前）

```
OnMouseWheel
{
    if reference[3] == 0 {
        "\0ころころすんな！\e"
    }
}
```

### 改善版（インターバル制御あり）

```
OnMouseWheel
{
    _wheel_interval = systemuptime - wheel_prev
    if _wheel_interval > 1 {
        wheel_prev = systemuptime
        if reference[3] == 0 {
            "\0ころころすんな！\e"
        }
    }
}

OnGhostUnload
{
    ERASEVAR('wheel_prev')
}
```

## 説明

- `systemuptime` : システム起動からの経過時間（秒）
- `wheel_prev` : 前回ホイール反応を実行した時刻を記録するグローバル変数
- `_wheel_interval > 1` の `1` は秒数。好みに応じて調整可能
- `reference[3]` : ホイールの回転方向（0 = 下向き、1 = 上向き）
- `OnGhostUnload` で `wheel_prev` 変数を削除する処理が必須

## 関連項目

- Tips/マウス反応（なで反応）を自然なものにする
- ERASEVAR
