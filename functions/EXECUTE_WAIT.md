# EXECUTE_WAIT

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/EXECUTE_WAIT

## Signature

```
EXECUTE_WAIT( path [, option] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 実行するファイルまたはアプリケーションのパス。相対パスは信頼性が低いため、絶対パスの使用を推奨。 |
| option | アプリケーションに渡す引数（省略可）。URLをブラウザで開く場合などに使用。 |

## Returns

- 成功時: 0以上の整数（OS依存）
- 失敗時: -1

## Description

コマンド文字列をOSのコマンドプロセッサに引き渡して外部アプリケーションやファイルを実行します。EXECUTE と異なり、アプリケーションの終了を待ってから処理を返します（同期実行）。C言語の system() 関数に相当します。

## Example

```
_val = EXECUTE_WAIT('CL.EXE','HELLOWORLD.C')
```

C コンパイラで HELLOWORLD.C をコンパイルし、完了を待ちます。

## Compatibility

- YAYA: TC532-1以降

## See Also

- EXECUTE
