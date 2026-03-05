# CUTSPACE

**Category:** 文字列操作
**Source:** マニュアル/関数/CUTSPACE

## Signature

```
CUTSPACE(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 処理対象の文字列 |

## Returns

成功時：文字列の先頭と末尾の空白文字（半角空白、全角空白、タブ）を除去した文字列
失敗時：VOID

文字列の両端にある空白文字を除去する。内部の空白（単語間）は保持される。

## Example

```
CUTSPACE(' さくら  まゆら   ') // 「さくら  まゆら」を返す
```

## Compatibility

- YAYA: 初版から利用可能
- AYA: バージョン5.8以降
