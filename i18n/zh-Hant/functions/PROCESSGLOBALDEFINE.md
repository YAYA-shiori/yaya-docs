# PROCESSGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
PROCESSGLOBALDEFINE(string)
```

## Parameters
| 引數 | 說明 |
|-----------|-------------|
| string | 要進行預處理的字串 |

## Returns
- 成功：套用全域定義後的處理完成字串
- 失敗：-1

## Description
執行與使用 `#globaldefine` 定義的預處理（字串取代處理）相同的處理。如需預處理器功能的詳細資訊，請參閱[預處理](../grammar/08-preprocessor.md)。

## Compatibility
- YAYA：自版本 Tc559-1 起即可使用

## See Also
- [預處理](../grammar/08-preprocessor.md)
