# WindowsDLLとしてのYAYA

**Source:** マニュアル/文法/A.WindowsDLLとしてのYAYA

## 概要

YAYA（読み: やや）は C 言語に似た構文を持つ文字列処理 DLL。「与えられた文字列を変形する」「プログラムされたルールに基づいて文字列を生成する」ことができる。直接使用にはプログラミングの知識が必要。

## 動作環境

Windows 95 以降に対応する Windows ベースの DLL。SSP 開発標準に基づいて構築されている。

## エクスポート関数

### load(HGLOBAL h, long len)

YAYA を使用前に初期化する。`LoadLibrary` の後に必ず1回実行する。パラメータ `h` は絶対ディレクトリパス、`len` は `h` の長さを受け取る。メモリの解放は DLL 側が行う。

### unload()

`FreeLibrary` の実行前に終了を通知する。

### request(HGLOBAL h, long \*len)

入力を処理し結果を返す。入力メモリは DLL が管理する。出力の長さは `*len` に更新される。呼び出し元は返却されたサイズで `GlobalFree` を使って結果を解放する必要がある。

## 技術的な注記

このインターフェースは SHIORI（「伺か」のキャラクターソフトウェア用の擬似AIのDLL）仕様と完全に一致する。

## 使用条件

- 同梱ドキュメントに従うこと
- `LICENSE` システム関数で YAYA が使用するライブラリのライセンス情報を表示できる

## 関連

- [LICENSE](../functions/LICENSE.md)
