# yaya_optional.dic

**Source:** システム辞書/yaya_optional.dic

## 概要

`yaya_optional.dic` は SHIORI3 フレームワーク操作のためのユーティリティ関数を含む YAYA システム辞書。SAKURAスクリプトタグの操作、ゴーストの検出、FMO（フレームメモリオブジェクト）テーブル管理の4つの主要機能を提供する。

## 関数一覧

### SHIORI3FW.EscapeDangerousTags

文字列内の危険なSAKURAスクリプトタグを無効化する。

```
SHIORI3FW.EscapeDangerousTags(script)
```

**危険と判定されるタグ:**
- `\![tag]` の中の: updatebymyself, vanishbymyself, enter/passivemode, leave/passivemode, lock/repaint, unlock/repaint, biff, open/browser, open/mailer, raise
- `\j[]` タグ

戻り値: 無効化された文字列

---

### SHIORI3FW.EscapeAllTags

すべての SAKURAスクリプトタグ（`\` で始まるもの）を無効化する。

```
SHIORI3FW.EscapeAllTags(script)
```

戻り値: エスケープされた文字列

---

### SHIORI3FW.IsGhostExist

指定名のゴーストが FMO 経由で現在起動しているか確認する。

```
SHIORI3FW.IsGhostExist(name [, fmoname])
```

| 引数 | 説明 |
|------|------|
| name | ゴースト名（`\0name`） |
| fmoname | FMO名（省略時デフォルト: "Sakura"） |

戻り値: 起動中なら `1`、起動していなければ `0`

内部で RefreshFMOTable を呼び出す。

---

### SHIORI3FW.RefreshFMOTable

FMOデータを処理し、リアルタイムのゴースト情報を取得するための文字列配列を生成する。

```
SHIORI3FW.RefreshFMOTable([fmoname [, hwnd]])
```

| 引数 | 説明 |
|------|------|
| fmoname | FMO名（省略時デフォルト: "Sakura"） |
| hwnd | 除外するウィンドウハンドル（省略時: sakurahwnd変数） |

#### 生成されるグローバル変数

**SHIORI3FW.FMOTable**（簡易配列形式）

```
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
```

フィールド: `id`（ゴーストID）、`name`（\0名）、`keroname`（\1名）、`hwnd`（\0ウィンドウハンドル）、`kerohwnd`（\1ウィンドウハンドル）、`path`（インストールディレクトリ）、`ghostpath`（ベースディレクトリ）

**SHIORI3FW.SakuraNameList**（汎用配列）

FMOTableから抽出した `\0名` 一覧。ランダムに起動中ゴーストを選ぶなどの操作に使える。

**注意:** デフォルトでは自分自身の情報は除外される。自分を含めるには `hwnd=-1` を指定する。

## 関連

- [yaya_shiori3.dic](./yaya-shiori3-dic.md)
