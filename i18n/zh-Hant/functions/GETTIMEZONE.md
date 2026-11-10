# GETTIMEZONE
**Category:** システム情報

## Signature
```
GETTIMEZONE( [ sec ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| sec | （可省略）從 EPOCH（1970年1月1日 00:00:00 UTC）起經過的秒數（整數）。省略時使用目前的系統時間 |

## Returns
傳回具有以下結構的通用陣列：

| 索引 | 值 | 詳細說明 |
|------------|---|------|
| 0 | 相對於 UTC 的偏移量 | 秒。東方為正（日本為 `32400`）。夏令時間期間包含夏令時間的偏移量 |
| 1 | 夏令時間旗標 | 0=標準時間 / 1=夏令時間 |
| 2 | 名稱 | Windows：OS 的顯示名稱（日文環境為 `東京 (標準時)`）。Linux / macOS：縮寫（如 `JST`、`EDT`） |
| 3 | IANA 名稱 | 如 `Asia/Tokyo` 的名稱。無法取得時為空字串（與 [GETSETTING](GETSETTING.md) 的 `coreinfo.timezone` 相同） |

當 `sec` 超出可處理範圍（約 ±9 億年）時，會發出警告 W0012（[GETLASTERROR](GETLASTERROR.md) 為 12）並傳回 `-1`。

## Description
傳回 OS 本地時區在 `sec` 所代表時刻的資訊。對於有夏令時間的時區，是否為夏令時間以及偏移量皆依照 `sec` 所代表時刻的規則決定。

索引 0 的偏移量，與 [GETTIME](GETTIME.md) / [GETSECCOUNT](GETSECCOUNT.md) 以本地時間處理時所使用的差值相同。

- Windows：IANA 名稱會透過 ICU（`icu.dll`，Windows 10 1903 以後）將 OS 的時區名稱（`Tokyo Standard Time`）轉換取得。較舊版本的 Windows 會傳回空字串。對應多個 IANA 名稱的 Windows 時區會使用代表性的名稱（`Pacific Standard Time` 對應 `America/Los_Angeles`）
- Linux / macOS：IANA 名稱會從環境變數 `TZ`、若未設定則從 `/etc/localtime` 的連結目標（`.../zoneinfo/Asia/Tokyo`）、若仍無法取得則從 `/etc/timezone` 取得。若 `TZ` 為 `JST-9` 這類 POSIX 格式，則會直接使用該字串

## Example
```
// 今のローカルタイムゾーン
_tz = GETTIMEZONE()
_tz[0]   // 32400
_tz[3]   // 'Asia/Tokyo'

// 夏時間のある地域で、ある日時のオフセット（秒）を求める
GETTIMEZONE(GETSECCOUNT(2024, 7, 1, 0, 12, 0, 0))[0]
```

## Compatibility
- YAYA：Tc606-1 以後

## See Also
- GETTIME
- GETSECCOUNT
- GETSETTING
