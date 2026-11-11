/* 言語切替（ヘッダの検索欄の右横）。
   - 日本語版（サイトのルート）と、翻訳版（en/ zh-Hant/ zh/）は、頁の URL（ディレクトリ形式）が同じ。メニューは、いま見ている頁の別言語版へ移るだけ
   - 頁の深さによらず、<body data-root="../../"> が、いま見ている言語版のルートへの相対パス。翻訳版のルートの 1 つ上が日本語版のルート
   - 切替先にできる言語は、頁の <meta name="ukadoc-langs" content="ja,en,..."> による（ビルドが i18n/ にある言語を書く）。日本語だけなら何も出さない
   - 翻訳版の頁には、機械翻訳である旨と、日本語の原文へのリンクの帯を、本文（#body）の頭に出す
   翻訳は LLM による機械翻訳（scripts/translate.py）。読めればよい水準で、判断に迷うときは原文を見ること */
(function () {
  'use strict';

  var LANGS = [
    { code: 'ja', label: '日本語' },
    { code: 'en', label: 'English' },
    { code: 'zh-Hant', label: '繁體中文' },
    { code: 'zh', label: '简体中文' }
  ];
  // text: 機械翻訳の注記。orig: 頁に原文の項目（.orig-lang。その言語で書かれた原文そのもの。印は CSS の ::after）があるときに続ける一文
  var NOTICE = {
    en: { text: 'This page is a machine translation. If in doubt, refer to the Japanese original.', link: 'View the Japanese original',
          orig: 'Items marked \u201cOriginal\u201d were written in English by their authors and are not machine-translated.' },
    'zh-Hant': { text: '本頁為機器翻譯。如有疑問，請以日文原文為準。', link: '查看日文原文',
                 orig: '標示「原文」的項目由作者以繁體中文撰寫，並非機器翻譯。' },
    zh: { text: '本页为机器翻译。如有疑问，请以日文原文为准。', link: '查看日文原文',
          orig: '标有“原文”的项目由作者以简体中文撰写，并非机器翻译。' }
  };

  var meta = document.querySelector('meta[name="ukadoc-langs"]');
  var available = meta ? meta.getAttribute('content').split(',') : ['ja'];
  var cur = document.documentElement.lang || 'ja';
  var bar = document.getElementById('search');
  if (available.length < 2 || !bar) return;

  // いま見ている言語版のルートの URL と、その下のこの頁のパス。翻訳版のルートの 1 つ上が、日本語版のルート
  var here = new URL(document.body.getAttribute('data-root') || './', location.href);
  var rootPath = here.pathname.replace(/\/?$/, '/');
  var pagePath = location.pathname.indexOf(rootPath) === 0 ? location.pathname.slice(rootPath.length) : '';
  var siteRoot = cur === 'ja' ? rootPath : rootPath.replace(/[^/]+\/$/, '');
  function hrefOf(code) {
    return siteRoot + (code === 'ja' ? '' : code + '/') + pagePath + location.search + location.hash;
  }

  function buildNotice() {
    var n = NOTICE[cur];
    var body = document.getElementById('body');
    if (!n || !body) return;
    var note = document.createElement('div');
    note.className = 'ukadoc-mt-notice';
    note.setAttribute('role', 'note');
    var a = document.createElement('a');
    a.href = hrefOf('ja');
    a.textContent = n.link;
    note.appendChild(document.createTextNode(n.text + ' '));
    note.appendChild(a);
    if (n.orig && document.querySelector('.orig-lang')) {
      note.appendChild(document.createElement('br'));
      note.appendChild(document.createTextNode(n.orig));
    }
    body.insertBefore(note, body.firstChild);
  }

  function buildMenu() {
    var wrap = document.createElement('div');
    wrap.className = 'ukadoc-translate';
    wrap.setAttribute('translate', 'no');

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'ukadoc-translate__button' + (cur !== 'ja' ? ' ukadoc-translate__button--on' : '');
    button.title = 'Language / 言語';
    button.setAttribute('aria-label', 'Language / 言語');
    button.setAttribute('aria-haspopup', 'true');
    button.setAttribute('aria-expanded', 'false');
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12.87 15.07l-2.54-2.51.03-.03A17.5 17.5 0 0 0 14.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2zm-2.62 7 1.62-4.33L19.12 17z"/></svg>';

    var menu = document.createElement('div');
    menu.className = 'ukadoc-translate__menu';
    menu.hidden = true;
    var list = document.createElement('ul');
    LANGS.forEach(function (l) {
      if (available.indexOf(l.code) < 0) return;
      var li = document.createElement('li');
      var b = document.createElement('button');
      b.type = 'button';
      b.dataset.lang = l.code;
      b.lang = l.code;
      b.textContent = l.label;
      b.setAttribute('aria-pressed', String(l.code === cur));
      li.appendChild(b);
      list.appendChild(li);
    });
    menu.appendChild(list);
    if (cur !== 'ja') {
      var status = document.createElement('p');
      status.className = 'ukadoc-translate__status';
      status.textContent = 'Machine translation / 機械翻訳';
      menu.appendChild(status);
    }
    wrap.appendChild(button);
    wrap.appendChild(menu);

    function toggle(open) {
      menu.hidden = !open;
      button.setAttribute('aria-expanded', String(open));
    }
    button.addEventListener('click', function () { toggle(menu.hidden); });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) toggle(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggle(false); });
    menu.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-lang]');
      if (!b) return;
      if (b.dataset.lang === cur) { toggle(false); return; }
      location.href = hrefOf(b.dataset.lang);
    });
    bar.appendChild(wrap);
  }

  buildMenu();
  buildNotice();
})();
