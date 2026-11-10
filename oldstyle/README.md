# oldstyle: 旧 AYAYA wiki の見た目を模した静的サイト

旧 AYAYA wiki（PukiWiki Plus! の `skin/default.css`。https://emily.shillest.net/ayayaold/）の見た目と構造を、このリポジトリの Markdown 原稿から再現する自前のビルド。Zensical・MkDocs は使わない（以前の Zensical 版は `old-zensical` ブランチ）。見た目だけを真似て、HTML は HTML5（旧版の XHTML・table レイアウト・IE 向けの補いは使わない）。wiki の道具（一覧・検索・最終更新・差分・履歴・凍結・編集・添付のリンク、最近更新されたページ、フッタ）は載せない。ヘッダに、検索欄と翻訳ボタンを足している。

```sh
python oldstyle/build.py              # scripts/prepare_site.py で _site_src/ を作り、_site/ に出力する
python oldstyle/build.py --no-prepare # _site_src/ を作り直さない
python oldstyle/build.py --lang=en    # 翻訳版（i18n/en/ の訳文を重ねたもの）だけを _site/en/ に出す。--no-langs: 日本語版だけ
python oldstyle/check.py              # _site/ の内部リンク（ファイル・アンカー・画像・スクリプト・フォーム・検索の索引）を調べる（--lang=en で翻訳版）
python -m http.server -d _site        # プレビュー（ディレクトリ形式の URL なので、file:// では見られない）
```

必要なもの: `pip install -r requirements.txt`（`Markdown` `pymdown-extensions` `mdx_truly_sane_lists` `lxml` `PyYAML`）。

## 作り

| 場所 | 内容 |
|---|---|
| `build.py` | `menu.yml` から階層（左のメニュー・パンくずリスト・索引ページ）を作り、原稿 → HTML → 旧版の構造に組む。リンク・画像のパスは出力先からの相対パスに書き換え、行き先が無ければエラーで止まる。`search-index.js` `sitemap.xml` `404.html` `search/` も作る |
| `static/` | `style.css`（旧 `skin/default.css` の規則のうち使う分）、`skin/title.png`（旧版のヘッダ画像）、`search.js`（サイト内検索）、`lang.js`（言語切替。`translate.js` はブラウザ翻訳の旧版で、いまは読み込まない）。ビルドで出力のルートにそのまま置く |
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

## 翻訳版

LLM（`../scripts/translate.py`）が作った `i18n/<言語>/` の訳文を、日本語の原稿に重ねてビルドする。`python oldstyle/build.py` が、日本語版の後に `i18n/` のある言語を `_site/<言語>/` へ続けて出す（`--lang=<言語>` でその言語だけ、`--no-langs` で日本語版だけ）。

- URL は日本語版と同じ形（`functions/string/` なら `en/functions/string/`）。言語切替（`lang.js`）は、`<body data-root>` から、いま見ている言語版のルートと、その下のこのページのパスを求め、別言語版へ移るだけ。切替先は、ページの `<meta name="ukadoc-langs">` に書く（`build.py` の `available_langs()`）
- 画像・添付ファイル（`assets/` `attachment/`）・`llms.txt`・生の原稿・まとめる前のページの転送 HTML・`404.html`・`sitemap.xml` は日本語版のもの。翻訳版のページは、画像などを `../` 付きで参照する（`build.py` の `BASE`、`rel_file`）。CSS・JS・`search-index.js` は、言語ごとに出力する。canonical と OGP の URL は `<言語>/` を含む
- 画面の枠の文言（検索欄・パンくず・検索ページ・OGP の言語など）は `build.py` の `UI`、関数の分類ページと文法ページの題・前書き・節の見出しは `prepare_site.py` の `TEXTS` と `HEADING_LOCAL` に、言語ごとの語を書く。言語を足すときは、`build.py` の `LANGS` と `UI`、`prepare_site.py` の `TEXTS` と `HEADING_LOCAL`、`lang.js` の `LANGS` と `NOTICE`、`search.js` の `MESSAGES`、`scripts/translate.py` の `LANGS` に足す
- メニュー（`menu.yml`）の訳は `i18n/<言語>/menu.yml`（`MENU_FILE`）。`page:` などは日本語のものと同じ（翻訳時に検査する）。`list:` のページの並びは日本語の原稿の H1 の順（`list_pages` の `sort_key`）
- 見出しの id は、日本語の原稿から作る（束ねないページは `prepare_site.py` の `pin_ids`、束ねるページは `shift_headings`）
- 翻訳版のサイトに OGP の題・説明（`OGP`）は使わない（日本語の文なので、ページの題と説明を使う。画像は共有）
