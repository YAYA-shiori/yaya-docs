# FUNCTIONEX
**Category:** 外部ライブラリ

## Signature
```
FUNCTIONEX( 'path' , 'Argument0', 'Argument1', ... )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | yaya.dllからの相対パスで、呼び出したいSAORIのパスを指定する。SAORI-universalならDLL、SAORI-basicなら実行ファイル（Tc604-1以降） |
| Argument* | SAORIへの引数。SAORI-basicの場合は実行ファイルのコマンドライン引数になる |

## Returns
- SAORI-universalの場合: Resultの値を返す。同時に`valueex`配列にSAORI-universalのValueデータが格納される
- SAORI-basicの場合: 標準出力を返す。複数行のときは行を `\r\n` の4文字でつないだものを返し、`valueex`配列には1行ずつ格納される（Tc604-1以降）

## Description
SAORIモジュール（外部プラグイン）を実行する関数。

システム関数ではなく、システム辞書（yaya_shiori3.dic）で定義された関数で、[LOADLIB](LOADLIB.md) と [REQUESTLIB](REQUESTLIB.md) を使ってSAORIを呼び出す。

SAORI-universalとSAORI-basicの両方に対応している。SAORI-universalの場合、戻り値としてResultが返されるとともに、`valueex`配列にValueデータが格納される。

SAORI-basicは、Tc604-1以降ではYAYA本体が直接実行するので、実行ファイルのパスをそのまま指定すればよい（POSIX 環境でも動く）。実行のしかたは [LOADLIB](LOADLIB.md#saori-basic) を参照。

```
_result = FUNCTIONEX('SAORI\sample.exe', 'はろーわーるど')
```

それより前のバージョンでは、proxy_ex.dll などのSAORI-universalを経由して呼び出す（pathにproxy_ex.dllのパス、Argument0にSAORI-basicのパス、以降にSAORI-basicへの引数を指定する）。

SAORIの具体的な使い方については、Tips「SAORIの使い方」を参照のこと。

## Compatibility
- YAYAの初期バージョンから使用可能
- Tc604-1: SAORI-basicの実行ファイルを直接指定できるようにした（それまではproxy_ex.dllなどを経由する必要があった）

## See Also
- [SAORIの使い方](../tips/saori-usage.md)
- LOADLIB
- REQUESTLIB
