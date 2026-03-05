# EXECUTE

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/EXECUTE

## Signature

```
EXECUTE( path [, option] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 起動するファイルまたはアプリケーションのパス。相対パスは信頼性が低いため、絶対パスの使用を推奨。 |
| option | アプリケーションに渡す引数（省略可）。URLをブラウザで開く場合などに使用。 |

## Returns

- 成功時: 0以上の整数（OS依存）
- 失敗時: -1

## Description

コマンド文字列をコマンドプロセッサに引き渡して外部アプリケーションやファイルを起動します。C言語の system() 関数を改良したもので、アプリケーションの終了を待たずに処理を返します。

## Example

```
_val = EXECUTE('IEXPLORE.EXE','http://www.yahoo.co.jp/')
```

Yahoo のホームページを Internet Explorer で開きます。

## Compatibility

- YAYA: 初版より対応

## See Also

- EXECUTE_WAIT
