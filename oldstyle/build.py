r"""YAYA マニュアルのサイトを作る（旧 AYAYA wiki の見た目を模した、自前の静的サイトのビルド）。

    python oldstyle/build.py              # scripts/prepare_site.py で _site_src/ を作り、_site/ に出力する
    python oldstyle/build.py --no-prepare # _site_src/ を作り直さない

原稿（Markdown）→ HTML → 旧 wiki の構造（ヘッダ・左の #menubar・本文の #body・前後のページ）に組む。HTML は HTML5。
ページの URL は Zensical 版と同じ（other/yaya/ のようにディレクトリ。外部からのリンクを切らないため）。
詳しくは oldstyle/README.md。
"""
import argparse
import copy
import json
import os
import posixpath
import re
import shutil
import string
import sys
from urllib.parse import urlsplit

import lxml.html
import markdown
import yaml
from lxml import etree
from pymdownx.slugs import slugify

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import prepare_site  # noqa: E402

SRC = prepare_site.OUT                  # 原稿の写し（_site_src/）
RAW = prepare_site.RAW                  # 生の Markdown 原稿の写し（_raw/）
OUT = os.path.join(ROOT, '_site')
STATIC = os.path.join(HERE, 'static')
SITE_URL = prepare_site.SITE_URL
SITE_PATH = urlsplit(SITE_URL).path     # /yaya-docs/（404.html のように、どの深さで開かれるかわからないページが使う）
SITE_NAME = 'YAYA マニュアル'
SITE_DESCRIPTION = '伺かの SHIORI「YAYA」の言語マニュアル'

# ページごとの OGP / Twitter カード。キーはページの URL（トップは ''）、image は SITE_URL からの相対パス（1200x630）
OGP = {
    'other/yaya6-launch/': {
        'title': 'YAYA 6 登場 ─ これまでで最も賢い YAYA。',
        'description': 'ハッシュ、入れ子、JSON / XML / YAML / TOML の読み書き、SQLite。YAYA 600 系、初の正式版 Tc603 の一般提供を開始しました。',
        'image': 'assets/yaya6/ogp.png',
    },
}

MD_EXTENSIONS = ['tables', 'admonition', 'attr_list', 'md_in_html', 'mdx_truly_sane_lists', 'pymdownx.superfences', 'toc']
MD_CONFIG = {
    'toc': {
        # GitHub と同じく日本語の見出しをそのままアンカーにする（prepare_site.py の heading_slug と同じ変換）
        'slugify': slugify(case='lower'),
        # 旧 wiki と同じ、見出しの末尾の †（その見出しへのリンク）
        'permalink': '†',
        'permalink_class': 'anchor_super',
        'permalink_title': 'この見出しへのリンク',
    },
}

errors = []


def error(msg):
    errors.append(msg)
    print(f'エラー: {msg}', file=sys.stderr)


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path) or OUT, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


# ---------------------------------------------------------------- URL

def page_url(md):
    """原稿（_site_src/ からのパス）のページの URL（サイトのルートから。トップは ''、末尾は /）"""
    if md == 'index.md':
        return ''
    stem = md[:-len('.md')]
    if posixpath.basename(stem) == 'index':
        return posixpath.dirname(stem) + '/'
    return stem + '/'


def rel_url(from_url, to_url):
    """ページ from_url から、ページ to_url へのリンク。from_url が None なら、サイトのルートからの絶対パス"""
    if from_url is None:
        return SITE_PATH + to_url
    r = posixpath.relpath(to_url.rstrip('/') or '.', from_url.rstrip('/') or '.')
    return './' if r == '.' else r + '/'


def rel_file(from_url, path):
    """ページ from_url から、サイトのルートからの path（画像・添付ファイルなど）へのパス"""
    if from_url is None:
        return SITE_PATH + path
    return posixpath.relpath(path, from_url.rstrip('/') or '.')


def root_of(url):
    return rel_url(url, '')


# ---------------------------------------------------------------- 章立て（.nav.yml）

def plain(text):
    # 見出しの Markdown 記法（コード・リンク・{#id} など）を除いた文字
    text = re.sub(r'\{[#:][^}]*\}', '', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text).replace('`', '')
    return text.strip()


def h1_of(md):
    for line in read(os.path.join(SRC, md)).split('\n'):
        if line.startswith('# '):
            return plain(line[2:])
    error(f'{md} に H1 が無い')
    return md


class Node:
    def __init__(self, title, page=None, depth=0, parent=None):
        self.title = title
        self.page = page          # 原稿の写しでのパス。無ければ見出しだけ（トップページの節への案内になる）
        self.depth = depth        # 最上位の項目が 1
        self.parent = parent
        self.children = []

    @property
    def url(self):
        return page_url(self.page) if self.page else None


def autolist(rel_dir):
    """.nav.yml の無いディレクトリの並び（awesome-nav と同じ。index.md が先頭、あとはファイル名順、題は H1）"""
    names = sorted((n for n in os.listdir(os.path.join(SRC, rel_dir)) if n.endswith('.md') and n != 'index.md'),
                   key=str.lower)
    entries = ['index.md'] if os.path.exists(os.path.join(SRC, rel_dir, 'index.md')) else []
    return entries + names


def read_nav_file(rel_dir):
    path = os.path.join(SRC, rel_dir, '.nav.yml')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)['nav']
    if rel_dir == '':
        error('.nav.yml が無い')
        return []
    return autolist(rel_dir)


def parse_entries(entries, rel_dir, parent):
    """.nav.yml（mkdocs-awesome-nav の書式のうち使っている分）の nav を、parent の子にする。
    `index.md` は parent 自身のページ、`file.md` は H1 を題にしたページ、`題: file.md` は題つきのページ、
    `題: フォルダ` は下の .nav.yml（無ければ自動の並び）"""
    for entry in entries:
        if isinstance(entry, str):
            md = posixpath.join(rel_dir, entry) if rel_dir else entry
            if entry == 'index.md':
                parent.page = md
            else:
                parent.children.append(Node(h1_of(md), page=md, depth=parent.depth + 1, parent=parent))
            continue
        (title, value), = entry.items()
        node = Node(title, depth=parent.depth + 1, parent=parent)
        parent.children.append(node)
        if value.endswith('.md'):
            node.page = posixpath.join(rel_dir, value) if rel_dir else value
        else:
            sub = posixpath.join(rel_dir, value) if rel_dir else value
            parse_entries(read_nav_file(sub), sub, node)


def load_nav():
    root = Node(SITE_NAME, depth=0)
    parse_entries(read_nav_file(''), '', root)
    # 最上位の index.md は、題を「トップページ」としてページにする（旧版のメニューの先頭）
    if root.page:
        home = Node('トップページ', page=root.page, depth=1, parent=root)
        root.children.insert(0, home)
        root.page = None
    return root


def flatten(node, out):
    for c in node.children:
        if c.page:
            out.append(c)
        flatten(c, out)
    return out


def first_page(node):
    if node.page:
        return node.page
    for c in node.children:
        p = first_page(c)
        if p:
            return p
    return None


def index_anchors():
    """トップページの「## 基本 (basic/)」のような節 → ディレクトリ名: 見出しの id。ページの無い節は、ここへ案内する"""
    anchors = {}
    for line in read(os.path.join(SRC, 'index.md')).split('\n'):
        m = re.match(r'^## +(.+?) +\(([^)/]+)/\) *$', line)
        if m:
            anchors[m.group(2)] = prepare_site.heading_slug(line[3:].strip())
    return anchors


ANCHORS = {}


def target(node):
    """メニュー・パンくずがその項目へ向かう先 (URL, フラグメント)。ページの無い節は、トップページの対応する節"""
    if node.page:
        return node.url, ''
    first = first_page(node)
    if first:
        frag = ANCHORS.get(posixpath.dirname(first).split('/')[0])
        if frag:
            return '', frag
    return None


def href(from_url, node):
    t = target(node)
    if t is None:
        return None
    return rel_url(from_url, t[0]) + ('#' + t[1] if t[1] else '')


MENU_FILE = os.path.join(HERE, 'menu.yml')
MENU = None     # menu.yml の項目（load_menu）。None なら、.nav.yml から自動で作るメニュー


def menu_target(spec, where):
    """menu.yml の page: に書いた原稿のパス（`INDEX.md#見出し`、まとめた元ページの `functions/IHASH.md` も可）の行き先 (URL, フラグメント)"""
    path, _, frag = spec.partition('#')
    path = 'index.md' if path == 'INDEX.md' else path
    if path in MD_PAGES:
        return page_url(path), frag
    if path in prepare_site.MERGED:
        page, prefix = prepare_site.MERGED[path]
        return page_url(page), prepare_site.FRAGMENTS.get((path, frag), prefix) if frag else prefix
    error(f'{where}: page: {spec} の原稿が無い')
    return None


def load_menu():
    """oldstyle/menu.yml の menu: を読む。各項目は title:（必須）、page:（原稿）か url:（外部）、children:（下の項目）"""
    if not os.path.exists(MENU_FILE):
        return None
    with open(MENU_FILE, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    def parse(items, where):
        out = []
        for i, it in enumerate(items or []):
            here = f'menu.yml {where}[{i}]'
            if not isinstance(it, dict) or not it.get('title'):
                error(f'{here}: title: が無い')
                continue
            if 'page' in it and 'url' in it:
                error(f'{here}: page: と url: は同時に書けない')
            target = None
            if it.get('page'):
                t = menu_target(it['page'], here)
                target = ('page',) + t if t else None
            elif it.get('url'):
                target = ('ext', it['url'])
            out.append({'title': str(it['title']), 'target': target, 'children': parse(it.get('children'), f'{where}[{i}]')})
        return out
    return parse(data.get('menu'), 'menu')


def custom_menu_html(items, current_url, from_url):
    """menu.yml のメニュー。旧版の MenuBar と同じく、下の階層まで常に全部出す"""
    def li(it):
        label = esc(it['title'])
        t = it['target']
        if t and t[0] == 'ext':
            label = f'<a href="{esc(t[1])}">{label}</a>'
        elif t:
            link = rel_url(from_url, t[1]) + ('#' + t[2] if t[2] else '')
            cur = ' aria-current="page"' if current_url is not None and t[1] == current_url and not t[2] else ''
            label = f'<a href="{link}"{cur}>{label}</a>'
        sub = '\n<ul>\n' + '\n'.join(li(c) for c in it['children']) + '\n</ul>\n' if it['children'] else ''
        return f'<li>{label}{sub}</li>'
    return '<ul>\n' + '\n'.join(li(it) for it in items) + '\n</ul>'


def menu_html(root, current, from_url):
    """左のメニュー。menu.yml があればその定義、無ければ .nav.yml から作る"""
    if MENU is not None:
        return custom_menu_html(MENU, current.url if current is not None else None, from_url)
    return nav_menu_html(root, current, from_url)


def nav_menu_html(root, current, from_url):
    """.nav.yml から作るメニュー。トップの項目は常に出し、いま開いているページのある節だけ、下の階層を開く"""
    opened = set()
    n = current
    while n is not None:
        opened.add(id(n))
        n = n.parent

    def li(node):
        label = esc(node.title)
        link = href(from_url, node)
        if link:
            cur = ' aria-current="page"' if node is current else ''
            label = f'<a href="{link}"{cur}>{label}</a>'
        sub = ''
        if node.children and id(node) in opened:
            sub = '\n<ul>\n' + '\n'.join(li(c) for c in node.children) + '\n</ul>\n'
        return f'<li>{label}{sub}</li>'
    return '<ul>\n' + '\n'.join(li(c) for c in root.children) + '\n</ul>'


def breadcrumb_html(node, from_url):
    # 旧版の「Top(FrontPage)」と同じく、トップページでも出す（そのページ自身は文字だけ）
    if node is None:
        return f'<nav id="breadcrumb" aria-label="パンくずリスト">\n<ul>\n<li><a href="{rel_url(from_url, "")}">トップ</a></li>\n</ul>\n</nav>\n'
    if node.page == 'index.md':
        return '<nav id="breadcrumb" aria-label="パンくずリスト">\n<ul>\n<li>トップ</li>\n</ul>\n</nav>\n'
    chain = []
    n = node
    while n.parent is not None:
        chain.append(n)
        n = n.parent
    chain.reverse()
    items = [f'<li><a href="{rel_url(from_url, "")}">トップ</a></li>']
    for n in chain:
        link = href(from_url, n) if n is not node else None
        items.append(f'<li><a href="{link}">{esc(n.title)}</a></li>' if link else f'<li>{esc(n.title)}</li>')
    return '<nav id="breadcrumb" aria-label="パンくずリスト">\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</nav>\n'


def navigation_html(node, prev, nxt, from_url, bottom):
    """旧版の ul.navi（Prev / Home / Next）。下のほうには、行き先のページ名も付く。Home は節（無ければトップページ）"""
    if prev is None and nxt is None:
        return ''
    home = node.parent if node.parent is not None and node.parent.depth >= 1 and target(node.parent) else None
    home_href = href(from_url, home) if home is not None else rel_url(from_url, '')

    def item(cls, label, link, name, rel=None):
        if link is None:
            return f'<li class="{cls}"></li>'
        a = f'<a href="{link}"' + (f' rel="{rel}"' if rel else '') + f'>{label}</a>'
        if bottom and name:
            a += f'<br><a href="{link}">{esc(name)}</a>'
        return f'<li class="{cls}">{a}</li>'
    items = [item('navi_left', 'Prev', href(from_url, prev) if prev else None, prev and prev.title, 'prev'),
             item('navi_none', 'Home', home_href, home.title if home is not None else 'トップページ'),
             item('navi_right', 'Next', href(from_url, nxt) if nxt else None, nxt and nxt.title, 'next')]
    nav = '<nav class="navi" aria-label="前後のページ">\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</nav>\n'
    return '<hr class="full_hr">\n' + nav if bottom else nav + '<hr class="full_hr">\n'


# ---------------------------------------------------------------- Markdown → HTML

def resolve(src, href_):
    """原稿 src（_site_src/ からのパス）の中のリンク href の行き先。(行き先のパス, フラグメント) か None（外部・ページ内）"""
    if not href_ or href_.startswith(('#', '/', 'mailto:', 'tel:', 'javascript:')) or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', href_):
        return None
    path, _, frag = href_.partition('#')
    return posixpath.normpath(posixpath.join(posixpath.dirname(src), path)), frag


def rewrite_links(tree, src, from_url):
    for a in tree.iter('a'):
        r = resolve(src, a.get('href'))
        if not r:
            continue
        t, frag = r
        frag = '#' + frag if frag else ''
        if t in MD_PAGES:
            a.set('href', rel_url(from_url, page_url(t)) + frag)
        elif os.path.exists(os.path.join(RAW, t)) and t.endswith('.md'):
            # ページにならない生の原稿（サイトにも原稿のまま置かれる）
            a.set('href', rel_file(from_url, t) + frag)
        elif os.path.isfile(os.path.join(SRC, t)):
            a.set('href', rel_file(from_url, t) + frag)
        else:
            error(f'{src}: リンク先 {a.get("href")} が無い')
    for img in tree.iter('img'):
        r = resolve(src, img.get('src'))
        if not r:
            continue
        if os.path.isfile(os.path.join(SRC, r[0])):
            img.set('src', rel_file(from_url, r[0]))
            img.set('loading', 'lazy')
        else:
            error(f'{src}: 画像 {img.get("src")} が無い')


def text_of(el):
    return re.sub(r'\s+', ' ', el.text_content()).strip()


def heading_text(el):
    """見出しの文字（末尾の † のリンクは除く）"""
    c = copy.deepcopy(el)
    for a in c.xpath('.//a[@class="anchor_super"]'):
        a.drop_tree()
    return text_of(c)


def nested_list(items):
    """[(見出しの深さ, リンクの HTML)] を、深さで入れ子にした ul にする"""
    out = ['<ul>']
    i = 0
    while i < len(items):
        level, link = items[i]
        i += 1
        sub = []
        while i < len(items) and items[i][0] > level:
            sub.append(items[i])
            i += 1
        out.append(f'<li>{link}{nested_list(sub) if sub else ""}</li>')
    out.append('</ul>')
    return '\n'.join(out)


def add_contents(tree, levels):
    """ページの先頭の目次（旧版の div.contents）。最初の見出しの前に置く"""
    heads = [h for h in tree.iter('h2', 'h3') if h.get('id') and int(h.tag[1]) in levels]
    if len(heads) < 3:
        return
    items = [(int(h.tag[1]), f'<a href="#{esc(h.get("id"))}">{esc(heading_text(h))}</a>') for h in heads]
    box = lxml.html.fragment_fromstring('<div class="contents">\n' + nested_list(items) + '\n</div>')
    heads[0].addprevious(box)


def render(md, from_url):
    text = read(os.path.join(SRC, md))
    html = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG, output_format='html').convert(text)
    tree = lxml.html.fragment_fromstring(html, create_parent='div')
    rewrite_links(tree, md, from_url)
    add_contents(tree, (2,) if md == 'index.md' else (2, 3))
    return tree


def inner_html(tree):
    out = (tree.text or '')
    out = esc(out) if out.strip() else ''
    for c in tree:
        out += etree.tostring(c, method='html', encoding='unicode')
    return out


def description_of(tree):
    for p in tree.iter('p'):
        t = text_of(p)
        if t:
            return t[:110] + ('…' if len(t) > 110 else '')
    return SITE_DESCRIPTION


def search_entries(tree, label, url):
    """検索の索引の行: [ページの名前, 節の題, サイトのルートからの URL, 本文]。節は H1〜H3 の区切り"""
    entries = []
    title, frag, buf = label, '', []

    def flush():
        text = ' '.join(buf).strip()
        if text or title:
            entries.append([label, title, url + ('#' + frag if frag else ''), re.sub(r'\s+', ' ', text)])

    for el in tree:
        if not isinstance(el.tag, str):
            continue
        if el.tag in ('h1', 'h2', 'h3'):
            flush()
            buf = []
            title = heading_text(el)
            frag = el.get('id', '')
        elif 'contents' not in (el.get('class') or '').split():
            buf.append(text_of(el).replace('†', ''))   # 節の中の見出し（H4 など）の † は、本文に混ぜない
    flush()
    return entries


# ---------------------------------------------------------------- 出力

def head_extra(url, page_title, description):
    """canonical・OGP・Twitter カード"""
    ogp = OGP.get(url, {})
    title = ogp.get('title', f'{page_title} - {SITE_NAME}' if url else SITE_NAME)
    description = ogp.get('description', description)
    full = SITE_URL + url
    out = f'<link rel="canonical" href="{esc(full)}">\n'
    out += (f'<meta property="og:type" content="{"article" if url else "website"}">\n'
            f'<meta property="og:site_name" content="{esc(SITE_NAME)}">\n'
            f'<meta property="og:title" content="{esc(title)}">\n'
            f'<meta property="og:description" content="{esc(description)}">\n'
            f'<meta property="og:url" content="{esc(full)}">\n'
            '<meta property="og:locale" content="ja_JP">\n')
    if 'image' in ogp:
        image = esc(SITE_URL + ogp['image'])
        out += (f'<meta property="og:image" content="{image}">\n<meta property="og:image:width" content="1200">\n'
                f'<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">\n'
                f'<meta name="twitter:image" content="{image}">\n')
    else:
        out += '<meta name="twitter:card" content="summary">\n'
    out += f'<meta name="twitter:title" content="{esc(title)}">\n<meta name="twitter:description" content="{esc(description)}">\n'
    return out


def build_pages(root):
    pages = flatten(root, [])
    nodes = {n.page: n for n in pages}
    for md in MD_PAGES:
        if md not in nodes:
            error(f'{md} が .nav.yml に無い（メニューに出せない。新しいディレクトリは .nav.yml に加える）')
    if errors:
        return None
    template = string.Template(read(os.path.join(HERE, 'templates', 'page.html')))
    index = []
    for i, node in enumerate(pages):
        url = node.url
        tree = render(node.page, url)
        prev = pages[i - 1] if i > 0 else None
        nxt = pages[i + 1] if i + 1 < len(pages) else None
        h1 = tree.find('h1')
        page_title = heading_text(h1) if h1 is not None else node.title
        description = description_of(tree)
        head = head_extra(url, page_title, description)
        if prev:
            head += f'<link rel="prev" href="{rel_url(url, prev.url)}">\n'
        if nxt:
            head += f'<link rel="next" href="{rel_url(url, nxt.url)}">\n'
        content = inner_html(tree)
        write(posixpath.join(url, 'index.html'), template.substitute(
            title=esc(page_title if not url else f'{page_title} - {SITE_NAME}'), description=esc(description), head=head,
            root=root_of(url), home=rel_url(url, ''), body_attr=' class="y6"' if 'y6-hero' in content else '',
            breadcrumb=breadcrumb_html(node, url), menu=menu_html(root, node, url), content=content,
            navigation_top=navigation_html(node, prev, nxt, url, False),
            navigation_bottom=navigation_html(node, prev, nxt, url, True)))
        index.extend(search_entries(tree, node.title, url))
    build_search_page(root, template)
    build_404(root, template)
    write('search-index.js', 'window.YAYA_INDEX=' + json.dumps(index, ensure_ascii=False, separators=(',', ':')) + ';\n')
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          ''.join(f'<url><loc>{esc(SITE_URL + n.url)}</loc></url>\n' for n in pages) + '</urlset>\n')
    return pages


def build_search_page(root, template):
    url = 'search/'
    content = ('<h1>検索</h1>\n<form id="search-form" action="./">\n<p><input id="search-q" name="q" type="search" size="30" autocomplete="off"> '
               '<button type="submit">検索</button></p>\n</form>\n<div id="search-results"></div>\n')
    write(url + 'index.html', template.substitute(
        title=esc(f'検索 - {SITE_NAME}'), description='YAYA マニュアルの内部検索', head='<meta name="robots" content="noindex">\n',
        root=root_of(url), home=rel_url(url, ''), body_attr='', breadcrumb=breadcrumb_html(Node('検索', depth=1, parent=root), url),
        menu=menu_html(root, None, url), content=content, navigation_top='', navigation_bottom=''))


def build_404(root, template):
    # どの深さの URL で開かれるかわからないので、リンクはサイトのルートからの絶対パス（SITE_PATH）にする
    content = '<h1>ページが見つかりません</h1>\n<p>お探しのページは、移動したか、無くなったようです。左のメニューか、上の検索欄から探してください。</p>\n'
    write('404.html', template.substitute(
        title=esc(f'ページが見つかりません - {SITE_NAME}'), description='ページが見つかりません', head='<meta name="robots" content="noindex">\n',
        root=SITE_PATH, home=SITE_PATH, body_attr='', breadcrumb=breadcrumb_html(None, None), menu=menu_html(root, None, None), content=content,
        navigation_top='', navigation_bottom=''))


def copy_static():
    """静的ファイル（CSS・JS・ヘッダの画像）、_site_src/ の .md 以外（assets/・attachment/・llms.txt・転送 HTML）、
    生の Markdown 原稿（llms.txt や INDEX.md の相対リンクを、サイト上でも辿れるようにする）を出力に置く"""
    shutil.copytree(STATIC, OUT, dirs_exist_ok=True)
    for base, _, names in os.walk(SRC):
        for name in names:
            if name.endswith('.md') or name == '.nav.yml':
                continue
            rel = os.path.relpath(os.path.join(base, name), SRC)
            dst = os.path.join(OUT, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(os.path.join(base, name), dst)
    shutil.copytree(RAW, OUT, dirs_exist_ok=True)


MD_PAGES = set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-prepare', action='store_true', help='_site_src/ を作り直さない')
    args = ap.parse_args()
    if not args.no_prepare:
        prepare_site.main()
    for base, _, names in os.walk(SRC):
        for name in names:
            if name.endswith('.md'):
                MD_PAGES.add(os.path.relpath(os.path.join(base, name), SRC).replace(os.sep, '/'))
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    copy_static()
    if args.no_prepare:
        # まとめた元ページ（functions/IHASH.md など）の行き先の表は、prepare_site.main() が作る。menu.yml が使うので、ここでも作る
        prepare_site.register_functions()
        prepare_site.register_grammar()
    root = load_nav()
    ANCHORS.update(index_anchors())
    global MENU
    MENU = load_menu()
    pages = build_pages(root)
    if pages is None or errors:
        sys.exit(f'ビルドに失敗: エラー {len(errors)} 件')
    print(f'{len(pages)} ページを {os.path.relpath(OUT)} に出力した')


if __name__ == '__main__':
    main()
