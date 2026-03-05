# DICUNLOAD

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/DICUNLOAD

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

## Compatibility

- YAYA: Tc561-1以降

## See Also

- DICLOAD
- UNDEFFUNC
- UNDEFGLOBALDEFINE
