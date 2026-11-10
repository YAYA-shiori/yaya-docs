# Basic Settings

## Overview

The default DLL file name for YAYA is `yaya.dll`, and the main file name `yaya` can be freely changed to another name.

A file called the “basic settings file” is required for YAYA to run. The basic settings file is named “main-file-name.txt”; by default, this is `yaya.txt`. If you change the DLL file name to `hoge.dll`, the basic settings file will be `hoge.txt`.

The basic settings file is a text file and is decoded using the default character encoding of the OS on which it runs. If internationalization needs to be considered, the basic settings file should contain only ASCII characters to avoid problems with multibyte character encodings.

If there is no settings file, or no dictionaries to load, YAYA runs in [shell mode](#シェルモード) (Tc574-7 / Tc602-12 and later; before then, it stopped with error E0005 if there was no settings file).

## Example Settings

```
// dics
dic, basis.dic
dic, control./*doc*/ayc

// option parameters
charset, UTF-8
charset.dic, Shift_JIS
charset.setting, Shift_JIS
charset.output, UTF-8
charset.file, Shift_JIS
charset.save, UTF-8
charset.extension, Shift_JIS

msglang, english
log, executelog.txt
iolog, off
fncdepth, 16
```

Specify settings by separating commands and parameters with commas. Blank lines (lines containing only a newline), everything after `//`, and areas enclosed by `/*` and `*/` are treated as comments.

## Behavior When a Dictionary Error Occurs During Loading

From Tc555-1 onward, if a dictionary error occurs during loading, YAYA first attempts to load again using the emergency basic settings file.

The emergency basic settings file is named “main-file-name_emerg.txt”; by default, this is `yaya_emerg.txt`. Its behavior when the DLL name is changed is the same as for the regular basic settings file.

If an error still occurs, the request function returns nothing (NULL).

You can retrieve the error log for problems that occur with [GETERRORLOG](../functions/GETERRORLOG.md).

Emergency mode using `yaya_emerg.txt` does not switch to [shell mode](#シェルモード). If `yaya_emerg.txt` does not exist, YAYA stops running as before.

## Settings

### charset, name

Sets the default character encoding. Specify one of the following reserved values. If none is specified, Shift_JIS is used.

- `Shift_JIS` / `ShiftJIS` / `SJIS`: Shift JIS encoding
- `UTF-8`: UTF-8
- `default`: The default character encoding of the OS on which it runs

The following settings that begin with `charset.` are individual settings. Always write them after the general `charset` setting.

### charset.dic

The character encoding of dictionaries.

### charset.setting

The character encoding of the basic settings file itself.

### charset.output

The character encoding for input and output through the request function.

### charset.log

The character encoding for log files and balloon output (Tc569-15 and later).

### charset.file

The character encoding for file input and output.

### charset.save

The character encoding for input and output of global variable save files.

### charset.save.old

The character encoding used when reading old-format save files that do not specify an encoding.

### charset.extension

The character encoding for input and output to external DLLs (such as SAORI).

### dic, filename ( , charset )

Loads the dictionary file `filename`. A dictionary file is a program source file containing YAYA scripts; YAYA runs based on the contents programmed in these files. Any number of dictionary files can be specified for loading.

Specify `filename` as a relative path from the path location specified by load.

The standard dictionary file is a plain text file written in the character encoding specified by `charset`. In addition, encrypted files scrambled according to a specific rule can also be loaded.

If you add a character encoding after the file name, separated by a comma, the specified file is read using that encoding.

### dicif, filename ( , charset )

Works like `dic`, but ignores the specified file if it does not exist (Tc571-2 and later).

### dicdir, dirname ( , charset )

Loads all files in the specified directory and its subdirectories as dictionaries (Tc556-1 and later). Otherwise, it works like `dic`.

!!! warning "Loading order"
    The order in which files are read is not fixed. As a result, the loading order may cause problems when defining items such as `globaldefine`. When defining `globaldefine`, be sure to load the dictionary containing its definition near the beginning.

If a file named `_loading_order_override.txt` or `_loading_order.txt` exists in the directory specified by `dicdir`, the behavior is the same as writing `includeEX,(directory)/_loading_order.txt`. YAYA checks for the files in the order `_loading_order_override.txt` → `_loading_order.txt`, and applies `includeEX` only to the first one it finds (Tc571-2 and later).

If no `dic` is specified, all files specified by `dicif` do not exist, the `dicdir` directory is empty, or there are otherwise no dictionaries to load, YAYA runs in [shell mode](#シェルモード) (Tc574-7 / Tc602-12 and later).

### msglang, language

!!! note "Usually not required"
    Usually, the language of error messages switches automatically, even if this is not specified (Tc573-5 and later).

Selects the language of error messages and similar text recorded in the log. Specify one of the following reserved values. If none is specified, `japanese` is used.

- `japanese`
- `english`
- `chinese-simplified`
- `chinese-traditional`
- `german`
- `korean`

This setting remains for backward compatibility. Use `messagetxt` instead.

### messagetxt, filename ( , charset )

!!! note "Usually not required"
    Usually, the language of error messages is switched automatically even if you do not specify it (Tc573-5 and later).

Loads a language file for error messages and similar messages recorded in the log. For example, write as follows. If `charset` is omitted, UTF-8 (with BOM) is used (Tc557 and later).

```
messagetxt,messagetxt/japanese.txt
messagetxt,messagetxt/english.txt
messagetxt,messagetxt/chinese-simplified.txt
messagetxt,messagetxt/chinese-traditional.txt
messagetxt,messagetxt/german.txt
messagetxt,messagetxt/korean.txt
```

You can check the language file names in [yaya-shiori's messagetxt](https://github.com/ponapalt/yaya-shiori/tree/500/messagetxt).

From Tc570-1 onward, language files are embedded in the DLL on Windows, so there is no need to distribute the language files themselves. The specification for writing file names in `messagetxt` remains as-is for environments other than Windows.

### basepath, directory

Resets the directory used as the base for loading dictionaries and other files to an arbitrary location. If not set, this is normally the same directory as `yaya.dll` (Tc557 and later).

### include, filename

Loads the contents of a basic settings file from another file. The contents of the specified file are also treated as valid basic settings.

### includeEX, filename

The process is basically the same as `include`, but if the file name specified in `filename` contains a directory name, the current directory is temporarily switched to that directory before processing `include` (Tc559 and later).

### log, logfilename

Records the execution log in the file `logfilename`. The log is written using the character encoding specified by `charset.log`. Specify `logfilename` as a relative path from the path specified by load.

### iolog, [on|off]

Specifies whether to record input and output strings and processing times in the log when executing load, unload, and request. Set to `on` to record them. The default is `on`, so set this to `off` if you do not need logging. Even if `off` is specified, logging is forcibly set to `on` when launched by dragging and dropping onto the ball.

### iolog.filter.keyword, [ignore-matching string]

If a request string contains the specified ignore-matching string, the I/O for that request is not recorded in the log (and is not output to the ball). Multiple strings can be specified. The old definition name is `ignoreiolog`.

Example: Do not record `OnSecondChange` and `OnMouse`-related events

```
ignoreiolog, ID: OnSecondChange //OnSecondChange無視
iolog.filter.keyword, OnMouse        //OnMouse系無視
```

Due to the syntax of basic settings files, whitespace before and after the ignore-matching string, as well as anything after the comment marker `//`, is ignored.

### iolog.filter.keyword.delete, [string]

Deletes the above. This form is intended for [SETSETTING](../functions/SETSETTING.md), so writing it directly in a definition file has little purpose.

### iolog.filter.keyword.regex, [ignore-matching string: regular expression]

The regular-expression version of `iolog.filter.keyword`.

### iolog.filter.keyword.regex.delete, [string]

Deletes the above. This form is intended for [SETSETTING](../functions/SETSETTING.md), so writing it directly in a definition file has little purpose.

### iolog.filter.mode, [mode]

For the conditions specified under `iolog.filter.keyword` above, switches between “do not output items that match the conditions” and “output only items that match the conditions.” If not defined, the mode is “do not output items that match the conditions.”

```
iolog.filter.mode,allowlist
iolog.filter.mode,whitelist
```

Switches to the mode that outputs only items that match the conditions.

```
iolog.filter.mode,denylist
iolog.filter.mode,blacklist
```

Switches to the mode that does not output items that match the conditions.

### fncdepth, [depth]

Specifies the maximum function call depth as a number. The default is 32. The minimum is 2; values smaller than this or invalid values are treated as 2. Setting this to 0 disables the depth limit check (Tc556-1 and later).

When the limit is reached, [shiori.OnCallLimit](../system/shiori-OnCallLimit.md) is called.

Separately from the depth limit, from Tc607-4 onward, if the remaining stack space of the thread running YAYA becomes low (roughly less than 128KB), calls are stopped and `shiori.OnCallLimit` is called, just as when the limit is reached. The value of the stopped call becomes empty. Even if `fncdepth` is set to 0 or a large value, the stack can no longer be exhausted, causing the baseware to crash. The depth at which calls stop depends on the size of the baseware thread's stack (several hundred levels with a 1MB stack). Up through Tc607-3, setting this to 0 and making calls too deeply would cause the baseware to crash.

### looplimit, [count]

Specifies the maximum number of loop iterations as a number. The default is 1000000 (from Tc574-10 / Tc606-4 onward; before that, it was 10000). Setting this to 0 disables the limit check, but execution will continue indefinitely and freeze. This has no effect on `foreach` (Tc564-1 and later).

When the limit is reached, [shiori.OnLoopLimit](../system/shiori-OnLoopLimit.md) is called.

### save.encode, [on|off]

Encrypts the save file. This encryption is not very strong, so think of it as making the file only somewhat harder to understand. Once set to `on`, the save file remains encrypted until it is deleted. Be very careful when changing this setting.

### save.auto, [on|off]

Toggle automatic save-file saving on or off. When on, backups are made at regular intervals and variables are automatically saved on exit. When off, nothing is saved unless a save function is explicitly called. The default is on.

### embed.lazy, [on|off]

Look up the names of strings embedded with `%` without parentheses at runtime (default: `on`). With `off`, names are resolved when the dictionary is loaded (Tc604-1 and later. [Details](06-string-embedding.md#名前を読み込み時に確定する)).

### maxlognum, [count]

Set the maximum number of log entries available through [GETERRORLOG](../functions/GETERRORLOG.md). The default value is 256 entries.

## Shell mode

Tc574-7 / Tc602-12 and later. If there is no configuration file, or no dictionaries to load, YAYA behaves as if it had loaded only the following dictionary.

```c
load { }
unload { }
request { EVAL(_argv[0]) }
```

The string passed to request is evaluated as-is with [EVAL](../functions/EVAL.md), and the result is returned. You can write a single expression, a sequence of statements separated by `;` or newlines, or control statements. This makes it easy to quickly check how YAYA expressions and functions work, without preparing a complete ghost or dictionary.

| request input | Return value |
|---------------|------|
| `1+2` | `3` |
| `_a = 3; _a * 5` | `15` |
| `'hello' + ' world'` | `hello world` |
| `X = 10` | Empty string (10 is assigned to the global variable `X`) |
| `X` | `10` |

- Global variables are retained for the duration of the same session
- If there is no configuration file, variables are not automatically saved or restored (`yaya_variable.cfg`). If a configuration file exists but no dictionary is specified, settings such as `save.auto` are followed
- When shell mode starts, note N0002 is written to the log
- Errors such as a dictionary file specified with `dic` not existing, a syntax error in a dictionary, or a missing `include` target do not result in shell mode
- Since SHIORI requests are also evaluated as-is, this mode is not intended for use as a ghost. It is intended for uses such as loading an empty directory with `load` in the executable version of YAYA (`yaya.exe`), then sending expressions with `request`
