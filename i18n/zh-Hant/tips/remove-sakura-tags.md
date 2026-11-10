# 移除 Sakura Script 標籤

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Version4/5 共用版

這個函式會接收包含 Sakura Script 標籤的字串作為引數，並傳回移除 Sakura Script 標籤後的字串。

[查看可直接複製貼上的辭典檔案-1](../attachment/EraseTag1.txt)

試著展開錨點標籤。（**ANCHOR_TOP** 到 **ANCHOR_END** 的部分是新增內容）

[查看可直接複製貼上的辭典檔案-2](../attachment/EraseTag2.txt)

### 僅限 Version5

如果只想簡單地刪除標籤，用這個就行。<br>
不過寫得相當粗略，請不要太過依賴它（喂

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

裡面寫了看不懂的正規表示式，不用在意（喂<br>
如果不需要將 \\\\ 改回 \\（例如之後還要再插入 Sakura Script 中使用），請移除

```
  _text = REPLACE(_text,'\\','\')
```

這一行。

若要避免對跳脫過的標籤產生反應，請使用以下寫法。

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'(?<!\\)\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

### 不移除，而是直接顯示在對話方塊中

- [跳脫 Sakura Script 標籤](escape-sakura-tags.md)

## 附件

- [EraseTag1.txt](../attachment/EraseTag1.txt)
- [EraseTag2.txt](../attachment/EraseTag2.txt)
