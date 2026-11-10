# YAYA Manual

This manual summarizes how to use YAYA, the SHIORI for Ukagaka (ukagaka), and its specifications. It also brings together information and tips about YAYA and its predecessor, AYA.

We aim to make this manual understandable even to people who have never programmed before. If you find anything unclear or incorrect, feel free to let us know via [Seibihan BTS](https://bts.shillest.net/) (report form). If you are familiar with GitHub, you can also use [Issues](https://github.com/YAYA-shiori/yaya-docs/issues) or submit a Pull Request.

> For AI agents, we provide [llms.txt](https://yaya-shiori.github.io/yaya-docs/llms.txt), a guide to finding information. The Markdown source for each page is available as `.md` at the same path in the repository (for example: `https://yaya-shiori.github.io/yaya-docs/startup/cheatsheet.md`).

## Download

- [Download (GitHub Releases)](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [Changelog](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)

## YAYA v6 (commonly known as the Tc600 series)

- This release incorporates the development branch by [steve green](https://github.com/steve02081504), adjusts compatibility, and provides substantial enhancements.
- It has been extensively revised while maintaining high compatibility with the 500 series, with improvements such as more flexible variables, faster header parsing, parsers for XML/JSON, and a DB (SQLite).
- Just want a quick overview? → [Introducing YAYA 6](other/yaya6-launch.md)
- Want to migrate from YAYA Tc5xx-x to Tc6xx-x (from v5 to v6)? → [Changes in 600](other/changes-600.md) (Just replace `yaya.dll`; your dictionaries and save files will continue to work as they are. There are only a few things to watch out for, such as function name conflicts.)

## For beginners

- What are YAYA and AYA? → [About YAYA](other/yaya.md)
- Want a quick overview of how to write YAYA? → [Cheat sheet](startup/cheatsheet.md)
- Want to create your first ghost? → [How to create a ghost](startup/creating-ghost.md)
- I made a ghost with AYA and want to move to YAYA → [Migrating from AYA](startup/migration-from-aya.md)
- I want to move from Satori to YAYA → [Migrating from Satori](startup/migration-from-satolili.md)

## Looking things up

- I've never programmed before! → [Basics](basic/)
- Want to learn YAYA syntax? → [Grammar](grammar/), [Cheat sheet](startup/cheatsheet.md)
- What built-in (system) functions are available? → [Function list by purpose](functions/)
- Want to look up a function by name? → [System function index](system/system-functions-index.md)
- Want to investigate or handle errors? → [Error handling functions](system/error-handling-functions.md)

You can also search using the search box at the top of the page.

## System dictionaries and templates

- About system dictionaries → [yaya_shiori3.dic](system/yaya-shiori3-dic.md), [yaya_optional.dic](system/yaya-optional-dic.md)
- About template ghosts → [How to create a ghost](startup/creating-ghost.md), [Simple YAYA template](other/simple-yaya-template.md)
- Want to write talk easily? → [talklib](other/talklib.md)
- Ways to use YAYA other than as SHIORI → [YAYA as SAORI](other/yaya-as-saori.md), [YAYA as MAKOTO](other/yaya-as-makoto.md), [YAYA as a plugin](other/yaya-as-plugin.md)

## When you need help

- Want to learn various techniques? → [Tips](tips/)
- Having trouble while creating something? → [Troubleshooting](other/troubleshooting.md)
- If you still cannot resolve the issue, or suspect a YAYA bug, ask at [Seibihan BTS](https://bts.shillest.net/) (report form). If you are familiar with GitHub, you can also use [yaya-shiori Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) or submit a Pull Request
- Searching [Development Information Search](http://ukadev.shillest.net/) may help you find an answer

## Related tools

- [Konnoyayame](https://github.com/YAYA-shiori/konnoyayame) — A YAYA template ghost
- [Tama (tama)](https://github.com/YAYA-shiori/tama/releases) — A tool for checking dictionary errors and debugging
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — A CI tool for checking dictionaries with GitHub Actions
- [ukagaka-doc-mcp](https://github.com/finelagusaz/ukagaka-doc-mcp) - A tool for having AI-assisted development look up Ukagaka-related specifications automatically
