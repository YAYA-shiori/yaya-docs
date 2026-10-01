"""GitHub Pages 用に原稿を _site_src/ へ写す。

- INDEX.md を index.md（トップページ）にし、INDEX.md へのリンクも書き換える
- GitHub では表示できるが Python-Markdown では崩れる書き方を直す
  （段落の直後に空行なしで続くリスト・表の前に空行を入れる）
- 関数ページなどの英語の見出し（Signature など）を日本語にする
- 本文中の関数名（functions/ にページがあるもの）を関数ページへのリンクにする
- `_in_` のように _ で挟んだ書き方（斜体になってしまう）を警告する
原稿そのものは書き換えない。
"""
import os
import re
import shutil
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, '_site_src')
DIRS = ['basic', 'functions', 'grammar', 'other', 'startup', 'system', 'tips']

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


def copy_md(src, dst):
    with open(src, encoding='utf-8') as f:
        text = f.read()
    check_underscore_em(text, os.path.relpath(src, ROOT).replace(os.sep, '/'))
    # 関数ページへの相対パスと、自分自身へはリンクしないための関数名
    func_dir = os.path.relpath(os.path.join(OUT, 'functions'), os.path.dirname(dst)).replace(os.sep, '/') + '/'
    self_name = None
    if func_dir == './':
        func_dir = ''
        self_name = os.path.basename(dst)[:-3]
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write(fix_markdown(text, func_dir, self_name))


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    copy_md(os.path.join(ROOT, 'INDEX.md'), os.path.join(OUT, 'index.md'))
    shutil.copy(os.path.join(ROOT, '.pages'), os.path.join(OUT, '.pages'))
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    shutil.copytree(os.path.join(ROOT, 'attachment'), os.path.join(OUT, 'attachment'))
    for d in DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, d))):
            if name.endswith('.md'):
                copy_md(os.path.join(ROOT, d, name), os.path.join(OUT, d, name))


if __name__ == '__main__':
    main()
