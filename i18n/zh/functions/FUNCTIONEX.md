# FUNCTIONEX
**Category:** 外部ライブラリ

## Signature
```
FUNCTIONEX( 'path' , 'Argument0', 'Argument1', ... )
```

## Parameters
| 参数 | 描述 |
|-----------|-------------|
| path | 指定要调用的 SAORI 的路径，相对于 yaya.dll。SAORI-universal 指定 DLL，SAORI-basic 指定可执行文件（Tc604-1 及以后） |
| Argument* | 传递给 SAORI 的参数。SAORI-basic 的情况下，会成为可执行文件的命令行参数 |

## Returns
- SAORI-universal 的情况下：返回 Result 的值。同时，SAORI-universal 的 Value 数据会存入 `valueex` 数组
- SAORI-basic 的情况下：返回标准输出。多行时，将各行用 `\r\n` 这 4 个字符连接后返回，并逐行存入 `valueex` 数组（Tc604-1 及以后）

## Description
执行 SAORI 模块（外部插件）的函数。

这不是系统函数，而是在系统词典（yaya_shiori3.dic）中定义的函数；它使用 [LOADLIB](LOADLIB.md) 和 [REQUESTLIB](REQUESTLIB.md) 调用 SAORI。

同时支持 SAORI-universal 和 SAORI-basic。SAORI-universal 的情况下，会将 Result 作为返回值返回，同时将 Value 数据存入 `valueex` 数组。

Tc604-1 及以后，YAYA 本体会直接执行 SAORI-basic，因此只需直接指定可执行文件的路径（也可以在 POSIX 环境中运行）。执行方法请参阅 [LOADLIB](LOADLIB.md#saori-basic)。

```
_result = FUNCTIONEX('SAORI\sample.exe', 'はろーわーるど')
```

在更早的版本中，则需要通过 proxy_ex.dll 等 SAORI-universal 调用（将 proxy_ex.dll 的路径指定为 path，将 SAORI-basic 的路径指定为 Argument0，之后的参数指定为传递给 SAORI-basic 的参数）。

当 `path` 以 `internal_` 开头时（例如 `internal_crypto`），不会加载 DLL，而是通过 DIRECTSSTP 调用 baseware（SSP 2.9.13 及以后）内置的模块（SAORI over DirectSSTP）。无法使用时返回 0。详情请参阅 [yaya_shiori3.dic](../system/yaya-shiori3-dic.md#ベースウェアの内蔵モジュールsaori-over-directsstp)。

关于 SAORI 的具体用法，请参阅 Tips「SAORI 的用法」。

## Compatibility
- 从 YAYA 的早期版本开始即可使用
- Tc604-1：现在可以直接指定 SAORI-basic 的可执行文件；此前必须通过 proxy_ex.dll 等调用

## See Also
- [SAORI 的用法](../tips/saori-usage.md)
- LOADLIB
- REQUESTLIB
