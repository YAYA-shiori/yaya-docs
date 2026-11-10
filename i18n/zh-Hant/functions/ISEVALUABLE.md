# ISEVALUABLE
**Category:** メタ操作・特殊関数

## Signature
```
ISEVALUABLE( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要以 YAYA 腳本執行的字串 |

## Returns
- 1：可使用 EVAL 評估並執行字串（語法正確）
- 0：無法評估字串（驗證失敗）

## Description
此函式會驗證指定的字串能否作為 YAYA 腳本由 EVAL 函式執行。

在使用 EVAL 執行任意字串之前，先用此函式進行驗證，即可避免因程式碼字串無效而發生執行階段錯誤。

語句序列（以 `;` 或換行分隔的多個語句，以及 if/for 等控制語句）也會依照與 EVAL 相同的規則判定並驗證（Tc574-6 / Tc602-9 以後）。

```
ISEVALUABLE('1 + 2')                  // 1
ISEVALUABLE('_a = 1; if _a { 2 }')    // 1
ISEVALUABLE('_a = 1; if { 2')         // 0
```

## Compatibility
- YAYA: Tc562-1 以後
- Tc574-6 / Tc602-9：配合 EVAL 改為可執行語句序列，也新增了驗證語句序列的功能

## See Also
- EVAL
- APPEND_RUNTIME_DIC
