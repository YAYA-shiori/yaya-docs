# 轉義 SAKURA 腳本標籤

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

- 適用於不想刪除，而是想讓標籤原樣顯示在對話方塊中的情況。「`\s[]`0」會轉換成「\\`\s[0]`」。
- 基本上，將「不知道裡面會放什麼」的變數顯示在對話方塊中時，最好使用這個函式，以策安全。

### 轉義所有 Sakura Script

- 使用 Hello YAYA World 或 SimpleYAYA 範本中的 [Escape～函式](../system/yaya-optional-dic.md)

```
EscapeAllTags( エスケープしたい文字列 )
```

#### 使用範例

```
OnGhostChanged
{
_name = EscapeAllTags( reference[0] )
"%(_name)さんから交代したよ～。\e"
}
```

如此一來，即使是從名為「青い`\105`のノート」的人格切換過來，對話方塊中也會原樣顯示「青い`\105`のノートさんから交代したよ～。」。

### 只轉義危險的 Sakura Script

- 使用 Hello YAYA World 或 SimpleYAYA 範本中的 [Escape～函式](../system/yaya-optional-dic.md)

```
EscapeDangerousTags( エスケープしたい文字列 )
```

只轉義 vanishbymyself 等執行後會造成困擾的 Sakura Script。
例如執行從某處取得、附有 Sakura Script 的對話時。

### 不想轉義，而是想移除

- [移除 SAKURA 腳本標籤](remove-sakura-tags.md)
