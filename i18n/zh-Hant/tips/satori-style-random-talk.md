# 寫出 Satori 風格的隨機對話

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 用 Satori 風格簡單地撰寫隨機對話＠AYA5

作者是＠ちに。

辭典：[satori_for_aya.dic](http://mistnar.hp.infoseek.co.jp/ukagaka/ayav_text/satori_for_aya.dic)

<span style="color:Red">※此處直接將 OnChoiceSelect 的選項寫成獨立函式。請參閱[將選項直接寫成獨立函式](independent-choice-function.md)。</span>

### 不太容易理解的說明

可以在 AYA 辭典中使用 Satori 風格的指令碼。<br>
不過，基本上它當然還是 AYA，請不要弄錯這一點。

### 使用方法

將 aya_aitalk.dic 中的

```
OnAiTalk
```

部分的

```
RandomTalk
```

改寫成

```
OnAiTalk.Satori
```

或是加上這段，就能運作。<br>
對話內容請寫在這份辭典的

```
RandomTalk.Satori
```

之中。<br>
Satori 風格指令碼僅在這個函式內有效。

### 支援的標籤

```
（サーフィス番号）
：
＠
＞
＿
```

以上就是支援的標籤。順帶一提，＠ 和 ＞ 的處理完全相同，因此使用哪個都可以。<br>
像（＿あそぶ）這樣寫，效果等同於 `\_q[あそぶ,＿あそぶ]`。

其他範例請看下方的 "RandomTalk.Satori"。

### 想用玉試試看

```
GET SHIORI/3.0
ID: OnAiTalk.Satori
Sender: CallAIMist
SecurityLevel: local
Charset: Shift_JIS
```

以上，請直接複製貼上。

### 注意事項

我沒有處理錯誤。<br>
如果不能運作，抱歉。（尤其是沒有測試＿標籤(ﾟ∀ﾟ)
