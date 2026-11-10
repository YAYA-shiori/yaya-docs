# ISEVALUABLE
**Category:** メタ操作・特殊関数

## Signature
```
ISEVALUABLE( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to execute as a YAYA script |

## Returns
- 1: The string can be evaluated and executed by EVAL (it is syntactically valid)
- 0: The string cannot be evaluated (validation failed)

## Description
Checks whether the specified string can be executed as a YAYA script using the EVAL function.

Validating the string with this function before executing an arbitrary string with EVAL can prevent runtime errors caused by invalid code strings.

Sequences of statements (multiple statements separated by `;` or newlines, or control statements such as if/for) are also checked and validated according to the same rules as EVAL (from Tc574-6 / Tc602-9 onward).

```
ISEVALUABLE('1 + 2')                  // 1
ISEVALUABLE('_a = 1; if _a { 2 }')    // 1
ISEVALUABLE('_a = 1; if { 2')         // 0
```

## Compatibility
- YAYA: Tc562-1 and later
- Tc574-6 / Tc602-9: Added validation of statement sequences to match EVAL's new ability to execute them

## See Also
- EVAL
- APPEND_RUNTIME_DIC
