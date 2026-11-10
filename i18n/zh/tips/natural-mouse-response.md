# 让鼠标反应（抚摸反应）更自然

> 转引自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

OnMouseMove的示例。<br>
当抚摸间隔超过一定时间（这里为1秒）时重置计数器，可以让抚摸反应更加自然。<br>
抚摸一小会儿→抚摸计数累积到接近设定值→鼠标移出→鼠标刚移回时计数器就达到设定值，立即触发抚摸反应，这种情况显得不自然。

[OnMouseWheel也可以用同样的方法处理](natural-wheel-response.md)。

（将reference\*写作`reference[*]`）

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

### 相关提示

- [让滚轮反应更自然](natural-wheel-response.md)
