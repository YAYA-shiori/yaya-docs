# REQUESTLIB
**Category:** 外部ライブラリ

## Signature
```
REQUESTLIB( path , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLLの位置。YAYAのある位置からの相対パス、または絶対パス。 |
| string | request関数に渡す文字列 |

## Returns
- 成功: request関数が生成した文字列
- 失敗: VOID（何も返さない）

## Description
事前にロードされた外部ライブラリのrequest関数を呼び出し、その結果を取得します。外部ライブラリのDLLは、YAYAと同じインターフェース（load/unload/request関数のエクスポート）を持つ必要があります。

Tc604-1以降、[LOADLIB](LOADLIB.md) で読み込んだSAORI-basicの実行ファイルを指定すると、YAYA が実行ファイルを起動して SAORI/1.0 の応答を返します（[詳細](LOADLIB.md#saori-basic)）。

### スレッドとの関係
応答の遅い外部ライブラリを待つ処理は、[THREADSTART](THREADSTART.md) で起動したスレッドから呼ぶと、待っている間も SSP からの `request` や他のスレッドが止まりません。

- 外部ライブラリは同時に1つのスレッドからしか呼べないものとして、同じライブラリへの呼び出しは順番に実行されます。ほかのスレッドが同じライブラリを呼び出している間は、その終わりを待ってから呼び出します。違うライブラリ同士は同時に呼び出せます
- 呼び出し中のライブラリを別のスレッドが [UNLOADLIB](UNLOADLIB.md) しても、解放されません（警告 W0013）
- 外部ライブラリは、`THREADSTART` のスレッドの上から呼ばれることになります。COM やウィンドウなど、呼び出すスレッドが決まっている SAORI は、ワーカーから呼ぶと動かないことがあります
- 呼び出しの途中では中断できません。[THREADSTOP](THREADSTOP.md) は、その呼び出しが返ってから効きます

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8以降で使用可能
- Tc604-1: SAORI-basic の実行ファイルに対応した
- Tc608-1: 待つ間にほかのスレッドが動けるようにした（`THREADSTART` のスレッドがあるとき）。同じライブラリへの呼び出しを順番にした

## See Also
- LOADLIB
- UNLOADLIB
- THREADSTART
