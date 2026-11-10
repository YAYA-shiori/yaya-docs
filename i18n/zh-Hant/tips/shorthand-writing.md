# 縮寫函式、變數與 Sakura Script

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

加入以下這一行後，就能將`reference[*]`縮寫為`Ref[*]`。<br>
函式或 Sakura Script 等內容也可以用相同方式替換。

```
#define Ref reference

OnGhostChanged
{
	"\\0\s[0]%(Ref[0])さんから交代。\e"
}
```

寫法為「`#define` 替換前文字 替換後文字」。<br>
`#define`的有效範圍是從下一行起，直到同一個辭典檔案結尾。<br>
`#globaldefine`的有效範圍是從下一行起，涵蓋之後載入的所有辭典檔案（載入順序依照 yaya.txt/aya.txt 中的記述）。<br>
`#define`會先於`#globaldefine`處理。<br>
請依用途選擇使用方式。

在 OnTranslate 中使用 REPLACE 函式進行替換時，只會在將指令碼（對話）顯示於對話方塊之前替換指令碼；但使用`#define`時，則會在載入辭典時替換辭典本身。<br>

### 注意事項

<span style="color:Red">辭典中寫入的所有文字都是替換對象，因此使用時請盡量縮寫成不容易與其他文字重複的內容。</span>
