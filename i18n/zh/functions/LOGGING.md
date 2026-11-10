# LOGGING
**Category:** デバッグ

## Signature
```
LOGGING(var)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要写入日志的值。可以指定任意类型 |

## Returns
VOID（无返回值）

## Description
将指定的值写入日志文件，同时显示在调试工具“玉”中。可以接收任意数据类型。

简易数组会以逗号连接各个值的形式输出。

## 输出格式

有多个参数或传入数组时，会将各个值以逗号分隔并写入一行。字符串会用 `"` 括起来。

```
LOGGING('a', 1, 2.5)   // "a",1,2.500000
```

值包含数组或哈希时（Tc602-8以后），数组用 `( )` 括起来，哈希用 `{ }` 括起来，哈希元素以 `键=值` 的形式写出。嵌套结构的内部也遵循相同规则，因此可以分辨出各层结构。

```
_h = PARSEJSON('{"l":[1,2],"m":{"x":"a"}}')
LOGGING(_h)                           // {"l"=(1,2),"m"={"x"="a"}}
LOGGING(PARSEJSON('[[1,[2,"s"]],3]'))  // (1,(2,"s")),3
```

最外层数组会展开为参数，因此不会用括号括起来。

## Compatibility
- YAYA：从早期版本起可用
- AYA：5.8版以后可用
- Tc602-8：改为用 `( )` 括起嵌套数组、用 `{ }` 括起哈希（此前内部结构也会用 `,` 或 `=` 连接，哈希键和值中的字符串不会用 `"` 括起来）

## See Also
- GETERRORLOG
- CLEARERRORLOG
- GETLASTERROR
- SETLASTERROR
