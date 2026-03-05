# FUNCTIONEX
**Category:** 外部ライブラリ
**Source:** マニュアル/関数/FUNCTIONEX

## Signature
```
FUNCTIONEX( 'path' , 'Argument0', 'Argument1', ... )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | yaya.dllからの相対パスで、呼び出したいSAORIユニバーサルモジュールのパスを指定する |
| Argument* | SAORIモジュールへの引数。SAORI-basicの場合は第1引数にproxy.dllのパス、第2引数にSAORI-basicのパス、以降にSAORI-basicへの引数を指定する |

## Returns
- SAORI-universalの場合: Resultの値を返す。同時に`valueex`配列にSAORI-universalのValueデータが格納される
- SAORI-basicの場合: 標準出力を返す

## Description
SAORIモジュール（外部プラグイン）を実行する関数。

SAORI-universalとSAORI-basicの両方に対応している。SAORI-universalの場合、戻り値としてResultが返されるとともに、`valueex`配列にValueデータが格納される。

SAORIの具体的な使い方については、Tips「SAORIの使い方」を参照のこと。

## Compatibility
YAYAの初期バージョンから使用可能。

## See Also
- Tips/SAORIの使い方
