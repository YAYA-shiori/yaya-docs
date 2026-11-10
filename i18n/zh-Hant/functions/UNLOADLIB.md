# UNLOADLIB
**Category:** 外部ライブラリ

## Signature
```
UNLOADLIB( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLL 的路徑。相對於 YAYA 目錄的相對路徑，或絕對路徑 |

## Returns
VOID（沒有傳回值）

## Description
卸載外部函式庫（DLL）。首次呼叫時會執行卸載操作，接著呼叫 FreeLibrary。

外部函式庫 DLL 必須具有與 YAYA 本身相同的介面（匯出 load/unload/request 函式）。

如果另一個執行緒（[THREADSTART](THREADSTART.md)）正透過 [REQUESTLIB](REQUESTLIB.md) 呼叫該函式庫，就不會卸載函式庫，而會發出警告 W0013。呼叫結束後，再次執行 UNLOADLIB 即可。

## Compatibility
- YAYA：自初始版本起
- AYA：5.8 之後
- Tc608-1：修改為不卸載其他執行緒正在呼叫的函式庫

## See Also
- LOADLIB
- REQUESTLIB
