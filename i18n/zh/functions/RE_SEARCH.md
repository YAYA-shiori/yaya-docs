# RE_SEARCH
**Category:** 正規表現

## Signature
```
RE_SEARCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要搜索的字符串 |
| regexp | 正则表达式模式 |

## Returns
- **1**: 找到匹配部分时
- **0**: 未匹配时

## Description
检查要处理的字符串中是否存在与正则表达式匹配的部分。若要检查整个字符串是否完全匹配，请使用 RE_MATCH。

可以通过 RE_GETSTR、RE_GETPOS、RE_GETLEN 获取匹配详情。

## Example
```
if (RE_SEARCH(reference[0], 'こんに?ち[はわ]|今日[はわ]')){
  "こんにちは、%(username)"
}
```

如果用户输入中包含「こんにちは」或「こんにちわ」等内容，就返回问候语的示例。可以先用 `\![open,inputbox,OnTalk,0]` 打开输入框，做出类似对话的效果。此示例会在句中包含「こんにちは」「こんにちわ」「こんちは」「こんちわ」「今日は」「今日わ」「コンニチハ」「コンニチワ」之一时作出反应（例如「こんにちはー、ほにゃらら」等）（如果写作 `'こんに?ち[はわ]|今日[はわ]|コンニチ[ハワ]'`）。

作为一个技巧，如果像下面这样写，那么句末有 `？` 或 `?` 时（例如「元気？」「ハンガーって美味しいよね?」等），就会始终回复「そうかもしれない」，因此更容易让对话接续下去（当然还应增加回复模式）。

```
if (RE_SEARCH(reference[0], '(？|\?)$')){
    "そうかもしれない"
}
```

## Compatibility
- YAYA: 初始版本起支持
- Tc606-6: 正则表达式引擎已更改为 uka_regexp（语法接近 PCRE2）。可以使用变量和函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- RE_MATCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
