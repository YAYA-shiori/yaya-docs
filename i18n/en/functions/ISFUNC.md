# ISFUNC
**Category:** 型取得/変換

## Signature
```
ISFUNC( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | Function name (string) to check for existence |

## Returns
- 0: Function does not exist
- 1: User-defined function exists
- 2: System function exists

## Description
Checks whether a function with the specified name exists in the system. The return value also distinguishes between a user-defined function and a system function.

## Example
```
// "DebugMenu" 関数が存在する場合のみデバッグメニューを追加
if ( ISFUNC("DebugMenu") )
{
    AYATEMPLATE.MenuItem( "【デバッグメニュー】","DebugMenu")
}
```

Useful when you do not want to include menus for debugging or similar purposes in the distribution files.

To combine this with the `On_enable_debug` event and add an item only when 「SHIORIデバッグモード有効」 is selected in the development palette, do the following.

```
if ( ISFUNC("DebugMenu") && debug_mode )
{
    AYATEMPLATE.MenuItem( "【デバッグメニュー】","DebugMenu")
}

On_enable_debug
{
    debug_mode = reference[0]
}
```

## Compatibility
- YAYA: Available from the initial release
- AYA: 5.8 and later

## See Also
- ISVAR
