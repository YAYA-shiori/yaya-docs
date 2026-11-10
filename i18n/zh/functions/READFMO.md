# READFMO
**Category:** システム情報

!!! warning "仅限 Windows"
    此函数只能在为 Windows 编译的 yaya 中运行。

## Signature
```
READFMO( [ name ] [ , charset ] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| name | （可省略）FMO 的标识符。省略时为 "Sakura" |
| charset | （可省略）字符编码（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。省略时使用操作系统默认值。新增于 Tc569-13。若值无效，则发出警告 W0012 并不返回任何内容 |

## Returns
- 成功：以字符串形式返回 FMO 的内容
- 失败：VOID（不返回任何内容）

## Description
以字符串形式获取文件映射对象（FMO）的内容。FMO 的前 4 个字节表示大小，是无符号整数；读取时会移除这 4 个字节。如果 FMO 中存在 null 字节（0x00），其行为未定义。

## Compatibility
- YAYA：在版本 Tc524-1 中引入
- Tc574-8 / Tc603-1：传入未知字符编码名称或无效 ID 时，会发出警告 W0012 并不返回任何内容（此前会将其作为操作系统默认值读取）
