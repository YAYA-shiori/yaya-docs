# shiori.OnCallLimit

## 概要

呼び出しの深さが限界に達したときに呼び出されるユーザー定義関数。

## Signature

```
shiori.OnCallLimit(_filename_, _linenum_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *filename* | エラーが発生した辞書ファイル名 |
| *linenum* | エラーが発生した行番号 |

## Returns

戻り値はシステムに無視される。

## Notes

- 実装は任意。エラー処理が不要な場合は辞書に書かなくても良い
- `GETCALLSTACK` 関数を使って問題箇所を特定できる
- 呼び出しの深さの上限は基礎設定の [`fncdepth`](../grammar/01-basic-settings.md#fncdepth-depth) で変更できる（デフォルト: 32 階層）
- 深さの上限に達していなくても、スタックの残りが少なくなったときはこの関数が呼ばれる（Tc607-4以降）。この関数の実行中にスタックがさらに足りなくなったときは、この関数を呼び直さず、エラーログ（E0097）だけを出して呼び出しを止める

## Compatibility

- YAYA: Tc564-2 以降
- Tc607-4: スタックの残りが少なくなったときも呼ばれるようにした（それまでは `fncdepth` を 0 にすると、ベースウェアごと落ちていた）

## See Also

- [shiori.OnLoopLimit](./shiori-OnLoopLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
