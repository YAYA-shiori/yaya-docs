# yaya_shiori3.dic

## What Is a System Dictionary?

A system dictionary is a collection of YAYA script files that provide a set of functions to make YAYA “easy to use as a ghost’s SHIORI.” The system dictionary currently consists of the following files (located in the `yaya_base` folder).

| File | Description |
|---------|------|
| `shiori3.dic` | SHIORI core dictionary. Implements the minimum functionality required to operate as SHIORI. Described on this page |
| `compatible.dic` | Legacy compatibility dictionary. Implements functions for compatibility with AYA4 and 5 (you do not need to load it if it is not needed) |
| `optional.dic` | Additional features dictionary. Implements useful functions that are not required ([yaya_optional.dic](./yaya-optional-dic.md)) |
| `lint.dic` | Provides `SHIORI3FW.Lint.Run`, which searches loaded dictionaries for undefined or unused variables and functions (YAYA Tc574-1 and later) |
| `config.dic` | A dictionary for setting and changing the parameters of `shiori3.dic`. This dictionary is intended to be modified by the user (ghost author). Details are included in the file itself |

In general, users do not need to modify any of the dictionaries except `config.dic`.

The latest stable version is available from “[Hello YAYA World (Konnoyayame)](http://ms.shillest.net/yayame.xhtml)”. Update it as appropriate. When updating, we recommend updating `yaya.dll` at the same time. The latest development version is available at [yaya-dic](https://github.com/YAYA-shiori/yaya-dic).

To use `yaya-dic`, add the following line to the basic settings file ([Basic Settings](../grammar/01-basic-settings.md)).

```
dicdir, yaya_base
```

By editing `_loading_order.txt`, you can disable `optional.dic` or enable `compatible.dic`.

## Overview

`yaya_shiori3.dic` is a system dictionary that provides core SHIORI/3.0 functionality to YAYA-based ghosts.

## SHIORI Event Input and Output

A SHIORI event passed from the baseware is a string such as the following.

```
GET SHIORI/3.0
Sender: SSP
Charset: UTF-8
SecurityLevel: local
ID: OnSecondChange
Status: talking
Reference0: 107
Reference1: 0
Reference2: 0
Reference3: 1
Reference4: 0
```

`yaya_shiori3.dic` interprets this string and performs the following actions.

| Header | Action |
|--------|------|
| `ID: OnSecondChange` | Interprets this as the event name and calls the `OnSecondChange` function. For an ID that does not start with `On`, calls the function with `On_` prefixed (for example: `hwnd` → `On_hwnd`) |
| `Sender: SSP` | Stores the value (`"SSP"`) in the global variables `basewarename` and `sender` |
| `Charset: UTF-8` | Character encoding. Interprets it appropriately and converts output to that encoding |
| `Status: talking` | Stores the value (`"talking"`) in the global variable `status` |
| `Reference0: 107` | Stores the value (107) in the global variable `reference[0]` |

After processing the event in the `OnSecondChange` function, `yaya_shiori3.dic` returns the result to the baseware as a string such as the following.

```
SHIORI/3.0 200 OK
Sender: AYA
Charset: UTF-8
Value: \0\s[0]あ、エミリさん。\1\s[10]テディも元気そうだな。
Reference0: Emily
```

| Header | Content |
|--------|------|
| `SHIORI/3.0 200 OK` | Automatically returns the appropriate code |
| `Sender: AYA` | Added automatically |
| `Charset: UTF-8` | Automatically returns the appropriate code |
| `Value: ～` | Contains the function’s result (that is, the talk content) |
| `Reference0: Emily` | If a global variable named `res_reference*` (`*` is a number) exists, its value is placed here (the baseware recognizes the Reference0 returned by SHIORI as the name of the ghost being communicated with) |

## Random Talk

To make it easy to perform random talk, this dictionary has a feature that calls the `OnAiTalk` function every `aitalkinterval` seconds. `OnAiTalk` is not normally a feature provided by the baseware; `yaya_shiori3.dic` adds it.

## Internal Translation

This dictionary has a feature that calls the `OnTranslateInternal` function after processing every event. The argument (`_argv[0]`) is the talk content that is about to be output to the baseware. The content returned by this function becomes the talk that is actually output to the baseware. Therefore, by suitably modifying `_argv[0]` and returning it from `OnTranslateInternal`, you can apply the same transformation to all talk, for example.

## Chain Talk

Chain talk is a feature that “uses a particular talk as a trigger to perform a series of talks in a specified order.” This is also implemented in `yaya_shiori3.dic`.

Chain talk is triggered by writing `:chain=○○` after `\e` in a talk (`○○` is an identifier used to distinguish chain talks; it can be any string except `end`). When chain talk is triggered, `OnAiTalk` calls the `○○` function (the chain function) described above instead of random talk (this feature is specified in the ghost template, not in `yaya_shiori3.dic`).

Unlike ordinary functions, chain functions are written as follows (when using `:chain=hoge`).

```
hoge
{{CHAIN
    "\0\s[0]りんご\e"
    "\0\s[1]ごりら\e"
    "\0\s[0]らっぱ\e:chain=end"
}}CHAIN
```

In an ordinary function, one of “りんご”, “ごりら”, or “らっぱ” is selected at random; in a chain function, the talks are chained in order from top to bottom. Chain talk can be stopped by writing `:chain=end` after `\e`.

### Chain delimiter (`:chain=`)

Append `:chain=EventName` to the end of a talk script to have the specified event called at the next random talk opportunity.

```
OnMyEvent
{
	'\0\s[0]続きがあるよ。\e' + ':chain=' + 'OnMyEventPart2'
}

OnMyEventPart2
{
	'\0\s[0]これが続きです。\e'
}
```

## Delayed EVAL

Writing `:eval=expression` after `\e` executes the expression (this is equivalent to writing `EVAL(expression)`). For example, writing `"\0\s[0]はじめまして。\e:eval=aisatu=1"` makes it easy to perform something like “flag processing triggered by speaking a particular talk.”

For security reasons, this feature is disabled by default. To enable it, first make sure you understand the security risks, then set `SHIORI3FW.ENABLE_DELAYED_EVAL` to 1 in `config.dic`.

## Installed ghost list

Interprets `ID: installedghostlist` and creates the global variable `installedghostlist` (a generic array of ghost names), among others.

When events such as `OnNotifyInstalledGhostName` are received, the following variables are automatically updated. Their indices correspond: the sakura name of the ghost in `installedghostlist[i]` is `installedsakuralist[i]`.

| Variable name | Contents |
|--------|------|
| `installedghostlist` | Array of installed ghost names |
| `installedsakuralist` | Array of installed ghost sakura names |
| `installedkerolist` | Array of installed ghost kero names |

## SAORI calls

To make SAORI calls easier, `yaya_shiori3.dic` provides the following functions. SAORI modules are also loaded and unloaded automatically when using `FUNCTIONEX`.

### FUNCTIONEX

```
FUNCTIONEX( dllname [, Argument0 , Argument1 , ... ] )
```

| Argument | Description |
|------|------|
| `dllname` | Name of the SAORI DLL to call. Specify a path relative to `yaya.dll` |
| `Argument0, 1, ...` | Arguments to pass to SAORI (optional) |

The return value of `FUNCTIONEX` is the SAORI return value (the value of Result). If SAORI returns additional values (Value0, 1, …), they are stored in the `valueex` array and the global variables `valueex0`, `valueex1`, … .

```
_result = FUNCTIONEX('kawari8.dll', 'こんにちは')
// 追加の戻り値は valueex[0], valueex[1], ... で参照
```

For details, see [FUNCTIONEX](../functions/FUNCTIONEX.md).

#### Baseware built-in modules (SAORI over DirectSSTP)

When `dllname` begins with `internal_` (such as `internal_crypto` or `internal_time.dll`; case-insensitive, and the trailing `.dll` is optional), the DLL is not loaded. Instead, the built-in module in the baseware (SSP 2.9.13 or later) is called using `DIRECTSSTP`. The syntax, return value, `valueex`, and `LIB.STATUSCODE` work the same as for DLL-based SAORI. See [SAORI over DirectSSTP](https://ssp.shillest.net/ukadoc/manual/spec_saori_ex.html) for the available modules and functions.

```
_hash = FUNCTIONEX('internal_crypto', 'Digest', 'sha256', 'abc')
_text = FUNCTIONEX('internal_time', 'Format', 0, '%Y/%m/%d', '--tz=+09:00')
```

- If the module is unavailable (older SSP, a baseware other than SSP, or an unknown module), 0 is returned. Availability is checked and remembered separately for each module, only the first time it is used, with `GET Version SAORI/1.0`. Immediately after startup, while the ghost window (`SHIORI3FW.HWnd[0]`) is not yet known, 0 is returned without remembering the result
- On failure (400, 500), Result is empty, and `LIB.STATUSCODE` contains a value such as `400 Bad Request`. The reason for the failure (`ErrorDescription`) can be read from `var.lib.key` / `var.lib.value`
- If an argument contains a newline (CR or LF), it could be used to add headers, so it is not sent and 0 is returned. Pass data containing newlines or leading or trailing whitespace in a format such as `--data-in=base64`
- The character encoding is fixed to UTF-8
- For operations that take time (`DeriveKey`, `HashPassword`, etc.), add `--async=identifier`. The result is delivered later in an event (such as `OnInternalSaoriComplete`), and the return value of `FUNCTIONEX` is empty (`LIB.STATUSCODE` is `204 No Content`)

### SAORI

A synonym (alias) for `FUNCTIONEX`. The syntax is the same as for `FUNCTIONEX` (including for `internal_` built-in modules). It is slower than `FUNCTIONEX` due to an additional layer of indirection, but not enough to be a concern.

### FUNCTIONLOAD

Loads a SAORI DLL. The argument is the SAORI DLL filename. Returns 1 on success and 0 on failure.

```
FUNCTIONLOAD('kawari8.dll')
```

### SHIORI3FW.SaoriUnloadAll

Unloads all currently loaded SAORI DLLs. Takes no arguments and returns no value.

## Baseware property functions

Read and write properties of baseware that supports DIRECTSSTP, such as SSP, and execute EXECUTE SSTP commands.

| Function | Description |
|------|------|
| `EXECUTE_SSTP(CommandName, Argument0, Argument1, ...)` | Sends `EXECUTE SSTP/1.1` to the baseware and returns the result (additional data) |
| `GET_PROPERTY(PropertyName)` | Gets a property value. Returns the property value as a string on success, or an empty string on failure |
| `SET_PROPERTY(PropertyName, Value)` | Sets a property value. Returns 1 on success and 0 on failure |

```
_vol = GET_PROPERTY('volume')
SET_PROPERTY('volume', '80')
```

### EXECUTE_SSTP

```
EXECUTE_SSTP( コマンド名 [, 引数0 , 引数1 , ... ] )
```

Sends an `EXECUTE SSTP/1.1` request to the baseware using DIRECTSSTP and returns the result. The second and subsequent arguments are sent as `Reference0`, `Reference1`, … . For available commands, see the baseware SSTP specification (`GetVersion`, `GetGhostNameList`, `GetStatus`, `GetCookie`, etc.).

- Return value: On success (status 2xx), returns the additional data after the blank line, with the trailing newline removed. Returns an empty string on failure. Results from commands that return a list are strings delimited by `C_CRLF`
- Result variables: `SSTP.STATUSCODE` contains the status line result (such as `200 OK` or `501 Not Implemented`), and `SSTP.STATUS` contains its numeric value. If the request could not be sent, these contain `''` and 0
- If the command or an argument contains a newline (CR or LF), it could be used to add headers, so it is not sent and an empty string is returned (`SSTP.STATUS` is 0)

Commands with no additional data return an empty string even on success, so check `SSTP.STATUS` to determine whether they succeeded.

```
_ver = EXECUTE_SSTP('GetShortVersion')
_ghosts = SPLIT(EXECUTE_SSTP('GetGhostNameList'), C_CRLF)

_dummy = EXECUTE_SSTP('SetCookie', 'mykey', 'value')
if SSTP.STATUS == 200 || SSTP.STATUS == 204 {
	// 成功
}
```

`GET_PROPERTY` is equivalent to `EXECUTE_SSTP('GetProperty', PropertyName)`, and `SET_PROPERTY` is equivalent to `EXECUTE_SSTP('SetProperty', PropertyName, Value)`; `SSTP.STATUSCODE` and `SSTP.STATUS` are set in the same way.

## Array Operations

| Function | Description |
|------|------|
| `JOIN(値0, 値1, ..., 区切り文字)` | Returns a string formed by joining the values other than the last argument, which is used as the delimiter (if an array is passed, its elements are joined) |
| `REVERSE(値0, 値1, ...)` | Returns an array with the arguments in reverse order |
| `UNIQUE(値0, 値1, ...)` | Returns an array with duplicates removed from the arguments (a wrapper for [ARRAYDEDUP](../functions/ARRAYDEDUP.md)) |
| `SPLITEX(文字列, 区切り文字)` | Works like [SPLIT](../functions/SPLIT.md), but does not convert empty elements into array elements |
| `MAX(値0, 値1, ...)` | Returns the largest argument. If the arguments include strings, the last one in lexicographical order is returned |
| `MIN(値0, 値1, ...)` | Returns the smallest argument. If the arguments include strings, the first one in lexicographical order is returned |
| `AVERAGE(値0, 値1, ...)` | Returns the average of the arguments. If the arguments include strings, an empty string is returned |

```
_配列 = ("A","B","C","D","E")
結果 = JOIN(_配列, "★")   // "A★B★C★D★E"
```

## Text Processing and Status Checks

### SHIORI3FW.RemoveAllTags

Returns a string with all Sakura Script tags (such as `\0` and `\s[0]`) removed.

```
_plain = SHIORI3FW.RemoveAllTags('\0\s[0]こんにちは。\e')
// → "こんにちは。"
```

To display tags escaped rather than removing them, use [SHIORI3FW.EscapeAllTags](./yaya-optional-dic.md#shiori3fwescapealltags).

### SHIORI3FW.CanTalk

Returns whether the current ghost can talk. If the `status` header contains any of `talking`, `choosing`, `minimizing`, or `timecritical`, the ghost is considered unable to talk. Returns 1 if it can talk, or 0 if it cannot.

```
if SHIORI3FW.CanTalk {
	// ランダムトーク発動
}
```

## Delayed Events (Events That "Speak Later")

Triggers a specific event just once after the specified number of seconds. The event is processed at the `OnSecondChange` (every second) timing.

### SHIORI3FW.SetDelayEvent

```
SHIORI3FW.SetDelayEvent( '発生させるイベント名' , 遅れる秒数 [, Reference0, ...] )
```

Registers a delayed event. If the event name is an empty string, the event is canceled. The third and subsequent arguments are Reference values to set when the event is triggered (optional).

```
// 10秒後に OnMyDelayedEvent を発動
SHIORI3FW.SetDelayEvent('OnMyDelayedEvent', 10)

// キャンセル
SHIORI3FW.SetDelayEvent('', 0)
```

### SHIORI3FW.GetDelayEvent

Returns information about the currently registered delayed event as `(event name, remaining seconds, Reference array)`.

## Adding Response Headers

You can add arbitrary headers to an event handler's response. The settings are reset for each request.

| Function | Description |
|------|------|
| `SHIORI3FW.PushAdditionalReturn(ヘッダ名, 値)` | Adds an arbitrary response header |
| `SHIORI3FW.Push_X_SSTP_PassThru(名前, 値)` | Adds an `X-SSTP-PassThru-名前` header (used for SSTP passthrough) |

Setting values for the following variables inside an event handler automatically adds them to the response headers.

| Variable name | Header | Content |
|--------|--------|------|
| `res_reference` or `res_reference0`–`res_reference31` | `Reference0:`– | Reference values for the event response. Specify them as an array or as individual variables |
| `marker` or `res_marker` | `Marker:` | SSTP marker value |
| `res_securitylevel` | `SecurityLevel:` | Security level |
| `res_valuenotify` | `ValueNotify:` | ValueNotify value |

```
OnMyEvent
{
	res_reference0 = 'value0'
	res_reference1 = 'value1'
	'\0\s[0]処理しました。\e'
}
```

The maximum index for `res_reference` is determined by `SHIORI3FW.RES_REF_MAX` in `config.dic` (default value: 32).

## Variable Management Utilities

### SHIORI3FW.RegisterTempVar

```
SHIORI3FW.RegisterTempVar( 変数名, ... )
```

Registers global variables for automatic deletion at shutdown (on unload). Use this to manage temporary global variables that do not need to be saved.

```
myTempVar = '一時データ'
SHIORI3FW.RegisterTempVar('myTempVar')
```

## Pseudo-Events

Define these functions in a ghost's dictionary to have them called at specific times.

| Function | When it is called |
|------|------------------|
| `OnSHIORI3FW.SurfaceRestore` | When 2/3 of the AI talk interval has elapsed. Use this for tasks such as restoring the surface to its default before a talk |
| `OnSHIORI3FW.ChangeSelfInfo` | When the ghost name, shell name, shell path, balloon name, or balloon path is updated |
| `OnSHIORI3FW.WindowCreate` | When a character window is newly created. The scope number is set in `reference[0]` |
| `OnSHIORI3FW.WindowDestroy` | When a character window is destroyed. The scope number is set in `reference[0]` |

```
OnSHIORI3FW.SurfaceRestore
{
	'\0\s[0]\1\s[10]\e'
}
```

## System Variables

The following variables are provided to make functions that are inconvenient to use directly easier to use. They can be used to obtain system information. The system updates these variables automatically, so use them for reference only.

### Time-Related Variables

| Variable name | Return value |
|--------|--------|
| `year` | Numeric value of the current year |
| `month` | Numeric value of the current month |
| `day` | Numeric value of the current day |
| `weekday` | Numeric value of the current day of the week (0=Sunday, 1=Monday … 6=Saturday) |
| `hour` | Numeric value of the current hour (24-hour clock) |
| `ampm` | Numeric value for AM or PM at the current time (0=AM, 1=PM) |
| `hour12` | Numeric value of the current hour (12-hour clock) |
| `hour12ex` | Numeric value of the current hour (12-hour clock). However, 12 is displayed as 0 or 12 |
| `minute` | Numeric value of the current minute |
| `second` | Numeric value of the current second |
| `systemuptime` | OS uptime (in seconds) |
| `systemupsecond` | Seconds component of OS uptime expressed as hours, minutes, and seconds |
| `systemupminute` | Minutes component of OS uptime expressed as hours, minutes, and seconds |
| `systemuphour` | Hours component of OS uptime expressed as hours, minutes, and seconds |
| `ghostupmin` | Ghost uptime (in minutes) |
| `ghostupmin_total` | Ghost's cumulative uptime (in minutes) |
| `ghostuptimes` | Ghost's cumulative number of starts |

### Memory Variables

| Variable Name | Return Value |
|--------|--------|
| `memoryload` | Physical memory usage |
| `memorytotalphys` | Amount of physical memory |
| `memoryavailphys` | Amount of available physical memory |
| `memorytotalvirtual` | Amount of virtual + physical memory |
| `memoryavailvirtual` | Amount of available virtual + physical memory |

### Sender Header Variables

| Variable Name | Return Value |
|--------|--------|
| `basewarenameex` | Name of the baseware running the ghost (`embryo` for MATERIA, `crow` for CROW, `SSP` for SSP). This is the value at first startup and does not change |
| `basewarename` | Name of the baseware that sent the current request (sender header name; may contain something other than a baseware name) |
| `sender` | Same as `basewarename` |

### Ghost and Shell Information

| Variable Name | Content |
|--------|------|
| `SHIORI3FW.GhostName` | Current ghost name |
| `SHIORI3FW.ShellName` / `SHIORI3FW.ShellPath` | Current shell name / shell path |
| `SHIORI3FW.BalloonName` / `SHIORI3FW.BalloonPath` | Current balloon name / balloon path |
| `selfname` / `sakuraname` | Character name of Sakura (scope 0) |
| `keroname` | Character name of Kero (scope 1) |
| `SHIORI3FW.HWnd` | Array of character window HWNDs. `[0]` is Sakura's |
| `SHIORI3FW.BalloonHWnd` | Array of balloon window HWNDs. `[0]` is Sakura's |
| `SHIORI3FW.LastSurface` | Array of the surface numbers displayed immediately before. `[0]` is Sakura's |
| `SHIORI3FW.IsVisible` | Surface visibility state (1 = visible, 0 = hidden). `[0]` is Sakura's |
| `SHIORI3FW.UserName` / `SHIORI3FW.UserNameFull` | User name (short / full name) |
| `SHIORI3FW.UserBirthday` | Birthday array `[year, month, day]` (integer type) |
| `SHIORI3FW.UserSex` | Sex |
| `SHIORI3FW.LastTalk` | Script spoken immediately before (for all events) |
| `SHIORI3FW.LastAITalk` | Script of the random talk immediately before |
| `SHIORI3FW.Eventid` | ID of the event currently being processed |
| `SHIORI3FW.Status` | Initial startup status (initialized by `Run`) |
| `SHIORI3FW.UniqueID` | ID used by Auth.SSTP |
| `SHIORI3FW.Capability` | Baseware header processing capabilities (generic array) |

## User-Configurable Variables

Variables that can be read and written to customize the ghost's behavior.

| Variable Name | Initial Value | Content |
|--------|--------|------|
| `aitalkinterval` | 180 (seconds) | Interval at which AI talk (random talk) is triggered. Set to 0 to disable |
| `communicateratio` | 0 (%) | Percentage of AI talk triggers that start a communication |

```
aitalkinterval = 300
```

## Main Settings in config.dic

You can change system behavior in `config.dic`.

| Constant Name | Initial Value | Content |
|--------|--------|------|
| `TALK_INTERVAL` | 180 | Initial value of `aitalkinterval` (seconds) |
| `COM_RATIO` | 0 | Initial value of `communicateratio` (%) |
| `SHIORI3FW.IGLIST_ACCEL` | 1 | When set to 1, builds the ghost list faster using SSP / CROW NOTIFY events (lists of Sakura and Kero names are not created) |
| `SHIORI3FW.IGLIST_MAX` | 0 | Maximum number of ghosts to retrieve when building the ghost list by scanning files. -1 means unlimited; 0 means none |
| `SHIORI3FW.RES_REF_MAX` | 32 | Maximum index for `res_reference*` variables |
| `SHIORI3FW.AUTO_DATA_CONVERT` | 0 | When set to 1, performs automatic type conversion of SAORI return values and replaces byte value 1 with a comma (AYA5 compatibility) |
| `SHIORI3FW.REF_ACCEL` | 0 | When set to 1, uses only `reference[0]` instead of creating variables such as `reference0` (for faster execution) |
| `SHIORI3FW.ENABLE_DELAYED_EVAL` | 0 | Enables delayed EVAL using `:eval=` (disabling it is recommended for security reasons) |

## Default Values for the AI Graph

SSP's AI graph (radar chart) is drawn using the SHIORI resource `getaistate`. If the ghost does not have `On_getaistate`, or returns an empty value, the system dictionary's `SHIORI3EV.On_getaistate` returns the following 6 axes. If `On_getaistate` is defined by the ghost, that definition takes precedence.

| Label | Display Value | Increment Value | Maximum Value |
|--------|--------|--------|--------|
| `Boot` | `ghostuptimes` (total number of startups) | 0 | Step scale |
| `Uptime(h)` | `ghostupmin_last / 60` (total startup time up to the previous session) | `ghostupmin / 60` (time for the current session) | Step scale |
| `Memory` | Number of elements in `GETVARLIST()` | 0 | Step scale |
| `Repertoire` | Number of elements in `GETFUNCLIST('On')` | 0 | Step scale |
| `Talk/h` | `3600 / aitalkinterval` (0 if `aitalkinterval` is 0 or less) | 0 | Step scale |
| `Social` | `communicateratio` | 0 | 100 |

- The step scale is the smallest value that can contain the value: 10, 20, 50, 100, 200, 500, … (`SHIORI3FW.AIGraphMax`)
- `Memory` and `Repertoire` include the system dictionary's own variables and functions
- The display and increment values for `Uptime(h)` are decimal values (SSP 2.4.26 and later can handle decimals)

## Related

- [yaya_optional.dic](./yaya-optional-dic.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
- [System Dictionary Function Manual (yaya-dic)](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
