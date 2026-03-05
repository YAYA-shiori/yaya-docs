# エラー処理関数

**Source:** マニュアル/エラー処理関数

## 概要

エラー処理関数は、スクリプト実行中に何かエラーが起きた時に自動的に呼び出されるユーザー関数。

これらの関数は任意実装。辞書に定義しなくてもスクリプトは正常に動作するが、デバッグやユーザー環境でのエラー分析に役立てられる。

## 共通特性

すべてのエラー処理関数は以下の特性を持つ：

- **実装は任意** — エラー処理が不要な場合は辞書に書かなくても良い
- **戻り値は無視** — 戻り値はシステムに無視される
- **`GETCALLSTACK`** 関数を使うと問題箇所を特定できる

## エラー処理関数一覧

| 関数 | 説明 |
|------|------|
| [shiori.OnCallLimit](./shiori-OnCallLimit.md) | 呼び出しの深さが限界に達したとき |
| [shiori.OnLoopLimit](./shiori-OnLoopLimit.md) | ループの反復回数が限界に達したとき |
| [shiori.OnMemoryError](./shiori-OnMemoryError.md) | メモリエラーが発生したとき |
| [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md) | メモリの限界に達したとき |

## 関連

- [GETCALLSTACK](../functions/GETCALLSTACK.md)
