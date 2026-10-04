# EXECUTE

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 起動するファイルまたはアプリケーションのパス。相対パスは信頼性が低いため、絶対パスの使用を推奨。 |
| option | アプリケーションに渡す引数（省略可）。URLをブラウザで開く場合などに使用。 |
| dir | 起動するプロセスの作業ディレクトリ（省略可）。相対パスは FOPEN などと同じく DLL のロードディレクトリを基準とする。省略するか空文字列なら指定しない。YAYA や SSP のカレントディレクトリは変わらない。 |

## Returns

- 成功時: 0以上の整数（OS依存。Windows では ShellExecute の返値、POSIX 環境では 0）
- 失敗時: -1（dir が存在しないディレクトリの場合も含む）

## Description

コマンド文字列をコマンドプロセッサに引き渡して外部アプリケーションやファイルを起動します。C言語の system() 関数を改良したもので、アプリケーションの終了を待たずに処理を返します。

## Example

```
_val = EXECUTE('IEXPLORE.EXE','http://www.yahoo.co.jp/')
```

Yahoo のホームページを Internet Explorer で開きます。

## Compatibility

- YAYA: 初版より対応
- Tc604-1: 第3引数 dir（作業ディレクトリ）を追加。POSIX 環境に対応した（以前は常に -1 を返していた）

## See Also

- EXECUTE_WAIT
