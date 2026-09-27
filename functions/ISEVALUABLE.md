# ISEVALUABLE
**Category:** メタ操作・特殊関数

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

文の並び（`;` や改行で区切った複数の文や、if/for などの制御文）も、EVALと同じ規則で判定して検証する（Tc574-6 / Tc602-9以降）。

```
ISEVALUABLE('1 + 2')                  // 1
ISEVALUABLE('_a = 1; if _a { 2 }')    // 1
ISEVALUABLE('_a = 1; if { 2')         // 0
```

## Compatibility
- YAYA: Tc562-1以降
- Tc574-6 / Tc602-9: EVALが文の並びを実行できるようになったのに合わせて、文の並びも検証できるようにした

## See Also
- EVAL
- APPEND_RUNTIME_DIC
