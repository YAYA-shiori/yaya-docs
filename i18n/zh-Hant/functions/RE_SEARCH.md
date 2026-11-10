# RE_SEARCH
**Category:** 正規表現

## Signature
```
RE_SEARCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 搜尋目標字串 |
| regexp | 正規表示式模式 |

## Returns
- **1**: 找到符合的部分時
- **0**: 沒有符合項目時

## Description
檢查要處理的字串中是否有符合正規表示式的部分。若要檢查整個字串是否完全符合，請使用 RE_MATCH。

可使用 RE_GETSTR、RE_GETPOS、RE_GETLEN 取得符合項目的詳細資訊。

## Example
```
if (RE_SEARCH(reference[0], 'こんに?ち[はわ]|今日[はわ]')){
  "こんにちは、%(username)"
}
```

這個範例會在使用者輸入包含「こんにちは」或「こんにちわ」等字詞時回應問候。先用 `\![open,inputbox,OnTalk,0]` 開啟輸入框，就能做出類似對話的效果。當文中含有「こんにちは」「こんにちわ」「こんちは」「こんちわ」「今日は」「今日わ」「コンニチハ」「コンニチワ」其中之一時（例如「こんにちはー、ほにゃらら」），這個範例就會回應（若寫成 `'こんに?ち[はわ]|今日[はわ]|コンニチ[ハワ]'` 的情況）。

提供一個小技巧：若改成下列寫法，當句尾有 `？` 或 `?` 時（例如「元気？」「ハンガーって美味しいよね?」），就會一律回覆「そうかもしれない」，讓對話更容易成立（雖然應該增加回應模式）。

```
if (RE_SEARCH(reference[0], '(？|\?)$')){
    "そうかもしれない"
}
```

## Compatibility
- YAYA: 自初始版本起支援
- Tc606-6: 將正規表示式引擎變更為 uka_regexp（語法接近 PCRE2）。可透過變數或函式解析模式中的子程式呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- RE_MATCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
