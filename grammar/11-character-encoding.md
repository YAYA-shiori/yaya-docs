# 文字コード関連

**Source:** マニュアル/文法/B.文字コード関連

## 内部文字コード

YAYA は内部文字コードとして **UCS-2** を使用する。辞書操作・ファイルI/O・外部ライブラリとのやり取りを行う際は、すべての文字列を自動的に UCS-2 との間で変換する。

## 文字コードIDシステム

一部の関数では、文字コードを数値IDで参照する：

| エンコーディング | テキスト表現 | ID |
|----------------|------------|-----|
| Shift JIS | Shift_JIS | 0 |
| UTF-8 | UTF-8 | 1 |
| EUC-JP | EUC_JP | 2 |
| BIG-5 | BIG-5 | 3 |
| GB-2312 | GB-2312 | 4 |
| EUC-KR | EUC_KR | 5 |
| ISO-2022-JP (JIS) | ISO-2022-JP | 6 |
| バイナリ | binary | 126 |
| OSデフォルト | OSNative | 127 |

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
