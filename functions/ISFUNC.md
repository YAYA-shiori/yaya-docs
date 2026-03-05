# ISFUNC
**Category:** 型取得/変換
**Source:** マニュアル/関数/ISFUNC

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

デバッグモードの状態確認と組み合わせて、デバッグ用関数の存在チェックをすることも可能。これにより、開発ツールを含まないゴースト配布版でも問題なく動作させることができる。

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降

## See Also
- ISVAR
