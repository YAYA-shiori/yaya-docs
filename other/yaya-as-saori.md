# YAYA as SAORI

**Source:** YAYA as SAORI

## 概要

Setoriが作成したモジュール。他の SHIORI 実装から `yaya.dll` を SAORI として呼び出し、YAYA の機能を利用できるようにする。デフォルトでは組み込みシステム関数のみが利用可能だが、カスタムモジュールで機能を拡張できる。

## 配布

最新バージョン（2021-10-08）: **yaya_as_saori_2021_10_08.zip**（481.2KB）
GitHub リリースからも追加バージョンを取得可能。

## モジュール開発API

### 引数の取り扱い

SAORIの引数はモジュール内で `REQ.ARGS[*]` 配列に格納される。Argument0 → `REQ.ARGS[0]`。

### 戻り値

- 単一返し: `RES.RESULT` を使用
- 複数返し: `RES.VALUE*` を使用（`RES.VALUE*` は配列ではないため、代入には `EVAL` システム関数を使う）

### エラー処理

実行失敗を示すには数値 `-1` を返す。YAYA as SAORIシステムは `-1` を無効な呼び出しとして扱いエラーを通知する。失敗の記録には `LOGGING` 関数を使用。

### モジュール命名規則

関数は `モジュール名.関数名` パターンに従う。これにより自動ロード・アンロード管理が可能になる。モジュール関数が初めて呼び出されると、YAYA as SAORI は `モジュール名.Load` を検索して実行する。アンロード時には `モジュール名.Unload` が実行される。

## 追加モジュール

- JSONパーサー（オブジェクト的な操作付き）
- カレンダー計算関数
- テキストファイル編集機能
- SSU（Satori SAORI）互換レイヤー
- ゴーストメタデータリーダー（Reta）

## 関連

- [SAORIの使い方](./saori-usage.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
- [LOADLIB](../functions/LOADLIB.md)
