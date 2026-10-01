# 選択肢をいきなり独立した関数で書く

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

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

こうしておけば、`\q[]`タグや`\_a[]`タグで作られた選択肢／アンカーの識別子そのままの名前で辞書に書くことができます。

### 注意

選択肢／アンカーの識別子がそのまま関数名となるので以下のルールのどれにもあてはまらない識別子名にしてください。

- 数字0～9で始まる。
- アンダースコア（"_"）で始まる。
- 以下の文字を含む。
空白　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　&lt;　=　>　?　@　[　]　`　{　|　}　<br>

- 予約語と完全に一致する。

## 関連ページ

- [切り替え反応もいきなり独立した関数で書く](independent-switch-function.md)
- [アンカータグからURLジャンプ](url-jump-from-anchor.md)
