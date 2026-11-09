# oldstyle: 旧 AYAYA wiki の見た目を模した静的サイト

旧 AYAYA wiki（PukiWiki Plus! の `skin/default.css`。https://emily.shillest.net/ayayaold/）の見た目と構造を、このリポジトリの Markdown 原稿から再現する自前のビルド。Zensical・MkDocs は使わない（以前の Zensical 版は `old-zensical` ブランチ）。見た目だけを真似て、HTML は HTML5（旧版の XHTML・table レイアウト・IE 向けの補いは使わない）。wiki の道具（一覧・検索・最終更新・差分・履歴・凍結・編集・添付のリンク、最近更新されたページ、フッタ）は載せない。ヘッダに、検索欄と翻訳ボタンを足している。

```sh
python oldstyle/build.py              # scripts/prepare_site.py で _site_src/ を作り、_site/ に出力する
python oldstyle/build.py --no-prepare # _site_src/ を作り直さない
python oldstyle/check.py              # _site/ の内部リンク（ファイル・アンカー・画像・スクリプト・フォーム・検索の索引）を調べる
python -m http.server -d _site        # プレビュー（ディレクトリ形式の URL なので、file:// では見られない）
```

必要なもの: `pip install -r requirements.txt`（`Markdown` `pymdown-extensions` `mdx_truly_sane_lists` `lxml` `PyYAML`）。

## 作り

| 場所 | 内容 |
|---|---|
| `build.py` | `menu.yml` から階層（左のメニュー・パンくずリスト・索引ページ）を作り、原稿 → HTML → 旧版の構造に組む。リンク・画像のパスは出力先からの相対パスに書き換え、行き先が無ければエラーで止まる。`search-index.js` `sitemap.xml` `404.html` `search/` も作る |
| `static/` | `style.css`（旧 `skin/default.css` の規則のうち使う分）、`skin/title.png`（旧版のヘッダ画像）、`search.js`（サイト内検索）、`translate.js`（翻訳ボタン）。ビルドで出力のルートにそのまま置く |
| `menu.yml` | サイトの階層の定義（旧 wiki の MenuBar に当たる）。`title:` と `page:`（原稿のパス。`INDEX.md#見出し` も可）か `index:`（自動で作る索引ページの URL）か `url:`、入れ子の `children:`、メニューに出さないページを下に置く `list:`。書き方はファイルの先頭 |
| `templates/page.html` | 1 ページの HTML5 の枠（`$title` などを `string.Template` で埋める） |
| `check.py` | 出力のリンク・アンカー・画像・フォームの宛先・検索の索引の URL の検査（旧 `zensical build --strict` の代わり。CI でも走る） |
| `../scripts/prepare_site.py` | 原稿を `_site_src/` に写して整える（関数・文法の束ね・用語リンク・空行補い・`_raw/`） |

## ページの構造

```
body[data-root]
  header#header     … 固定（sticky。幅 800px 以下を除く）。#site-logo（旧版のタイトル画像）、#header1（#site-name = ロゴ画像、nav#breadcrumb、#search = 検索欄 + 翻訳ボタン）
  div#page
    nav#menubar     … 左のメニュー（menu.yml の children: の入れ子の ul。下の階層まで全部出す。いま開いているページは太字）
    main#body       … 本文（先頭に div.contents の目次）
```

- ページの URL は、Zensical 版と同じディレクトリ形式（`other/yaya/` など）。リンクと静的ファイルのパスは、ページの深さに応じた相対パス（`../../style.css` など）。`<body data-root>` が、サイトのルートへの相対パス
- 旧版は table だったが、ここでは `flex`。幅が 800px 以下では、ヘッダ → 本文 → 目次の縦並びになる
- 階層の元は menu.yml だけ。パンくずリストは、そのページが menu.yml で最初に出てくる項目から、親をたどって作る。ページが menu.yml のどこにも（`children:` にも `list:` にも）載っていないと、ビルドが止まる
- `index:` を書いた項目の索引ページ（`basic/` `tips/` など）は、ビルドが `children:` と `list:` のページを並べた Markdown を `_site_src/` と `_raw/` に書いて作る（`_site_src/.generated` に記録し、`--no-prepare` のときの消し残しを防ぐ）。検索の索引には入れない。9 件以上の一覧は、`ul.index-grid` として 3 列のグリッドにする（幅が狭くなると列が減り、スマホ幅では 1 列）。`build.py` の `mark_index_grid()` が class を付け、`style.css` が並べる
- 原稿のリンクの `basic/` のようなディレクトリは、そのディレクトリの索引ページ（`index.md`）への link になる
- 見出しの末尾の `†` は、その見出しへのリンク。ページ先頭の `div.contents` は、H2・H3 の目次
- OGP は `build.py` の `OGP`、`other/yaya6-launch.md` の部品（ヒーロー画像・ボタン・数字のカードなど）は `style.css` の `.y6-*`（配色はほかのページと同じ）
- ヘッダの画像 `skin/title.png` は旧 wiki のもの。ロゴ画像 `skin/logo.png` は、このサイト用に作り直したもの（旧版のロゴは「Wiki」「PukiWiki Plus!」の文字入りだった）
