# 使用case简化条件分支

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

使用条件分支时，如果采用if～else if～else的写法，就必须反复写出相同的条件，有时会很麻烦。<br>
这时可以使用case～when～others来简化写法。

以下是人格切换事件的示例。<br>
在when后面写上人格名称，并在{}中写对话内容。

#### 切换到其他人格

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

#### 从其他人格切换而来

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

#### 列举多个条件

when后面可以用逗号分隔，列举多个条件。<br>
例如，可以用这种方式编写根据月份获取季节的函数。

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

#### 连续数值的简写方式

数值连续时，也可以采用下面这种写法。

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
