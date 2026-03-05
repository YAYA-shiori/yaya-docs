# ISEVALUABLE
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/ISEVALUABLE

## Signature
```
ISEVALUABLE( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | YAYAスクリプトとして実行する文字列 |

## Returns
- 1: 文字列をEVALで評価・実行できる（構文的に正しい）
- 0: 文字列を評価できない（検証失敗）

## Description
指定した文字列をYAYAスクリプトとしてEVAL関数で実行できるかどうかを検証する関数。

EVALで任意の文字列を実行する前にこの関数で事前検証することで、不正なコード文字列による実行時エラーを防ぐことができる。

## Compatibility
- YAYA: Tc562-1以降

## See Also
- EVAL
- APPEND_RUNTIME_DIC
