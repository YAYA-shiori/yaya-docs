# GETTIMEZONE
**Category:** システム情報

## Signature
```
GETTIMEZONE( [ sec ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| sec | （省略可）EPOCH（1970年1月1日 00:00:00 UTC）からの経過秒数（整数）。省略時は現在のシステム時刻 |

## Returns
以下の構造を持つ汎用配列:

| インデックス | 値 | 詳細 |
|------------|---|------|
| 0 | UTCからのオフセット | 秒。東が正（日本は `32400`）。夏時間のときは夏時間を含めた値 |
| 1 | 夏時間フラグ | 0=標準時 / 1=夏時間 |
| 2 | 名前 | Windows: OSの表示名（日本語環境なら `東京 (標準時)`）。Linux / macOS: 略称（`JST`、`EDT` など） |
| 3 | IANAの名前 | `Asia/Tokyo` のような名前。取得できないときは空文字列（[GETSETTING](GETSETTING.md) の `coreinfo.timezone` と同じ） |

`sec` が扱える範囲（約±9億年）を超えているときは、警告 W0012（[GETLASTERROR](GETLASTERROR.md) は 12）を出して `-1` を返す。

## Description
OSのローカルタイムゾーンについて、`sec` の時点での情報を返す。夏時間があるタイムゾーンでは、夏時間かどうか・オフセットは `sec` の時点の規則で決まる。

インデックス0のオフセットは、[GETTIME](GETTIME.md) / [GETSECCOUNT](GETSECCOUNT.md) がローカルタイムとして扱うときの差と同じ。

- Windows: IANAの名前は、OSのタイムゾーン名（`Tokyo Standard Time`）をICU（`icu.dll`、Windows 10 1903 以降）で変換して求める。それより古いWindowsでは空文字列。複数のIANA名に対応するWindowsのタイムゾーンは、代表的な名前になる（`Pacific Standard Time` は `America/Los_Angeles`）
- Linux / macOS: IANAの名前は、環境変数 `TZ`、無ければ `/etc/localtime` のリンク先（`.../zoneinfo/Asia/Tokyo`）、それも無ければ `/etc/timezone` から求める。`TZ` が `JST-9` のようなPOSIX形式のときは、その文字列がそのまま入る

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
- YAYA: Tc606-1以降

## See Also
- GETTIME
- GETSECCOUNT
- GETSETTING
