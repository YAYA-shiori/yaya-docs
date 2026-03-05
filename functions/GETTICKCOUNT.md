# GETTICKCOUNT
**Category:** システム情報
**Source:** マニュアル/関数/GETTICKCOUNT

## Signature
```
GETTICKCOUNT( [ flag ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| flag | 現在は実質的な意味を持たない。歴史的には0以外の値を指定すると `GetTickCount() >> 31` の第32ビット値を返し、長時間計測に使われていた |

## Returns
OSが起動してからの経過時間（ミリ秒単位）

## Description
OSが起動してからの経過時間をミリ秒単位で返す。

Windows XP以前では約24日20時間で0にリセットされる。Vista以降や他のOSではその制約はない。

## Compatibility
- YAYA: 初期から利用可能
- AYA 5.8: 利用可能

## See Also
- GETTIME
- GETSYSTEMFUNCLIST
