# caseを使って条件分岐で手抜きをする

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

条件分岐のとき、if～else if～elseだと、何度も同じ条件を書かねばならず、面倒なことがあります。<br>
そこで、case～when～othersを使って手抜きをしてしまいましょう。

ゴースト切り替えイベントの例。<br>
whenに続けてゴースト名を書き、{}の中にトークを書きます。

#### 他のゴーストへ切り替え

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

#### 他のゴーストから切り替り

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

#### 複数条件の列挙

whenは、カンマで区切ることで複数条件を列挙できます。<br>
これを利用して月から季節を取得する関数などが書けます。

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

#### 数値が連続する時の略記法

数値が連続する場合、以下のような書き方も可能です。

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
