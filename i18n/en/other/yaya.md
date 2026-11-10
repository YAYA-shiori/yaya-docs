# About YAYA

## What are YAYA and AYA?

- It is pronounced “Yaya.” It is a DLL for processing strings.
- It is one of the basic components called SHIORI (栞, shiori) that control the brain of a ghost (a character that stands on your desktop and runs on baseware such as [SSP](http://ssp.shillest.net/)).
- Other SHIORI implementations include [Satori](https://ukatech.shillest.net/satori-docs/), [Kawari](https://ukatech.shillest.net/kawari-docs/), and Yuna.
- If you want to migrate from Satori, see [Migrating from Satori](../startup/migration-from-satolili.md).

## Concept

- Its distinctive feature is syntax similar to C. If you have some programming experience, you may find it easy to get started.
- This manual also includes [Basics](../basic/) so that people with no programming experience can use it.
- Since it was designed as a general-purpose language, its uses are not limited to SHIORI. For uses other than SHIORI, see the following pages.
  - [YAYA as SAORI](yaya-as-saori.md)
  - [YAYA as MAKOTO](yaya-as-makoto.md)
  - [YAYA as a plugin](yaya-as-plugin.md)
- It is also used as SAORI by replacing the system dictionary.
- It is also possible to use it as a general-purpose embedded language for string processing, even outside of ghosts. For information about YAYA as a general-purpose language DLL, see [YAYA as a Windows DLL](../grammar/10-yaya-as-windows-dll.md).
- The distributed binary is `yaya.dll` for Windows. The source can also be built on Linux, FreeBSD, and macOS, and its operation has been tested there (only the Windows version is distributed). If you find something that does not work, please let us know.

## What does “designed as a general-purpose language” mean?

- `yaya.dll` by itself has no functionality for use as SHIORI. It is a general-purpose language DLL whose format merely conforms to the SHIORI specification.
- Therefore, it uses a set of YAYA script files called the “system dictionary” to operate as SHIORI.
- The [Grammar](../grammar/) and [System Functions](../functions/) sections of this manual explain YAYA as a general-purpose language. Its operation as SHIORI is explained on the [System Dictionary](../system/) pages.
- For this reason, you may find the manual's grammar section confusing when you refer to it for “using YAYA as a ghost's SHIORI” (for example, “There is no request function!” or “When are On~ events called?”).
- If you want to understand “YAYA as a ghost's SHIORI” in depth, we also recommend reading the [yaya_shiori3.dic](../system/yaya-shiori3-dic.md) page.

## Differences between YAYA and AYA

- AYA is a SHIORI created by umeici. Its final version is 5.8, and it is available from [::: et cetera.](http://umeici.onjn.jp/).
- YAYA is based on umeici's AYA Ver.5 and is maintained, modified, and developed further by the YAYA development team (the maintenance team).
- YAYA has the 500 series (Tc5xx-x) and the 600 series (Tc6xx-x, YAYA 6). The 600 series supports hashes, nested arrays, reading and writing JSON and XML, and SQLite. 500-series dictionaries work almost as-is by simply replacing `yaya.dll`. For details, see [Introducing YAYA 6](yaya6-launch.md) and [Changes in 600](changes-600.md).

### Which one should I use?

Here is a brief comparison to help you decide whether to use AYA or YAYA.

|  | New features and updates | Stability |
|---|---|---|
| AYA | △ AYA is no longer being updated. | ○ It has been a long time since AYA 5.8 was released, and it is stable. |
| YAYA | ○ The YAYA development team continues to add new features and release updates. | △ Because it is updated frequently, behavior may vary between versions. Check the changelog when updating. |

Simply put…

- If you already have a ghost running on AYA and are not particularly dissatisfied with its features, there is no problem with continuing to use AYA.
- If you are about to create a ghost or want to try new features as they are added, use YAYA. If you want to migrate from AYA, see [Migrating from AYA](../startup/migration-from-aya.md).

This manual focuses on YAYA.

## Distribution and related tools

- [Download (GitHub Releases)](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [Changelog](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)
- [Konnoyayame](https://github.com/YAYA-shiori/konnoyayame) — a YAYA template ghost
- [Tama](https://github.com/YAYA-shiori/tama/releases) — a tool for checking dictionary errors and debugging
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — a CI tool for checking dictionaries with GitHub Actions

## How this manual is organized

| What you want to know | Page |
|---|---|
| Get a quick overview of how to write YAYA | [Cheat sheet](../startup/cheatsheet.md) |
| Create a ghost for the first time | [Creating a ghost](../startup/creating-ghost.md), [Tutorial](../startup/tutorial-01-preparation.md) |
| I have no programming experience | [Basics](../basic/) |
| Learn the grammar | [Grammar](../grammar/) |
| Look up built-in functions | [Function list by use](../functions/), [System function list](../system/system-functions-index.md) |
| Learn about the system dictionary | [yaya_shiori3.dic](../system/yaya-shiori3-dic.md), [yaya_optional.dic](../system/yaya-optional-dic.md) |
| Learn various techniques | [Tips](../tips/) |
| When you run into problems | [Troubleshooting](troubleshooting.md) |
