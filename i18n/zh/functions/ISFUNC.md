# ISFUNC
**Category:** 型取得/変換

## Signature
```
ISFUNC( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要确认是否存在的函数名（字符串） |

## Returns
- 0：函数不存在
- 1：存在用户自定义函数
- 2：存在系统函数

## Description
检查指定名称的函数是否存在于系统中。返回值还会区分该函数是用户自定义函数还是系统函数。

## Example
```
// "DebugMenu" 関数が存在する場合のみデバッグメニューを追加
if ( ISFUNC("DebugMenu") )
{
    AYATEMPLATE.MenuItem( "【デバッグメニュー】","DebugMenu")
}
```

当不希望将调试菜单等内容包含在分发文件中时，此函数很有用。

如果要与 `On_enable_debug` 事件结合，仅在开发用面板的“启用 SHIORI 调试模式”开启时添加项目，请按如下方式编写。

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
- YAYA: 从初始版本起可用
- AYA: 5.8及之后

## See Also
- ISVAR
