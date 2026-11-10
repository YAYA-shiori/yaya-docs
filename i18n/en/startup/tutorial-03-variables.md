# Tutorial 3: Using Variables

A “variable” is like a container or box for storing strings or numbers. For a ghost, “user name,” “number of launches,” “time of launch,” and “affection” are all examples of variables. YAYA has several types of variables.

## Strings and Numbers

There are two types of variables: “strings” and “numbers” (more precisely, there are three types: integers, real numbers, and strings).

```
変数 = 1
```

Written this way, the value of the variable is the number `1`.

```
変数 = "1"
```

When you assign a value enclosed in `" "` or `' '` like this, the string `"1"` is stored. Putting a value into a variable like this is called “assignment.”

Full-width characters such as “１,” “２,” and “３” cannot be numbers, so they are treated as strings. **String-type variables cannot be compared or calculated as numbers.** For example, adding the numbers `1` and `2` gives `3`, but adding the strings `"1"` and `"2"` joins them into `"12"`. There are other differences as well, so be careful.

You can convert variables between strings and numbers whenever you like by using YAYA system functions.

- Convert a variable to a string variable: `変数 = TOSTR(変数)`
- Convert a variable to a numeric variable: `変数 = TOINT(変数)`

There is also [TOAUTO](../functions/TOAUTO.md), which automatically determines whether a value is an integer, real number, or string and converts it accordingly (system functions are explained in more detail later).

### Global and Local

If a variable name begins with `_`, it is a local variable.

```
_変数名
```

Otherwise, it is a global variable.

```
変数名
```

Roughly speaking, local variables are “temporary values that disappear quickly,” while global variables “remain until deleted.” To reduce the workload and save data, it is recommended that you use local variables wherever possible, except for variables such as “user name” and “affection” that need to remain stored.

### Local Variable Lifetime

(This part is a little complicated, so if it is hard to understand, you can skip it for now and read it later if you become curious.)

As for how long local variables can be used, “they can be used only within the current `{ }` and in deeper nested scopes. Their lifetime ends when they leave the relevant `{ }`” (from [Values and Variables](../grammar/03-values-and-variables.md#スコープとライフタイム)).

This is difficult to explain in words, so here is an example.

```
ローカル変数テスト {
	{
		_変数 = 1
	}
	結果 = _変数
}
```

Written this way, `_変数` disappears when moving from the deeper scope to the shallower one, so `結果` also ends up empty. However,

```
ローカル変数テスト {
	_変数 = ""
	{
		_変数 = 1
	}
	結果 = _変数
}
```

if you write it this way, `_変数` is created first in the shallower scope and then moves from the shallower scope → deeper scope → shallower scope… So it does not disappear when moving back from the deeper scope to the shallower one, and `結果` becomes 1. The key point is whether the scope where `_変数` is first created is the same as, or shallower than, the scope containing `結果 = _変数`.

In other words, if you want a local variable to live longer, first write a line such as `_○○ = ""` in the shallowest scope.

## Try Using Variables

### Preparation

Open `dic_main.dic` and find the following lines.

```
//クリックされたら「MouseDoubleClick_(キャラ番号)(当たり判定識別子)」イベントにジャンプ
OnMouseDoubleClick{EVAL("MouseDoubleClick_%(reference[3])%(reference[4])")}
```

Add `//` to the beginning of the `OnMouseDoubleClick` line to comment it out. Then write the following three lines somewhere in its place.

```
OnMouseDoubleClick {
	"\0\s[0]変数の実験をやるよー！\e"
}
```

This event occurs when “the ghost is double-clicked with the left mouse button.” Typical ghosts often respond to being poked or display a menu.

### Try Using Variables Created from SHIORI Events

When the `OnMouseDoubleClick` event occurs, variables such as `reference[0]`, `reference[1]`, and so on are created automatically. The meanings of these variables are documented in the [CROW/SSP Reference - Shiori](http://crow.aqrs.jp/reference/all/Shiori/index.html), which was introduced earlier (the variable written as `Reference0` there is written as `reference[0]` in YAYA).

Try putting `reference[3]`, which contains the number of the clicked character, into the talk.

```
OnMouseDoubleClick {
	"\0\s[0]変数の実験をやるよー！\n\n"
	--
	reference[3]
	--
	"番のキャラがつつかれたよ！\e"
}
```

If you do not enclose a variable in `" "` or `' '`, its value is expanded and becomes part of the talk. Simple! Double-click the main character (character 0) and the sub-character (character 1) to check that it works correctly.

If this way of writing is hard to understand or cumbersome, you can write it as follows.

```
OnMouseDoubleClick {
	"\0\s[0]変数の実験をやるよー！\n\n%(reference[3])番のキャラがつつかれたよ！\e"
}
```

**When using a variable inside `" "`, write it as `%(variable name)`.** If you enclose text in `' '` instead of `" "`, the variable is not expanded and is displayed as-is.

### Try Creating Your Own Variables

Let’s give the ghost a present. To put the string “bouquet” into a variable called “present,” write “variable = value to assign to the variable,” as explained earlier, inside `{ }`.

```
OnMouseDoubleClick
{
	プレゼント = "花束"

	"\0\s[0]わーい「%(プレゼント)」ありがとう！\e"
}
```

```
【ここ】プレゼント【ここ】=【ここ】1【ここ】
```

You can put spaces or tabs in place of 【ここ】. Operators (symbols such as `=` and `+`) can only be half-width. Many people put half-width spaces on either side of operators to make them easier to read.

In this example, the value “bouquet” assigned to the variable is not a number, so enclose it in `" "` or `' '`. This is the same as when writing a talk.

```
OnMouseDoubleClick
{
	プレゼント = 花束

	"\0\s[0]わーい「%(プレゼント)」ありがとう！\e"
}
```

If you accidentally write it this way, the value of “present” will be empty. This is because **YAYA interprets `花束` by itself as “a variable named ‘花束’,” not as `"花束"`**. So it misunderstands the expression to mean “put the value of the variable ‘花束’ into the variable ‘プレゼント’.” Since there is no variable named “花束,” its value ends up empty.

### Try Calculating with Variables

You can also perform calculations with numeric variables.

```
OnMouseDoubleClick
{
	好感度 = 好感度 + 1

	"\0\s[0]ユーザーさんだいすき！\n\n（好感度が「%(好感度)」になった！）\e"
}
```

This is also simple. You can also use the following shorthand.

```
OnMouseDoubleClick
{
	好感度++

	"\0\s[0]ユーザーさんだいすき！\n\n（好感度が「%(好感度)」になった！）\e"
}
```

`好感度++` means “increase 好感度 by 1” and has the same meaning as `好感度 = 好感度 + 1`. `好感度--` decreases it by 1. `好感度 += 2` is the same as `好感度 = 好感度 + 2`, and `好感度 -= 2` is the same as `好感度 = 好感度 - 2`. For explanations of other arithmetic symbols you can use in YAYA, see [Arithmetic](../grammar/04-arithmetic.md).

You can also add strings together.

```
プレゼント = "花" + "束"
```

When written this way, the value of the variable `プレゼント` becomes `"花束"`.

### Check Whether Variables Are Being Saved Correctly

Exit the ghost, then open the save data file (`yaya_variable.cfg`) in a text editor. In the example above, if you see a line like this,

```
プレゼント,"花束",",",
```

the variable was saved successfully. Note that for numeric variables, the number stored in the variable is not enclosed in `" "`:

```
好感度,1,",",
```

For details about the save format, see [SAVEVAR](../functions/SAVEVAR.md#保存形式).

## Previous Step

- [Tutorial 2: Writing Talks](./tutorial-02-writing-dialogue.md)

## Related

- [Basics/Variables](../basic/variables.md)
- [Grammar/3. Values and Variables](../grammar/03-values-and-variables.md)
- [TOSTR](../functions/TOSTR.md)
- [TOINT](../functions/TOINT.md)
