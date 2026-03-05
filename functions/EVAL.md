# EVAL

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/EVAL

## Signature

```
EVAL( string )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | YAYA スクリプトの式として実行するテキスト文字列 |

## Returns

- 成功時: 評価した式の結果
- 失敗時: VOID（返り値なし）

## Description

引数の文字列を単一の YAYA スクリプト式として実行します。式の展開や実行時の関数名合成などに対応しますが、if/for などの制御構造や関数定義は実行できません。複数ステートメントのスクリプトには対応していません。

## Example

```
EVAL("i=1")

EVAL("i=%(CHR(34))test%(CHR(34))")

EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")
```

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- ISEVALUABLE
- APPEND_RUNTIME_DIC
