# TOLOWER
**Category:** 文字列操作

## Signature
```
TOLOWER( string [ , locale ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要轉換的字串 |
| locale | （可省略）地區設定名稱。省略時使用 C 模式（只將 A-Z 轉換為 a-z） |

## Returns
- 成功：轉換後的小寫字串
- 失敗：VOID

## Description
將字串中的所有大寫字母轉換為小寫後傳回。省略 locale 時，會使用 C 模式（只將 A-Z 轉換為 a-z）。

locale 可指定 `"ja-JP"` `"tr_TR"` `"tr_TR.UTF-8"` 等名稱。轉換時會依照該地區設定的規則進行，也會轉換非 ASCII 字元（`É`→`é`、全形英文字母等）。土耳其語（`tr-TR`）中，`I` 會轉換為 `ı`。`"C"` 和 `"POSIX"` 會使用 C 模式，空字串則會使用 OS 的使用者設定地區。也可以使用 [GETSETTING](GETSETTING.md) 的 `coreinfo.locale` 所傳回的名稱。

- Windows：使用 OS 的地區設定名稱。也可以使用 `"Japanese_Japan.932"` 這類 C 執行階段的地區設定名稱
- Linux / macOS：必須使用 OS 中安裝的地區設定（可在 `locale -a` 中看到）。省略字元編碼時（例如 `tr_TR`），會優先尋找 UTF-8 版本
- 不會影響其他處理或程序的地區設定

指定無法使用的地區設定時，會發出警告 W0012（[GETLASTERROR](GETLASTERROR.md) 為 12），並傳回使用 C 模式轉換的結果。

## Example
```
_str = 'sAkuRa'
_str = TOLOWER( _str )
_str // 'sakura'
```

## Compatibility
- YAYA：自初期版本起（locale 參數自 Tc569-5 起提供）
- Tc606-1：變更 locale 的處理方式。可以使用 `ja-JP` 這類名稱指定地區設定，並在不切換程序地區設定的情況下進行轉換。指定無法使用的地區設定時，會發出警告 W0012，並使用 C 模式轉換（以前不會發出警告，而是依當時的地區設定進行轉換）
- AYA：5.8 以後

## See Also
- TOUPPER
