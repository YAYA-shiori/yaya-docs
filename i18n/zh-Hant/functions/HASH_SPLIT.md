# HASH_SPLIT
**Category:** ハッシュ操作

## Signature
```
HASH_SPLIT( str, sep1, sep2 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | 要分割的字串 |
| sep1 | 元素的分隔符 |
| sep2 | 鍵與值的分隔符 |

## Returns
雜湊

## Description
使用 `sep1` 將字串分割成多個元素，再使用 `sep2` 將各元素分割成鍵和值，以此建立雜湊。

- 略過空元素
- 不包含 `sep2` 的元素會成為只有鍵的元素（值為 VOID）
- 捨棄鍵為空的元素（例如 `=x`）
- 使用第一個 `sep2` 進行分割。`d=4=5` 會成為鍵 `d`、值 `4=5`
- 當 `sep1` 或 `sep2` 是空字串時，會發出警告 W0010，並傳回空雜湊

## Example
```
_h = HASH_SPLIT("a=1,b=2,,c,=x,d=4=5", ",", "=")
// a=1,b=2,c=,d=4=5 （要素数 4）
```

## Compatibility
- YAYA: Tc600-3 以後

## See Also
- IHASH
- SPLIT
