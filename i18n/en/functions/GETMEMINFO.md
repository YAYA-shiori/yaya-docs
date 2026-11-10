# GETMEMINFO
**Category:** システム情報

## Signature
```
GETMEMINFO()
```

## Parameters
None (takes no arguments)

## Returns
A generic array containing memory information for the operating environment (5 elements):

| Index | Content |
|------------|------|
| 0 | Physical memory usage percentage |
| 1 | Total physical memory |
| 2 | Free physical memory |
| 3 | Total virtual plus physical memory |
| 4 | Free virtual plus physical memory |

## Description
Gets memory information for the operating environment.

## Compatibility
- YAYA: Available since the initial version
- AYA: Version 5.8 and later
