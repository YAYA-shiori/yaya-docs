# EXECUTE_WAIT

**Category:** メタ操作・特殊関数

## Signature

```
EXECUTE_WAIT( path [, option [, dir ]] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 実行するファイルまたはアプリケーションのパス。相対パスは信頼性が低いため、絶対パスの使用を推奨。 |
| option | アプリケーションに渡す引数（省略可）。URLをブラウザで開く場合などに使用。 |
| dir | 起動するプロセスの作業ディレクトリ（省略可）。相対パスは FOPEN などと同じく DLL のロードディレクトリを基準とする。省略するか空文字列なら指定しない。YAYA や SSP のカレントディレクトリは変わらない。 |

## Returns

- 成功時: 実行したプロセスの終了コード。起動済みのアプリケーションに処理を渡した場合など、待つプロセスがなければ 0
- 失敗時: -1（dir が存在しないディレクトリの場合や、POSIX 環境でシグナルにより終了した場合も含む）

## Description

コマンド文字列をOSのコマンドプロセッサに引き渡して外部アプリケーションやファイルを実行します。EXECUTE と異なり、アプリケーションの終了を待ってから処理を返します（同期実行）。C言語の system() 関数に相当します。

## Example

```
_val = EXECUTE_WAIT('CL.EXE','HELLOWORLD.C')
```

C コンパイラで HELLOWORLD.C をコンパイルし、完了を待ちます。

## Compatibility

- YAYA: TC532-1以降
- Tc604-1: 第3引数 dir（作業ディレクトリ）を追加。返値を終了コードにした（以前は Windows では成功時に 1、POSIX 環境では system() の返値をそのまま返していた）

## See Also

- EXECUTE
