# CHARSETLIB

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIB(code)
CHARSETLIB()
CHARSETLIB
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | （可省略）以字元編碼 ID 或表示字元編碼的文字指定字元編碼（[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)）。若名稱不明，會發出警告 W0012，且不變更設定 |

## Returns

省略引數時：以字串傳回目前的 DLL 字元編碼設定
指定引數時：VOID（不傳回任何值）

設定與外部函式庫交換資料時使用的字元編碼。必須在 LOADLIB 之前呼叫。預設編碼取自設定檔的 charset.extension 項目（若未指定，則取自 charset）。

CHARSETLIB 會全域套用至所有外部函式庫，而 CHARSETLIBEX 則可為個別函式庫設定。

## Compatibility

- YAYA: 初版起即可使用。省略引數的功能從 Tc531 起支援
- AYA: 5.8 版以後
- Tc574-8 / Tc603-1: 傳入不明的字元編碼名稱時，會發出警告 W0012，且不變更設定（在此之前不會發出警告，而是視為作業系統預設值）

## See Also

- CHARSETLIBEX
- CHARSETIDTOTEXT
