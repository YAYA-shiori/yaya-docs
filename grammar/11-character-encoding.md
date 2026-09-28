# 文字コード関連

## 内部文字コード

YAYA は内部文字コードとして **UCS-2** を使用する。辞書操作・ファイルI/O・外部ライブラリとのやり取りを行う際は、すべての文字列を自動的に UCS-2 との間で変換する。

## 文字コードIDシステム

一部の関数では、文字コードを数値IDで参照する。名前で指定できる関数では、テキスト表現の名前を使う（[文字コードの名前](#文字コードの名前)）：

| エンコーディング | テキスト表現 | ID |
|----------------|------------|-----|
| Shift JIS | Shift_JIS | 0 |
| UTF-8 | UTF-8 | 1 |
| EUC-JP | EUC-JP | 2 |
| Big5 | Big5 | 3 |
| GB2312 | GB2312 | 4 |
| EUC-KR | EUC-KR | 5 |
| ISO-2022-JP (JIS) | ISO-2022-JP | 6 |
| バイナリ | binary | 126 |
| OSデフォルト | default（OSNative も同じ） | 127 |

## 文字コードの名前

文字コードを名前で指定するときは、上の表のテキスト表現を使う。大文字小文字は区別しない。

使えない名前（`UTF-16`、`ISO-8859-1` など）をシステム関数に渡すと、警告 W0012 を出して失敗する（GETLASTERROR は 12）。どう失敗するかは関数ごとのページを参照。Tc574-8 / Tc603-1 より前は、警告を出さずに OS デフォルトとして扱っていた。

設定ファイル（`charset` など）に使えない名前を書いたときは、これまでどおり警告を出さずに OS デフォルトになる。

## バイナリエンコーディングの特殊ケース

バイナリ形式は「UCS-2文字列の下位バイトをそのままバイト列にした特殊な文字コード」。変換なしにデータをやり取りするために `FWRITEBIN` や `FREADBIN` などの関数向けに設計されている。

**重要な制限:** バイナリモードであっても YAYA は文字列内のヌルバイト（0x00）を処理できない。また `FUNCTIONEX` などの既存システム辞書はバイナリ文字列値を想定していない。

## 関連

- [CHARSETLIB](../functions/CHARSETLIB.md)
- [CHARSETLIBEX](../functions/CHARSETLIBEX.md)
- [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md)
- [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md)
- [FCHARSET](../functions/FCHARSET.md)
- [STRENCODE](../functions/STRENCODE.md)
- [STRDECODE](../functions/STRDECODE.md)
