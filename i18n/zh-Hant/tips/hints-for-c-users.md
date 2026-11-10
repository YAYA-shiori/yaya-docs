# 給 C 語言使用者的提示

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 這篇文章是什麼？

AYA 是一種 SHIORI，具有以 C-like 整理的語法、簡單（層次較薄）的規格，<br>
以及強大的程式設計能力等特點，因此 C 系語言的使用者即使幾乎不看手冊，<br>
也能直接使用。

然而，這些特點反而可能帶來意想不到的陷阱。

簡而言之，這是我過去失敗經驗的筆記。<br>
其中大部分只要確實閱讀手冊就能避免……

（撰文：浮子屋）

<span style="color:Red">※以下內容是針對 AYA5 撰寫的。有些項目可能不適用於 YAYA。</span>

## 最基本的基本

- 函式的傳回值會從此前輸出的候選項目中選出。
- 因此，若因某些錯誤而讓空字串成為候選項目，就可能造成偶爾什麼也不說等難以發現的錯誤。<span style="color:Red">請注意。</span>
- 若要避免這種情況，可以善用 void 或輸出確定子 --。
- 從 Tc573-1 起，可以使用帶引數的 return，因此能採用與 C 相同的寫法。帶引數的 return 會取代此前的輸出候選項目，所以回傳空字串的錯誤應該會大幅減少。

## 字串展開

- "" 會展開字串中的變數和函式。
- 習慣 C 語言的話，很容易想用 " 撰寫字串常值，但最好記住 ' 才是字串。<span style="color:Red">請注意。</span>
- 不過，內部似乎會在產生中間碼時，將不含 % 的字串當作與 ' 相同的字串常值處理。
- "abc%(hemo)efg" 和寫成 'abc'+EVAL('hemo')+'efg'（大概）幾乎相同。
- 因此，如果是「從許多候選項目中擇一」這類函式，展開所有候選項目是多餘的。
- 選定候選項目後，再使用 EVAL 展開內嵌內容即可。[效能最佳化](optimization.md)
- 除非有特殊理由，否則應使用%()明確指定範圍。只使用%進行名稱最長匹配展開的處理負擔很重。
- "abc%hemoefg" 大概會在產生中間碼時變成 'abc'+"%hemoefg"，執行時則必須解析 "%hemoefg"。

## 變數、運算

- 變數分為全域和區域。區域變數是以 _ 開頭的變數。
- 全域變數會在 SHIORI 載入和卸載時儲存至檔案，並從檔案讀取。
- 因此，不需要保存的全域變數最好使用 ERASEVAR 刪除。
- 變數的初始值是空字串，不是「0 或空字串」。<span style="color:Red">請注意。</span>
- 字串和數值的運算結果，在加法時會是字串，其他運算則會是空字串。
- 因此，若算式中混入不存在的變數，結果就會是字串或空字串。<span style="color:Red">請注意。</span>
- 會持續遞增的變數若一開始沒有以數值初始化，可能會導致意料之外的錯誤。
- 例如，依照上述邏輯，i++ 這段程式碼會變成 "11111" 之類的字串。<span style="color:Red">請注意。</span>
- 不確定變數是否已用數值初始化時，也可以使用 CVINT 強制轉換為數值。
- 區域變數的作用範圍是&color(Red){「只在目前及其更深層的{ }內有效」};。
- 上述規格有時會導致意料之外的錯誤。請看以下程式碼範例。<span style="color:Red">請特別注意。</span>

```
hogehoge{
  // ここに _sum=0 が必要。無いとこの関数の結果は空文字
  for _i=0 ; _i<10 ; _i++ {
    _sum+=_i
  }
  _sum
}
```

- 使用比較運算 == 比較數值和字串時，結果會是假。
- 使用比較運算 == 比較未定義變數和 '' 時，結果會是真。

## 流程控制

- 與 C 語言的 else if 相近的是 elseif。
- 與 C 語言的 switch 相近的不是 switch，而是 case ～ when。
- 使用 for `_i` = 1; `_i` < 11; `_i`++ 這類寫法時，如果寫成 i 而不是 `_i`，通常會造成無限迴圈並凍結。
- 因此，若在迴圈中凍結，請留意是否漏寫 _。這很容易忘記，<span style="color:Red">請注意。</span>

## 人格範本（aya_shiori3.dic）

- OnAiTalk 是 AYA 特有的事件。它會在 OnSecondChange 觸發後，每隔 aitalkinterval 秒從 aya_shiori3.dic 發出通知。
- 鏈結是透過人格的辭典中 OnAiTalk 內的條件分支，以及範本端的 ChainTalk 完成的。
- 因此，若任意改寫人格辭典中的 OnAiTalk，會破壞鏈結機制。
- res_reference0 看起來是普通變數，但只要指定值，就會在範本中將 Reference?: 加入請求回應。
- 也就是說，指定值就會觸發通訊。<span style="color:Red">請注意。</span>
- ghostexlist / ghostexcount 是根據本體的 otherghostname 通知產生，因此可能不精確。
- On_otherghostname 和 On_hwnd 不在 aya_shiori3.dic 中，而是在人格的 `*_string.dic` 中。
- 使用自訂事件時，如果名稱開頭不是「On」，就會自動呼叫前面加上「`On_`」的函式名稱。
- SAORI 的傳回值會轉換成適當的型別後傳回。字串中的位元組值 1 會變成逗號。
- 此時的優先順序為 CVINT→CVREAL→字串。

## 其他

- SAORI 會在首次使用時載入，並在 SHIORI 卸載時卸載。
- 也就是說，若 SSP 啟用了人格快取，SHIORI 會被快取，因此人格結束後，SAORI 也可能不會卸載，<span style="color:Red">請注意。</span>[確保在人格啟動與結束時執行動作](reliable-boot-shutdown.md)
- 人格結束時必須一併結束的 SAORI，需要使用 UNLOADLIB 明確結束（也可以使用 SHIORI3FW.SaoriUnloadAll）。
- 若只用 C 語言的思維來看，很容易忽略函式名稱或變數名稱也能在執行時透過 EVAL 動態組合。
- 若要依照某個變數的值呼叫對應函式，可以使用 EVAL("`func_`%(`_var`)") 這種語法。[將選項直接寫成獨立函式](independent-choice-function.md)
- 若某個變數的值是包含 %() 的字串，之後想展開它時，可以使用 EVAL(CHR(0x22)+`_var`+CHR(0x22)) 這種語法。[效能最佳化](optimization.md)
