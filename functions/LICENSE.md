# LICENSE
**Category:** メタ操作・特殊関数

## Signature
```
LICENSE()
LICENSE
```

## Parameters
なし

## Returns
YAYAのライセンス文字列を格納した汎用配列。各エントリは改行で区切られる。

## Description
YAYAのライセンス文字列を返します。YAYA 本体に続けて、組み込んでいるライブラリ（MT19937、parson、TinyXML-2）のライセンス文も含みます。

## Compatibility
- YAYA: Tc530-1以降で使用可能
- Tc601-1: parson と TinyXML-2 のライセンス文を追加した

## See Also
- LETTONAME
- LINT.GetFuncUsedBy
