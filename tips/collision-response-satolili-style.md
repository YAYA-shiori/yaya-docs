# 見切れ・重なり反応を里々風に

**Source:** Tips/見切れ・重なり反応を里々風に

## 概要

YAYAで里々スタイルの見切れ・重なりイベント処理を実装する方法を説明します。里々では見切れ・重なり状態でも「多少の間を空けてから」イベントが発生するため、YAYAでもこの自然な動作を再現できます。

タイマー機構を使って5秒の遅延を設けてから反応させることで、即時反応ではなく自然な挙動を実現します。

## コード例

### 実装例1（基本版）

`OnSecondChange`イベント内でタイマー機構を使用します。

```
OnSecondChange {
    // 見切れ処理
    if reference1 == 0 {
        // メインキャラが見切れている
        if mikireflag == 0 {
            mikireflag = 1
            mikiretimer = 5
        }
        elseif mikiretimer > 0 {
            mikiretimer--
        }
        else {
            // 5秒経過で反応
            mikireflag = 0
            "\0\s[0]はみ出てます。\e"
        }
    }
    else {
        mikireflag = 0
        mikiretimer = 0
    }

    // 重なり処理
    if kasanarienable {
        if reference2 == 1 {
            if kasanaritimer > 0 {
                kasanaritimer--
            }
            else {
                kasanarienable = 0
                "\0\s[0]重なってます。\e"
            }
        }
        else {
            kasanaritimer = 5
        }
    }
}
```

### 実装例2（改良版）

配列形式の`reference[1]`・`reference[2]`を使用し、`ISVAR()`関数で変数初期化を確認するより堅牢な構造です。

```
OnSecondChange {
    // 変数の初期化確認
    if !ISVAR(mikiretimer) {
        mikiretimer = 0
        mikireflag = 0
    }

    if reference[1] == 0 {
        if mikireflag == 0 {
            mikireflag = 1
            mikiretimer = 5
        }
        elseif mikiretimer > 0 {
            mikiretimer--
        }
        else {
            mikireflag = 0
            "\0\s[0]はみ出てます。\e"
        }
    }
    else {
        mikireflag = 0
        mikiretimer = 0
    }
}
```

## 説明

主な変数の役割：

| 変数 | 説明 |
|------|------|
| `mikiretimer` | 見切れ検出までの待機時間（5秒） |
| `mikireflag` | 見切れ状態を追跡するフラグ |
| `reference1` / `reference[1]` | メインキャラの表示状態 |
| `kasanaritimer` | 重なり検出用タイマー |
| `kasanarienable` | 重なり反応の有効フラグ |

改良版では`reference[1]`・`reference[2]`の配列形式を使用し、`ISVAR()`で変数の初期化チェックを行うことで、より安全な実装が可能です。

**作者:** 関谷博志
**最終更新:** 2021年2月27日

## 関連項目

- マニュアル/関数/ISVAR
- Tips/高速化
