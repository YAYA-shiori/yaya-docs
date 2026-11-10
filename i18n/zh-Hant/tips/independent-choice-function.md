# 直接以獨立函式撰寫各個選項

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

```
 OnChoiceSelect
 {
    if ISFUNC(reference0) {
    EVAL(reference0)
    }
 }
 
 OnAnchorSelect
 {
    if ISFUNC(reference0) {
    EVAL(reference0)
    }
 }
```

如此一來，就能在辭典中使用與 `\q[]` 標籤或 `\_a[]` 標籤所建立的選項／錨點識別碼完全相同的名稱。

### 注意事項

由於選項／錨點的識別碼會直接成為函式名稱，因此請勿使用符合以下任一規則的識別碼名稱。

- 以數字 0～9 開頭。
- 以底線（"_"）開頭。
- 包含以下字元。
空白　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　<　=　>　?　@　[　]　`　{　|　}　<br>

- 與保留字完全相同。

## 相關頁面

- [直接以獨立函式撰寫切換反應](independent-switch-function.md)
- [從錨點標籤跳轉至 URL](url-jump-from-anchor.md)
