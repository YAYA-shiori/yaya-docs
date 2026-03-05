# SLEEP
**Category:** デバッグ
**Source:** マニュアル/関数/SLEEP

## Signature
```
SLEEP(millisecond)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| millisecond | 待機時間（ミリ秒単位） |

## Returns
- 成功時: 0
- 失敗時: -1

## Description
指定したミリ秒数だけ処理を一時停止します。

長時間の待機を指定するとアプリケーション全体がフリーズするため、短い時間やデバッグ用途に限定して使用することを推奨します。

## Compatibility
- YAYA: Tc564-1以降
