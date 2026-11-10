# 使用玉檢查辭典錯誤

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 使用「玉」檢查辭典錯誤

使用除錯工具「玉」即可輕鬆偵測錯誤。

- [玉改良專案](https://github.com/nikolat/tama)　可從右側的 Releases 下載。
- [「玉」下載網站](http://umeici.onjn.jp/)　可從「tama(debugger for aya)」下載。

### 步驟1

#### 1.啟動玉

請在**啟動人格之前**先啟動玉。

#### 2.啟動人格

如果沒有錯誤，訊息會以驚人的速度大量顯示。<br>
如果有錯誤，則會以紅字顯示相關訊息。

#### 3.查看顯示的錯誤

![Image2.png](../attachment/Image2.png)

橘色代表警告，紅色代表致命錯誤。<br>
橘色的情況下仍可正常運作，但紅色是**會導致人格無法運作的致命錯誤**，因此必須修復。

```
aya_mouse.dic(8) : error E???? ...
```

最左側是發生錯誤的辭典檔案名稱，括號內則表示錯誤位於第幾行。

### 步驟2

#### 1.結束人格

請**結束所有正在開發中的人格等程式**。<br>
「玉」也可以用來顯示執行狀況，因此如果有正在執行的人格，畫面就會以驚人的速度不斷顯示訊息。

#### 2.將 AYA 的 DLL 拖放到玉上

![Image1.png](../attachment/Image1.png)

請拖放 DLL，而不是辭典檔案。

#### 3.查看顯示的錯誤

與步驟1的第3項相同。

### 補充 - 右鍵選單說明

**jump to Top**：捲動到最上方。

**jump to Bottom**：捲動到最下方。

**Copy to clipboard**：將內容複製到剪貼簿。

**receiVe**：~

顯示正在執行的人格的運作狀況。<br>
如果想在保持人格執行的狀態下使用玉進行各種操作，可以取消勾選此項。

**reQuest dialog**：提供進階開發者使用的除錯功能。一般情況下請勿使用（喂

**Reload(unload and load)**：重新載入。若要修改辭典後再次檢查，不必每次都拖放 DLL，直接使用此選單即可。

**Unload**：卸載已載入的 AYA。一般情況下不需要使用。

**eXit(auto unload)**：結束程式。點擊視窗的 × 標記也會執行相同操作。

## 附件

- [Image1.png](../attachment/Image1.png)
- [Image2.png](../attachment/Image2.png)
