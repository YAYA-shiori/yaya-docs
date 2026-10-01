# 関数・変数・さくらスクリプトを短縮して書く

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

以下の一行を入れるとそれ以降`reference[*]`を`Ref[*]`と短縮して記述できるようになります。<br>
関数やさくらスクリプトなども同様に置換えできます。

```
#define Ref reference

OnGhostChanged
{
	"\\0\s[0]%(Ref[0])さんから交代。\e"
}
```

書き方は「#define 置換え前テキスト 置換え後テキスト」。<br>
有効範囲は#defineはその次の行から同じ辞書ファイルの終わりまで。<br>
#globaldefineはその次の行から次以降に読み込む辞書ファイル全て（読み込む順番はyaya.txt/aya.txtに記述されてる順）。<br>
#defineが#globaldefineより先に処理されます。<br>
用途に応じて使い分けてください。

OnTranslate内でREPLACE関数で置換えを行うとスクリプト（トーク）をバルーンに表示する直前にスクリプトのみ置換えますが、#defineは辞書を読み込むタイミングで辞書そのものが置換えられます。<br>

### 注意点

<span style="color:Red">辞書に書かれてるテキストは全て置換え対象になるので、使用する場合はなるべく被らなそうなテキストに短縮してください。</span>
