"""GitHub Pages 用に原稿を _site_src/ へ写す。

- INDEX.md を index.md（トップページ）にし、INDEX.md へのリンクも書き換える
- GitHub では表示できるが Python-Markdown では崩れる書き方を直す
  （段落の直後に空行なしで続くリスト・表の前に空行を入れる）
- 関数ページなどの英語の見出し（Signature など）を日本語にする
- 本文中の関数名（functions/ にページがあるもの）を関数ページへのリンクにする
- `_in_` のように _ で挟んだ書き方（斜体になってしまう）を警告する
- functions/*.md を分類（各ページの **Category:** 行、並びは INDEX.md）ごとの 1 ページにまとめる
  （functions/<分類>.md と、全分類の一覧 functions/index.md）
- grammar/01〜14 を 1 ページ（grammar/index.md）にまとめる
- まとめた元ページ（functions/NAME.md、grammar/NN-xxx.md）へのリンクは、まとめたページの見出しへのリンクに
  書き換える。元ページの URL には移動先へ飛ばすだけの HTML を置く（外部からのリンクを切らないため）
原稿そのものは書き換えない。
"""
import os
import posixpath
import re
import shutil
import sys

from pymdownx.slugs import slugify

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, '_site_src')
DIRS = ['basic', 'other', 'startup', 'system', 'tips']

# 分類名 → functions/ に作るページのファイル名（関数名と区別できる小文字の ASCII）
CATEGORY_PAGES = {
    '型取得/変換': 'conversion',
    '配列操作': 'array',
    'ハッシュ操作': 'hash',
    '文字列操作': 'string',
    '正規表現': 'regex',
    '数学関数': 'math',
    'ビット演算': 'bitwise',
    'ファイル操作': 'file',
    'データベース': 'database',
    '外部ライブラリ': 'library',
    'システム情報': 'sysinfo',
    'メタ操作・特殊関数': 'meta',
    '通信・プロセス間通信': 'ipc',
    'デバッグ': 'debug',
}
FUNCTIONS_TITLE = 'システム関数(組み込み関数)'
GRAMMAR_TITLE = '文法'

HEADING_LINE = re.compile(r'^(#{1,6}) +(.+?)(?: +#+)? *$')
LINK_MD = re.compile(r'\[([^\]]*)\]\([^)]*\)')

# 元ページ（ROOT からの相対パス）→ (まとめたページ, 先頭の id)、(元ページ, 元の見出しの id) → まとめたページでの id
MERGED = {}
FRAGMENTS = {}

BLOCK_START = re.compile(r'^\s*(?:[-*+]\s|\d+\.\s|\|)')
FENCE = re.compile(r'^\s*(```|~~~)')
INDEX_LINK = re.compile(r'(\]\((?:\.\./)*)INDEX\.md')
CODE_SPAN = re.compile(r'`[^`]*`')

# 関数ページなどの英語の見出しをサイトでは日本語で表示する
HEADING_JA = {
    'Signature': '書式',
    'Parameters': '引数',
    'Returns': '戻り値',
    'Description': '解説',
    'Example': '使用例',
    'Compatibility': '互換性',
    'See Also': '関連項目',
    'Notes': '備考',
    'Availability': '対応バージョン',
    'Error Codes': 'エラーコード',
    'Information Types': '取得できる情報',
}
HEADING = re.compile(r'^(#{2,6} +)(' + '|'.join(map(re.escape, HEADING_JA)) + r') *$')

# 旧 wiki の自動リンクの代わりに、本文中の関数名を関数ページへのリンクにする。
# 既存のリンク・HTML タグ・URL の中は触らない。コードスパンは中身が関数名か
# 関数呼び出し（`FOPEN(...)` など）のときだけリンクにする
FUNC_NAMES = sorted((n[:-3] for n in os.listdir(os.path.join(ROOT, 'functions')) if n.endswith('.md')),
                    key=len, reverse=True)
FUNC_ALT = '|'.join(map(re.escape, FUNC_NAMES))
BARE_FUNC = re.compile(r'(?<![A-Za-z0-9_./\-])(' + FUNC_ALT + r')(?![A-Za-z0-9_\-]|\.[A-Za-z])')
CODE_FUNC = re.compile(r'`(' + FUNC_ALT + r')(?:\(.*\))?`')
PROTECTED = re.compile(r'!?\[[^\]]*\]\([^)]*\)|`[^`]*`|<[^>]+>|https?://\S+')

# `_in_` や `_RUNTIME_DIC_` のように _ で挟んだ名前は GitHub でも MkDocs でも斜体になってしまう。
# 斜体は *var* で書く決まりにして、コードスパンの外の _名前_ を警告する（Python-Markdown と同じ判定）
UNDERSCORE_EM = re.compile(r'(?<!\w)_(?!_)(.+?)(?<!_)_(?!\w)')
NOT_EM = re.compile(r'`[^`]*`|<[^>]+>|https?://\S+|\]\([^)]*\)')
ESCAPED = re.compile(r'\\.')


def unescape_table_code(line):
    # GitHub では表のコードスパン内の | を \| と書く必要があるが、
    # Python-Markdown はコードスパン内の | を区切りとみなさず \ をそのまま表示してしまう
    return CODE_SPAN.sub(lambda m: m.group(0).replace('\\|', '|'), line)


def autolink(line, func_dir, self_name):
    def link(name, label):
        if name == self_name:
            return label
        return f'[{label}]({func_dir}{name}.md)'

    def text(part):
        return BARE_FUNC.sub(lambda m: link(m.group(1), m.group(1)), part)

    out = []
    pos = 0
    for m in PROTECTED.finditer(line):
        out.append(text(line[pos:m.start()]))
        code = CODE_FUNC.fullmatch(m.group(0))
        out.append(link(code.group(1), m.group(0)) if code else m.group(0))
        pos = m.end()
    out.append(text(line[pos:]))
    return ''.join(out)


def fix_markdown(text, func_dir, self_name):
    out = []
    in_fence = False
    prev = ''
    for line in text.split('\n'):
        if FENCE.match(line):
            if not in_fence and prev.strip() != '':
                out.append('')
            in_fence = not in_fence
        elif not in_fence and HEADING.match(line):
            m = HEADING.match(line)
            line = m.group(1) + HEADING_JA[m.group(2)]
        elif not in_fence and BLOCK_START.match(line):
            # 直前が本文の行（空行・同種のブロック・見出し以外）なら空行を入れる
            if prev.strip() != '' and not BLOCK_START.match(prev) and not prev.startswith((' ', '\t')):
                out.append('')
            if line.lstrip().startswith('|'):
                line = unescape_table_code(line)
        if not in_fence and not FENCE.match(line) and not line.startswith('#'):
            line = autolink(line, func_dir, self_name)
        out.append(line)
        prev = line
    return INDEX_LINK.sub(r'\1index.md', '\n'.join(out))


def check_underscore_em(text, path):
    in_fence = False
    for lineno, line in enumerate(text.split('\n'), 1):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            # \_ のようにエスケープした文字は区切りにならない
            for m in UNDERSCORE_EM.finditer(ESCAPED.sub('x', NOT_EM.sub(' ', line))):
                print(f'警告: {path}:{lineno}: {m.group(0)} が斜体になる。'
                      f'名前ならコードスパンで囲み、斜体なら *{m.group(1)}* と書く', file=sys.stderr)


def heading_slug(title):
    # toc 拡張が見出しの id を作るのと同じ変換（リンク記法とコードの記号は除く）
    title = LINK_MD.sub(r'\1', title).replace('`', '')
    return slugify(case='lower')(title, '-')


def unique_id(base, used):
    # Python-Markdown の toc と同じ重複回避（_1, _2, ...）
    while base in used or not base:
        m = re.match(r'^(.*)_([0-9]+)$', base)
        base = f'{m.group(1)}_{int(m.group(2)) + 1}' if m else f'{base}_1'
    used.add(base)
    return base


def scan_headings(text):
    """コードブロックの外の見出しを (行番号, 深さ, 見出し, 元の id) で返す"""
    used = set()
    in_fence = False
    for i, line in enumerate(text.split('\n')):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            m = HEADING_LINE.match(line)
            if m:
                yield i, len(m.group(1)), m.group(2), unique_id(heading_slug(m.group(2)), used)


def register(src, page, prefix, text):
    """元ページ src をまとめたページ page に入れるとき、見出しの id の対応を登録する。先頭の見出しの id は prefix"""
    MERGED[src] = (page, prefix)
    for n, (_, _, _, old) in enumerate(scan_headings(text)):
        FRAGMENTS[(src, old)] = prefix if n == 0 else f'{prefix}-{old}'


def shift_headings(text, src, depth_of):
    """見出しの深さを depth_of(元の深さ) にし、まとめたページ内で重ならない id を振る。
    英語の見出し（Signature など）はここで日本語にする（id は元の見出しから作る）"""
    page, prefix = MERGED[src]
    lines = text.split('\n')
    for n, (i, level, title, old) in enumerate(scan_headings(text)):
        new_id = FRAGMENTS[(src, old)]
        title = HEADING_JA.get(title, title) if level >= 2 else title
        lines[i] = f'{"#" * depth_of(level)} {title} {{#{new_id}}}'
    return '\n'.join(lines)


def rewrite_links(text, src, dst):
    """まとめた元ページへのリンク（相対パス・#見出し）を、まとめたページの見出しへのリンクにする"""
    def target(page, frag):
        if page == dst:
            return f'#{frag}'
        return posixpath.relpath(page, posixpath.dirname(dst) or '.') + f'#{frag}'

    def link(m):
        path, frag = m.group(1), (m.group(2) or '')[1:]
        if path == '':
            if src not in MERGED or not frag:
                return m.group(0)
            key, page = src, MERGED[src][0]
        elif path.endswith('.md') and not re.match(r'^[a-z]+:', path):
            key = posixpath.normpath(posixpath.join(posixpath.dirname(src), path))
            if key not in MERGED:
                return m.group(0)
            page = MERGED[key][0]
        else:
            return m.group(0)
        if not frag:
            return f']({target(page, MERGED[key][1])})'
        if (key, frag) not in FRAGMENTS:
            print(f'警告: {src}: リンク先の見出し {key}#{frag} が無い', file=sys.stderr)
            return f']({target(page, MERGED[key][1])})'
        return f']({target(page, FRAGMENTS[(key, frag)])})'

    out = []
    in_fence = False
    for line in text.split('\n'):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            line = re.sub(r'\]\(([^)#\s]*)(#[^)\s]*)?\)', link, line)
        out.append(line)
    return '\n'.join(out)


def render(src, text, dst, shift=None):
    """元ページ src（ROOT からの相対パス）の本文 text を、サイトのページ dst（OUT からの相対パス）用に直す"""
    check_underscore_em(text, src)
    if shift:
        text = shift_headings(text, src, shift)
    # 関数ページへの相対パスと、自分自身へはリンクしないための関数名
    func_dir = posixpath.relpath('functions', posixpath.dirname(dst) or '.') + '/'
    self_name = None
    if func_dir == './':
        func_dir = ''
        if src.startswith('functions/'):
            self_name = posixpath.basename(src)[:-3]
    return rewrite_links(fix_markdown(text, func_dir, self_name), src, dst)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def function_categories():
    """分類名 → 関数名の並び。並びは INDEX.md の表、分類は各ページの **Category:** 行。食い違いや漏れは止める"""
    index = read('INDEX.md')
    section = index.split(f'## {FUNCTIONS_TITLE} (functions/)', 1)[1].split('\n## ', 1)[0]
    cats = {}
    current = None
    for line in section.split('\n'):
        if line.startswith('### '):
            current = cats.setdefault(line[4:].strip(), [])
        else:
            m = re.search(r'\]\(functions/([^)]+)\.md\)', line)
            if m and current is not None:
                current.append(m.group(1))
    errors = []
    listed = [n for names in cats.values() for n in names]
    files = sorted(n[:-3] for n in os.listdir(os.path.join(ROOT, 'functions')) if n.endswith('.md'))
    for name in sorted(set(files) - set(listed)):
        errors.append(f'functions/{name}.md が INDEX.md の表に無い')
    for name in sorted(set(listed) - set(files)):
        errors.append(f'INDEX.md の functions/{name}.md が無い')
    for name in sorted({n for n in listed if listed.count(n) > 1}):
        errors.append(f'{name} が INDEX.md の表に 2 回以上ある')
    for cat, names in cats.items():
        if cat not in CATEGORY_PAGES:
            errors.append(f'分類「{cat}」のページ名が CATEGORY_PAGES に無い')
        for name in names:
            m = re.search(r'^\*\*Category:\*\* *(.+?) *$', read(f'functions/{name}.md'), re.M)
            if not m or m.group(1) != cat:
                errors.append(f'functions/{name}.md の Category が INDEX.md の分類「{cat}」と合わない')
    if len({n.lower() for n in files} | set(CATEGORY_PAGES.values()) | {'index'}) != len(files) + len(CATEGORY_PAGES) + 1:
        errors.append('関数名と分類のページ名が大文字小文字を無視すると重なる')
    if errors:
        sys.exit('エラー: 関数の分類\n  ' + '\n  '.join(errors))
    return cats


def site_url():
    with open(os.path.join(ROOT, 'mkdocs.yml'), encoding='utf-8') as f:
        return re.search(r'^site_url: *(\S+)', f.read(), re.M).group(1)


def write_redirect(old, page, frag):
    """まとめる前のページ old（.md）の URL に置く、まとめたページの見出しへ飛ばす HTML"""
    base = old[:-3] + '/'
    rel = posixpath.relpath(page[:-3], base) + f'/#{frag}'
    absolute = site_url() + page[:-3] + f'/#{frag}'
    write(base + 'index.html',
          '<!doctype html>\n<html lang="ja">\n<meta charset="utf-8">\n<title>移動しました</title>\n'
          f'<link rel="canonical" href="{absolute}">\n'
          f'<meta http-equiv="refresh" content="0; url={rel}">\n'
          f'<p><a href="{rel}">こちら</a>へ移動しました。</p>\n</html>\n')


def register_functions():
    cats = function_categories()
    for cat, names in cats.items():
        page = f'functions/{CATEGORY_PAGES[cat]}.md'
        for name in names:
            register(f'functions/{name}.md', page, heading_slug(name), read(f'functions/{name}.md'))
    return cats


def build_functions(cats):
    for cat, names in cats.items():
        page = f'functions/{CATEGORY_PAGES[cat]}.md'
        parts = [f'# {cat}\n\n{len(names)} 個の関数。']
        for name in names:
            src = f'functions/{name}.md'
            text = re.sub(r'^\*\*Category:\*\*.*\n', '', read(src), count=1, flags=re.M)
            # 関数名は H2。その下の節（Signature など）は H4 にして、右の目次を関数名だけにする
            parts.append(render(src, text, page, lambda level: 2 if level == 1 else level + 2).strip('\n'))
        write(page, '\n\n'.join(parts) + '\n')
    overview = [f'# {FUNCTIONS_TITLE}', '', 'YAYA に組み込まれている関数を、分類ごとのページにまとめています。関数名から探すときは'
                ' [システム関数一覧](../system/system-functions-index.md) か、サイト上部の検索を使ってください。']
    for cat, names in cats.items():
        overview += ['', f'## [{cat}]({CATEGORY_PAGES[cat]}.md)（{len(names)}）', '',
                     ' ・ '.join(f'[{n}]({CATEGORY_PAGES[cat]}.md#{MERGED[f"functions/{n}.md"][1]})' for n in names)]
    write('functions/index.md', '\n'.join(overview) + '\n')
    write('functions/.nav.yml', 'nav:\n  - index.md\n' + ''.join(f'  - {p}.md\n' for p in CATEGORY_PAGES.values()))
    for names in cats.values():
        for name in names:
            page, prefix = MERGED[f'functions/{name}.md']
            write_redirect(f'functions/{name}.md', page, prefix)


def register_grammar():
    chapters = sorted(n for n in os.listdir(os.path.join(ROOT, 'grammar')) if n.endswith('.md'))
    for name in chapters:
        register(f'grammar/{name}', 'grammar/index.md', name[:-3], read(f'grammar/{name}'))
    return chapters


def build_grammar(chapters):
    parts = [f'# {GRAMMAR_TITLE}\n\nYAYA の文法を 1 ページにまとめています。章ごとの内容は右の目次から飛べます。']
    for name in chapters:
        src = f'grammar/{name}'
        parts.append(render(src, read(src), 'grammar/index.md', lambda level: level + 1).strip('\n'))
    write('grammar/index.md', '\n\n'.join(parts) + '\n')
    for name in chapters:
        write_redirect(f'grammar/{name}', *MERGED[f'grammar/{name}'])


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    # リンクの書き換えには全ページの見出しの対応が要るので、登録を先に済ませる
    cats = register_functions()
    chapters = register_grammar()
    build_functions(cats)
    build_grammar(chapters)
    write('index.md', render('INDEX.md', read('INDEX.md'), 'index.md'))
    shutil.copy(os.path.join(ROOT, '.nav.yml'), os.path.join(OUT, '.nav.yml'))
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    shutil.copytree(os.path.join(ROOT, 'attachment'), os.path.join(OUT, 'attachment'))
    for d in DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, d))):
            if name.endswith('.md'):
                write(f'{d}/{name}', render(f'{d}/{name}', read(f'{d}/{name}'), f'{d}/{name}'))


if __name__ == '__main__':
    main()
