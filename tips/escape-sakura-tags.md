# SAKURAスクリプトタグをエスケープする

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

- 削除するのではなくそのままバルーンに表示させたい時向け。「`\s[]`0」の場合「\\`\s[0]`」と変換します。
- 基本的に「中身に何が入ってるかわからない」変数をバルーンに表示するときはこの関数を使っておいたほうが安心。

### 全てのさくらスクリプトをエスケープ

- はろーYAYAわーるどやSimpleYAYAテンプレートにある、[Escape～関数](../system/yaya-optional-dic.md)を使用

```
EscapeAllTags( エスケープしたい文字列 )
```

#### 使用例

```
OnGhostChanged
{
_name = EscapeAllTags( reference[0] )
"%(_name)さんから交代したよ～。\e"
}
```

こうすると仮に「青い`\105`のノート」なんて名前のゴーストから交代したとしても、そのまんま「青い`\105`のノートさんから交代したよ～。」とバルーンに表示されるように。

### 危険なさくらスクリプトだけエスケープ

- はろーYAYAわーるどやSimpleYAYAテンプレートにある、[Escape～関数](../system/yaya-optional-dic.md)を使用

```
EscapeDangerousTags( エスケープしたい文字列 )
```

vanishbymyself等の実行されたら困るさくらスクリプトだけエスケープ。
どっかから拾ってきたさくらスクリプト付きトークを実行する時など。

### エスケープじゃなく取り除きたい

- [SAKURAスクリプトタグを取り除く](remove-sakura-tags.md)
