# CVINT

**Category:** 型取得/変換

## Signature

```
CVINT(var)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| var | 要转换为整数类型的变量 |

## Returns

无返回值（直接转换变量）

将存储整数格式字符串的变量转换为实际的整数类型。小数部分会被截去。

## Example

```
_val = '583'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）

_val = '583.12'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）
_val // 583 を返す（小数部分は除去される）
```

## Compatibility

- YAYA: 从初版开始可用
- AYA: 5.8 及以上版本
- Tc574-4 / Tc602-6：修复了将数字后跟 `a`（`A`）的字符串中的 `a` 当作 10 进制位读取的问题，因此 `'1a'` 原本会变成 20，现在会变成 1

## See Also

- CVREAL
- CVSTR
- CVAUTO
