# shiori.OnMemoryError

**Source:** マニュアル/エラー処理関数/shiori.OnMemoryError

## 概要

メモリエラーが発生したときに呼び出されるユーザー定義関数。

## Signature

```
shiori.OnMemoryError()
```

## Parameters

None

## Returns

戻り値はシステムに無視される。

## Notes

- 実装は任意。定義しない場合、システムはエラーログを生成するだけ
- `GETCALLSTACK` 関数を使って問題箇所を特定できる

## Compatibility

- YAYA: Tc567-2 以降

## See Also

- [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
