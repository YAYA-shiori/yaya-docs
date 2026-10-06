# TOLOWER
**Category:** 文字列操作

## Signature
```
TOLOWER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換したい文字列 |
| locale | （省略可）ロケール名。省略時はCモード（A-Zのみa-zに変換） |

## Returns
- 成功: 変換後の小文字文字列
- 失敗: VOID

## Description
文字列中の大文字をすべて小文字に変換して返す。localeを省略した場合はCモード（A-Zのみa-zに変換）となる。

localeには `"ja-JP"` `"tr_TR"` `"tr_TR.UTF-8"` のような名前を指定する。そのロケールの規則で変換し、非ASCIIの文字（`É`→`é`、全角英字など）も変換される。トルコ語（`tr-TR`）では `I` が `ı` になる。`"C"` と `"POSIX"` はCモード、空文字列はOSのユーザー設定のロケールになる。[GETSETTING](GETSETTING.md) の `coreinfo.locale` が返す名前も使える。

- Windows: OSのロケール名を使う。`"Japanese_Japan.932"` のようなCランタイムのロケール名も使える
- Linux / macOS: OSに入っているロケール（`locale -a` に出るもの）が必要。`tr_TR` のように文字コードを省いたときは、UTF-8版を先に探す
- 他の処理や、プロセスのロケールには影響しない

使えないロケールを指定すると、警告 W0012（[GETLASTERROR](GETLASTERROR.md) は 12）を出し、Cモードで変換した結果を返す。

## Example
```
_str = 'sAkuRa'
_str = TOLOWER( _str )
_str // 'sakura'
```

## Compatibility
- YAYA: 初期バージョンより（localeパラメータはTc569-5以降）
- Tc605-3: localeの扱いを変更。ロケールは `ja-JP` のような名前で指定でき、プロセスのロケールを切り替えずに変換する。使えないロケールは警告 W0012 を出してCモードで変換する（以前は警告なしで、そのときのロケールのまま変換していた）
- AYA: 5.8以降

## See Also
- TOUPPER
