# APPEND_RUNTIME_DIC

**Category:** メタ操作・特殊関数

## Signature

```
APPEND_RUNTIME_DIC(dic_content)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| dic_content | 辞書ファイルの内容と同等の文字列。複数行や関数定義を含むことができる |

## Returns

成功時：0
失敗時：-1

## Description

`_RUNTIME_DIC_` という辞書名のメモリ上の辞書に、`dic_content` の中身を書いたのと同じ効果をもたらす。動的に新たなユーザー関数の定義などができる。`dic_content` には複数行や関数定義を書け、ファイルから辞書を読んだのと同じ挙動になる。

[THREADSTART](THREADSTART.md) で起動したスレッドが動いている間は、警告 W0032 を出して何も追加せず -1 を返す。

## Compatibility

- YAYA: Tc562-1 以降
- Tc608-1: ワーカースレッドが動いている間は追加できないようにした

## See Also

- EVAL
- ISEVALUABLE
