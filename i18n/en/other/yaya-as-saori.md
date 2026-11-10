# YAYA as SAORI

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Overview

A module created by Setsuri that lets you call yaya.dll as a SAORI.<br>
It allows you to use YAYA's functionality from SHIORI implementations other than YAYA.

By default, only YAYA's built-in (system) functions are available.<br>
Adding modules expands its uses even further. If you understand YAYA syntax, you can create these additional modules yourself.<br>

### Download

- ~~[yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)~~
- [Releases · YAYA-shiori/yaya-as-saori · GitHub](https://github.com/YAYA-shiori/yaya-as-saori/releases)

### Additional Modules

- [JSON parser with something like objects](http://c-lege.hacca.jp/ukgk/ukst.html)
  - A module that reads JSON in a JavaScript object-like format and provides operations such as retrieving elements.
- [calendae](http://gallnuts.webcrow.jp/dump.shtml)
  - A module for calendar-related calculations.
- [sub-edittext](http://gallnuts.webcrow.jp/dump.shtml)
  - A module for editing text files.
- [ssu.aym](http://rabbitbike.oh.land.to/nicky/log200803.html)
  - Provides the same behavior as ssu (the SAORI included with Satori).
- [Reta](http://navy.nm.land.to/post/)
  - Reads text files, the shell names of installed ghosts, and save data from Bun, Satori, Kawari, and Misaka.

### Reference Sites

- [SAORI/YAYA - Satori Wiki](http://soliton.sub.jp/satori/index.php?SAORI%2FYAYA)
  - An explanation of how to use it from Satori.
- [A Brief Guide to AYA as SAORI for Satori](http://navy.nm.land.to/post/a_a_s.html)
  - This explains AYA as SAORI, but can also be used for YAYA as SAORI (however, it does not cover functions added in YAYA).

### Demo Ghost

- [Konnosayame](http://navy.nm.land.to/post/)
  - A demo ghost for Satori. The included SAORI version is old, so replacing it is recommended.

### Creating Your Own Modules

- You can add modules freely by appending them to [yaya.txt](../grammar/01-basic-settings.md), just as you would with a regular dictionary.<br>By convention, the extension is often set to “.aym” (short for aya module), but other extensions do not affect operation.
- SAORI arguments are stored in the module in an array named `REQ.ARGS[*]`.<br>Argument0 is `REQ.ARGS[0]`, and subsequent arguments are handled in the same way.
- SAORI return values are returned by assigning them to the variables RES.RESULT and `RES.VALUE*` in the module.<br>The single return value Result is returned in RES.RESULT, while each of the multiple return values Value\* is returned in its own `RES.VALUE*`.<br>Note that `RES.VALUE*` is **not an array**. The system function [EVAL](../functions/EVAL.md) may be useful for assignments.
- If the SAORI function cannot execute normally, for example because an argument is invalid, return the number -1 as the function's return value (not as a SAORI return value).<br>When the YAYA as SAORI system component receives -1 as the return value, it reports an error for an invalid call.<br>In this case, it is recommended that you use YAYA's system function [LOGGING](../functions/LOGGING.md) to log the name of the SAORI function where the error occurred and a description of the error.
- You can choose any function names you like, but using a structure such as “module name.function name” has at least two benefits.
  - First, YAYA as SAORI provides a mechanism for loading and unloading modules with function names that use this structure.<br>When a function name containing a period, such as module name.function name, is called, YAYA as SAORI remembers the module name.<br>Then, when a function with that module name is called for the first time, it looks for a function named **module name.Load** and runs it if one is found.<br>Also, when yaya.dll is unloaded, it looks for a function named **module name.Unload** and runs it if one is found.<br>This mechanism can be used for initialization and cleanup when using global variables shared across an entire module.
  - Second, prefixing function names with the module name in this way makes function names less likely to conflict.<br>Modules created by different people may coexist, and of course one person may also create several separate modules.<br>Naming functions this way with those cases in mind can reduce the risk of function name conflicts to some extent.

## Attachments

- [yaya_as_saori_2014_01_04.zip](../attachment/yaya_as_saori_2014_01_04.zip)
- [yaya_as_saori_2014_11_08.zip](../attachment/yaya_as_saori_2014_11_08.zip)
- [yaya_as_saori_2014_11_08b.zip](../attachment/yaya_as_saori_2014_11_08b.zip)
- [yaya_as_saori_2015_12_30.zip](../attachment/yaya_as_saori_2015_12_30.zip)
- [yaya_as_saori_2021_06_14-2.zip](../attachment/yaya_as_saori_2021_06_14-2.zip)
- [yaya_as_saori_2021_06_14.zip](../attachment/yaya_as_saori_2021_06_14.zip)
- [yaya_as_saori_2021_06_17.zip](../attachment/yaya_as_saori_2021_06_17.zip)
- [yaya_as_saori_2021_06_24-2.zip](../attachment/yaya_as_saori_2021_06_24-2.zip)
- [yaya_as_saori_2021_06_24.zip](../attachment/yaya_as_saori_2021_06_24.zip)
- [yaya_as_saori_2021_06_25.zip](../attachment/yaya_as_saori_2021_06_25.zip)
- [yaya_as_saori_2021_06_28.zip](../attachment/yaya_as_saori_2021_06_28.zip)
- [yaya_as_saori_2021_06_30.zip](../attachment/yaya_as_saori_2021_06_30.zip)
- [yaya_as_saori_2021_07_10.zip](../attachment/yaya_as_saori_2021_07_10.zip)
- [yaya_as_saori_2021_07_11-2.zip](../attachment/yaya_as_saori_2021_07_11-2.zip)
- [yaya_as_saori_2021_07_11.zip](../attachment/yaya_as_saori_2021_07_11.zip)
- [yaya_as_saori_2021_07_16.zip](../attachment/yaya_as_saori_2021_07_16.zip)
- [yaya_as_saori_2021_08_31.zip](../attachment/yaya_as_saori_2021_08_31.zip)
- [yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)
