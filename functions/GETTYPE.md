# GETTYPE
**Category:** 型取得/変換

## Signature
```
GETTYPE( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 型を調べる値・変数・式 |

## Returns
- 0: 内部エラー（失敗）
- 1: 整数
- 2: 浮動小数点数
- 3: 文字列
- 4: 汎用配列
- 5: ハッシュ（Tc600-3以降）

## Description
指定した値のデータ型を取得する。

「要素数1の汎用配列は、その最初の（唯一の）要素の型を返します」という後方互換性のための動作がある。要素数1の汎用配列の型を正確に調べたい場合は `GETTYPEEX` を使用することが推奨される。

この動作は、唯一の要素が配列やハッシュ（[入れ子](../grammar/13-nesting.md)）のときも同じで、それぞれ 4 と 5 を返す。

```
GETTYPE(PARSEJSON('[[1,2]]'))     // 4
GETTYPE(PARSEJSON('[{"a":1}]'))   // 5
```

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降
- Tc600-3: ハッシュのとき 5 を返すようになった
- Tc602-10: 要素数1の汎用配列で、唯一の要素が配列やハッシュのとき 0 を返していたのを直した（4 や 5 を返す）

## See Also
- GETTYPEEX
- IHASH
