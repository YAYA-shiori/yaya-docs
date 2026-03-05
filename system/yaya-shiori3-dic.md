# yaya_shiori3.dic

**Source:** システム辞書/yaya_shiori3.dic

## 概要

`yaya_shiori3.dic` は YAYA ベースのゴーストに核心機能を提供する基本システム辞書。

## コア機能

### SHIORIイベント処理
SHIORI/3.0 プロトコルメッセージをベースウェアから受け取り、イベントIDを対応する関数にマッピングする。グローバル変数 `basewarename`、`sender`、`status`、`Reference` 配列を管理する。

### ランダムトークシステム
一定間隔（`aitalkinterval`）で呼び出される `OnAiTalk` 関数を実装。ベースウェアのサポートなしに自動AIトークが可能。

### 内部トランスレータ
すべてのイベント出力を送信前に処理する `OnTranslateInternal` 関数。セリフ全体に均一なテキスト変換を適用できる。

### チェーンダイアログ
`:chain=識別子` 構文でダイアログシーケンスを連鎖させ、ランダム選択ではなく連続した対話を実現する。

### 遅延評価
`:eval=式` 構文で遅延コード実行を行える（デフォルトではセキュリティのため無効）。

## 配列操作ユーティリティ関数

| 関数 | 説明 |
|------|------|
| `JOIN` | 配列要素をセパレータで連結 |
| `REVERSE` | 要素の順序を逆にする |
| `UNIQUE` | 重複エントリを削除 |
| `SPLITEX` | 空要素を除いた高度な文字列分割 |
| `MAX` / `MIN` | 最大値・最小値を取得（MINは文字列の辞書順にも対応） |
| `AVERAGE` | 数値の平均を計算 |

## システム変数

### 時間変数
`year`、`month`、`day`、`weekday`、`hour`、`minute`、`second`、`systemuptime`、`ghostupmin`

### メモリ変数
`memoryload`、`memorytotalphys`、`memoryavailphys`

### センダー変数
`basewarenameex`、`basewarename`、`sender`

## SAORI連携

`FUNCTIONEX` 関数でSAORI DLLの呼び出しを自動ロード・アンロードで簡略化できる。
構文: `FUNCTIONEX(dllname, Argument0, ...)` - 結果は `valueex` 変数に格納される。

## 関連

- [yaya_optional.dic](./yaya-optional-dic.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
