# SETGLOBALDEFINE
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/SETGLOBALDEFINE

## Signature
```
SETGLOBALDEFINE( define_name , define_value )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| define_name | #globaldefine で定義する名前 |
| define_value | #globaldefine で割り当てる値 |

## Returns
- **1**: 成功
- **0**: 失敗

## Description
メモリ上の "_RUNTIME_DIC_" という名前の辞書に `#globaldefine` を記述したのと同等の効果をもたらします。

## Compatibility
- YAYA: Tc562-1以降

## See Also
- ISGLOBALDEFINE
- UNDEFGLOBALDEFINE
- PROCESSGLOBALDEFINE
