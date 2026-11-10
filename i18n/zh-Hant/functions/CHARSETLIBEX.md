# CHARSETLIBEX

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIBEX(path, code)
CHARSETLIBEX(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | DLL 檔案的位置。指定相對於 YAYA 目錄的相對路徑，或絕對路徑 |
| code | （可省略）字元編碼 ID 或表示字元編碼的文字識別碼（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。若名稱不明，會發出警告 W0012，且不變更設定 |

## Returns

省略 code 時：以字串傳回指定 DLL 目前的字元編碼設定
指定 code 時：VOID（不傳回任何值）

個別指定與外部函式庫交換資料時使用的字元編碼。Tc530-2 以後，在 LOADLIB 之前呼叫即可生效，並可在「初始化中」設定。預設編碼取自設定檔的 charset.extension 項目（若未指定，則取自 charset）。但在 POSIX 環境中，SAORI-basic（Tc604-1 以後）的預設值為 UTF-8。

## Compatibility

- YAYA: 初版起即可使用。省略引數的功能從 Tc531 起支援
- Tc574-8 / Tc603-1: 傳入不明的字元編碼名稱時，會發出警告 W0012，且不變更設定（在此之前不會發出警告，而是視為作業系統預設值）

## See Also

- CHARSETLIB
- CHARSETTEXTTOID
