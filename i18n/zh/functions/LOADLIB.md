# LOADLIB
**Category:** 外部ライブラリ

## Signature
```
LOADLIB(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要加载的 DLL 或 SAORI-basic 可执行文件（Tc604-1以后）的路径。指定相对于 YAYA 所在目录的相对路径或绝对路径 |

## Returns
- 1：加载成功
- 2：已加载
- 0：加载失败

## Description
加载外部库（DLL）文件。仅在首次调用时执行 LoadLibrary，并调用加载函数。要加载的外部 DLL 必须具有与 YAYA 相同的接口（导出 load/unload/request 函数）。

### SAORI-basic

Tc604-1以后，指定 DLL 以外的文件时，会将其视为 SAORI-basic（接收命令行参数并将结果写入标准输出的可执行文件）。通过扩展名判断文件是否为 DLL。

- Windows：除 `.dll` 和无扩展名以外的文件（如 `.exe`）
- POSIX 环境：除 `.dll` `.so` `.dylib` `.bundle` 以外的文件（包括无扩展名文件）

加载时只会检查文件是否存在（在 POSIX 环境中还会检查文件是否可执行），不会执行文件。每次通过 [REQUESTLIB](REQUESTLIB.md) 发送 SAORI/1.0 请求时，YAYA 都会启动该可执行文件并生成响应。无需使用 proxy_ex.dll 等文件。

- `EXECUTE SAORI/1.0`：将 Argument0、Argument1、……分别作为命令行参数启动（含空格或 `"` 的参数也不会被拆分。在 POSIX 环境中不会经过 shell）
    - 工作目录为可执行文件所在目录。标准输入和标准错误输出不会连接
    - 去除标准输出末尾的换行符后，将各行以4个字符 `\r\n` 连接后放入 Result，并将每一行分别放入 Value0、Value1、……，然后返回 `200 OK`。若输出为空，则返回 `204 No Content`
    - 若10秒内未结束或输出达到16MB，则强制终止进程并返回 `500 Internal Server Error`。启动失败时也返回500
    - 对于 SecurityLevel 不为 local 的请求，返回 `400 Bad Request` 拒绝处理
- `GET Version SAORI/1.0`：YAYA 返回 `200 OK`

参数和标准输出的字符编码遵循 [CHARSETLIBEX](CHARSETLIBEX.md) 的设置。默认设置与其他 SAORI 相同，为 charset.extension，但 POSIX 环境下的 SAORI-basic 仅使用 UTF-8。在 Windows 中，无论字符编码如何，参数都会以 Unicode 形式传递。

## Compatibility
- YAYA：从早期版本起可用
- AYA：5.8版以后可用
- Tc604-1：新增加载 SAORI-basic 可执行文件的功能

## See Also
- REQUESTLIB
- UNLOADLIB
- FUNCTIONEX
