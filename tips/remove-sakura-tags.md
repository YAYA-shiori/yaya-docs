# SAKURAスクリプトタグを取り除く

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### Version4/5共用版

引数にSAKURAスクリプトタグを含む文字列を受け取ると、SAKURAスクリプトタグを取り除いた文字列を返す関数です。

[そのままコピペできる辞書ファイルを見る-1](../attachment/EraseTag1.txt)

アンカータグを展開してみる。（**ANCHOR_TOP**から**ANCHOR_END**の所が追加部分）

[そのままコピペできる辞書ファイルを見る-2](../attachment/EraseTag2.txt)

### Version5のみ

単純にタグを削ってしまいたいだけならこれで済みます。<br>
かなり大雑把なので、あまりあてにしないでください（何

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

謎の正規表現が書いてありますが気にしないでください（何<br>
\\\\を\\に直す必要のない場合（後でまたSakuraScriptの中に挿入して使う場合）は

```
  _text = REPLACE(_text,'\\','\')
```

を抜いてください。

エスケープされたタグに反応しないようにする場合は以下のようにします。

```
RemoveSakuraScript
{
  _text = RE_REPLACE(_argv[0],'(?<!\\)\\_{0,2}[a-zA-Z0-9*!&-](\d|\[("([^"]|\\")+?"|([^\]]|\\\])+?)+?\])?','')
  _text = REPLACE(_text,'\\','\')
  _text
}
```

### 取り除くのではなくそのままバルーンに表示させたい

- [SAKURAスクリプトタグをエスケープする](escape-sakura-tags.md)

## 添付ファイル

- [EraseTag1.txt](../attachment/EraseTag1.txt)
- [EraseTag2.txt](../attachment/EraseTag2.txt)
