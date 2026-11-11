# SPLIT
**Category:** 文字列操作

## Signature
```
SPLIT(src, delim [, max])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 要分割的字串（建議先使用 TOSTR 將數值變數轉換後再傳入） |
| delim | 分隔字串 |
| max | 最大分割數（省略或指定為 0 時會完整分割） |

## Returns
- 成功時：包含分割後字串元素的通用陣列
- 失敗時：空陣列

## Description
分割字串並以通用陣列傳回。由於不會進行正規表示式處理，因此比 RE_SPLIT 更快速。

指定 `max` 時，會在分割到該數量後停止，並將剩餘部分合併至最後一個元素。將 `max` 指定為 1 時不會分割，只會進行一般的字串指派。

## Example
```
_array = SPLIT("A//B//C//D//E", "//", 3)
// 結果: ("A", "B", "C//D//E")
```

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 以後

## See Also
- RE_SPLIT（使用正規表示式分割）
