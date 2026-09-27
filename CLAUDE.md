このリポジトリは伺かの SHIORI「YAYA」の言語マニュアル（Markdown）です。
YAYA 本体のソースは `../yaya-shiori` にあります。

このリポジトリが YAYA マニュアルの正本です。旧 wiki（emily.shillest.net/ayaya）への参照やページ名は書かないこと。

## 書式

- UTF-8、LF
- 関数ページ（`functions/*.md`）は既存ページの見出し構成（Signature / Parameters / Returns / Description / Example / Compatibility / See Also）に合わせる
- 対応バージョンは `Tc600-3以降` のように書く。変更履歴は Compatibility に `- Tc600-3: 変更内容` の形で追記する
- リンクは相対パスで `.md` まで書く（例: `[IHASH](../functions/IHASH.md)`、`[保存形式](SAVEVAR.md#保存形式)`）。見出しへのアンカーは GitHub と同じく日本語の見出しをそのまま使う

## ページを追加・改名したとき

- `INDEX.md` の該当する表に追加する
- 関数なら `system/system-functions-index.md` にも追加する
- 新しいディレクトリを作ったら、`.pages` の `nav` と `scripts/prepare_site.py` の `DIRS` に加える

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が MkDocs（Material テーマ）でビルドし、https://yaya-shiori.github.io/yaya-docs/ に公開する。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする（`assets/` の画像・CSS も写す）。その際 `INDEX.md` は `index.md`（トップページ）になり、`INDEX.md` へのリンクも書き換えられる
- 左メニューの章立ては `.pages`（mkdocs-awesome-pages-plugin）、各ページの名前は H1 から決まる
- GitHub では表示できても MkDocs（Python-Markdown）では崩れる書き方がある。段落の直後に空行なしで続くリストや表は `prepare_site.py` が空行を補うので、原稿は GitHub 向けのままでよい。表の中のコードスパンの `|` は GitHub 向けに `\|` と書く（`prepare_site.py` がサイト用に `|` へ戻す）。2スペース字下げの入れ子リストは mdx_truly_sane_lists で扱える
- ヘッダの色は `mkdocs.yml` の `theme.palette` の `primary`（現在は black）で決まる
- MkDocs は 1.6 系に固定している（`requirements.txt`）。MkDocs 2.0 はプラグインや Material テーマと互換性が無い

手元で確認するとき（`_site_src/` と `_site/` は `.gitignore` 済み）:

```sh
pip install -r requirements.txt
python scripts/prepare_site.py
mkdocs build     # 警告（リンク切れ・アンカー切れ）が出ないことを確認する
mkdocs serve     # http://127.0.0.1:8000/yaya-docs/ でプレビュー
```
