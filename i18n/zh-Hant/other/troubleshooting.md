# 遇到問題時的處理方式

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

開發相關的問題請至伺か開發論壇 <http://ghost.sakura.tv/fluxbb/viewforum.php?id=4>
提問

### 執行速度很慢

是否忘了關閉記錄執行日誌的設定？<br>
請重新檢查對話設定檔 aya.txt。<br>

或者，是否在「`***_shiori3.dic`」中設定了「取得已安裝的人格清單」？<br>
請試著減少取得的最大數量。如果完全不使用人格清單，設為 0 也沒問題。<br>

### 有時能選擇選項，有時不能

可能是某處忘了關閉 {}。<br>

### 選擇選項後只會說「1」。

如果是 YAYA 版本 5.0～5.2 以前的版本，OnChoiceSelect 中指定的函式可能包含以下字元。

```
(　)　[　]　!　++　--　*　/　%　+　-　&　==　!=　<=　>=　<　>　_in_　!_in_
&&　||　=　:=　+=　-=　*=　/=　%=　+:=　-:=　*:=　/:=　%:=　,=
```

只要修改函式名稱，避免包含上述字元，就可能恢復正常運作。<br>
（摘自 [:::et cetera. - bbs](http://umeici.hp.infoseek.co.jp/bbs2.html)）。

### 對話中混入奇怪的「0」或「1」

指派變數時，是否把「i = 1」寫成了「i == 1」？

### 不再播放隨機對話

可能是刪除了 OnSecondChange。<br>
如果刪除了它，就不會呼叫 OnAiTalk。<br>
如果 OnSecondChange 不需要執行任何動作，請<br>

```
OnSecondChange{}
```

這樣寫。（摘自 [SatisFactory](http://www5d.biglobe.ne.jp/~satis/) 的雜記）<br>

### 無法正常啟動

很可能是腳本有語法錯誤。<br>
如果是 YAYA 版本 5，使用 YAYA 版本 5 公開頁面上的語法檢查工具「玉」，就能找出大部分的語法錯誤。

[使用玉檢查辭典錯誤](../tips/tama-error-check.md)

容易犯的錯誤範例。

- 忘記關閉 ' ' 或 " "
- 在 ' ' 中使用了 '，或在 " " 中使用了 "
  - %(CHR(0x22)) = " / %(CHR(0x27)) = '。請善加利用。
- 把 elseif 寫成 else if
- 沒有寫 if，就直接從 elseif 開始
- ( ) 或 { } 太多或太少
  - 請尋找能檢查括號是否配對的文字編輯軟體（編輯器）
- 變數名稱、函式名稱的大小寫
- 嘗試使用從未用過的變數
  - 參照從未使用過的變數不會發生錯誤。
- 辭典的字元編碼錯誤
  - 僅限使用 UTF-8 辭典的情況。當然，如果用 ShiftJIS 編寫，就會被大量莫名其妙的錯誤搞得焦頭爛額；反過來也是一樣。

### 辭典中的特定函式全部都出現「引數型別不正確」錯誤

使用函式時，如果應該輸入數值型引數的地方輸入了字串型引數，或反過來，就可能連正確記述的函式也一起出現錯誤。

即使只是「可能會傳入非數值型或非字串型的引數」，有時也會出錯。請善加利用 TOINT 或 TOSTR。<br>

- 範例

```
i = TOSTR( i )
REPLACE( i , "abc" , "bca" )
```

### 執行 SAORI 時凍結

可能是路徑的寫法有問題。<br>
請寫成 "saori`\xxx`.dll"，而不要寫成 "saori\\`\xxx`.dll" 或 "saori/xxx.dll"。

### 想在 Sakura Script 的 [] 中記述「]」。

請用 "" 括住整個字串。<br>
在「"」括住的內容中，若要寫入「"」，請寫成「""」。

```
_txt=REPLACE(テキスト,'"','""')
_txt='"' + _txt + '"'
"\![open,input,ID,-1,%(_txt)]"
```

可以先準備一個方便使用的函式。

```
ESCAPE_TEXT
{
	_r = _argv[0]
	if RE_SEARCH(_r,'["\[\]]') >= 0 {
		'"' + REPLACE(_r,'"','""') + '"'
	}
	else {
		_r
	}
}
```

將它寫在某處，

```
ESCAPE_TEXT(テキスト)
```

這樣應該就能正常運作。

### 發布人格時，不知道要刪除哪些檔案

如果 ghost`\master` 中有以下檔案，請將它們移除。
（\*\*\* 中的字串會依人格的設定而異）

```
***_variable.cfg　（セーブデータ）
***.log　（AYA/YAYA実行ログ）
ssp_shiori_log.txt （SSP実行ログ）
「profile」フォルダまるごと
「var」フォルダまるごと
tama.exe
aycencode.exe
暗号化前の***.dic （※辞書の暗号化をしている場合）
```
