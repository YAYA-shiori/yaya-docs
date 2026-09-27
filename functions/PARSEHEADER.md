# PARSEHEADER
**Category:** 型取得/変換

## Signature
```
PARSEHEADER( str [, conv ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTTP や SHIORI のようなヘッダ形式の文字列 |
| conv | 省略可。0 以外なら値を [TOAUTOEX](TOAUTOEX.md) と同じ規則で整数・実数に変換する。省略時は 0（変換しない） |

## Returns
- 成功時: 次のキーを持つハッシュ
- 失敗時: 空（VOID）

| キー | 内容 |
|------|------|
| `start` | 開始行（`GET SHIORI/3.0` や `HTTP/1.1 200 OK` など）。開始行がなければ空文字列 |
| `header` | ヘッダのキー→値のハッシュ。同じキーが複数あるときは後に出たものが残る |
| `key` | ヘッダのキーの配列（出現順、重複も含む） |
| `value` | ヘッダの値の配列（出現順）。`conv` が 0 以外なら変換後の値 |
| `rawvalue` | 変換前の値（文字列）の配列（出現順） |
| `body` | 空行より後ろの文字列。空行がなければ空文字列 |

## Description
HTTP や SHIORI・SAORI・SSTP のリクエスト／レスポンスのような「開始行 + `キー: 値` の行 + 空行 + 本文」の形の文字列を解析し、ハッシュと配列にまとめて返す。1 行ずつ [STRSTR](STRSTR.md) や [SUBSTR](SUBSTR.md) で切り出すよりも速い。

- 改行は CRLF と LF のどちらでもよい
- 最初の空行でヘッダが終わり、その後ろはすべて `body` になる
- 各行は最初の `:` でキーと値に分ける。値は `:` の直後の空白（スペースかタブ）を 1 つだけ飛ばしたもので、残りの空白はそのまま残す（`Key:  a` の値は ` a`）
- 最初の `:` より前が空、または空白を含む行はヘッダの行とみなさない。1 行目がそうなら開始行として `start` に入れ、2 行目以降なら無視する。このため開始行のない、ヘッダだけの文字列も解析できる
- キーの大文字・小文字は区別する
- `conv` を 0 以外にしたときの変換は [TOAUTOEX](TOAUTOEX.md) と同じで、文字列に戻したときに元と一致する場合だけ変換する。`12` は整数になるが、`007` や `1.5` は文字列のまま

`header` のハッシュはキー順に並ぶので、出現順が必要なときは `key` / `value` / `rawvalue` を使う。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない | W0009 | 9 |

## Example
```
request
{
	_r = PARSEHEADER(_argv[0], 1)
	// _argv[0] が
	//   GET SHIORI/3.0
	//   Charset: UTF-8
	//   ID: OnBoot
	//   Reference0: 12
	//   Reference1: 007
	// のとき

	_r["start"]                 // GET SHIORI/3.0
	_r["header"]["ID"]          // OnBoot
	_r["header"]["Reference0"]  // 12（整数）
	_r["header"]["Reference1"]  // 007（文字列）
	_r["key"]                   // Charset,ID,Reference0,Reference1
	_r["rawvalue"][2]           // 12（文字列）
}
```

```
_nl = CHR(13) + CHR(10)
_r = PARSEHEADER('HTTP/1.1 200 OK' + _nl + 'Content-Type: text/plain' + _nl + _nl + 'hello')
_r["start"]                     // HTTP/1.1 200 OK
_r["header"]["Content-Type"]    // text/plain
_r["body"]                      // hello
```

500 系と共用する辞書では、`#ifdef __AYA_SYSTEM_SYSFUNC_PARSEHEADER__` で使えるかどうかを判定して書き分けられる（[プリプロセス](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)）。

## Compatibility
- YAYA: Tc602-3以降

## See Also
- [TOAUTOEX](TOAUTOEX.md)
- [HASH_SPLIT](HASH_SPLIT.md)
- [PARSEJSON](PARSEJSON.md)
- [SPLIT](SPLIT.md)
