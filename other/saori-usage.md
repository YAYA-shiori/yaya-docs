# SAORIの使い方

**Source:** SAORIの使い方

## 概要

SAORI は伺かにおいて、SHIORI 以外の汎用言語（C言語など）で書かれた処理を実装する機能。2つのSAORI規格が存在する：

| 規格 | 形式 | 備考 |
|------|------|------|
| SAORI-basic | 実行ファイル（.exe） | コマンドライン引数と標準出力を使用 |
| SAORI-universal | ダイナミックライブラリ（.dll） | SSTP の知識が必要 |

## SAORI-basic の実装

コマンドライン引数を受け取り、標準出力で結果を返す形式。コンパイル時は依存関係を避けるため静的ビルドを推奨。

**デフォルトの文字コードはShift-JIS**（UTF-8ではない）。ただしYAYAはUnicodeをサポートしている。

### YAYAとの連携

YAYAでのSAORI-basic呼び出しは `FUNCTIONEX` 関数と `proxy_ex.dll` を使用する：

```
// FUNCTIONEXの第一引数はyaya.dllからproxy_ex.dllへの相対パス
FUNCTIONEX("proxy_ex.dll", "saori/xxx.exe", Argument0, ...)
```

パス区切りは **バックスラッシュ** を使うこと：`"saori\xxx.dll"`（`"saori\\xxx.dll"` や `"saori/xxx.dll"` は不可）。

### 配列出力の扱い

複数の返り値はデリミタベースの簡易配列または `SPLIT` 関数で取り扱える。

## SAORI-universal の実装

.dll 形式。Result と Value0/Value1 パラメータを返す。`proxy_ex.dll` は不要。返り値はグローバル変数 `valueex[]` 配列に格納される。

## Python との連携

Pythonスクリプトを PyInstaller でスタンドアロン実行ファイルに変換することでPython統合が可能。ユーザー環境にPythonインタープリタのインストールが不要になる。

```
PyInstaller (ファイル名).py
PyInstaller --onefile (ファイル名).py  # 単一ファイルで出力
```

## 関連

- [YAYA as SAORI](./yaya-as-saori.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
- [LOADLIB](../functions/LOADLIB.md)
- [REQUESTLIB](../functions/REQUESTLIB.md)
