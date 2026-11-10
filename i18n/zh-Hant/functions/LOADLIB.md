# LOADLIB
**Category:** 外部ライブラリ

## Signature
```
LOADLIB(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要載入的 DLL 或 SAORI-basic 執行檔（Tc604-1 以後）的路徑。請指定相對於 YAYA 目錄的相對路徑，或絕對路徑 |

## Returns
- 1：載入成功
- 2：已載入
- 0：載入失敗

## Description
載入外部函式庫（DLL）檔案。僅在首次呼叫時執行 LoadLibrary，並呼叫載入函式。要載入的外部 DLL 必須具有與 YAYA 相同的介面（匯出 load/unload/request 函式）。

### SAORI-basic

Tc604-1 以後，指定 DLL 以外的檔案時，會將其視為 SAORI-basic（接收命令列引數，並將結果寫入標準輸出的執行檔）。是否為 DLL 會依副檔名判斷。

- Windows：除 `.dll` 和沒有副檔名的檔案以外（例如 `.exe`）
- POSIX 環境：除 `.dll` `.so` `.dylib` `.bundle` 以外（包含沒有副檔名的檔案）

載入時只會確認檔案是否存在（POSIX 環境也會確認檔案是否可執行），不會執行檔案。每當透過 [REQUESTLIB](REQUESTLIB.md) 傳送 SAORI/1.0 要求時，YAYA 會啟動該執行檔並產生回應。不需要 proxy_ex.dll 等檔案。

- `EXECUTE SAORI/1.0`：將 Argument0, Argument1, ... 原封不動地各自當成一個命令列引數來啟動（即使引數包含空白或 `"` 也不會拆開。在 POSIX 環境中不會透過 shell）
    - 工作目錄是執行檔所在的目錄。標準輸入和標準錯誤輸出不會連接
    - 去除標準輸出末尾的換行後，將各行以 4 個字元 `\r\n` 連接成 Result，並將每一行依序放入 Value0, Value1, ...，然後傳回 `200 OK`。若輸出為空，則傳回 `204 No Content`
    - 若 10 秒內未結束，或輸出達到 16MB，便會強制終止程序並傳回 `500 Internal Server Error`。啟動失敗時也會傳回 500
    - 若要求的 SecurityLevel 不是 local，則以 `400 Bad Request` 拒絕
- `GET Version SAORI/1.0`：YAYA 會傳回 `200 OK`

引數和標準輸出的字元編碼遵循 [CHARSETLIBEX](CHARSETLIBEX.md) 的設定。預設值與其他 SAORI 相同，為 charset.extension；但只有 POSIX 環境中的 SAORI-basic 使用 UTF-8。在 Windows 中，引數會以 Unicode 傳遞，不受字元編碼影響。

## Compatibility
- YAYA：從初始版本起可使用
- AYA：版本 5.8 以後可使用
- Tc604-1：新增載入 SAORI-basic 執行檔的功能

## See Also
- REQUESTLIB
- UNLOADLIB
- FUNCTIONEX
