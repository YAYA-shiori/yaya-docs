# FUNCTIONEX
**Category:** 外部ライブラリ

## Signature
```
FUNCTIONEX( 'path' , 'Argument0', 'Argument1', ... )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 以相對於 yaya.dll 的路徑指定要呼叫的 SAORI 路徑。若為 SAORI-universal，請指定 DLL；若為 SAORI-basic，請指定執行檔（Tc604-1 以後） |
| Argument* | 傳遞給 SAORI 的引數。若為 SAORI-basic，則會成為執行檔的命令列引數 |

## Returns
- 若為 SAORI-universal：傳回 Result 的值。同時會將 SAORI-universal 的 Value 資料存入 `valueex` 陣列
- 若為 SAORI-basic：傳回標準輸出。若有多行，會以 4 個字元 `\r\n` 串接各行後傳回，並逐行存入 `valueex` 陣列（Tc604-1 以後）

## Description
執行 SAORI 模組（外部外掛程式）的函式。

這不是系統函式，而是在系統辭典（yaya_shiori3.dic）中定義的函式，會使用 [LOADLIB](LOADLIB.md) 和 [REQUESTLIB](REQUESTLIB.md) 呼叫 SAORI。

同時支援 SAORI-universal 和 SAORI-basic。若為 SAORI-universal，會以傳回值傳回 Result，並將 Value 資料存入 `valueex` 陣列。

在 Tc604-1 以後，YAYA 本體會直接執行 SAORI-basic，因此只要直接指定執行檔的路徑即可（也能在 POSIX 環境中運作）。執行方式請參閱 [LOADLIB](LOADLIB.md#saori-basic)。

```
_result = FUNCTIONEX('SAORI\sample.exe', 'はろーわーるど')
```

在更早的版本中，則會透過 proxy_ex.dll 等 SAORI-universal 呼叫（在 path 指定 proxy_ex.dll 的路徑，在 Argument0 指定 SAORI-basic 的路徑，並在後續引數中指定傳遞給 SAORI-basic 的引數）。

當 `path` 以 `internal_` 開頭時（例如 `internal_crypto`），不會載入 DLL，而是透過 DIRECTSSTP 呼叫 baseware（SSP 2.9.13 以後）的內建模組（SAORI over DirectSSTP）。若無法使用，則會傳回 0。詳細資訊請參閱 [yaya_shiori3.dic](../system/yaya-shiori3-dic.md#ベースウェアの内蔵モジュールsaori-over-directsstp)。

SAORI 的具體用法請參閱 Tips「SAORI 的使用方式」。

## Compatibility
- 從 YAYA 初期版本起即可使用
- Tc604-1：可直接指定 SAORI-basic 的執行檔；在此之前必須透過 proxy_ex.dll 等程式呼叫

## See Also
- [SAORI 的使用方式](../tips/saori-usage.md)
- LOADLIB
- REQUESTLIB
