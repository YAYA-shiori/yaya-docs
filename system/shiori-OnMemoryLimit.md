# shiori.OnMemoryLimit

**Source:** マニュアル/エラー処理関数/shiori.OnMemoryLimit

## 概要

メモリの限界に達したときに呼び出されるユーザー定義関数。

## Signature

```
shiori.OnMemoryLimit()
```

## Parameters

None

## Returns

戻り値はシステムに無視される。

## Notes

- 実装は任意。エラー処理が不要な場合は辞書に書かなくても良い
- `GETCALLSTACK` 関数を使って問題箇所を特定できる

## Compatibility

- YAYA: Tc567-2 以降

## See Also

- [shiori.OnMemoryError](./shiori-OnMemoryError.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
