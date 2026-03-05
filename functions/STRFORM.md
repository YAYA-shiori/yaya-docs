# STRFORM
**Category:** 文字列操作
**Source:** マニュアル/関数/STRFORM

## Signature
```
STRFORM(format [, arg ...])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| format | フォーマット文字列 |
| arg | フォーマット文字列に埋め込む引数（複数指定可） |

## Returns
- 成功時: フォーマットされた文字列
- 失敗時: 動作は未定義

## Description
C言語の sprintf に相当するフォーマット済み文字列を返します。

フォーマット指定子は `%` の代わりに `$` をプレフィックスとして使用します（例: `$04d`, `$s`）。各フォーマット指定子で展開される文字列は最大1024文字です。

## Example
```
year = 1941
warname = "太平洋"
str = STRFORM("$04d年　$s戦争勃発。", year, warname)
// 結果: "1941年　太平洋戦争勃発。"
```

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降
