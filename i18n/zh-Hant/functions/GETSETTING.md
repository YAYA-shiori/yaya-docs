# GETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
GETSETTING( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要取得資訊的識別字（以下所列字串或基礎設定的項目名稱） |

## Returns
- 成功：要求的資訊（字串）
- 失敗：空字串

## Description
傳回目前執行中的文句所設定的資訊。

`string` 可以指定以下識別字（字串），也可以指定為了向後相容而提供的數值（0〜4）。此外，也可以指定[基礎設定](../grammar/01-basic-settings.md)的項目名稱。

## Information Types
| 識別字 | 舊數值 | 取得的資料 | 範例 |
|--------|--------|----------------|-----|
| `coreinfo.version` | 0 | YAYA 的版本號碼 | `"Tc522-1"` |
| （數值 1）          | 1 | 目前的字元編碼 ID | `0` |
| `coreinfo.path`    | 2 | 目錄的絕對路徑 | `"c:\hogehoge\"` |
| `coreinfo.name`    | 3 | DLL 名稱 | `"YAYA"` |
| `coreinfo.author`  | 4 | DLL 作者 | `"umeici/The Maintenance Shop"` |
| `coreinfo.savefile` | — | 存檔檔案的路徑 | `"d:/ghost/konno_yayame/..."` |
| `coreinfo.mode`    | — | 執行模式 | `"normal"` 或 `"emergency"` |
| `coreinfo.locale`   | — | OS 使用者設定的地區（數值和日期格式）語系 | `"ja-JP"` |
| `coreinfo.uilocale` | — | OS 使用者設定的顯示語言語系 | `"ja-JP"` |
| `coreinfo.timezone` | — | OS 本地時區的 IANA 名稱 | `"Asia/Tokyo"` |

`coreinfo.locale` / `coreinfo.uilocale` 會傳回 `語言-地區` 格式（BCP 47）的名稱。無法取得時會傳回空字串。

- Windows：使用者的預設語系名稱（`coreinfo.uilocale` 為顯示語言）
- Linux / macOS：從環境變數取得。`coreinfo.locale` 依序使用 `LC_ALL` → `LC_NUMERIC` → `LANG`，`coreinfo.uilocale` 依序使用 `LANGUAGE`（第一個語言）→ `LC_ALL` → `LC_MESSAGES` → `LANG`，並取最先設定的值。`ja_JP.UTF-8` 會轉換為 `ja-JP`。`C` / `POSIX` 或未設定時會傳回空字串
- 傳回的名稱可直接傳入 [TOUPPER](TOUPPER.md) / [TOLOWER](TOLOWER.md) 的語系引數

`coreinfo.timezone` 會傳回如 `Asia/Tokyo` 這類 IANA 時區名稱。無法取得時會傳回空字串。

- Windows：使用 ICU（`icu.dll`、Windows 10 1903 以後）轉換 OS 時區名稱。較舊的 Windows 版本會傳回空字串
- Linux / macOS：依序使用環境變數 `TZ`、`/etc/localtime` 的連結目標，若兩者皆不存在則使用 `/etc/timezone`。`TZ` 為 `JST-9` 這類 POSIX 格式時，會原樣傳回該字串
- 包含日光節約時間和時差的資訊可透過 [GETTIMEZONE](GETTIMEZONE.md) 取得

## Compatibility
- YAYA：可從初期版本開始使用。`coreinfo.mode` 於 Tc556-2 新增，`coreinfo.locale` / `coreinfo.uilocale` / `coreinfo.timezone` 於 Tc606-1 新增
- AYA：5.8 以後（僅支援數值引數 0〜4）

## See Also
- SETSETTING
- [基礎設定](../grammar/01-basic-settings.md)
