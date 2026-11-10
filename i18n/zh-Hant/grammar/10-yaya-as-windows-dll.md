# 作為 Windows DLL 的 YAYA

## 概要

YAYA（讀音：yaya）是用於處理字串的 DLL。使用類似 C 語言的語法，可以進行下列處理：

- 加工給定的字串
- 根據程式化的規則產生字串

YAYA 是 Windows DLL，因此若要直接使用，需要具備一定程度的程式設計知識。

## 執行環境

適用於 Windows。使用與 SSP 相同的開發環境建置，也就是以預期能在 Windows 95 上執行的設定建置。

## 匯出函式

YAYA 提供下列公開函式。使用 YAYA 的程式會先對 YAYA 執行 `LoadLibrary`，再呼叫這些函式以執行所需的處理。

### load

```c
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len)
```

指示 YAYA 初始化。在透過 `LoadLibrary` 載入 YAYA 並開始使用之前，務必執行此函式一次。`h` 傳入「YAYA 視為目前目錄的目錄絕對路徑」，`len` 傳入 `h` 的長度。`h` 所占用的記憶體區域會由 YAYA 端釋放，因此呼叫端不必處理，可直接交由 YAYA 管理。

### unload

```c
extern "C" __declspec(dllexport) BOOL __cdecl unload()
```

指示 YAYA 結束。在對 YAYA 執行 `FreeLibrary` 之前，執行一次即可。

### request

```c
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len)
```

指示 YAYA 執行處理並取得結果。`h` 傳入處理對象的字串，`*len` 傳入 `h` 的長度。傳入的 `h` 所占用的記憶體區域會由 YAYA 端釋放，因此呼叫端不必處理，可直接交由 YAYA 管理。

處理結果會透過傳回值取得。處理結果的長度會存入 `*len`（也就是說，此值會被改寫）。取得傳回值後，請依照 `*len` 所指定的大小釋放記憶體區域（`GlobalFree`）。

## 技術備註

這與桌面吉祥物軟體「伺か」所使用的擬似 AI DLL「SHIORI」介面規格完全相同。

## 使用規範

- 請遵循隨附文件
- 可透過 [LICENSE](../functions/LICENSE.md) 系統函式顯示 YAYA 所使用程式庫的授權條款
