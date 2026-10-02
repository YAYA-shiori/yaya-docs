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

- `INDEX.md` の該当する表に追加する
- 関数なら `system/system-functions-index.md` にも追加する
- 新しいディレクトリを作ったら、`.nav.yml` の `nav` と `scripts/prepare_site.py` の `DIRS` に加える

## 言語仕様が変わったとき

- 記法・式・制御構造・関数・設定ファイルなど、言語仕様に関わる変更をしたら、チートシート（`startup/cheatsheet.md`）も同じ変更に合わせて更新する
- 関数やシステム関数の追加・改名・削除、対応バージョンの変更も、チートシートの該当する表に反映する
- チートシートの例は、`yaya.exe`（`../yaya-shiori` の EXE 構成）で動かして出力を確かめてから書く。マニュアルの文面と実機が食い違っていたら、実機を正としてページを直す

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が Zensical（Material for MkDocs の後継。Material テーマ互換）でビルドし、https://yaya-shiori.github.io/yaya-docs/ に公開する。ビルドは `zensical build --strict` で、リンク切れ・アンカー切れがあると失敗する。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする（`assets/` の画像・CSS も写す）。その際 `INDEX.md` は `index.md`（トップページ）になり、`INDEX.md` へのリンクも書き換えられる
- 設定は `mkdocs.yml` をそのまま読ませている。左メニューの章立ては `.nav.yml`（mkdocs-awesome-nav）、各ページの名前は H1 から決まる
- GitHub では表示できても MkDocs（Python-Markdown）では崩れる書き方がある。段落の直後に空行なしで続くリストや表は `prepare_site.py` が空行を補うので、原稿は GitHub 向けのままでよい。表の中のコードスパンの `|` は GitHub 向けに `\|` と書く（`prepare_site.py` がサイト用に `|` へ戻す）。2スペース字下げの入れ子リストは mdx_truly_sane_lists で扱える
- `_in_` や `_RUNTIME_DIC_` のように `_` で挟んだ名前は、GitHub でも MkDocs でも斜体になってしまう。名前はコードスパンで囲み、斜体（引数の仮置き名など）は `*var*` と書く。コードスパンの外にある `_名前_` は `prepare_site.py` が警告する
- 本文や See Also に書いた関数名（`functions/` にページがあるもの。素の `FOPEN` でもコードスパンの `` `FOPEN` `` / `` `FOPEN(...)` `` でもよい）は、`prepare_site.py` がサイト用に関数ページへのリンクにする（旧 wiki の自動リンクの代わり）。見出し・コードブロック・既存のリンクの中と、関数ページ自身の名前はリンクにしない。原稿には書き込まれないので GitHub 上ではリンクにならない
- 関数ページの見出し（Signature / Parameters / Returns など）は原稿では英語のまま書く。サイトでは `prepare_site.py` の `HEADING_JA` で日本語に置き換える
- ヘッダの色は `mkdocs.yml` の `theme.palette` の `primary`（現在は black）で決まる
- OGP / Twitter カードのタグは `overrides/main.html` が全ページに出す。ページごとのタイトル・説明・画像（1200x630 の PNG）は `mkdocs.yml` の `extra.ogp` にページの URL（`other/yaya6-launch/` のように末尾が `/`。トップは空文字）をキーにして書く（原稿に front matter は書かない。GitHub で表として表示されてしまうため）
- Zensical は 0.0.x の版を固定している（`requirements.txt`）。Material for MkDocs は 2026-11-05 にサポート終了のため移行した（MkDocs 2.0 はプラグインや Material テーマと互換性が無い）
- Zensical のテンプレートは MiniJinja で、`page.file` や `page.is_homepage` が無い。`overrides/main.html` はページの URL（`page.url`）で判定する
- 見た目は `theme.variant: classic` で従来のまま。Zensical の既定は新デザインの modern

手元で確認するとき（`_site_src/` と `_site/` は `.gitignore` 済み）:

```sh
pip install -r requirements.txt
python scripts/prepare_site.py
zensical build --strict    # 警告（リンク切れ・アンカー切れ）が出ないことを確認する
zensical serve             # http://127.0.0.1:8000/yaya-docs/ でプレビュー
```
