# TOUPPER
**Category:** 文字列操作

## Signature
```
TOUPPER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要轉換的字串 |
| locale | （可省略）地區設定名稱。省略時使用 C 模式（僅將 a-z 轉換為 A-Z） |

## Returns
- 成功：轉換後的大寫字串
- 失敗：VOID

## Description
將字串中的所有小寫字母轉換為大寫後傳回。省略 locale 時，使用 C 模式（僅將 a-z 轉換為 A-Z）。

locale 的格式與 [setlocale 可使用的地區設定字串](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setlocale-wsetlocale)相同。locale 可指定 `"ja-JP"`、`"tr_TR"`、`"tr_TR.UTF-8"` 等名稱。會依照該地區設定的規則進行轉換，也會轉換非 ASCII 字元（`é`→`É`、全形英文字母等）。土耳其語（`tr-TR`）中，`i` 會轉換為 `İ`。`"C"` 和 `"POSIX"` 代表 C 模式，空字串則代表 OS 使用者設定的地區設定。也可以使用 [GETSETTING](GETSETTING.md) 的 `coreinfo.locale` 傳回的名稱。

- Windows：使用 OS 的地區設定名稱。也可使用 `"Japanese_Japan.932"` 這類 C 執行階段的地區設定名稱
- Linux / macOS：必須使用 OS 中安裝的地區設定（可透過 `locale -a` 查看）。省略字元編碼的 `tr_TR` 等名稱會優先尋找 UTF-8 版本
- 不會影響其他處理或處理程序的地區設定

指定無法使用的地區設定時，會發出警告 W0012（[GETLASTERROR](GETLASTERROR.md) 為 12），並傳回以 C 模式轉換的結果。

## Example
```
_str = 'sAkuRa'
_str = TOUPPER( _str )
_str // 'SAKURA'
```

## Compatibility
- YAYA：從初期版本起即可使用（locale 參數自 Tc569-5 起提供）
- Tc606-1：變更 locale 的處理方式。可使用 `ja-JP` 等名稱指定地區設定，並在不切換處理程序地區設定的情況下進行轉換。指定無法使用的地區設定時，會發出警告 W0012，並以 C 模式進行轉換（先前不會發出警告，而是沿用當時的地區設定進行轉換）
- AYA：5.8 以後

## See Also
- TOLOWER
- TRANSLATE
