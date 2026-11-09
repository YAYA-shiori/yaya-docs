このリポジトリは伺かの SHIORI「YAYA」の言語マニュアル（Markdown）です。
YAYA 本体のソースは `../yaya-shiori` にあります。

このリポジトリが YAYA マニュアルの正本です。旧 wiki（emily.shillest.net/ayaya）への参照やページ名は書かないこと。

例外として、`other/` と `tips/` のうち旧 wiki の原文を転載したページは、見出し直下に `> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載` と明記している。これらのページは原文に寄せて書いてあるので、書き換えるときも原文の文面・構成を勝手に要約しない。添付ファイルは `attachment/` にまとめ、ページからは `../attachment/ファイル名` で参照する（`scripts/prepare_site.py` がサイトにも写す）。

## 書式

- UTF-8、LF
- 関数ページ（`functions/*.md`）は既存ページの見出し構成（Signature / Parameters / Returns / Description / Example / Compatibility / See Also）に合わせる
- 対応バージョンは `Tc600-3以降` のように書く。変更履歴は Compatibility に `- Tc600-3: 変更内容` の形で追記する
- リンクは相対パスで `.md` まで書く（例: `[IHASH](../functions/IHASH.md)`、`[保存形式](SAVEVAR.md#保存形式)`）。見出しへのアンカーは GitHub と同じく日本語の見出しをそのまま使う

## ページを追加・改名したとき

- `oldstyle/menu.yml` に加える。サイトの階層（左のメニュー・パンくずリスト・各節の索引ページ）は、すべてこのファイルから作られる。`children:` に書くと左のメニューにも出る。`list: ディレクトリ名` を書いた項目の下には、メニューに載っていないそのディレクトリのページが（左のメニューには出さずに）自動で入る（`tips/` の新しいページは、何もしなくてよい）。どちらにも載らないページがあると、ビルドが止まる
- `INDEX.md`（トップページ）に全ページを並べる必要は無い。節の一覧は、`menu.yml` から自動で作る索引ページ（`basic/` `tips/` など）が受け持つ
- 関数なら `functions/README.md`（分類別の一覧。ビルドの元データ）と `system/system-functions-index.md` にも追加する
- 新しいディレクトリを作ったら、`scripts/prepare_site.py` の `DIRS` に加え、`menu.yml` に載せる

## 言語仕様が変わったとき

- 記法・式・制御構造・関数・設定ファイルなど、言語仕様に関わる変更をしたら、チートシート（`startup/cheatsheet.md`）も同じ変更に合わせて更新する
- 関数やシステム関数の追加・改名・削除、対応バージョンの変更も、チートシートの該当する表に反映する
- チートシートの例は、`yaya.exe`（`../yaya-shiori` の EXE 構成）で動かして出力を確かめてから書く。マニュアルの文面と実機が食い違っていたら、実機を正としてページを直す

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が `oldstyle/build.py` と `oldstyle/check.py` を走らせ、https://yaya-shiori.github.io/yaya-docs/ に公開する。以前の Zensical 版は `old-zensical` ブランチに残してある。ビルドの仕組みは [`oldstyle/README.md`](oldstyle/README.md)。原稿を書くうえで知っておくことは次のとおり。

- サイトの見た目と構造は、旧 AYAYA wiki（PukiWiki Plus! の skin/default.css）を模している。上にヘッダ（左に旧版のタイトル画像、右の黒い帯にロゴ画像・パンくずリスト・検索欄・翻訳ボタン。幅が 800px を超えるときは、スクロールしても上に固定する）、左に目次（`#menubar`）、右に本文（`#body`）。旧版にあった wiki の道具（一覧・検索・最終更新・編集・添付のリンク、最近更新されたページ、フッタ）は無い。HTML は HTML5 で、JavaScript は検索（`search.js`）と翻訳ボタン（`translate.js`）だけ
- ページの URL は、Zensical 版と同じディレクトリ形式（`other/yaya/` など）。外部からのリンクや OGP を切らないため、変えない。`file://` ではディレクトリのリンクが `index.html` を開かないので、手元では `python -m http.server -d _site` で見る
- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする。その際 `INDEX.md` は `index.md`（トップページ）になり、`INDEX.md` へのリンクも書き換えられる。原稿内のリンク（`../functions/IHASH.md` や `05-arrays.md#範囲外の要素` など）は、ビルドが出力先の相対パス（`../string/#ihash`）に書き換える。行き先が無ければビルドが止まる
- 関数ページ（`functions/*.md`）は、サイトでは分類ごとの 1 ページ（`functions/string/` など）にまとめて出す。分類は各ページの `**Category:**` 行、並びは `functions/README.md` の一覧（`## 分類` の下のリスト）で決まる。新しい関数は `functions/README.md` の一覧に 1 回だけ載せ、分類名を `**Category:**` と合わせる（食い違い・漏れは `prepare_site.py` が止める。新しい分類は `CATEGORY_PAGES` にも加える）。文法（`grammar/01〜14`）も 1 ページ（`grammar/`）にまとめる。原稿は 1 ファイル 1 ページのまま書き、リンクも従来どおり書く（`prepare_site.py` がまとめたページの見出しへのリンクに書き換える）
- まとめた元ページの URL（`functions/IHASH/` など）には、移動先へ飛ばすだけの HTML を `prepare_site.py` が置く。まとめたページでは関数名が H2、その下の節（書式・引数など）が H4 になる
- 各ページの先頭（最初の H2 の前）に、旧版の `div.contents` にあたる目次を `oldstyle/build.py` が付ける（H2・H3 が 3 つ以上あるページ。トップページは H2 だけ）。見出しの末尾の `†` は、その見出しへのリンク（旧 wiki と同じ）
- `llms.txt`（AI エージェント向けの探し方の案内。`INDEX.md` と各ディレクトリの入口だけを書く）はサイトのルートに置かれる。ページごとの一覧は載せないので、ページを足しても直さなくてよい。ディレクトリを足したときは「構成」に 1 行足す
- 生の Markdown 原稿（`README.md` と `CLAUDE.md` 以外の `.md`）は、リポジトリと同じパスでサイトにも置かれる（`prepare_site.py` が `_raw/` に写し、ビルドが出力に重ねる）。`llms.txt` や `INDEX.md` の相対リンクは、このおかげでサイト上でも辿れる
- サイトの階層の元は `oldstyle/menu.yml`（旧 wiki の MenuBar に当たる、手で選んだ一覧。書き方はファイルの先頭に書いてある）ひとつだけ。左のメニュー、上のパンくずリスト、各節の索引ページが、同じ木から作られる。`index: basic/` と書いた項目には、下の項目（`children:` と `list:` のページ）を並べるだけの小さな索引ページを、ビルドが自動で作る（原稿は無い。サイトには生の `index.md` も置かれる）。`list:` のページの並びは、ディレクトリに `.nav.yml` があればその順（`functions/.nav.yml` は `prepare_site.py` が作る）、残りは各ページの H1 の順。パンくずは、ページが最初に出てくる項目の下になる。原稿のパスや `INDEX.md#見出し` が違う、載っていないページがある、とビルドが止まる。`INDEX.md` や他のページから節へのリンクは、`[基本](basic/)` のようにディレクトリで書く（GitHub ではファイルの一覧、サイトでは索引ページになる）
- Markdown の拡張は `tables` `admonition` `attr_list` `md_in_html` `mdx_truly_sane_lists` `pymdownx.superfences` `toc`。見出しのアンカーは GitHub と同じく日本語のまま（`pymdownx.slugs.slugify(case='lower')`）で、`prepare_site.py` のリンク書き換えと同じ変換
- GitHub では表示できても Python-Markdown では崩れる書き方がある。段落の直後に空行なしで続くリストや表は `prepare_site.py` が空行を補うので、原稿は GitHub 向けのままでよい。表の中のコードスパンの `|` は GitHub 向けに `\|` と書く（`prepare_site.py` がサイト用に `|` へ戻す）。2スペース字下げの入れ子リストは mdx_truly_sane_lists で扱える
- `_in_` や `_RUNTIME_DIC_` のように `_` で挟んだ名前は、GitHub でも Python-Markdown でも斜体になってしまう。名前はコードスパンで囲み、斜体（引数の仮置き名など）は `*var*` と書く。コードスパンの外にある `_名前_` は `prepare_site.py` が警告する
- 注意書きは `!!! note "タイトル"` / `!!! warning "タイトル"`（admonition）で書く。本文は 4 スペース字下げ。転載ページの `> [AYAYA Wiki](...) より転載` は引用のまま（旧版の `blockquote` の橙の枠になる）
- 本文や See Also に書いた関数名（`functions/` にページがあるもの。素の `FOPEN` でもコードスパンの `` `FOPEN` `` / `` `FOPEN(...)` `` でもよい）は、`prepare_site.py` がサイト用に関数ページへのリンクにする（旧 wiki の自動リンクの代わり）。見出し・コードブロック・既存のリンクの中と、関数ページ自身の名前はリンクにしない。原稿には書き込まれないので GitHub 上ではリンクにならない
- 関数ページの見出し（Signature / Parameters / Returns など）は原稿では英語のまま書く。サイトでは `prepare_site.py` の `HEADING_JA` で日本語に置き換える
- 見た目は `oldstyle/static/style.css`（旧 `skin/default.css` の規則のうち使う分。色と寸法は旧版のまま）。ダークモードは無い。ヘッダの画像 `oldstyle/static/skin/title.png` は旧 wiki のもの（`assets/logo.png` と同じキャラクター）。ロゴ画像 `oldstyle/static/skin/logo.png`（350x40、地色 `#212121`）は、このサイト用に作り直したもの。パンくずリストはトップページでも出す。`other/yaya6-launch.md` の部品（ヒーロー画像・ボタン・数字のカードなど。`.y6-*`、`style.css` の末尾）も、配色はほかのページと同じ旧版の配色
- OGP / Twitter カードのタグは `oldstyle/build.py` が全ページに出す。ページごとのタイトル・説明・画像（1200x630 の PNG）は `build.py` の `OGP` に、ページの URL（`other/yaya6-launch/` のように末尾が `/`。トップは空文字）をキーにして書く（原稿に front matter は書かない。GitHub で表として表示されてしまうため）
- 検索は、ビルド時に作る `search-index.js`（節ごとの本文）を、`search.js` が空白区切りの語の AND で部分一致検索する。ヘッダの検索欄に打ち込むとドロップダウンが出て、Enter で `search/?q=` に全件が並ぶ。ページの深さが違うので、`<body data-root="../../">` でサイトのルートへの相対パスを渡している
- ヘッダに翻訳ボタンがある（`oldstyle/static/translate.js`。見た目は `style.css` の `.ukadoc-translate`）。ブラウザ組み込みの Translator API（Chrome 138 以降のデスクトップ版など）で、本文と左メニューを日本語から英語・中国語（繁体 `zh-Hant`・簡体 `zh`）へ機械翻訳する。API が無いブラウザではボタンを出さない。訳すのは日本語を含む文だけで、`code` `pre` `kbd` と `translate="no"` の中は訳さない。文はブロック（`p` `li` `td` など）の中の連なりを単位にまとめて訳し、リンク・太字・コードスパンは印（`<x1/>` `<a2>…</a2>`）に置き換えて訳してから元の要素へ戻す（印が崩れた文は断片ごとの訳に切り替える）。訳したくない語は原稿で `<span translate="no">…</span>` と囲める。読める程度の品質でよいとしている。JavaScript を使うのは検索とこのボタンだけ
- `sitemap.xml` と `404.html` もビルドが作る。404.html のリンクは、どの深さで開かれるかわからないので、サイトのルートからの絶対パス（`/yaya-docs/…`）

手元で確認するとき（`_site_src/` `_site/` `_raw/` は `.gitignore` 済み）:

```sh
pip install -r requirements.txt
python oldstyle/build.py    # prepare_site.py で _site_src/ を作り、_site/ に出力する（--no-prepare で作り直さない）
python oldstyle/check.py    # 出力のリンク切れ・アンカー切れ・画像の切れ・検索の索引の URL を調べる（エラーが 0 件であること）
python -m http.server -d _site    # http://127.0.0.1:8000/ でプレビュー
```
