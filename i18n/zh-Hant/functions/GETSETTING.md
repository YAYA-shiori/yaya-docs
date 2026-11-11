# GETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
GETSETTING( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要取得資訊的識別碼（下述字串或基本設定的項目名稱） |

## Returns
- 成功：要求的資訊（字串）
- 失敗：空字串

## Description
傳回目前執行的對話中所設定資訊的函式。

`string` 可指定下列識別碼（字串），或為了向後相容而使用數值（0～4）。也可以指定[基本設定](../grammar/01-basic-settings.md)的項目名稱。

## Information Types
| 識別碼 | 舊數值 | 取得的資料 | 範例 |
|--------|--------|----------------|-----|
| `coreinfo.version` | 0 | YAYA 的版本號碼 | `"Tc522-1"` |
| （數值 1）          | 1 | 目前的字元編碼 ID（0=Shift_JIS、1=UTF-8、127=OS 預設值） | `0` |
| `coreinfo.path`    | 2 | 目錄的絕對路徑 | `"c:\hogehoge\"` |
| `coreinfo.name`    | 3 | DLL 名稱 | `"YAYA"` |
| `coreinfo.author`  | 4 | DLL 作者 | `"umeici/The Maintenance Shop"` |
| `coreinfo.savefile` | — | 存檔檔案的路徑 | `"d:/ghost/konno_yayame/..."` |
| `coreinfo.mode`    | — | 執行模式 | `"normal"` 或 `"emergency"` |
| `coreinfo.locale`   | — | OS 使用者設定中，數值與日期格式所用的地區設定 | `"ja-JP"` |
| `coreinfo.uilocale` | — | OS 使用者設定中，顯示語言所用的地區設定 | `"ja-JP"` |
| `coreinfo.timezone` | — | OS 本地時區的 IANA 名稱 | `"Asia/Tokyo"` |

`coreinfo.locale` / `coreinfo.uilocale` 會傳回 `語言-地區` 格式（BCP 47）的名稱。若無法取得，則傳回空字串。

- Windows：使用者的預設地區設定名稱（`coreinfo.uilocale` 為顯示語言）
- Linux / macOS：從環境變數取得。`coreinfo.locale` 依序採用 `LC_ALL` → `LC_NUMERIC` → `LANG`，`coreinfo.uilocale` 則依序採用 `LANGUAGE`（第一個語言）→ `LC_ALL` → `LC_MESSAGES` → `LANG`，並使用第一個已設定的值。`ja_JP.UTF-8` 會轉為 `ja-JP`。若為 `C` / `POSIX` 或未設定，則傳回空字串
- 傳回的名稱可直接作為 [TOUPPER](TOUPPER.md) / [TOLOWER](TOLOWER.md) 的地區設定引數

`coreinfo.timezone` 會傳回 `Asia/Tokyo` 這類 IANA 時區名稱。若無法取得，則傳回空字串。

- Windows：使用 ICU（`icu.dll`、Windows 10 1903 以後）轉換 OS 時區名稱。更舊版本的 Windows 會傳回空字串
- Linux / macOS：依序使用環境變數 `TZ`、`/etc/localtime` 的連結目標，若皆無則使用 `/etc/timezone`。若 `TZ` 為 `JST-9` 這類 POSIX 格式，則會直接傳回該字串
- 包含日光節約時間與時差的資訊可透過 [GETTIMEZONE](GETTIMEZONE.md) 取得

## Compatibility
- YAYA：自初期版本起可使用。`coreinfo.mode` 於 Tc556-2 加入，`coreinfo.locale` / `coreinfo.uilocale` / `coreinfo.timezone` 於 Tc606-1 加入
- AYA：5.8 版以後（僅支援數值引數 0～4）

## See Also
- SETSETTING
- [基本設定](../grammar/01-basic-settings.md)
