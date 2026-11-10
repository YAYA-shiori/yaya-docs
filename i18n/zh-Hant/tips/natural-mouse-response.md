# 讓滑鼠反應（撫摸反應）更自然

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

OnMouseMove 範例。<br>
當撫摸間隔超過一定時間（此處為 1 秒）時，藉由重設計數器，可以讓撫摸反應更自然。<br>
稍微撫摸一下→撫摸計數累積到接近設定值→游標移開→游標一移回去，計數器就達到設定值並立即觸發撫摸反應，這種情況並不自然。

[OnMouseWheel 也可以用相同方式處理](natural-wheel-response.md)。

（將reference\*寫成`reference[*]`）

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

### 相關 Tips

- [讓滑鼠滾輪反應更自然](natural-wheel-response.md)
