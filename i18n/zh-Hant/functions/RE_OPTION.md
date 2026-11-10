# RE_OPTION
**Category:** 正規表現

## Signature
```
RE_OPTION( オプション文字列 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| 選項字串 | 要設定的 Perl 相容正規表示式選項字串（i, s, m, x）。省略時傳回目前的設定 |

## Returns
表示目前有效選項的字串（i, s, m, x 的組合）

## Description
設定 Perl 相容的正規表示式選項。

支援的選項:
- **i**: 比對時不區分大小寫
- **m**: 將輸入視為多行
- **s**: 讓萬用字元（.）也能比對換行字元
- **x**: 忽略正規表示式模式中的註解（#）與空白

預設為不啟用任何選項（`RE_OPTION("")` 也會回到相同狀態）。不帶引數呼叫時，會以字串傳回目前的選項。

也可以在模式中指定選項（例如 `(?i)abc`）。詳情請參閱[正規表示式](../grammar/14-regular-expressions.md#オプション)。

## Compatibility
- YAYA: Tc534-1 以後

## See Also
- RE_MATCH
- RE_SEARCH
- RE_REPLACE
- [正規表示式](../grammar/14-regular-expressions.md)
