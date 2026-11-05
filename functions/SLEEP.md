# SLEEP
**Category:** デバッグ

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

[THREADSTART](THREADSTART.md) で起動したスレッドから呼んだときは、待っている間ほかのスレッド（SSP からの `request` を含む）が動けます。[THREADSTOP](THREADSTOP.md) や `unload` で中断を求められると、待ちの途中で戻ります。

## Compatibility
- YAYA: Tc564-1以降
- Tc608-1: ワーカースレッドから呼んだときに、待つ間ほかのスレッドが動けるようにし、中断で途中で戻るようにした

## See Also
- THREADSTART
