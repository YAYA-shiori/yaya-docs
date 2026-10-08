# yaya_optional.dic

## 概要

`yaya_optional.dic` は、必須ではないがあると便利な、補助的なユーティリティ関数を持つシステム辞書。`shiori3.dic`（[yaya_shiori3.dic](./yaya-shiori3-dic.md)）とともに自動的に読み込まれる。さくらスクリプトタグの操作、文字列の整形、バルーンの初期化、ゴーストの検出（FMO）などの機能を提供する。

## SHIORI3FW.EscapeDangerousTags

```
SHIORI3FW.EscapeDangerousTags( script )
```

文字列中に含まれる「危険な」さくらスクリプトタグを無効化（エスケープ）する。危険な操作を行うタグ（ブラウザ起動・メーラー起動・パッシブモード切り替えなど）のバックスラッシュだけを `\\` にエスケープし、安全なタグはそのまま残る。

「危険」とみなすタグは、現在のところ次のとおり。

- `\![]` の中に、次の文字列を含むタグ: `updatebymyself` / `vanishbymyself` / `enter,passivemode` / `leave,passivemode` / `lock,repaint` / `unlock,repaint` / `biff` / `open,browser` / `open,mailer` / `raise`
- `\j[]` タグ

| 引数 | 説明 |
|------|------|
| `script` | 無効化したい文字列 |

返り値は、無効化された文字列。

```
_safe = SHIORI3FW.EscapeDangerousTags(外部から受け取ったテキスト)
```

## SHIORI3FW.EscapeAllTags

```
SHIORI3FW.EscapeAllTags( script )
```

文字列中に含まれる「すべての」さくらスクリプトタグをエスケープする。`\` で始まるものは何であれエスケープされる。ユーザー入力をそのままバルーンに表示したいときなどに使う。

| 引数 | 説明 |
|------|------|
| `script` | エスケープしたい文字列 |

返り値は、エスケープされた文字列。

```
_display = SHIORI3FW.EscapeAllTags('\0\s[0]これはタグではなくテキストです。\e')
// → "\\0\\s[0]これはタグではなくテキストです。\\e" として表示される
```

[SHIORI3FW.RemoveAllTags](./yaya-shiori3-dic.md#shiori3fwremovealltags) はタグを**削除**するが、こちらはタグを**エスケープして表示**する。

## SHIORI3FW.TranslateSystemChar

```
SHIORI3FW.TranslateSystemChar( text [ , 置換文字 ] )
```

YAYA の演算子・区切り文字など、システム予約文字を指定の文字に置き換える。変数名や識別子として使える安全な文字列を生成したいときに便利。

| 引数 | 説明 |
|------|------|
| `text` | 処理対象のテキスト |
| `置換文字` | 置換後の文字（省略時は `_`） |

```
_varname = SHIORI3FW.TranslateSystemChar('hello world!')
// → "hello_world_"

_varname = SHIORI3FW.TranslateSystemChar('foo/bar', '-')
// → "foo-bar"
```

## 文字列整形

バルーン内メニューなど、表示幅を揃えたいときに使う関数。文字数はすべて**半角換算**（全角 1 文字＝半角 2 文字）で指定する。

| 関数 | 説明 |
|------|------|
| `SHIORI3FW.MakeLongText(テキスト, 文字数)` | テキストが指定の半角換算文字数に満たない場合、末尾にスペースを補って長さを揃える。すでに指定長以上なら元のテキストをそのまま返す |
| `SHIORI3FW.MakeShortText(テキスト, 文字数)` | テキストが指定の半角換算文字数を超える場合、末尾を切り詰めて `...` または `..` を付加する。指定長以内なら元のテキストをそのまま返す |
| `SHIORI3FW.MakeJustText(テキスト, 文字数)` | 上の 2 つを組み合わせて、テキストをちょうど指定の半角換算文字数に整形する |

```
_item  = SHIORI3FW.MakeJustText('設定', 20)
_short = SHIORI3FW.MakeShortText('これはとても長いテキストです', 10)   // "これは..." のように切り詰められる
```

## SHIORI3FW.InitBalloons

```
SHIORI3FW.InitBalloons()
```

現在有効なすべてのスコープのバルーンをクリアする、さくらスクリプトを生成する。マルチスコープ環境で、バルーンをまとめてリセットしたいときに使う。引数はなく、返り値は全スコープの `\p[n]\c\b[-1]` を連結したさくらスクリプト文字列。

```
OnMyEvent
{
	SHIORI3FW.InitBalloons + '\0\s[0]初期化しました。\e'
}
```

## FMO 関連

FMO（File Mapping Object）とは、SSP が管理する「現在起動中のゴーストの情報」の共有メモリ。次の関数を使うと、他のゴーストの存在確認や情報取得ができる。

### SHIORI3FW.IsGhostExist

```
SHIORI3FW.IsGhostExist( name [ , fmoname ] )
```

指定された名前（\0 名）のゴーストが、現在起動しているかを FMO を用いて調べる。FMO を用いるので、この関数を呼んだ瞬間の情報を取得できる。内部で `SHIORI3FW.RefreshFMOTable` を呼ぶ。

| 引数 | 説明 |
|------|------|
| `name` | ゴースト名 |
| `fmoname` | 調べる FMO 名（省略可能。省略すると `Sakura` になる。普通は省略してよい） |

そのゴーストが起動していれば 1、起動していなければ 0 を返す。

```
if SHIORI3FW.IsGhostExist('ゆっくり霊夢') {
	'\0\s[0]霊夢がいるよ！\e'
}
```

### SHIORI3FW.RefreshFMOTable

```
SHIORI3FW.RefreshFMOTable( [ fmoname [ , hwnd ] ] )
```

[READFMO](../functions/READFMO.md) 関数を用いて、FMO を処理しやすい文字列配列として構築する。FMO には「現在起動中の」ゴーストに関する情報が含まれているので、この関数を使うと、起動中のゴーストの情報をリアルタイムで取得できる。FMO の内容が前回から変わっていない場合は、再解析をスキップする（キャッシュ）。

| 引数 | 説明 |
|------|------|
| `fmoname` | 読み込む FMO 名（省略可能。省略すると `Sakura` になる。Unicode 版は `SakuraUnicode`。普通は省略してよい） |
| `hwnd` | 無視するゴーストのウィンドウハンドル（省略可能。省略すると `SHIORI3FW.HWnd[0]` が使われる。普通は省略してよい） |

返り値はないが、次のグローバル変数が構築される。これらの変数は SHIORI の終了時に自動的に消去される。

「一時起動」（SSTPVIEWER やダミーエントリなど）のゴーストは、FMO テーブルから自動的に除外される。

#### SHIORI3FW.FMOTable

形式は簡易配列で、コンマと `|` で区切られる。SSP ではすべての項目が埋まるが、ベースウェアによっては存在しない（空の）項目もある。また、Windows 以外の OS では利用できない。

```
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
...
```

| 項目 | 意味 |
|------|------|
| `id` | ゴーストを表す ID。通常は知っても意味のない文字列 |
| `name` | \0 名 |
| `keroname` | \1 名 |
| `hwnd` | \0 のウィンドウハンドル |
| `kerohwnd` | \1 のウィンドウハンドル |
| `path` | ゴーストのインストール先ディレクトリ（通常は `ssp.exe` のある位置だが、SSP は複数のゴーストインストール先を持てる） |
| `ghostpath` | ゴーストのベースディレクトリ。`install.txt` や `thumbnail.png` がある場所 |

#### SHIORI3FW.SakuraNameList

形式は汎用配列。上記から \0 名だけを抜き出した配列。たとえば `ANY(SHIORI3FW.SakuraNameList)` とすることで、起動中のゴーストからランダムに 1 体選んで名前を取得する、などが簡単にできる。

```
// 起動中の全ゴースト名を列挙する例
SHIORI3FW.RefreshFMOTable
_list = SHIORI3FW.SakuraNameList
_n = ARRAYSIZE(_list)
for _i = 0; _i < _n; _i++ {
	// _list[_i] にさくら名が入っている
}
```

#### SHIORI3FW.FMOCache

前回読み取った FMO の生データ（キャッシュ用）。直接参照することは少ない。

#### 備考

通常は、自分自身の情報は（`hwnd` に `SHIORI3FW.HWnd[0]` が指定されるため）上記変数に含まれない。自分自身を含みたい場合は、`hwnd` に -1 などを入れる。

## SHIORI3FW.HTTPCodeToMessage

```
SHIORI3FW.HTTPCodeToMessage( コード )
```

ネットワーク更新などで返ってきた HTTP ステータスコードを、日本語のエラーメッセージに変換する。対応するコードがない場合は空文字列を返す。

| コード | 戻り値 |
|--------|--------|
| `'403'` | `'アクセス拒否'` |
| `'404'`、`'410'` | `'ファイル無し'` |
| `'500'`、`'502'`、`'503'` | `'サーバ側の不調'` |
| `'timeout'` | `'タイムアウト'` |
| `'fileio'` | `'ファイル書き込みエラー'` |
| `'artificial'` | `'手動中断'` |

```
OnNetworkUpdateComplete
{
	if reference[1] != '200' {
		_msg = SHIORI3FW.HTTPCodeToMessage(reference[1])
		'\0\s[0]更新に失敗しました：%(_msg)\e'
	}
}
```

## 関連

- [yaya_shiori3.dic](./yaya-shiori3-dic.md)
- [システム辞書内関数マニュアル（yaya-dic）](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
