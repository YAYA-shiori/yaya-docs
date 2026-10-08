# ISFUNC
**Category:** 型取得/変換

## Signature
```
ISFUNC( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 存在を確認する関数名（文字列） |

## Returns
- 0: 関数が存在しない
- 1: ユーザー定義関数が存在する
- 2: システム関数が存在する

## Description
指定した名前の関数がシステム内に存在するかどうかを確認する。ユーザー定義関数かシステム関数かも区別して返す。

## Example
```
// "DebugMenu" 関数が存在する場合のみデバッグメニューを追加
if ( ISFUNC("DebugMenu") )
{
    AYATEMPLATE.MenuItem( "【デバッグメニュー】","DebugMenu")
}
```

デバッグ用のメニューなどを配布ファイルに含めたくない場合に有用。

`On_enable_debug` イベントと組み合わせて、開発用パレットの「SHIORIデバッグモード有効」時のみ項目を追加する場合は、次のようにする。

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
- YAYA: 初期から利用可能
- AYA: 5.8以降

## See Also
- ISVAR
