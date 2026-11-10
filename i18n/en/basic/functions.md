# Functions

Function names can also use full-width characters.

## Basic function definitions

```
Test{
  "Hello World!"
}
```

This `Test` function outputs the string `"Hello World!"`. One characteristic of YAYA is that a bare variable or string (in this example, `"Hello World!"`) that is not an assignment expression is treated as the return value.

In other words,

```
Test{
  _A = 10
  _B = 11+32
  "Hello World!"
}
```

the return value is still `"Hello World!"`.

The braces can also be written as follows.

```
Test
{
  "Hello World!"
  "Hallo Welt!"
}
```

## Multiple return value candidates

If there are multiple return value candidates, one of them is selected at random.

```
Test{
  A = 10
  "Hello World!"
  "Hallo Welt!"
  10
  11+32
}
```

In this example, one of `"Hello World!"`, `"Hallo Welt!"`, `10`, or `43` is returned.

## Arguments

You can pass arguments to a function. The received arguments are stored in the local variable array `_argv`, and the number of arguments (the size of `_argv`) is stored in `_argc`.

```
てすと{
  "入力は「" + _argv[0] + "」だよ"
}
```

Define a function like this, and

```
てすと("うかがか")
```

execute it as shown above to output `"入力は「うかがか」だよ"`.

## The function's own name

The local variable `_FUNC_NAME_` contains the name of the function currently being executed. It was added for convenience as dynamic definition commands such as [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) were expanded.

## Defining variables

You can declare variables freely inside a function. Variables, whether local or global, can only be defined inside a function. Variable names that begin with `_` are treated as local variables; those that do not are treated as global variables.

| Type | Name | Scope |
|------|------|---------|
| Local variable | Begins with `_` | Only within the curly braces where it is defined |
| Global variable | Does not begin with `_` | Can be used anywhere once defined during function execution. Retained even after the ghost exits |

To erase a global variable, you must use the [ERASEVAR](../functions/ERASEVAR.md) function.

```
テスト2{
  _aa = 200  // これはローカル
  bb = 200   // これはグローバル
}
```

To reduce the likelihood of bugs, use local variables whenever possible for variables that are only used within a function. For example, use a local variable (`_i`) as the counter in a loop, as follows.

```
テスト2{
  for _i = 0; _i < 10; _i++
  {
    _i + "\n"
  }
}
```

## Function call limit

You can set the function call depth (not the number of calls) in [`fncdepth` in the basic settings file](../grammar/01-basic-settings.md). The default is 32 levels.

When the limit is reached, [shiori.OnCallLimit](../system/shiori-OnCallLimit.md)(function name, line) is called. If memory runs out during execution, [shiori.OnMemoryLimit](../system/shiori-OnMemoryLimit.md)() is called, but stack overflows cannot be detected.

## Related

- [Grammar/2. Functions](../grammar/02-functions.md)
