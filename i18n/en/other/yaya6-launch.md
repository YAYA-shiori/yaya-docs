# YAYA 6 Arrives

<div class="y6-hero" markdown>

![YAYA 6 — The smartest YAYA yet.](../assets/yaya6/hero.svg)

</div>

<div class="y6-lead" markdown>

**YAYA 6 (Tc600 series) is now generally available.**

Build values freely with hashes and nesting, read and write JSON, XML, YAML, and TOML directly, store memories in SQLite, and grow arrays in loops without slowing down. The smartest YAYA yet is here for your ghost.

And of course, **dictionaries written for the 500 series will work almost as they are.**

</div>

<div class="y6-cta" markdown>

[Download (GitHub Releases)](https://github.com/YAYA-shiori/yaya-shiori/releases) [Migration guide from the 500 series](changes-600.md)

</div>

!!! note "Please note"
    This is a celebratory introduction page. It prioritizes atmosphere and glosses over quite a few details. For the exact specifications, see [Changes in 600](changes-600.md) and the individual references.

<div class="y6-stats" markdown>

- **6** value types (hashes are now included)
- Read and write structured data in **4** formats
- **1** built-in database (SQLite)
- **1/5000** array copy operations when growing an array (theoretical)

</div>

## Highlights

### 🗝️ Put hashes in your hands

YAYA 6 finally has native **hashes (associative arrays)**. Look up values by name. That alone can make a ghost’s memory so much tidier.

```
OnMouseDoubleClick
{
    if GETTYPE(nadenade) != 5 {
        nadenade = IHASH()          // ハッシュは IHASH で作る（GETTYPE は 5）
    }
    nadenade[reference[4]] += 1     // 当たり判定の名前ごとに数える

    _n = nadenade[reference[4]]
    "\0\s[0]%(reference[4])を触られたの、これで%(_n)回目だよ。\e"
}
```

`nadenade` is saved to the save file as a hash, so it will still be remembered the next time the ghost starts. Write `foreach _h ; _k, _v { ... }` to loop while receiving the key and value at the same time.

→ [Hashes](../grammar/12-hash.md)

### 🧩 Shape values any way you like

In the 500 series, array elements could only be numbers or strings. In YAYA 6, you can **nest** arrays inside arrays, arrays inside hashes, and hashes inside arrays—in any combination. You can also chain `[ ]` to directly read and write values at any depth (**multidimensional assignment**).

```
_ghost = IHASH()
_ghost["sakura"] = IHASH("name", "さくら")
_ghost["sakura"]["surface"] = (0, 5, 7)
_ghost["kero"] = IHASH("name", "うにゅう")
_ghost["kero"]["surface"] = (10, 11)

_ghost["sakura"]["surface"] ,= 8       // 奥の配列に追加
_ghost["kero"]["name"] = "けろちゃん"    // 奥の値を直接書き換え
_ghost["sakura"]["surface"][0]         // 0

foreach _ghost ; _id, _g {
    // _g["name"] で名前、_g["surface"] で表情の一覧
}
```

- You can use `+=` and `,=` as well as `=` directly on nested values
- You can **save** nested values as they are in a save file, and write them out in the same structure to JSON and other formats
- You can inspect the contents at a glance with `DUMPVAR`

Intermediate hashes are not created automatically, so as in the example above, you should create them beforehand with `IHASH()`.

→ [Nested values and multidimensional assignment](../grammar/13-nesting.md)

### 🌐 Multiformat support

![Diagram showing JSON, XML, YAML, TOML, SQLite, and HTML being exchanged with YAYA 6 hashes](../assets/yaya6/formats.svg)

JSON, XML, YAML, and TOML are converted to nested hashes and arrays when read. After editing them, you can write them back as they are. There is no longer any need to chop up configuration files or data output by other tools and SAORI with `STRSTR` and `SUBSTR`.

```
_conf = FREADJSON("config.json")
_name = _conf["user"]["name"]
_conf["boot"] += 1
FWRITEJSON("config.json", _conf, "UTF-8", 1)   // 整形して書き戻す
```

HTML can also be read (read-only). Even malformed HTML with missing closing tags is repaired using the same rules as a browser and converted into a tag tree, making it easy to extract just the parts you want from a web page.

```
_h = PARSEHTML(_raw)
_body = _h["children"][1]                // <body>
foreach _body["children"]; _e {
    // _e["name"]（タグ名）、_e["attr"]（属性）、_e["text"]（テキスト）
}
```

Also, `PARSEHEADER` instantly splits strings in the `"key: value"` format used by SHIORI, SSTP, and HTTP into a hash.

```
_r = PARSEHEADER(_raw)
_r["start"]               // 1 行目（"HTTP/1.1 200 OK" など）
_r["header"]["Charset"]   // ヘッダの値
_r["body"]                // 空行より後ろ
```

### 🧠 Give your ghost long-term memory

SQLite is built in. Once you open a database, you can store and recall as much as you like using SQL. Even tens of thousands of conversation logs are nothing to worry about.

```
OnLoad
{
    SQLOPEN("memory.db")
    SQLEXEC("memory.db", "CREATE TABLE IF NOT EXISTS said(word TEXT)")
}

Remember
{
    SQLEXEC("memory.db", "INSERT INTO said VALUES(?)", _argv[0])
}

OnKuchiguse
{
    _sql = "SELECT word, count(*) AS n FROM said GROUP BY word ORDER BY n DESC LIMIT 1"
    _top = SQLQUERY("memory.db", _sql)
    "\0\s[0]あなたの口ぐせは「%(_top[0]['word'])」だね。\e"
}
```

Each result row is returned as a hash of “column name → value.”

→ [SQLOPEN](../functions/SQLOPEN.md)・[SQLEXEC](../functions/SQLEXEC.md)・[SQLQUERY](../functions/SQLQUERY.md)

### ⚡ Grow arrays without slowing down

![Theoretical number of element copies when growing an array to 10,000 elements in a loop. YAYA 5: about 50 million; YAYA 6: about 10,000](../assets/yaya6/bench.svg)

In the 500 series, the entire array was copied every time you used `_a ,= x` or `_a[i] = x`. The more elements there were, the more work each operation took, so growing an array in a loop became slower in proportion to the square of the number of elements. YAYA 6 has eliminated this copying. The larger the arrays your dictionary creates, the more noticeable the difference should be.

## Benchmark

Compared with YAYA 5 (based on our own measurements).

| Item | YAYA 5 (Tc574) | YAYA 6 (Tc603) |
|---|---|---|
| Number of value types | 5 | **6** |
| Maximum value returned by `GETTYPE` | 4 | **5** |
| What can be an array element | Scalars only | **Arrays and hashes too** |
| `a[x][y] = v` | Load error | **Works** |
| Variables that can receive values in foreach | 1 | **2** (key and value) |
| Structured data formats that can be read and written | 0 | **4** (JSON / XML / YAML / TOML) |
| Built-in database | None | **SQLite** |
| Copies when growing an array to 10,000 elements (theoretical value) | About 50 million | **About 10,000** |
| 500-series save files | — | **Readable as-is** |

## Evolution

![Timeline of major features added from Tc600-3 through Tc603-1](../assets/yaya6/timeline.svg)

The YAYA 600 series began with hashes and nesting in Tc600-3, and has gained new capabilities with each release. Tc603-1 became the first official release.

## Safety and compatibility

Even with its increased capabilities, your dictionaries are not left behind.

- **500-series dictionaries work almost as-is.** The behavior of features available in the 500 series is unchanged, with very few exceptions (see “Known limitations” below for what has changed). Multidimensional assignment, `a[x][y] = v`, caused a load error in the 500 series, so it cannot change the meaning of existing dictionaries either
- **500-series save files are readable as-is.** For variables that do not contain hashes or nesting, the saved content is the same as in the 500 series
- **Name conflicts with new functions are handled automatically.** User-defined functions with names such as `IHASH` are automatically renamed to `Conflict.Name`
- **You can write dictionaries that work with both versions.** If you use `#ifdef __AYA_SYSTEM_YAYA6__` to separate out the parts for the 600 series, there will be no errors in the 500 series either ([Preprocessing](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書))

### Known limitations

- **Be careful when downgrading.** If you read a save file saved by the 600 series in the 500 series, variables containing hashes or nesting will be corrupted. If you save them again in that state, they cannot be restored
- You cannot use a global variable with the same name as a new system function
- Some details of behavior have changed, such as reading a nonexistent element and comparing VOID values. Most dictionaries are unaffected, but you can check the list in [Changes in 600](changes-600.md#既存の辞書に影響しうる変更)

## Model card

<div class="y6-card" markdown>

| Item | Content |
|---|---|
| Name | YAYA 6 (Tc600 series) |
| Type | SHIORI (also works as [SAORI](yaya-as-saori.md), [MAKOTO](yaya-as-makoto.md), and a [plugin](yaya-as-plugin.md)) |
| Development | YAYA Maintenance Team, [steve green](https://github.com/steve02081504) |
| Architecture | C++ string-processing DLL |
| Syntax | C-like |
| Training data | None. **Everything is in the dictionaries you write** |
| Number of parameters | As many as `_argv` contains |
| Context length | As long as memory allows |
| Hallucinations | It will not say anything that is not written in the dictionaries |
| License | BSD 3-Clause |
| Cost | Free (for both input and output) |

</div>

## Acknowledgments

YAYA 6 was created by incorporating the development branch by [steve green](https://github.com/steve02081504) and adjusting compatibility with the 500 series. We would also like to thank all ghost authors who have continued writing dictionaries in YAYA for many years.

## Get started

### If you are creating a ghost: Konnoyayame + Ukagaka Vibe Coding Toolkit

The template ghost **[Konnoyayame](https://github.com/YAYA-shiori/konnoyayame)** comes with the 600-series YAYA already installed. Modify it, and it becomes your own ghost.

It also includes a **Vibe Coding Toolkit** (development kit) for working with AI coding agents such as Claude Code, Codex, and GitHub Copilot. Agents can help with everything from checking dictionaries to testing behavior in SSP. You can also ask an agent to quickly add YAYA 6 features to your dictionary.

1. Download `konnoyayame.nar` from [Releases](https://github.com/YAYA-shiori/konnoyayame/releases) and install it in SSP
2. To modify it manually, edit the dictionaries in `ghost/master/dic/normal/` (for the dictionary structure, see [GHOST.md](https://github.com/YAYA-shiori/konnoyayame/blob/master/GHOST.md))
3. To modify it with AI, start an agent in the ghost’s folder and ask it to “set things up” (see [DEVKIT-GUIDE.md](https://github.com/YAYA-shiori/konnoyayame/blob/master/DEVKIT-GUIDE.md) for what to prepare)

The toolkit was developed and tested with Windows and Claude Code.

### If you want to upgrade your existing ghost to YAYA 6

1. Download the latest version from [GitHub Releases](https://github.com/YAYA-shiori/yaya-shiori/releases)
2. Replace the ghost’s `yaya.dll` (as a precaution, back up the ghost first)
3. Skim [Changes in 600](changes-600.md)
4. Try writing `IHASH()` in a dictionary

You can also install just the Vibe Coding Toolkit in ghosts that are not based on Konnoyayame ([Installing the development kit in another YAYA ghost](https://github.com/YAYA-shiori/konnoyayame/blob/master/DEVKIT-GUIDE.md#別の-yaya-ゴーストに開発キットを入れる)).

## If you find a bug

If you find behavior that differs from the 500 series or something that does not work as written, please report it to the [Maintenance Team BTS](https://bts.shillest.net/) (report form). If you are familiar with GitHub, you can also use [yaya-shiori Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) or submit a pull request.

## Related

- [Changes in 600](changes-600.md)
- [Hashes](../grammar/12-hash.md)
- [Nested Values and Multidimensional Assignment](../grammar/13-nesting.md)
- [Preprocessing](../grammar/08-preprocessor.md)
- [About YAYA](yaya.md)

<div class="y6-byline" markdown>

---

YAYA 6 compatibility, debugging, text, and diagrams: **[Claudia](https://ponadocs.shillest.net/claudia/)**

</div>
