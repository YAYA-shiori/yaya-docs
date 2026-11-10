# Nested Values and Multidimensional Assignment (Tc600-3 and Later)

From Tc600-3 onward, arrays and hashes can be stored as array elements, hash values, and hash keys (**nesting**). To read or write values inside nested structures, write consecutive `[ ]` pairs. Directly assigning to an element of an element is called **multidimensional assignment**.

In the 500 series, array elements could only be scalar values, and `a[x][y] = v` caused error E0029 when loaded. For changes from the 500 series, see [Changes in 600](../other/changes-600.md).

See [Hashes](12-hash.md) for hashes themselves.

## Creating Nested Structures

### Storing a Hash as a Value

Assigning to a hash element stores an array or hash as-is.

```
_h = IHASH()
_h["list"] = (1, 2, 3)        // 値に配列
_h["sub"] = IHASH("x", 1)     // 値にハッシュ
```

When you write an array as an argument to [IHASH](../functions/IHASH.md), it is expanded, just as it is with other functions. `IHASH("list", (1, 2, 3))` is the same as `IHASH("list", 1, 2, 3)`, so the value is not stored as an array. To store an array as a value, assign it afterward as shown above. Hashes are not expanded, so you can write `IHASH("sub", IHASH("x", 1))`.

### Storing a Hash in an Array Element

A hash is not expanded by the `,` operator or when assigned to an element; it becomes a single element.

```
_h = IHASH("x", 1)
_a = (0, _h, 2)     // 要素数 3。_a[1] はハッシュ
_a[2] = _h          // 同上
_a ,= _h            // 末尾に追加
```

### Storing an Array in an Array Element

There is no syntax for storing a new array inside an array. The `,` operator, `,=`, and assignment to an element (`_a[1] = (8, 9)`) all **expand and insert** the array on the right-hand side (as in the 500 series).

```
_a = (1, 2)
_a[1] = (8, 9)      // 1,8,9 （要素数 3）
_a[1] = IARRAY()    // 1,9 （空の配列を差し込むと要素が消える）
```

However, if the target element already contains an array or hash, it is replaced as a whole without being expanded (Tc603-1 and later. [Replacing an inner array or hash as a whole](#内側の配列やハッシュを丸ごと書き換える)).

The following functions return values containing arrays inside arrays.

- [HASH_VALUES](../functions/HASH_VALUES.md): When passed a hash whose values are arrays, returns an array containing each array as a single element
- [PARSEJSON](../functions/PARSEJSON.md) / [PARSEYAML](../functions/PARSEYAML.md) / [PARSETOML](../functions/PARSETOML.md) / [PARSEXML](../functions/PARSEXML.md), and functions such as [FREADJSON](../functions/FREADJSON.md) that read from files
- [RESTOREVAR](../functions/RESTOREVAR.md): Restores variables saved with their nested structure intact

```
_v = PARSEJSON('[[1,2,3],[4]]')   // 要素数 2。_v[0] は配列 (1,2,3)
```

You can also modify arrays inside arrays obtained this way using multidimensional assignment (Tc602-7 and later. [How intermediate values behave](#途中の値ごとの動作)).

### Building Nested Structures Step by Step

Inner hashes are not created automatically. Create intermediate hashes with [IHASH](../functions/IHASH.md), then assign values inside them.

```
_m = IHASH()
_m["a"] = IHASH()
_m["a"]["b"] = 1
_m["a"]["list"] = IARRAY()
_m["a"]["list"] ,= "p"
_m["a"]["list"] ,= "q"
DUMPJSON(_m)   // {"a":{"b":1,"list":["p","q"]}}
```

If you write `_m["c"]["d"] = 1` without creating the intermediate hash, `_m["c"]` becomes an array `(1)`, not a hash ([How intermediate values behave](#途中の値ごとの動作)).

## Reading Values

When you write consecutive `[ ]` pairs, the second `[ ]` is applied to the result of the first `[ ]`, the third to that result, and so on.

```
_h = IHASH()
_h["list"] = (1, 2, 3)
_h["sub"] = IHASH("x", 1)
_a = (0, _h, 2)

_h["sub"]["x"]      // 1
_h["list"][1]       // 2
_a[1]["sub"]["x"]   // 1
_a[1]["list"]       // (1,2,3) そのものが返る
```

Each `[ ]` behaves as follows, depending on the type of the current value. At any step, if the specified element does not exist, the result is VOID, just as for an undefined variable, and all subsequent `[ ]` pairs also result in VOID (no error occurs. [Out-of-range elements](05-arrays.md#範囲外の要素)).

| Value | Result of `[x]` |
|---|---|
| Array | The x-th element. If the element is an array or hash, it is returned as-is |
| Hash | The value for key x ([Matching keys](12-hash.md#キーの一致)) |
| String | The x-th element as a simple array |
| Number | The value itself if x is 0; otherwise VOID |
| VOID (such as an undefined variable) | VOID |

Up to Tc602-13, an out-of-range array index, a missing hash key, or `[ ]` applied to VOID returned an empty string (out-of-range indexes for strings and numbers have returned VOID from the beginning).

Range selection is also available. The result of an array range selection `[a, b]` is an array containing any nested elements as-is. If the range is out of bounds, the result is an empty array. A hash range selection returns an empty string.

```
_v = PARSEJSON('[[1,2],[3,4],[5,6]]')
_v[0, 1]     // 要素数 2 の配列。どちらの要素も配列のまま
```

### Simple Array Delimiters

A delimiter set for a variable with [SETDELIM](../functions/SETDELIM.md) applies only to the first-level `[ ]` attached directly to that variable. When reading a string inside a nested structure as a simple array, specify the delimiter in the second-level or later `[ ]`.

```
_s = "a|b"
SETDELIM(_s, "|")
_t = (_s, "c")
_t[0][1]         // VOID （2段目は "," で区切られるので範囲外）
_t[0][1, "|"]    // "b"
```

### Embedding in Strings

You can also write consecutive `[ ]` pairs inside strings.

```
"値は %_h['sub']['x'] です"      // 値は 1 です
"値は %(_h['list'][1]) です"     // 値は 2 です
```

Embedding a nested array or hash itself produces the result of [string conversion](#文字列化と保存).

## Function Arguments and the `,` Operator

Only the **outermost array** is expanded when passed as function arguments or by the `,` operator. Arrays and hashes inside its elements are not expanded and remain as single elements. Hashes are not expanded even when they are outermost.

```
_v = PARSEJSON('[[1,2,3],[4]]')

func(_v)        // _argc は 2。_argv[0] は配列 (1,2,3)
func(_v[0])     // _argc は 3。_argv は 1,2,3
func(_v, 9)     // _argc は 3。_argv[0] は配列 (1,2,3)
_c = (_v, 9)    // 要素数 3。_c[0] は配列 (1,2,3)

ARRAYSIZE(_v)      // 2
ARRAYSIZE(_v[0])   // 3
```

When you pass a nested array to a function, the outermost array itself becomes `_argv`. The receiving side has no way to distinguish between “one array argument” and “multiple arguments,” so when passing a nested array to a function, it is best to wrap it in a hash or pass its elements one at a time.

When you pass an array with only one element to [GETTYPE](../functions/GETTYPE.md), it returns the type of that element, not the array (the same as in the 500 series). In the example above, `GETTYPE(_v[1])` returns 1, not 4.

## foreach

You can also iterate over nested arrays and hashes with foreach. The loop variable receives each element as-is, so if an element is an array or hash, you can iterate over it with another foreach or access it with `[ ]`.

```
_h = PARSEJSON('{"a":{"x":1,"y":2},"b":{"x":3}}')
foreach _h ; _k, _sub {
  foreach _sub ; _k2, _v {
    // _k/_k2 = _v の順に a/x=1, a/y=2, b/x=3
  }
}

foreach _h["a"] ; _k, _v { ... }   // 内側だけを回す
```

For two-variable foreach, see [Hashes](12-hash.md#foreach) and [Flow Control](07-flow-control.md#foreach-ループ).

## Copying Values

Assignment and passing arguments copy values. The source and destination do not affect each other, including for nested values.

```
_h = IHASH("a", 1)
_h["self"] = _h
_h["self"]["a"] = 2
_h["a"]             // 1 のまま
```

Even if you extract and modify an inner value, the original value does not change. To change the original value, assign the modified value back or use multidimensional assignment.

```
_sub = _h["self"]
_sub["a"] = 3        // _h["self"]["a"] は 2 のまま
_h["self"] = _sub    // これで _h["self"]["a"] が 3 になる
```

## Comparison

The `==` operator compares the contents of arrays with arrays and hashes with hashes. The same rule is applied recursively to nested values.

- Arrays: true if they have the same number of elements and each corresponding element is equal
- Hashes: true if the number of elements, keys, and values all match ([Behavior as a Value](12-hash.md#値としての振る舞い))

```
PARSEJSON('{"a":[1,2]}') == PARSEJSON('{"a":[1,2]}')   // 1
```

The same rule applies when [ASEARCH](../functions/ASEARCH.md) searches an array of hash elements. However, if you pass an array as the value to search for, it is expanded as an argument, so you cannot search for the array itself.

[ASORT](../functions/ASORT.md) converts array or hash elements to strings (and treats them as 0 for `int` / `double`) before sorting them ([When Elements Are Arrays or Hashes](../functions/ASORT.md#要素が配列やハッシュのときtc600-3以降)).

## Multidimensional Assignment

You can assign directly to an element inside another element. You can use any assignment operator, including `=`, `+=`, and `,=`.

```
_h["sub"]["x"] = 5
_h["list"][0] += 10
_h["list"] ,= 4               // 内側の配列の末尾に追加
_a[1]["sub"]["y"] = "new"
```

As with one-dimensional assignment, the right-hand value is inserted at the position of the last `[ ]`. Therefore, if the element at that position is a scalar, a right-hand array is expanded and inserted. To replace an inner array as a whole, assign to the level one step above it.

```
_h["list"] = (1, 2, 3)
_h["list"][0] = (7, 8)    // _h["list"] は 7,8,2,3
_h["list"] = (7, 8)       // _h["list"] を (7,8) に置き換える
```

Range assignment (`_h["list"][0, 1] = "R"`) works the same way as in one-dimensional assignment.

### Replacing an Inner Array or Hash as a Whole

For an assignment that does not specify a range, if the target element is currently an **array or hash**, the right-hand value replaces the entire element without being expanded (Tc603-1 and later). You can replace, append to, or perform element-wise calculations on an array inside another array using the same syntax as for assignment to the level one step above.

```
_v = PARSEJSON('[[1,2],[3,4]]')
_v[0] = (7, 8, 9)     // _v は (7,8,9),(3,4)   丸ごと置き換える
_v[0] ,= 5            // _v は (7,8,9,5),(3,4) 内側の末尾に追加する
_v[0] += 1            // _v は (8,9,10,6),(3,4) 内側の要素ごとに計算する
_v[0] = _v[0]         // 変わらない
_v[0] = IARRAY        // _v は (),(3,4)        空の配列に置き換える（要素は消えない）
_v[0, 0] = IARRAY     // _v は (3,4)           範囲指定なら展開して差し込む（要素を消す）
```

- If the target element is a scalar or out of range (does not exist yet), the right-hand array is expanded and inserted as before (inserting with `_a[1] = (8, 9)`, deleting with `_a[1] = IARRAY`)
- Range assignments expand and insert the value regardless of the element type, just like assignment to a Python slice. To delete an inner array as a whole, write `_v[0, 0] = IARRAY`
- If the root is a hash (`_h["list"] = ...`), the element is replaced as before
- The 500 series has no nested arrays, so the behavior of 500-series dictionaries does not change

Up to Tc602-13, when the root was an array, inner arrays were expanded and nesting was lost (`_v[0] = _v[0]` made `_v` into three elements, `1`, `2`, and `(3,4)`, while `_v[0] ,= 5` made it into four elements, `1`, `2`, `5`, and `(3,4)`).

### Behavior of Intermediate Values

Multidimensional assignment modifies the value at each level, starting from the last level and moving toward the root variable, then assigns it back to the level immediately above. The behavior at each level depends on the type of its value, as follows.

| Intermediate value | Behavior |
|---|---|
| Hash | Adds or overwrites the value for the key |
| Array | Replaces the element. If out of range, fills the gap with VOID and appends it to the end |
| String | Modifies it as a simple array |
| Number | Converts it to an array before modifying it. Element 0 becomes VOID, and the original number is lost |
| Missing (out of range or key does not exist) | Creates a generic array and modifies it, just as for an undefined variable |

```
_a = ("p,q", 1)
_a[0][1] = "Q"        // _a[0] は "p,Q"

_h = IHASH("l", (1, 2))
_h["l"][4] = 9        // _h["l"] は 1,2,VOID,VOID,9

_n = (1, 2.5)
_n[1][2] = 9          // _n[1] は配列 (VOID,VOID,9)

_e = IHASH()
_e["n"]["x"] = 5      // _e["n"] は配列 (5) （ハッシュは作られない）
_e["m"][2] = 5        // _e["m"] は配列 (VOID,VOID,5)
```

`_e["n"]` becomes `(5)` in `_e["n"]["x"] = 5` because the key `"x"` is treated as an array ordinal, which becomes element 0. This produces the same result as `_x["x"] = 5` for an undefined variable.

Up to Tc602-13, missing levels were modified as simple arrays of empty strings, so `_e["n"]` became the string `"5"` and `_e["m"]` became the string `",,5"`.

When the modified value is assigned back to the level immediately above, it is not expanded, even if it is an array; it replaces the value as a single element. Since the right-hand array is expanded only at the last level, nested arrays can also be modified while remaining nested.

```
_v = PARSEJSON('[[1,2],[3,4]]')
_v[0][0] = "A"        // _v は ("A",2),(3,4)
_v[1][0] = (7, 8)     // _v は ("A",2),(7,8,4)
```

However, when an intermediate level specifies a range (`_v[0, 1][0] = 9`), the array from the selected range is modified, then expanded and assigned back into the original range.

Up to Tc602-6, when you used multidimensional assignment on an array inside another array, the modified inner array was expanded into the outer array, breaking the nesting (the `_v[0][0] = "A"` example above produced three elements in `_v`: `"A"`, `2`, and `(3,4)`). The same expansion into the outer array also occurred when an intermediate value was a number. Write-back with reference passing (`&_v[0][0]`) behaved the same way.

### Assignment Root

The root of an assignment must be a variable. `(式)[0] = 1` and `func()[0] = 1` result in error E0029.

### Passing by Reference

You can also pass an element of an element using the [feedback operator](04-arithmetic.md#フィードバック演算子) (passing by reference) (Tc600-4 and later). If you modify `_argv[0]` inside `func(&_h["sub"]["x"])`, `_h["sub"]["x"]` changes. In Tc600-3, the preceding dimension was ignored, and the value was written to `_h["x"]`.

## String Conversion and Saving

When a nested value is converted to a string ([TOSTR](../functions/TOSTR.md), concatenation with a string, embedding, and so on), the inner values are also joined with `,` or `=`, making it unclear where the inner values begin and end.

```
_h = IHASH()
_h["l"] = (1, 2)
_h["m"] = IHASH("x", 1)
TOSTR(_h)    // "l=1,2,m=x=1"
```

Use the following methods when you want to work with nested values while preserving their structure.

| Purpose | Method |
|---|---|
| Save variables to a file and restore them | [SAVEVAR](../functions/SAVEVAR.md) / [RESTOREVAR](../functions/RESTOREVAR.md). Nested values are saved in the form `IARRAY{...}` / `IHASH{...}` ([Save format](../functions/SAVEVAR.md#保存形式)) |
| Inspect the contents | [DUMPVAR](../functions/DUMPVAR.md) (Tc600-4 and later). Nested values are displayed as `(array)[ ... ]` / `(hash){ ... }`. [LOGGING](../functions/LOGGING.md) (Tc602-8 and later) also writes nested arrays enclosed in `( )` and hashes enclosed in `{ }` |
| Pass values as strings | [DUMPJSON](../functions/DUMPJSON.md) and [PARSEJSON](../functions/PARSEJSON.md). However, distinctions that cannot be represented in JSON (such as integer keys versus string keys, or VOID versus an empty string) are lost. To preserve these distinctions, use [SERIALIZEVAR](../functions/SERIALIZEVAR.md) and [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) (Tc607-3 and later). The result is a string in the same format as a save file |

## Limitations

- For a hash whose key is an array, the first element of the key's ordinal representation is used as the key in `h[キー]`, so you cannot look up a value using an array as the key (you can retrieve it using foreach or [HASH_KEYS](../functions/HASH_KEYS.md)). If the key is a hash, you can look it up with `h[キー]`

## Related

- [Hash](12-hash.md)
- [Array](05-arrays.md)
- [HASH_VALUES](../functions/HASH_VALUES.md)
- [PARSEJSON](../functions/PARSEJSON.md)
- [DUMPJSON](../functions/DUMPJSON.md)
- [SAVEVAR](../functions/SAVEVAR.md)
- [DUMPVAR](../functions/DUMPVAR.md)
- [Changes in 600](../other/changes-600.md)
