# Handling Special Characters

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

A solution for cases where you want to use characters assigned special Unicode code points, but your editor only supports Shift JIS, or when you run into other difficulties.

### When You Do Not Need to Process Them Internally

If you only want to display the character,

```
\_u[0x2122]
```

will display it in the balloon.
Inside the brackets, enter 0x followed by the hexadecimal code (or just enter the decimal code).

### When You Need to Process Them Internally

In this case, the quickest solution is to simply change the dictionary's character encoding to UTF-8, but you may not be able to do that because of limitations in an editor you are used to, for example. In that case…

```
CHR(0x2122)
```

All you need to do is call the CHR system function, so, for example, if you want to embed it in a string,

```
"Enbug Masters%(CHR(0x2122))"
'Enbug Masters' + CHR(0x2122)
```

you can write it like this.

However, as is, you can process the character internally, but it will not be output correctly to the balloon. In this case, in the [basic settings file](../grammar/01-basic-settings.md),

```
charset.output, UTF-8
```

you need to write this (if it is already there, change the value on the right to UTF-8).
