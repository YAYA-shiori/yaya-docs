# Cut corners on conditional branching with case

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

When using conditional branching, writing if～else if～else can be tedious because you have to repeat the same conditions many times.<br>
Instead, use case～when～others to cut corners.

Example of a ghost-switching event.<br>
Write a ghost name after when, and put the talk inside {}.

#### Switching to another ghost

```
OnGhostChanging_normal
{
   _NOWDATE      = "%(year),%(month),%(day),%(hour),%(minute),%(second)"
   CloseTime     = _NOWDATE

   _ghostname = reference0
   if reference2 != "" {
      _ghostname = reference2
   }

   case reference0 {
      when "タケシ" {
         "\1\s[10]\0\s[0]再起動かな？\w9\1さぁ？\w9\e"
         "\1\s[10]\0\s[0]再起動するぞ。\w9\e"
      }

      when "コノハ" {
         "\1\s[10]\0\s[5]\_s名古屋開始。\w9\e"
      }

      when "所長たん" {
         "\1\s[10]\0\s[4]あ～、できればこのプログラムのデバッグ、お願いできませんか？\w9\1無茶言うな。\w9\e"
      }

      when "あさたろう" {
         "\1\s[10]\0\s[5]同じSEなのに、あっちは気楽そうでいいよな。\w9\1転職するか？\w9\e"
      }

      others {
         "\0\s[0]\1\s[10]%(_ghostname)へ交代か。\w9\0\s[5]%(reference0)、後はよろしく頼むぜ。\w9\e"
      }
   }
}
```

#### Switching from another ghost

```
OnGhostChanged_normal
{
   _StartUpTimeBack = StartUpTime
   StartUpTime      = "%(year),%(month),%(day),%(hour),%(minute),%(second)"

   _ghostname = reference0
   if reference2 != "" {
      _ghostname = reference2
   }

   case reference0 {
      when "タケシ" {
         StartUpTime = _StartUpTimeBack
         "\1\s[10]\0\s[0]再起動完了。\e"
      }

      when "所長たん" {
         "\1\s[10]\0\s[4]所長たんみたいにのびのびプログラムができればなぁ。\w9\1サラリーマンはそうは行かないからな。\e"
      }

      when "あさたろう" {
         "\1\s[10]\0\s[4]同じSEなのに、この格差はなんなんだろう‥‥‥‥\w9\1考えるな、考えたら負けだ。\w9たぶん。\e"
      }

      others {
         "\0\s[0]\1\s[10]%(_ghostname)から切り替わったぞ。\w9\0\s[5]%(reference0)、お疲れさん。\e"
      }
   }
}
```

#### Listing multiple conditions

You can list multiple conditions for when by separating them with commas.<br>
You can use this to write a function that gets the season from the month, for example.

```
GetSeasonSlot
{
   case month {
      when 3,4,5 {
         "春"
      }

      when 6,7,8 {
         "夏"
      }

      when 9,10,11 {
         "秋"
      }

      when 12,1,2 {
         "冬"
      }
   }
}
```

#### Shorthand for consecutive numbers

When numbers are consecutive, you can also write them as follows.

```
GetSeasonSlot
{
   case month {
      when 3-5 {
         "春"
      }

      when 6-8 {
         "夏"
      }

      when 9-11 {
         "秋"
      }

      when 12,1,2 {
         "冬"
      }
   }
}
```
