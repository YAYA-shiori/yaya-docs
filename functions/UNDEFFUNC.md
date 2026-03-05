# UNDEFFUNC
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/UNDEFFUNC

## Signature
```
UNDEFFUNC( funcname )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| funcname | 読み込み解除する関数名 |

## Returns
- 0: 成功
- 1: 失敗

## Description
指定した関数を読み込み解除する。

アンロードにより辞書ファイルに問題が生じる場合はエラーとなり、何も起こらない。また、既に他の箇所から参照されている関数はアンロードできない。

## Compatibility
- YAYA: Tc561-1 以降

## See Also
- DICUNLOAD
- UNDEFGLOBALDEFINE
