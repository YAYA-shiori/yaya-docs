# CVINT

**Category:** 型取得/変換

## Signature

```
CVINT(_var_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 整数型に変換する変数 |

## Returns

戻り値なし（変数をその場で変換する）

整数形式の文字列を保持する変数を実際の整数型に変換する。小数部分は切り捨てられる。

## Example

```
_val = '583'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）

_val = '583.12'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）
_val // 583 を返す（小数部分は除去される）
```

## Compatibility

- YAYA: 初版から利用可能
- AYA: バージョン5.8以降
- Tc574-4 / Tc602-6: 数字の後に `a`（`A`）が続く文字列で、`a` を 10 という桁として読んでしまい `'1a'` が 20 になっていたのを修正（1 になる）

## See Also

- CVREAL
- CVSTR
- CVAUTO
