# LSO
**Category:** メタ操作・特殊関数

## Signature
```
LSO
LSO()
```

## Parameters
なし

## Returns
直前のセレクション操作で選択された位置を示す数値。

## Description

"last Selection Order" の略。最後に行われた選択の結果を、位置を表す数値で返す。

```
request
{
    _i = foo
    LSO
}

foo
{
    "earth"
    "moon"
    "sun"
}
```

`_i` に `"sun"` が代入された場合、`LSO` は 2 になる（0 始まり）。とにかく択一がされる場合すべてについて動作する。したがって、該当の処理が完了した直後に値を取得しないと意味がない。

### 取得する位置に注意

次のコードは、`ANY` の選択結果を得ようとしているなら誤り。この位置にある `LSO` は、`{ }` の選択結果を取得する。したがって `res` は常に 0 になる。

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
    }
    res = LSO
}
```

次のように修正すると、意図どおりに動作する。

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
        res = LSO
    }
}
```

### 出力確定子がある場合

出力確定子（`--`）がある場合、`LSO` はすべての取り得る組み合わせに対して動作する。

```
request
{
    {
        "1"
        "2"
        "3"
        --
        "A"
        "B"
    }
    _i = LSO
}
```

たとえば上の関数内の `{ }` 部は、`"1A"` `"2A"` `"3A"` `"1B"` `"2B"` `"3B"` のいずれかを出力する。`LSO` の値の範囲もこれと一致し、0〜5 を取る。各値は上の並びと一致する。

## Compatibility
- YAYA: 初期バージョンより使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- ANY
