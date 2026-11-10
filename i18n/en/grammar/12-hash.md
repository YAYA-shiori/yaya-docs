# Hashes (Tc600-3 and later)

Starting with Tc600-3, **hashes** (associative arrays) were added as a value type.

Arrays and hashes can be stored as hash values or keys (nesting). See [Nested Values and Multidimensional Assignment](13-nesting.md) for reading and writing nested values and for multidimensional assignment.

For changes affecting compatibility with the 500 series, see [Changes in 600](../other/changes-600.md).

## Creation

Create a hash with [IHASH](../functions/IHASH.md). List keys and values in alternating order. `IHASH()` creates an empty hash.

```
_h = IHASH("name", "さくら", "age", 16)
_e = IHASH()
```

To create a hash from a string, use [HASH_SPLIT](../functions/HASH_SPLIT.md).

```
_h = HASH_SPLIT("a=1,b=2", ",", "=")
```

Hash variables must first be created as hashes using IHASH or a similar function. If you write `_x["a"] = 1` for an undefined variable, it is treated as a generic array, not a hash (`"a"` is interpreted as index 0 because it is treated as a number).

## Referencing and Assigning Elements

Read a value with `h[key]`; add or overwrite a value with `h[key] = value`.

```
_h = IHASH()
_h["name"] = "さくら"
_h["name"]       // "さくら"
_h["none"]       // VOID （キーが無いときは未定義の変数と同じ）
_h["age"] += 1   // 複合代入も使える
```

- If a key does not exist, it returns **VOID**, just like an undefined variable (Tc603-1 and later; it returned an empty string through Tc602-13). It is treated as an empty string when used as a string and as 0 when used as a number, so `_h["none"] == ""` is 1 and `_h["none"] + 1` evaluates to the integer 1 ([Out-of-Range Elements](05-arrays.md#範囲外の要素))
- If the key on the left side of a compound assignment (`+=` `-=` `*=` `/=` `%=`) does not exist, it is also evaluated as VOID (Tc602-10 and later). You can count occurrences with `_count[_name] += 1`. If the key exists and its value is an empty string, it is evaluated as an empty string as before (`"" + 1` is `"1"`)
- To distinguish between a missing key and a value that is an empty string or VOID, use [HASH_EXIST](../functions/HASH_EXIST.md)
- Values can also be arrays or hashes ([Nesting](13-nesting.md))
- Any second or later subscript (range specification or delimiter) is ignored. A read with a range, `h[a, b]`, returns an empty string

## Key Matching

Scalar keys are compared as either “numbers” or “strings.”

- Treated as numbers: integers, real numbers, and **strings representing integers in canonical form** (such as `"9"` and `"-3"`)
  - `"09"`, `"-0"`, `"+1"`, `" 1"`, and digit strings that do not fit in 64 bits are treated as strings
- Numbers are compared by value. Integers and real numbers are also compared without loss of precision
- Strings are compared as strings. VOID and the empty string are treated as the same key

Therefore, `h[1]`, `h["1"]`, and `h[1.0]` are all the **same key**. On the other hand, `h[1.5]` and `h["1.5"]`, and `h[0]` and `h["-0"]`, are different keys.

If you pass multiple values that are considered the same key to IHASH, the first key and value are retained.

```
IHASH(9, "i9", "9", "s9")   // 9=i9 だけ
```

## Ordering

Hash elements are ordered by **key**, not by insertion order. [HASH_KEYS](../functions/HASH_KEYS.md), [HASH_VALUES](../functions/HASH_VALUES.md), stringification, foreach, and save files all use this order.

- Numbers come before strings. Numbers are ordered by value, and strings by string order
- When keys are arrays or hashes, the order is scalar < array < hash; arrays and hashes are compared element by element, starting with the first

```
_h = IHASH(10,1, 9,1, 100,1, -1,1, "b",1, "B",1, 2.5,1)
HASH_KEYS(_h)   // -1,2.5,9,10,100,B,b
```

## Behavior as a Value

| Operation | Result |
|---|---|
| Truth value | True if there is at least one element; false if empty |
| `GETTYPE` / `GETTYPEEX` | 5 |
| Stringification (`TOSTR` or concatenation with a string) | Joins `key=value` pairs with `,`. Example: `a=1,b=x` |
| Numeric conversion | 0 |
| `h1 == h2` | True if the element counts, keys, and values all match. Nested values are compared recursively |
| `==` between a hash and a non-hash | Always false (even if the stringified results are the same) |
| `+` (when the other operand is a scalar or hash) | Converts both to strings and concatenates them |
| `+` (when the other operand is an array) | Concatenates each array element with the hash as a string |
| `-` `*` `/` `%` | Emits warning W0024 (see below) |

```
_h = IHASH("a", 1)
_h + 1        // "a=11"
'z' + _h      // "za=1"
_h + _h       // "a=1a=1"
(1,2) + _h    // ("1a=1","2a=1")
```

When either operand of `-` `*` `/` `%` (including compound assignment) is a hash, warning W0024 is emitted. The result is the right operand as-is if the other operand is a scalar (`h - 1` returns `1`, and `1 * h` returns `h`); if the other operand is an array, the operation is performed on each element. Do not use these operations, as they do not produce meaningful results. Note that W0024 is not emitted when an array element is a hash, as in `(h, 1) - 1`.

## Function Arguments and the `,` Operator

Generic arrays are expanded when used as arguments or with the `,` operator, but hashes are not expanded and remain a single element.

```
_a = (0, _h, 2)   // 要素数 3。_a[1] はハッシュ
func(_h)          // func の中で _argv[0] がハッシュになる
```

## foreach

Hashes can also be iterated over with foreach. In the one-variable form, values are assigned in key order.

```
_h = IHASH("a", 1, "b", 2)
foreach _h ; _v
{
  // _v = 1, 2
}
```

When you specify two variables, the first receives the key and the second receives the value. This form also works with arrays and simple arrays; the first variable receives an index starting from 0.

```
foreach _h ; _k, _v { _s += _k + '=' + _v + ' ' }   // "a=1 b=2 "
foreach ("p", "q") ; _i, _v { ... }                  // _i = 0, 1
foreach "x,y" ; _i, _v { ... }                       // 簡易配列も同じ
```

See [Flow Control](07-flow-control.md#foreach-ループ) for details.

## See Also

- [IHASH](../functions/IHASH.md)
- [HASH_KEYS](../functions/HASH_KEYS.md)
- [HASH_VALUES](../functions/HASH_VALUES.md)
- [HASH_SPLIT](../functions/HASH_SPLIT.md)
- [HASH_EXIST](../functions/HASH_EXIST.md)
- [HASH_SIZE](../functions/HASH_SIZE.md)
- [Nested Values and Multidimensional Assignment](13-nesting.md)
- [Arrays](05-arrays.md)
- [Changes in 600](../other/changes-600.md)
