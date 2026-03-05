# ERASEVAR

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/ERASEVAR

## Signature

```
ERASEVAR( name [, name ...] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| name | 削除する変数名（文字列で指定）。複数指定可能。 |

## Returns

返り値はありません（VOID）。

## Description

変数を消去します。変数名は文字列として指定する必要があります。

```
ERASEVAR("i")          // 正しい例：変数 i を削除
ERASEVAR("i","j","k")  // 正しい例：複数の変数を一度に削除
ERASEVAR(i)            // 誤った例：変数名は文字列リテラルで指定すること
```

セーブデータに残す必要のないグローバル変数の消去などに利用できます。

## Compatibility

- YAYA: 初版より対応
- TC532-1以降: 複数変数の同時削除に対応
- AYA: 5.8以降

## See Also

- ERASE
- EVAL
