# GETFUNCINFO
**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/GETFUNCINFO

## Signature
```
GETFUNCINFO( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | 情報を取得したい関数名（必須） |

## Returns
- 成功: 汎用配列
  - インデックス0: 関数が定義されているファイルのフルパス
  - インデックス1: 開始行番号
  - インデックス2: 終了行番号
- 失敗: -1

## Description
現在読み込んでいる辞書の（ユーザー）関数の情報を取得する関数。

関数が定義されているファイルのパスと、その開始・終了行番号を取得できる。デバッグ用途で、ある関数がどのファイルのどこに定義されているかを動的に調べる際に有用。

## Example
```
// デバッグモード時に関数の定義位置を表示する例（Taromati2より）
if _debug_mode
    _info = GETFUNCINFO('MyFunction')
    if _info != -1
        "定義ファイル: %(_info[0])"
        "開始行: %(_info[1])"
    endif
endif
```

## Compatibility
YAYA: Tc558-1以降

## See Also
- GETFUNCLIST
