# Discarding a Function's Return Value

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

When you call a function without assigning its return value to a variable, the return value becomes a candidate for output.<br>
This can cause problems, such as mysterious “1” or “0” values appearing in talks.

#### Example of a Problem

For example, with the following dictionary, “0” or “1” will appear in the balloon with a 50% chance, leaving you wondering why.

```
OnTestTalk
{
   //乱数のシードを設定
   SRAND( "ほげほげ" ) //SRAND関数は返り値を返すので出力候補になる。

   //サイコロを振る
   _num = RAND(6)

   "\0サイコロを振るよ！\1結果は(_num)だな。\e"
}
```

#### Example of a Solution

Since the SRAND function returns a value, you can assign it to an appropriate variable to remove it from the candidates for output.

```
OnTestTalk
{
   //乱数のシードを設定
   _hoge = SRAND( "ほげほげ" ) //SRAND関数の返り値を捨て変数に代入させる。

   //サイコロを振る
   _num = RAND(6)

   "\0サイコロを振るよ！\1結果は(_num)だな。\e"
}
```

#### Using void

You can also discard a return value by adding “void” to a function call.<br>
Note that this is not an assignment. (No “=” is needed.)

```
OnTestTalk
{
   //乱数のシードを設定
   void SRAND( "ほげほげ" ) //SRAND関数の返り値を捨てる

   //サイコロを振る
   _num = RAND(6)

   "\0サイコロを振るよ！\1結果は(_num)だな。\e"
}
```
