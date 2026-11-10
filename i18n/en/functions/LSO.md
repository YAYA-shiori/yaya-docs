# LSO
**Category:** メタ操作・特殊関数

## Signature
```
LSO
LSO()
```

## Parameters
None

## Returns
A number indicating the position selected by the most recent selection operation.

## Description

Short for "last Selection Order." Returns the result of the most recent selection as a number indicating its position.

```
request
{
    _i = foo
    LSO
}

foo
{
    "earth"
    "moon"
    "sun"
}
```

If `"sun"` is assigned to `_i`, `LSO` returns 2 (zero-based). It works for any kind of choice that selects one option from several. Therefore, the value is only meaningful if retrieved immediately after the relevant operation completes.

### Note the position being retrieved

The following code is incorrect if you are trying to get the result of the selection made by `ANY`. The `LSO` at this position retrieves the result of the selection made by `{ }`. Therefore, `res` is always 0.

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
    }
    res = LSO
}
```

The following change makes the code work as intended.

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
        res = LSO
    }
}
```

### When an output-finalization operator is present

When an output-finalization operator (`--`) is present, `LSO` works for all possible combinations.

```
request
{
    {
        "1"
        "2"
        "3"
        --
        "A"
        "B"
    }
    _i = LSO
}
```

For example, the `{ }` block in the function above outputs one of `"1A"` `"2A"` `"3A"` `"1B"` `"2B"` `"3B"`. The range of `LSO` values matches this, from 0 to 5. Each value corresponds to the order shown above.

## Compatibility
- YAYA: Available since the initial version
- AYA: Available from version 5.8 onward

## See Also
- ANY
