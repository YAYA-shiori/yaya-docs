# ISFUNC
**Category:** 型取得/変換

## Signature
```
ISFUNC( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要確認是否存在的函式名稱（字串） |

## Returns
- 0：函式不存在
- 1：使用者自訂函式存在
- 2：系統函式存在

## Description
確認指定名稱的函式是否存在於系統中，並區分傳回的是使用者自訂函式還是系統函式。

## Example
```
// "DebugMenu" 関数が存在する場合のみデバッグメニューを追加
if ( ISFUNC("DebugMenu") )
{
    AYATEMPLATE.MenuItem( "【デバッグメニュー】","DebugMenu")
}
```

若不希望在發行檔案中包含除錯用選單等內容，此函式便很有用。

若要搭配 `On_enable_debug` 事件，只在開發用調色盤的「啟用 SHIORI 除錯模式」時新增項目，請如下撰寫。

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
- YAYA: 從初期版本起即可使用
- AYA: 5.8 以後

## See Also
- ISVAR
