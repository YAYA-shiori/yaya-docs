# Making Mouse Responses (Petting Responses) More Natural

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

An OnMouseMove example.<br>
When the interval between petting actions exceeds a certain amount of time (one second here), resetting the counter makes petting responses feel more natural.<br>
It would be unnatural for the counter to build up to just below its threshold after a brief petting, then for the cursor to leave and the counter to reach the threshold the instant the cursor returns, triggering a petting response immediately.

[You can handle OnMouseWheel in the same way](natural-wheel-response.md).

(reference\* is written as `reference[*]`)

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

--Sekiya Hiroshi

### Related Tips

- [Making Wheel Responses More Natural](natural-wheel-response.md)
