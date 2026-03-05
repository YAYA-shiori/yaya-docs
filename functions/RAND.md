# RAND
**Category:** 数学関数
**Source:** マニュアル/関数/RAND

## Signature
```
RAND([max])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| max | （省略可）乱数の上限値。0 〜 (max-1) の範囲で生成される。省略時はデフォルト100（0〜99の値を生成） |

## Returns
- 成功: 指定された範囲内のランダムな整数
- 失敗: 0

## Description
整数の乱数を得ます。シードの初期化なしに単独で動作します。SRANDでシードを設定することもできますが、基本的な使用では必須ではありません。

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8から使用可能

## See Also
- SRAND
