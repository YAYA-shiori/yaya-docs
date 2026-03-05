# DICLOAD

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/DICLOAD

## Signature

```
DICLOAD( filename [, code] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | 読み込む辞書ファイル名 |
| code | 文字コードID（省略時は基本設定ファイルの設定に従う） |

## Returns

- `0`: 成功
- `1`: 失敗

## Description

指定した辞書ファイルを動的に読み込みます。

注意事項：

- 辞書に問題がある場合はエラーとなり、何も変更されません。
- 読み込んだ辞書は次のリクエスト呼び出しまで有効にならず、現在実行中の関数は保護されます。
- 文字列埋め込み要素のスコープ展開構文は DICLOAD 後には機能しません。読み込んだ辞書の内容をすぐに認識できる EVAL の使用を検討してください。
- 読み込んだ辞書は DICUNLOAD で解除できますが、制限があります。

## Compatibility

- YAYA: Tc556-1以降

## See Also

- DICUNLOAD
- EVAL
