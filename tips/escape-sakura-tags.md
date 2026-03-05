# SAKURAスクリプトタグをエスケープする

**Source:** Tips/SAKURAスクリプトタグをエスケープする

## 概要

中身に何が入っているかわからない変数をバルーンに表示するとき、SAKURAスクリプトタグをそのまま表示させる（無効化する）方法。「中身に何が入ってるかわからない変数をバルーンに表示するときはこの関数を使っておいた方が安心」とされている。

## 関数

エスケープ関数は `yaya_optional.dic`（はろーYAYAわーるど / SimpleYAYAテンプレート）に収録されている。

### EscapeAllTags

```
EscapeAllTags(エスケープしたい文字列)
```

すべてのSAKURAスクリプトタグを無効化する。

### EscapeDangerousTags

```
EscapeDangerousTags(エスケープしたい文字列)
```

「実行されたら困る」タグ（`vanishbymyself` など）のみを処理する。外部トークンの実行時に推奨。

## コード例

```
OnGhostChanged
{
  _name = EscapeAllTags(reference[0])
  "%(\_name)さんから交代したよ～。\e"
}
```

`reference[0]` には交代前ゴーストの名前が入るが、その名前にSAKURAスクリプトタグが含まれていても安全に表示できる。

## 方針の選択

| 状況 | 推奨関数 |
|------|---------|
| 内容が完全に不明な変数を表示する | `EscapeAllTags` |
| 外部ゴーストや外部トークンのテキストを処理する | `EscapeDangerousTags` |

## 関連項目

- Tips/SAKURAスクリプトタグを取り除く
- システム辞書/yaya_optional.dic
