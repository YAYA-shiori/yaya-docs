# ERASE

**Category:** 文字列操作
**Source:** マニュアル/関数/ERASE

## Signature

```
ERASE( src, pos, len )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| src | 削除対象の文字列 |
| pos | 削除開始位置（0が先頭）。負の値を指定すると末尾からのオフセットとして扱われる。 |
| len | 削除する文字数。文字列の総文字数を超えた場合は空文字列を返す。 |

## Returns

削除後の文字列。削除長が文字列全体を超える場合は空文字列を返す。

## Example

```
_str = 'さくらまゆらねここ'
ERASE( _str, 2, 6 ) // 「さくこ」を返す
```

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降
- Tc539-3以降: pos に負の値を指定できるようになった

## See Also

- ERASEVAR
