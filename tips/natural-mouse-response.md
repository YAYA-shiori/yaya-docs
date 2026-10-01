# マウス反応（なで反応）を自然なものにする

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

OnMouseMoveの例。<br>
撫で間隔が一定の時間(ここでは1秒)以上開いたときにカウンタをリセットすることによって、撫で反応をより自然なものにできます。<br>
ちょっと撫でる→撫でカウントが設定値ギリギリまで溜まる→カーソル外れる→カーソルが乗った瞬間カウンタが設定値に達し、瞬時に撫で反応発動、と言うのは不自然なので。

[OnMouseWheelも同様にして処理できます](natural-wheel-response.md)。

（reference\*を`reference[*]`と書いています）

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

//メイン側の頭なで反応トーク
//（イベント名はMouseReaction[キャラ番号][識別子]）
MouseReaction0Head
{
　　""
}
```

--せきやひろし

### 関連Tips

- [ホイール反応を自然なものにする](natural-wheel-response.md)
