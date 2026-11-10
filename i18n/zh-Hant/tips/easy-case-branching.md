# 使用case簡化條件分支

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

進行條件分支時，使用if～else if～else有時會很麻煩，因為必須重複撰寫相同的條件。<br>
這時就用case～when～others來簡化吧。

以下是人格切換事件的範例。<br>
在when後面接上人格名稱，並在{}中撰寫對話。

#### 切換至其他人格

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

#### 從其他人格切換過來

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

#### 列出多個條件

when可以用逗號分隔，列出多個條件。<br>
利用這個功能，可以撰寫依月份取得季節的函式。

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

#### 連續數值的簡寫方式

遇到連續的數值時，也可以使用以下寫法。

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
