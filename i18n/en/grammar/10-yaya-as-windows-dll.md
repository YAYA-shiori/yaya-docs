# YAYA as a Windows DLL

## Overview

YAYA (pronounced “Yaya”) is a DLL for processing strings. It uses syntax similar to C, and can perform operations such as:

- Processing a given string
- Generating a string based on programmed rules

YAYA is a Windows DLL, so some programming knowledge is required to use it directly.

## Operating Environment

For Windows. It is built with the same development environment as SSP, using settings that are expected to work even on Windows 95.

## Exported Functions

YAYA provides the following exported functions. A program that uses YAYA should call these functions to perform the desired operations after calling `LoadLibrary` for YAYA.

### load

```c
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len)
```

Instructs YAYA to initialize. Call this function exactly once, immediately before you start using YAYA after calling `LoadLibrary`. Pass the absolute path of the directory that YAYA recognizes as the current directory in `h`, and the length of `h` in `len`. YAYA frees the memory pointed to by `h`, so the caller does not need to free it.

### unload

```c
extern "C" __declspec(dllexport) BOOL __cdecl unload()
```

Instructs YAYA to shut down. Call this function exactly once, immediately before calling `FreeLibrary` for YAYA.

### request

```c
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len)
```

Instructs YAYA to process a string and returns the result. Pass the string to be processed in `h`, and the length of `h` in `*len`. YAYA frees the memory pointed to by `h`, so the caller does not need to free it.

The result is returned as the return value. The length of the result is stored in `*len` (that is, this value is overwritten). After obtaining the return value, free the memory (`GlobalFree`) using the size specified by `*len`.

## Technical Notes

This is exactly the same as the interface specification for the pseudo-AI DLL “SHIORI” used by the desktop mascot software “Ukagaka.”

## Terms of Use

- Follow the accompanying documentation.
- The [LICENSE](../functions/LICENSE.md) system function can display the license terms for the libraries used by YAYA.
