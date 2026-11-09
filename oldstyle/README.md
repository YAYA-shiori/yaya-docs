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
| `build.py` | `_site_src/` の `.nav.yml` から章立てを読み、原稿 → HTML → 旧版の構造に組む。リンク・画像のパスは出力先からの相対パスに書き換え、行き先が無ければエラーで止まる。`search-index.js` `sitemap.xml` `404.html` `search/` も作る |
| `static/` | `style.css`（旧 `skin/default.css` の規則のうち使う分）、`skin/title.png`（旧版のヘッダ画像）、`search.js`（サイト内検索）、`translate.js`（翻訳ボタン）。ビルドで出力のルートにそのまま置く |
| `templates/page.html` | 1 ページの HTML5 の枠（`$title` などを `string.Template` で埋める） |
| `check.py` | 出力のリンク・アンカー・画像・フォームの宛先・検索の索引の URL の検査（旧 `zensical build --strict` の代わり。CI でも走る） |
| `../scripts/prepare_site.py` | 原稿を `_site_src/` に写して整える（関数・文法の束ね・用語リンク・空行補い・`_raw/`） |

## ページの構造

```
body[data-root]
  header#header     … #site-logo（旧版のタイトル画像）、#header1（#site-name、nav#breadcrumb、#search = 検索欄 + 翻訳ボタン）
  div#page
    nav#menubar     … 左のメニュー（入れ子の ul）。いま開いているページのある章だけ、下の階層を出す
    main#body       … nav.navi（Prev / Home / Next）、本文（先頭に div.contents の目次）、nav.navi
```

- ページの URL は、Zensical 版と同じディレクトリ形式（`other/yaya/` など）。リンクと静的ファイルのパスは、ページの深さに応じた相対パス（`../../style.css` など）。`<body data-root>` が、サイトのルートへの相対パス
- 旧版は table だったが、ここでは `flex`。幅が 800px 以下では、ヘッダ → 本文 → 目次の縦並びになる
- 前後のページは `.nav.yml` の深さ優先の順。Home は、そのページのある章（無ければトップページ）
- ページの無い章（基本・Tips など）の項目は、トップページの `## 基本 (basic/)` のような節へのリンクになる
- 見出しの末尾の `†` は、その見出しへのリンク。ページ先頭の `div.contents` は、H2・H3 の目次
- OGP は `build.py` の `OGP`、`other/yaya6-launch.md` の暗い装いは `style.css` の `body.y6` と `.y6-*`
- ヘッダの画像 `skin/title.png` は旧 wiki のもの。旧版のロゴ画像（「Wiki」「PukiWiki Plus!」の文字入り）は使わず、サイト名は文字で出している
