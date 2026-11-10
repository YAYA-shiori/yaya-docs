# LICENSE
**Category:** メタ操作・特殊関数

## Signature
```
LICENSE()
LICENSE
```

## Parameters
None

## Returns
A generic array containing the YAYA license text. Each entry is separated by a newline.

## Description
Returns the YAYA license text. In addition to YAYA itself, it includes the license texts for the bundled libraries (MT19937, parson, TinyXML-2, and SQLite).

## Compatibility
- YAYA: Available since Tc530-1
- Tc601-1: Added the license texts for parson and TinyXML-2
- Tc602-11: Added a notice for SQLite (public domain)

## See Also
- LETTONAME
- LINT.GetFuncUsedBy
