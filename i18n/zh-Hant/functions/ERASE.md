# ERASE

**Category:** 文字列操作

## Signature

```
ERASE( src, pos, len )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| src | 要刪除的字串 |
| pos | 刪除起始位置（0 表示開頭）。指定負值時，會視為從末尾算起的偏移量。 |
| len | 要刪除的字元數。若超過字串總字元數，則傳回空字串。 |

## Returns

刪除後的字串。若刪除長度超過整個字串，則傳回空字串。

## Description

刪除字串中指定的部分。

## Example

```
_str = 'さくらまゆらねここ'
ERASE( _str, 2, 6 ) // 「さくこ」を返す
```

## Compatibility

- YAYA: 自初版起支援
- AYA: 5.8 以後
- Tc539-3 以後：pos 可以指定負值

## See Also

- ERASEVAR
