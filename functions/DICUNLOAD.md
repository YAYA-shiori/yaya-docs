# DICUNLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICUNLOAD( filename )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | アンロードする辞書ファイル名 |

## Returns

- `0`: 成功
- `1`: 失敗

## Description

指定した辞書ファイルに含まれる関数および globaldefine グループをアンロードします。辞書ファイルに問題がある場合はエラーとなり何も起こりません。他の辞書から使われている関数を含む辞書はアンロードできません。

[THREADSTART](THREADSTART.md) で起動したスレッドが動いている間は、警告 W0032 を出して何もせず 1 を返します。

## Compatibility

- YAYA: Tc561-1以降
- Tc608-1: ワーカースレッドが動いている間はアンロードできないようにした

## See Also

- DICLOAD
- UNDEFFUNC
- UNDEFGLOBALDEFINE
