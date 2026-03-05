# マウス反応（なで反応）を自然なものにする

**Source:** Tips/マウス反応（なで反応）を自然なものにする

## 概要

マウスの撫で反応をより自然に実装する方法を説明しています。

素のなで反応実装では、「ちょっと撫でる→撫でカウントが設定値ギリギリまで溜まる→カーソルが外れる→カーソルが乗った瞬間にカウンタが設定値に達し、瞬時に撫で反応発動」という不自然な状態が起きます。

**解決策:** 撫で間隔が一定時間（例: 1秒）以上開いたときにカウンタをリセットすることで、自然な反応を実現します。

## コード例

```
OnMouseMove
{
    if reference[4] != "" {
        //----どこかが撫でられている
        if reference[4] == prev_reference4 {
            _nade_interval = systemuptime - nade_prev
            if _nade_interval > 1 {
                //1秒以上間隔が空いたらカウンタをリセット
                stroke = 0
            }
            nade_prev = systemuptime

            stroke++
            //---- 撫でられた量が一定量に達したら「なでられている」と判断
            if stroke >= 96 {
                //---- 撫でられた。撫でられた部位を見てトークする
                EVAL("MouseReaction%(reference[3])%(reference[4])")
                stroke = 0
            }
        }
        else {
            stroke = 0
        }
        prev_reference4 = reference[4]
    }
    else {
        // 定義された部位はどこも撫でられていない
        stroke = 0
    }
}

MouseReaction0Head
{
    ""
}
```

## 説明

- `reference[3]` : キャラクター番号（0 = さくら側, 1 = うにゅう側）
- `reference[4]` : ヒット領域の識別子（撫でられている部位名）
- `stroke` : 撫でカウンター。96 以上で「なでられた」と判定
- `nade_prev` : 前回の撫で時刻（`systemuptime` で記録）
- `prev_reference4` : 前フレームのヒット領域。変わったらカウンタリセット
- `_nade_interval > 1` の `1` は秒数。調整可能
- `MouseReaction[キャラクター番号][ヒット識別子]` の形式でトーク関数を定義する
- 同様の手法は `OnMouseWheel` でも適用可能

## 関連項目

- Tips/ホイール反応を自然なものにする
- EVAL
