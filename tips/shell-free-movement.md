# シェルの自由移動

**Source:** Tips/シェルの自由移動

## 概要

SSP/CROW ベースのシェルをデスクトップ上で自由に移動させる機能の実装方法を説明しています。

> **注意:** SSP/CROW でのみ使用できます。Materia では自由移動になりません。

## コード例

### 基本: 起動時に自由移動を有効にする

会話スクリプト内で以下を実行する:

```
\0\1\_s\![set,alignmenttodesktop,free]\_s
```

`OnBoot` に組み込む例:

```
OnBoot
{
    "\0\s[0]\1\s[10]\0\1\_s\![set,alignmenttodesktop,free]\_s"
    _timeslot = GetTimeSlot
    if _timeslot == "朝"
    ...
}
```

### 応用: 自由移動と画面下固定の切り替え

```
Free_movement { "\0\s[0]どうされますか？..." }
Free_movement_On  { movement = 1; "\0\1\_s\![set,alignmenttodesktop,free]\_s\e" }
Free_movement_Off { movement = 0; "\0\1\_s\![set,alignmenttodesktop,bottom]\_s\e" }

movement_status  { CALLBYNAME("movement_status%movement") }
movement_status0 { "\0\1\_s\![set,alignmenttodesktop,bottom]\_s" }
movement_status1 { "\0\1\_s\![set,alignmenttodesktop,free]\_s" }
```

`OnBoot`、`OnGhostChanged`、`OnShellChanged` などのイベントで `%movement_status` を呼び出して状態を反映させる:

```
OnShellChanged { "\0\s[0]%reference0シェルに替わりました...%movement_status\e" }
```

## 説明

- `alignmenttodesktop,free` : デスクトップ上を自由に移動できるモード
- `alignmenttodesktop,bottom` : 画面下部に固定するモード
- グローバル変数 `movement` で現在のモードを管理する（0: 下固定, 1: 自由移動）
- `movement_status` 関数はモードに応じたスクリプトを返すヘルパー関数

## 関連項目

- CALLBYNAME
