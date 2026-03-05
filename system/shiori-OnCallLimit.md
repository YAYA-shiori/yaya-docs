# shiori.OnCallLimit

**Source:** マニュアル/エラー処理関数/shiori.OnCallLimit

## 概要

呼び出しの深さが限界に達したときに呼び出されるユーザー定義関数。

## Signature

```
shiori.OnCallLimit(_filename_, _linenum_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| _filename_ | エラーが発生した辞書ファイル名 |
| _linenum_ | エラーが発生した行番号 |

## Returns

戻り値はシステムに無視される。

## Notes

- 実装は任意。エラー処理が不要な場合は辞書に書かなくても良い
- `GETCALLSTACK` 関数を使って問題箇所を特定できる

## Compatibility

- YAYA: Tc564-2 以降

## See Also

- [shiori.OnLoopLimit](./shiori-OnLoopLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
