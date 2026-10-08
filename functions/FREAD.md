# FREAD

**Category:** ファイル操作

## Signature

```
FREAD(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | FOPENで指定したファイルの相対パス（yaya.dll からの相対パス） |

## Returns

- 成功時: 読み取った1行の文字列（CR・LF等の行末文字は除去される）。FCHARSETで指定した文字コードからYAYAの内部エンコーディングに変換される
- ファイル終端に達した場合: -1
- 失敗時: 空文字列

事前に FOPEN でファイルを開いておく必要がある。

## Description

ファイルから 1 行読み取る。

- `FREAD` する前には、`FOPEN` でファイルをオープンしておく必要がある
- 文字コードは、`FCHARSET` で指定した文字コードから YAYA 内部の文字コードに変換される
- 行の末尾の改行文字（CR、LF）は取り除かれる

### 注意

EOF 検出のために次のようなコードを書くと、「`-1` しか書かれていない行」がファイルに存在した場合に、それを EOF と誤認識して、読み込みが終わってしまうことがある。

```
_line = FREAD(_filename);
if(_line == -1) { break; }
```

これは、次のようにすると回避できる。

```
_line = FREAD(_filename);
if(GETTYPE(_line) == 1 && _line == -1) { break; }
```

EOF の `-1` は整数値で、ファイルから読み込んだ `"-1"` は文字列なので、[GETTYPE](GETTYPE.md) で値の種類を調べ、「整数値としての `-1`」の場合にのみ EOF として扱う。

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- FWRITE
- FREADBIN
- FOPEN
- FREADENCODE
- FWRITE2
- FCHARSET
