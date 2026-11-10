# List of System Functions

## Overview

A list of system functions built into YAYA. See each function's page (the `functions/` directory) for details.

## A-C

| Function | Description |
|------|------|
| [ACOS](../functions/ACOS.md) | Returns the arccosine (in radians) |
| [ANY](../functions/ANY.md) | Selects a random element from an array |
| [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) | Dynamically appends to a runtime dictionary |
| [ARRAYDEDUP](../functions/ARRAYDEDUP.md) | Removes duplicate elements from an array |
| [ARRAYSIZE](../functions/ARRAYSIZE.md) | Returns the number of elements in an array |
| [ASEARCH](../functions/ASEARCH.md) | Searches an array and returns the index of the first match |
| [ASEARCHEX](../functions/ASEARCHEX.md) | Searches an array and returns the indices of all matches |
| [ASIN](../functions/ASIN.md) | Returns the arcsine (in radians) |
| [ASORT](../functions/ASORT.md) | Sorts an array |
| [ATAN](../functions/ATAN.md) | Returns the arctangent (in radians) |
| [BINSTRTOI](../functions/BINSTRTOI.md) | Converts a binary string to an integer |
| [BITWISE_AND](../functions/BITWISE_AND.md) | Bitwise AND |
| [BITWISE_NOT](../functions/BITWISE_NOT.md) | Bitwise NOT |
| [BITWISE_OR](../functions/BITWISE_OR.md) | Bitwise OR |
| [BITWISE_SHIFT](../functions/BITWISE_SHIFT.md) | Bit shift |
| [BITWISE_XOR](../functions/BITWISE_XOR.md) | Bitwise XOR |
| [CEIL](../functions/CEIL.md) | Rounds up |
| [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md) | Converts a character encoding ID to text |
| [CHARSETLIB](../functions/CHARSETLIB.md) | Sets the character encoding for an external library |
| [CHARSETLIBEX](../functions/CHARSETLIBEX.md) | Sets the character encoding for a specific external library |
| [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md) | Converts character encoding text to an ID |
| [CHR](../functions/CHR.md) | Converts a UCS-2 code to a character |
| [CHRCODE](../functions/CHRCODE.md) | Returns the UCS-2 code of a character |
| [CLEARERRORLOG](../functions/CLEARERRORLOG.md) | Clears the error log |
| [COS](../functions/COS.md) | Returns the cosine |
| [COSH](../functions/COSH.md) | Returns the hyperbolic cosine |
| [CUTSPACE](../functions/CUTSPACE.md) | Removes leading and trailing spaces and tabs |
| [CVAUTO](../functions/CVAUTO.md) | Automatically converts a string to an appropriate type |
| [CVAUTOEX](../functions/CVAUTOEX.md) | Extended version of CVAUTO |
| [CVINT](../functions/CVINT.md) | Converts a variable to an integer |
| [CVREAL](../functions/CVREAL.md) | Converts a variable to a real number |
| [CVSTR](../functions/CVSTR.md) | Converts a variable to a string |

## D-F

| Function | Description |
|------|------|
| [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) | Restores a variable from a SERIALIZEVAR string (Tc607-3 and later) |
| [DICLOAD](../functions/DICLOAD.md) | Loads a dictionary file |
| [DICUNLOAD](../functions/DICUNLOAD.md) | Unloads a dictionary file |
| [DUMPJSON](../functions/DUMPJSON.md) | Converts a value to a JSON string (Tc602-1 and later) |
| [DUMPTOML](../functions/DUMPTOML.md) | Converts a hash to a TOML string (Tc602-5 and later) |
| [DUMPVAR](../functions/DUMPVAR.md) | Dumps a variable |
| [DUMPXML](../functions/DUMPXML.md) | Converts an element hash to an XML string (Tc602-1 and later) |
| [DUMPYAML](../functions/DUMPYAML.md) | Converts a value to a YAML string (Tc602-5 and later) |
| [ERASE](../functions/ERASE.md) | Removes a substring from a string |
| [ERASEVAR](../functions/ERASEVAR.md) | Deletes a variable |
| [EVAL](../functions/EVAL.md) | Evaluates a string as an expression or sequence of statements |
| [EXECUTE](../functions/EXECUTE.md) | Runs an external program |
| [EXECUTE_CAPTURE](../functions/EXECUTE_CAPTURE.md) | Runs an external program, passes standard input to it, and captures standard output and standard error (Tc608-3 and later) |
| [EXECUTE_WAIT](../functions/EXECUTE_WAIT.md) | Runs an external program and waits for it to finish |
| [FATTRIB](../functions/FATTRIB.md) | Gets or sets file attributes |
| [FCHARSET](../functions/FCHARSET.md) | Sets the character encoding of a file |
| [FCLOSE](../functions/FCLOSE.md) | Closes a file |
| [FCOPY](../functions/FCOPY.md) | Copies a file |
| [FDEL](../functions/FDEL.md) | Deletes a file |
| [FDIGEST](../functions/FDIGEST.md) | Calculates a file hash |
| [FENUM](../functions/FENUM.md) | Lists files and directories |
| [FLOOR](../functions/FLOOR.md) | Rounds down |
| [FMOVE](../functions/FMOVE.md) | Moves a file |
| [FOPEN](../functions/FOPEN.md) | Opens a file |
| [FREAD](../functions/FREAD.md) | Reads from a file |
| [FREADBIN](../functions/FREADBIN.md) | Reads a file as binary data |
| [FREADENCODE](../functions/FREADENCODE.md) | Reads while converting the encoding |
| [FREADHTML](../functions/FREADHTML.md) | Reads an entire HTML file and converts it to a hash (Tc605-1 and later) |
| [FREADJSON](../functions/FREADJSON.md) | Reads an entire JSON file and converts it to a hash or array (Tc601-1 and later) |
| [FREADTOML](../functions/FREADTOML.md) | Reads an entire TOML file and converts it to a hash (Tc602-5 and later) |
| [FREADXML](../functions/FREADXML.md) | Reads an entire XML file and converts it to a hash (Tc601-1 and later) |
| [FREADYAML](../functions/FREADYAML.md) | Reads an entire YAML file and converts it to a hash or array (Tc602-5 and later) |
| [FRENAME](../functions/FRENAME.md) | Renames a file |
| [FSEEK](../functions/FSEEK.md) | Moves the file pointer |
| [FSIZE](../functions/FSIZE.md) | Returns the file size |
| [FSTATUS](../functions/FSTATUS.md) | Returns the status of file I/O operations |
| [FTELL](../functions/FTELL.md) | Returns the file pointer position |
| [FUNCDECL_ERASE](../functions/FUNCDECL_ERASE.md) | Deletes a dynamic function declaration |
| [FUNCDECL_READ](../functions/FUNCDECL_READ.md) | Reads dynamic function declarations |
| [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md) | Writes dynamic function declarations |
| [FUNCTIONEX](../functions/FUNCTIONEX.md) | Calls an external library function |
| [FWRITE](../functions/FWRITE.md) | Writes to a file |
| [FWRITE2](../functions/FWRITE2.md) | Writes to a file (with a newline) |
| [FWRITEBIN](../functions/FWRITEBIN.md) | Writes binary data to a file |
| [FWRITEDECODE](../functions/FWRITEDECODE.md) | Writes while converting the encoding |
| [FWRITEJSON](../functions/FWRITEJSON.md) | Converts a value to JSON and writes it to a file (Tc602-1 and later) |
| [FWRITETOML](../functions/FWRITETOML.md) | Converts a hash to TOML and writes it to a file (Tc602-5 and later) |
| [FWRITEXML](../functions/FWRITEXML.md) | Converts an element hash to XML and writes it to a file (Tc602-1 and later) |
| [FWRITEYAML](../functions/FWRITEYAML.md) | Converts a value to YAML and writes it to a file (Tc602-5 and later) |

## G-I

| Function | Description |
|------|------|
| [GETCALLSTACK](../functions/GETCALLSTACK.md) | Get the call stack |
| [GETDELIM](../functions/GETDELIM.md) | Get the current delimiter |
| [GETENV](../functions/GETENV.md) | Get an environment variable |
| [GETERRORLOG](../functions/GETERRORLOG.md) | Get the error log |
| [GETFUNCINFO](../functions/GETFUNCINFO.md) | Get function information |
| [GETFUNCLIST](../functions/GETFUNCLIST.md) | Get a list of user-defined functions |
| [GETLASTERROR](../functions/GETLASTERROR.md) | Get the last error code |
| [GETMEMINFO](../functions/GETMEMINFO.md) | Get memory information |
| [GETSECCOUNT](../functions/GETSECCOUNT.md) | Get the seconds count |
| [GETSETTING](../functions/GETSETTING.md) | Get a setting value |
| [GETSTRBYTES](../functions/GETSTRBYTES.md) | Return the number of bytes in a string |
| [GETSYSTEMFUNCLIST](../functions/GETSYSTEMFUNCLIST.md) | Get a list of system functions |
| [GETTICKCOUNT](../functions/GETTICKCOUNT.md) | Get the tick count |
| [GETTIME](../functions/GETTIME.md) | Get the current time |
| [GETTIMEZONE](../functions/GETTIMEZONE.md) | Get local time zone information |
| [GETTYPE](../functions/GETTYPE.md) | Return the type of a variable |
| [GETTYPEEX](../functions/GETTYPEEX.md) | Return detailed information about a variable's type |
| [GETVARLIST](../functions/GETVARLIST.md) | Get a list of global variables |
| [HAN2ZEN](../functions/HAN2ZEN.md) | Convert half-width characters to full-width characters |
| [HASH_EXIST](../functions/HASH_EXIST.md) | Check whether a hash contains a key (Tc600-3 and later) |
| [HASH_KEYS](../functions/HASH_KEYS.md) | Return the keys of a hash as an array (Tc600-3 and later) |
| [HASH_SIZE](../functions/HASH_SIZE.md) | Return the number of elements in a hash (Tc600-3 and later) |
| [HASH_SPLIT](../functions/HASH_SPLIT.md) | Split a string to create a hash (Tc600-3 and later) |
| [HASH_VALUES](../functions/HASH_VALUES.md) | Return the values of a hash as an array (Tc600-3 and later) |
| [HEXSTRTOI](../functions/HEXSTRTOI.md) | Convert a hexadecimal string to an integer |
| [IARRAY](../functions/IARRAY.md) | Initialization value for a generic array |
| [IHASH](../functions/IHASH.md) | Create a hash (Tc600-3 and later) |
| [INSERT](../functions/INSERT.md) | Insert a string into a string |
| [ISEVALUABLE](../functions/ISEVALUABLE.md) | Check whether a value can be evaluated by EVAL |
| [ISFUNC](../functions/ISFUNC.md) | Check whether a function exists |
| [ISGLOBALDEFINE](../functions/ISGLOBALDEFINE.md) | Check whether a global definition exists |
| [ISINTSTR](../functions/ISINTSTR.md) | Check whether a string represents an integer |
| [ISREALSTR](../functions/ISREALSTR.md) | Check whether a string represents a real number |
| [ISVAR](../functions/ISVAR.md) | Check whether a variable exists |

## J-P

| Function | Description |
|------|------|
| [LETTONAME](../functions/LETTONAME.md) | Assign a value using a dynamically specified variable name |
| [LICENSE](../functions/LICENSE.md) | Display license information |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | Get the locations where a function is used (LINT) |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | Get the locations where a global variable is assigned (LINT) |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | Get the locations where a global variable is used (LINT) |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | Get the locations where a local variable is assigned (LINT) |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | Get the locations where a local variable is used (LINT) |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | Get the locations where a user-defined function is used (LINT) |
| [LINT.GetVarRefs](../functions/LINT.GetVarRefs.md) | Get each occurrence of variables and functions, along with its block (LINT) |
| [LOADLIB](../functions/LOADLIB.md) | Load an external library |
| [LOG](../functions/LOG.md) | Return the natural logarithm |
| [LOG10](../functions/LOG10.md) | Return the common logarithm |
| [LOGGING](../functions/LOGGING.md) | Write to the log |
| [LSO](../functions/LSO.md) | Return the index of the last selected option |
| [MKDIR](../functions/MKDIR.md) | Create a directory |
| [OUTPUTNUM](../functions/OUTPUTNUM.md) | Set the output format for numbers |
| [PARSEHEADER](../functions/PARSEHEADER.md) | Convert a header such as HTTP or SHIORI into a hash or array (Tc602-3 and later) |
| [PARSEHTML](../functions/PARSEHTML.md) | Convert an HTML string into a hash (Tc605-1 and later) |
| [PARSEJSON](../functions/PARSEJSON.md) | Convert a JSON string into a hash or array (Tc601-1 and later) |
| [PARSETOML](../functions/PARSETOML.md) | Convert a TOML string into a hash (Tc602-5 and later) |
| [PARSEXML](../functions/PARSEXML.md) | Convert an XML string into a hash (Tc601-1 and later) |
| [PARSEYAML](../functions/PARSEYAML.md) | Convert a YAML string into a hash or array (Tc602-5 and later) |
| [POW](../functions/POW.md) | Return a power |
| [PROCESSGLOBALDEFINE](../functions/PROCESSGLOBALDEFINE.md) | Process global definitions |

## Q-S

| Function | Description |
|------|------|
| [RAND](../functions/RAND.md) | Generate a random number |
| [READFMO](../functions/READFMO.md) | Read data from FMO |
| [REPLACE](../functions/REPLACE.md) | Replace a string |
| [REQUESTLIB](../functions/REQUESTLIB.md) | Send a request to an external library |
| [RESTOREVAR](../functions/RESTOREVAR.md) | Restore variables |
| [RE_ASEARCH](../functions/RE_ASEARCH.md) | Search an array using a regular expression |
| [RE_ASEARCHEX](../functions/RE_ASEARCHEX.md) | Search an array using a regular expression (all matches) |
| [RE_GETLEN](../functions/RE_GETLEN.md) | Return the length of a regular expression match |
| [RE_GETPOS](../functions/RE_GETPOS.md) | Return the position of a regular expression match |
| [RE_GETSTR](../functions/RE_GETSTR.md) | Return the string matched by a regular expression |
| [RE_GREP](../functions/RE_GREP.md) | Filter using a regular expression |
| [RE_MATCH](../functions/RE_MATCH.md) | Check for a regular expression match |
| [RE_OPTION](../functions/RE_OPTION.md) | Set regular expression options |
| [RE_REPLACE](../functions/RE_REPLACE.md) | Replace using a regular expression |
| [RE_REPLACEEX](../functions/RE_REPLACEEX.md) | Replace using a regular expression (extended) |
| [RE_SEARCH](../functions/RE_SEARCH.md) | Search using a regular expression |
| [RE_SPLIT](../functions/RE_SPLIT.md) | Split using a regular expression |
| [RMDIR](../functions/RMDIR.md) | Delete a directory |
| [ROUND](../functions/ROUND.md) | Round to the nearest integer |
| [SAVEVAR](../functions/SAVEVAR.md) | Save variables |
| [SERIALIZEVAR](../functions/SERIALIZEVAR.md) | Convert variable values to a string in save-file format (Tc607-3 and later) |
| [SETDELIM](../functions/SETDELIM.md) | Set the delimiter |
| [SETGLOBALDEFINE](../functions/SETGLOBALDEFINE.md) | Set a global definition |
| [SETLASTERROR](../functions/SETLASTERROR.md) | Set the last error code |
| [SETSETTING](../functions/SETSETTING.md) | Change a setting value |
| [SETTAMAHWND](../functions/SETTAMAHWND.md) | Set the window handle for the tama |
| [SIN](../functions/SIN.md) | Return the sine |
| [SINH](../functions/SINH.md) | Return the hyperbolic sine |
| [SLEEP](../functions/SLEEP.md) | Pause execution |
| [SPLIT](../functions/SPLIT.md) | Split a string and return an array |
| [SPLITPATH](../functions/SPLITPATH.md) | Split a path into its components |
| [SQLCLOSE](../functions/SQLCLOSE.md) | Close an SQLite database (Tc602-11 and later) |
| [SQLEXEC](../functions/SQLEXEC.md) | Execute SQL (Tc602-11 and later) |
| [SQLOPEN](../functions/SQLOPEN.md) | Open an SQLite database (Tc602-11 and later) |
| [SQLQUERY](../functions/SQLQUERY.md) | Execute SQL and return the result rows (Tc602-11 and later) |
| [SQRT](../functions/SQRT.md) | Return the square root |
| [SRAND](../functions/SRAND.md) | Set the random seed |
| [STRDECODE](../functions/STRDECODE.md) | Decode a string |
| [STRDIGEST](../functions/STRDIGEST.md) | Calculate the hash of a string |
| [STRENCODE](../functions/STRENCODE.md) | Encode a string |
| [STRFORM](../functions/STRFORM.md) | Generate a formatted string |
| [STRLEN](../functions/STRLEN.md) | Return the length of a string |
| [STRSTR](../functions/STRSTR.md) | Search a string |
| [SUBSTR](../functions/SUBSTR.md) | Get a substring |

## T-Z

| Function | Description |
|------|------|
| [TAN](../functions/TAN.md) | Returns the tangent |
| [TANH](../functions/TANH.md) | Returns the hyperbolic tangent |
| [THREADCLOSE](../functions/THREADCLOSE.md) | Discards the thread record (Tc608-1 and later) |
| [THREADJOIN](../functions/THREADJOIN.md) | Waits for the thread to finish (Tc608-1 and later) |
| [THREADRESULT](../functions/THREADRESULT.md) | Returns the return value of a function in a finished thread (Tc608-1 and later) |
| [THREADSTART](../functions/THREADSTART.md) | Runs a function in another thread (Tc608-1 and later) |
| [THREADSTATE](../functions/THREADSTATE.md) | Returns the state of a thread (Tc608-1 and later) |
| [THREADSTOP](../functions/THREADSTOP.md) | Requests that a thread stop (Tc608-1 and later) |
| [TOAUTO](../functions/TOAUTO.md) | Automatically converts a value to an appropriate type |
| [TOAUTOEX](../functions/TOAUTOEX.md) | Extended version of TOAUTO |
| [TOBINSTR](../functions/TOBINSTR.md) | Converts an integer to a binary string |
| [TOHEXSTR](../functions/TOHEXSTR.md) | Converts an integer to a hexadecimal string |
| [TOINT](../functions/TOINT.md) | Converts a value to an integer |
| [TOLOWER](../functions/TOLOWER.md) | Converts a string to lowercase |
| [TOREAL](../functions/TOREAL.md) | Converts a value to a real number |
| [TOSTR](../functions/TOSTR.md) | Converts a value to a string |
| [TOUPPER](../functions/TOUPPER.md) | Converts a string to uppercase |
| [TRANSLATE](../functions/TRANSLATE.md) | Transforms a string |
| [UNDEFFUNC](../functions/UNDEFFUNC.md) | Deletes a function definition |
| [UNDEFGLOBALDEFINE](../functions/UNDEFGLOBALDEFINE.md) | Deletes a global definition |
| [UNLOADLIB](../functions/UNLOADLIB.md) | Unloads an external library |
| [ZEN2HAN](../functions/ZEN2HAN.md) | Converts full-width characters to half-width characters |
