# READFMO
**Category:** システム情報

!!! warning "Windows専用"
    This function works only with YAYA compiled for Windows.

## Signature
```
READFMO( [ name ] [ , charset ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | (Optional) FMO identifier. Defaults to "Sakura" |
| charset | (Optional) Character encoding ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). Defaults to the OS default. Added in Tc569-13. If invalid, emits warning W0012 and returns nothing |

## Returns
- Success: Returns the FMO contents as a string
- Failure: VOID (returns nothing)

## Description
Gets the contents of a file mapping object (FMO) as a string. The first 4 bytes of an FMO represent its size as an unsigned integer, and are removed when reading it. Behavior is undefined if the FMO contains a null byte (0x00).

## Compatibility
- YAYA: Introduced in version Tc524-1
- Tc574-8 / Tc603-1: Changed to emit warning W0012 and return nothing when given an unknown character encoding name or an invalid ID (previously, it read using the OS default)
