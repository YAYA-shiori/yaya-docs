# INSERT
**Category:** 文字列操作

## Signature
```
INSERT( src , pos , insert )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 挿入先の元の文字列 |
| pos | 挿入位置（0=先頭）。負の値を指定すると末尾からのオフセットとして扱われる（Tc574-8 / Tc603-1以降） |
| insert | 挿入する文字列 |

## Returns
- 成功時: 挿入後の文字列
- エラー時: VOID

## Description
文字列 `src` の `pos` で指定した位置に、文字列 `insert` を挿入する。位置0は文字列の先頭を表す。

`pos` が負の値のときは、`src` の文字数を足した位置に挿入する（-1 なら最後の1文字の前）。それでも負になるときは先頭に、`src` の文字数より大きいときは末尾に挿入する。

```
INSERT('abc', 1, 'X')    // aXbc
INSERT('abc', -1, 'X')   // abXc
INSERT('abc', 10, 'X')   // abcX
INSERT('abc', -10, 'X')  // Xabc
```

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降
- Tc574-8 / Tc603-1: 負の位置を末尾から数え、範囲外の位置を先頭か末尾に寄せるようにした（それまではエラーで処理が中断していた）。`insert` に数値を渡したときも挿入するようにした（それまでは何も挿入されなかった）
