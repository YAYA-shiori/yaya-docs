# Changes in 600 (Tc600-3 and later)

This summarizes the specification changes from the 500 series (up to Tc574-1) in YAYA (600 series) from Tc600-3 onward.

!!! note "TL;DR"
    **Just replacing `yaya.dll` is enough to keep 500-series dictionaries and save files working as they are.** No rewriting is needed. The development team also replaces it without giving it much thought in most cases.

    You only need to pay attention in the following cases.

    - Your dictionary has a function or variable with the same name as a new system function, such as `IHASH` or `HASH_KEYS` → the function is renamed to `Conflict.name`, and the variable cannot be used ([details](#新しいシステム関数と同じ名前))
    - Your code relies on comparing VOID values in array elements or on `ARRAYDEDUP` with arrays containing mixed types → the result changes ([details](#既存の辞書に影響しうる変更))
    - You revert to the 500 series after running with the 600 series → variables containing hashes or nesting become corrupted ([details](#セーブファイルの互換性))

    You can use the new features (hashes, nested arrays, JSON / XML / SQLite, and so on) whenever you want. Dictionaries shared with the 500 series can use `#ifdef` to distinguish the code for each version ([details](#500-系と共用する辞書)).

## Overview

| Item | 500 series | 600 series |
|---|---|---|
| Value types | VOID / integer / real number / string / generic array | ＋ **hash** (associative array) |
| `GETTYPE` / `GETTYPEEX` | 0–4 | Hash is **5** |
| Array elements | Scalars only | Arrays and hashes can also be elements (**nesting**) |
| Assignment to elements | Only `a[x] = v` | `a[x][y]... = v` (**multidimensional assignment**) is also supported |
| foreach | `foreach expression ; variable` | ＋ `foreach expression ; key variable, value variable` |
| Save files | Array `a:b:c` | ＋ Hash `"k"=v:...`, nesting `IARRAY{...}` / `IHASH{...}` |
| New system functions | — | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_VALUES](../functions/HASH_VALUES.md) [HASH_SPLIT](../functions/HASH_SPLIT.md) [HASH_EXIST](../functions/HASH_EXIST.md) [HASH_SIZE](../functions/HASH_SIZE.md), [FREADJSON](../functions/FREADJSON.md) [FREADXML](../functions/FREADXML.md) [PARSEJSON](../functions/PARSEJSON.md) [PARSEXML](../functions/PARSEXML.md) from Tc601-1, [FWRITEJSON](../functions/FWRITEJSON.md) [FWRITEXML](../functions/FWRITEXML.md) [DUMPJSON](../functions/DUMPJSON.md) [DUMPXML](../functions/DUMPXML.md) from Tc602-1, [PARSEHEADER](../functions/PARSEHEADER.md) from Tc602-3, [FREADYAML](../functions/FREADYAML.md) [FREADTOML](../functions/FREADTOML.md) [PARSEYAML](../functions/PARSEYAML.md) [PARSETOML](../functions/PARSETOML.md) [FWRITEYAML](../functions/FWRITEYAML.md) [FWRITETOML](../functions/FWRITETOML.md) [DUMPYAML](../functions/DUMPYAML.md) [DUMPTOML](../functions/DUMPTOML.md) from Tc602-5, [SQLOPEN](../functions/SQLOPEN.md) [SQLCLOSE](../functions/SQLCLOSE.md) [SQLEXEC](../functions/SQLEXEC.md) [SQLQUERY](../functions/SQLQUERY.md) from Tc602-11, [FREADHTML](../functions/FREADHTML.md) [PARSEHTML](../functions/PARSEHTML.md) from Tc605-1 |
| New warnings | — | W0024 (a hash used with `-` `*` `/` `%`), W0025 (file cannot be opened) and W0026 (JSON/XML/YAML/TOML cannot be parsed) from Tc601-1, W0027 (cannot convert to JSON/XML/YAML/TOML) from Tc602-1, W0029 (SQLite operation failed) from Tc602-11, W0030 (more values passed than there are SQL parameters) from Tc602-13, W0031 (could not resolve the name after `%` with `embed.lazy, off`) from Tc604-1 |
| Regular expressions | DEELX | uka_regexp (syntax close to PCRE2) from Tc606-6. Subroutine calls in patterns can be resolved using variables and functions ([regular expressions](../grammar/14-regular-expressions.md)) |

For syntax, see [hashes](../grammar/12-hash.md) and [nested values and multidimensional assignment](../grammar/13-nesting.md).

In the 500 series, `a[x][y] = v` caused a load-time error E0029, so no existing dictionaries contain this syntax.

## Changes that may affect existing dictionaries

### Comparing VOID values in array elements

When comparing array elements, **two VOID values** are now considered equal. This aligns the behavior with comparisons between scalar VOID values.

- `(1, undefined variable) == (1, undefined variable)` now evaluates to 1 instead of 0
- `ASEARCH(undefined variable, array)` now returns the position of a VOID element in the array (it returned -1 in the 500 series)
- The same applies to `HASH_EXIST`, `ARRAYDEDUP`, and `==` between hashes

This change applies only when both the key and the element are VOID; comparisons between integers, real numbers, and strings are unchanged.

### Passing an array with mixed types to ARRAYDEDUP

In the 500 series, passing an array containing a mix of integers, real numbers, and strings produced different results depending on the order of the elements. In the 600 series, duplicates are removed using the same rules as hash keys, and values are sorted in the order number < string.

```
ARRAYDEDUP((10, "9", 9, "a", 1.0, 1, "1"))
// 500 系: 1,1.000000,9,10,9,a
// 600 系: 1.000000,9,10,a
```

`1.0`, `1`, and `"1"` are considered the same value, and the first one (`1.0`) remains. The results for arrays containing only integers, only real numbers, or only strings are the same as in the 500 series.

### Arrays passed to setters and watchers

When the value passed to [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md) (setter) or [FUNCDECL_READ](../functions/FUNCDECL_READ.md) (watcher) is a generic array, the value was corrupted in the 500 series (`_argv[1]` and `_argv[2]` for a setter became empty, `_argv[1]` for a watcher contained only the first element, and a variable became empty if the setter returned its value as-is).

In the 600 series, an array is passed as a nested element of `_argv`. The number of elements in `_argv` remains 3 for setters and 2 for watchers.

Attaching a setter or watcher to an array variable did not work correctly in the 500 series, so this should not cause any actual problems. Note that, as in the 500 series, a setter is not called when assigning to an index (`a[0] = v`).

### Names matching new system functions

- A user-defined function with the same name as `IHASH`, `HASH_KEYS`, and so on is renamed to `Conflict.name`, and calls are directed to the system function (the same mechanism used when TOAUTOEX was added)
- A global variable with the same name cannot be used. Warning W0002 is issued when restoring it from a save file

### Compound assignment to a missing element (Tc602-10 and later)

When the left-hand side of a compound assignment (`+=` `-=` `*=` `/=` `%=` and their colon-suffixed variants) is an out-of-range element of a generic array or a missing hash key, it is now evaluated as VOID, just like an undefined variable. In the 500 series and up to Tc602-9, it was evaluated as an empty string, so `+= number` concatenated strings.

```
_c = IHASH()
_c["a"] += 1
_c["a"] += 1     // 500 系・Tc602-9 まで: "11"（文字列）　Tc602-10 以降: 2（整数）

_a = IARRAY
_a[2] += 1       // 500 系・Tc602-9 まで: "1"（文字列）　Tc602-10 以降: 1（整数）
```

- Only `+=` with a numeric right-hand side changes. `-=` `*=` `/=` `%=` already treated empty strings as numbers, so the result is unchanged. `+= "string"` is also unchanged
- When an element exists and its value is an empty string (after `_a[0] = ""`, `_a[0] += 1`), the result remains `"1"` as before
- Out-of-range elements of simple arrays (strings) were already evaluated as VOID
- In Tc602-10, reads (`h["none"]` or out-of-range `a[9]`) still returned an empty string. Starting with Tc603-1, reads also return VOID (see below)
- In multidimensional assignment, only the final level is affected. When an intermediate level is missing (for example, `_h["a"]["b"] += 1` on an empty `_h`), rewrite the code as described in [Behavior for each intermediate value](../grammar/13-nesting.md#途中の値ごとの動作). `_h["a"]` is the string `"1"` through Tc602-13, and becomes the array `(1)` starting with Tc603-1
- `,=` is unchanged

### Reading a missing element (Tc603-1 and later)

Reading an out-of-range element of a generic array, a missing hash key, or a VOID value with `[ ]` now returns VOID, just like an undefined variable. Previously, it returned an empty string (out-of-range elements of simple arrays and numbers already returned VOID). The 500 series behaves the same way starting with Tc574-8 (except for hashes). For details, see [Out-of-range elements](../grammar/05-arrays.md#範囲外の要素).

```
_h = IHASH()
_h["none"] == 0      // Tc602-13 まで: 0　Tc603-1 以降: 1
_h["none"] + 1       // Tc602-13 まで: "1"（文字列）　Tc603-1 以降: 1（整数）
GETTYPE(_h["none"])  // Tc602-13 まで: 3　Tc603-1 以降: 0
```

The results of `== ""`, if conditions, and concatenation with strings are unchanged.

### Assigning to arrays or hashes inside an array (Tc603-1 and later)

With an assignment that does not specify a range (such as `_v[0] = x`, `_v[0] ,= x`, or `_v[0] += x`), if the destination element is an array or hash, the right-hand side is now replaced as a whole without being expanded. Previously, if the root was an array, the right-hand array was expanded and nesting was lost (this also happened with `_v[0] = _v[0]`). Insertion and deletion when the destination element is a scalar (such as `_a[1] = (8, 9)` or `_a[1] = IARRAY`) are unchanged. For details, see [Replacing an inner array or hash as a whole](../grammar/13-nesting.md#内側の配列やハッシュを丸ごと書き換える).

```
_v = PARSEJSON('[[1,2],[3,4]]')
_v[0] ,= 5     // Tc602-13 まで: 1,2,5,(3,4)　Tc603-1 以降: (1,2,5),(3,4)
```

## Save file compatibility

- Variables that do not contain hashes or nesting are written and read exactly as in the 500 series. 500-series save files can be read as they are
- Variables containing hashes or nesting are saved in the new format (see [SAVEVAR](../functions/SAVEVAR.md))
- **Caution when downgrading**: If a file saved with the 600 series is read by the 500 series, only variables containing hashes or nesting become corrupted (the program does not crash, and other variables are unaffected). If the file is saved again while corrupted, the original contents are lost

## Dictionaries shared with the 500 series

In the 500 series from Tc574-2 onward and the 600 series from Tc602-2 onward, `#ifdef __AYA_SYSTEM_YAYA6__` and `#ifdef __AYA_SYSTEM_SYSFUNC_関数名__` can be used to distinguish the parts intended for the 600 series. Sections that are not loaded are not parsed, so new 600-series syntax and functions can be written without causing errors in the 500 series. For details, see [Preprocessing](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書).

## Performance

In the 500 series, `_a ,= x` and `_a[i] = x` copied the entire array each time (growing an array in a loop became slower in proportion to the square of the number of elements). The 600 series does not make these copies, so operations that grow arrays in a loop are much faster.

## Related

- [Hashes](../grammar/12-hash.md)
- [Nested values and multidimensional assignment](../grammar/13-nesting.md)
- [Flow control (foreach)](../grammar/07-flow-control.md#foreach-ループ)
- [SAVEVAR](../functions/SAVEVAR.md)
- [Preprocessing](../grammar/08-preprocessor.md)
