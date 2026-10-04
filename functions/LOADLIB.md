# LOADLIB
**Category:** 外部ライブラリ

## Signature
```
LOADLIB(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込むDLL、またはSAORI-basicの実行ファイル（Tc604-1以降）のパス。YAYAのディレクトリからの相対パス、または絶対パスで指定する |

## Returns
- 1: 読み込み成功
- 2: すでに読み込み済み
- 0: 読み込み失敗

## Description
外部ライブラリ（DLL）ファイルを読み込みます。初回呼び出し時のみLoadLibraryを実行し、ロード関数を呼び出します。読み込む外部DLLはYAYAと同じインターフェース（load/unload/request関数のエクスポート）を持つ必要があります。

### SAORI-basic

Tc604-1以降、DLL以外のファイルを指定すると、SAORI-basic（コマンドライン引数を受け取り、標準出力に結果を書く実行ファイル）として扱います。DLLかどうかは拡張子で判断します。

- Windows: `.dll` と拡張子なし以外（`.exe` など）
- POSIX 環境: `.dll` `.so` `.dylib` `.bundle` 以外（拡張子なしを含む）

読み込み時は、ファイルがあるか（POSIX 環境では実行できるかも）を確かめるだけで、実行はしません。[REQUESTLIB](REQUESTLIB.md) に SAORI/1.0 の要求を渡すたびに、YAYA が実行ファイルを起動して応答を作ります。proxy_ex.dll などは要りません。

- `EXECUTE SAORI/1.0`: Argument0, Argument1, ... をそのまま1つずつのコマンドライン引数にして起動します（空白や `"` を含む引数も分かれません。POSIX 環境ではシェルを通しません）
    - 作業ディレクトリは実行ファイルのあるディレクトリ。標準入力と標準エラー出力はつながりません
    - 標準出力の末尾の改行を除き、Result に行を `\r\n` の4文字でつないだもの、Value0, Value1, ... に1行ずつを入れて `200 OK` を返します。出力が空なら `204 No Content` です
    - 10秒で終わらないか、出力が16MBに達したら、プロセスを強制終了して `500 Internal Server Error` を返します。起動に失敗したときも 500 です
    - SecurityLevel が local でない要求は `400 Bad Request` で断ります
- `GET Version SAORI/1.0`: YAYA が `200 OK` を返します

引数と標準出力の文字コードは [CHARSETLIBEX](CHARSETLIBEX.md) の設定に従います。既定は他のSAORIと同じく charset.extension ですが、POSIX 環境のSAORI-basicだけは UTF-8 です。Windows では引数は文字コードによらず Unicode のまま渡ります。

## Compatibility
- YAYA: 初期バージョンより使用可能
- AYA: バージョン5.8以降で使用可能
- Tc604-1: SAORI-basic の実行ファイルを読み込めるようにした

## See Also
- REQUESTLIB
- UNLOADLIB
- FUNCTIONEX
