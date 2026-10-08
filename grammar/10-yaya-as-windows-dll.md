# WindowsDLLとしてのYAYA

## 概要

YAYA（読み: やや）は、文字列処理を行うための DLL。C 言語に似た文法を使用して、

- 与えられた文字列を加工する
- プログラムした規則に基づいて文字列を生成する

といった処理ができる。YAYA は Windows DLL なので、直接利用するためには、プログラミングに関する知識がある程度必要。

## 動作環境

Windows 用。SSP と同じ開発環境、つまり Windows 95 でも動くと思われる設定で構築されている。

## エクスポート関数

YAYA は次の公開された関数を持つ。YAYA を利用するプログラムは、YAYA を `LoadLibrary` した後にこれらの関数を実行して、所望の処理を行う。

### load

```c
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len)
```

YAYA に初期化を指示する。YAYA を `LoadLibrary` して使用を開始する直前に、この関数を一度だけ必ず実行すること。`h` には「YAYA がカレントとして認識するディレクトリの絶対パス」を、`len` には `h` の長さを渡す。`h` の領域の解放は YAYA 側で行うので、呼び出し側では使いっぱなしでかまわない。

### unload

```c
extern "C" __declspec(dllexport) BOOL __cdecl unload()
```

YAYA に終了を指示する。YAYA を `FreeLibrary` する直前に一度だけ実行すること。

### request

```c
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len)
```

YAYA に処理を指示し、結果を得る。`h` には処理対象の文字列を、`*len` には `h` の長さを渡す。渡した `h` の領域の解放は YAYA 側で行うので、呼び出し側では使いっぱなしでかまわない。

処理結果は戻り値で得られる。処理結果の長さは `*len` に格納される（つまりこの値は書き換えられる）。戻り値を取得した後、領域を `*len` で示されるサイズで解放（`GlobalFree`）すること。

## 技術的な注記

これは、デスクトップマスコットソフトウェア「伺か」で使用される擬似 AI 用 DLL「SHIORI」のインタフェース規格と完全に同一のもの。

## 利用規定

- 同梱のドキュメントに従うこと
- [LICENSE](../functions/LICENSE.md) システム関数により、YAYA が利用しているライブラリのライセンス条文を表示できる
