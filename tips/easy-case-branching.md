# caseを使って条件分岐で手抜きをする

**Source:** Tips/caseを使って条件分岐で手抜きをする

## 概要

条件分岐を書くとき、`if〜elseif〜else` では同じ変数への比較を何度も書く必要があって冗長になる。`case〜when〜others` を使うとすっきり書ける。

## 基本的な使い方

### ゴースト切り替えイベントへの適用

```
OnGhostChanging_normal
{
  case reference0
  when "タケシ" { "タケシのところに行くのね。" }
  when "所長たん" { "所長たんに呼ばれたの？" }
  others { reference0 + "のところね。" }
}

OnGhostChanged_normal
{
  case reference0
  when "タケシ" { "タケシから戻ってきたよ。" }
  when "所長たん" { "所長たんから戻ってきたよ。" }
  others { reference0 + "から戻ってきたよ。" }
}
```

## 応用テクニック

### 複数条件の同時指定

`when` はカンマ区切りで複数の値を同時にマッチさせられる：

```
// 春（3〜5月）の処理
when 3,4,5 { "春だよ。" }
```

### 範囲指定

連続した数値はハイフンで範囲指定できる：

```
GetSeasonSlot
{
  case GETTIME[1]
  when 3-5  { "春" }
  when 6-8  { "夏" }
  when 9-11 { "秋" }
  others    { "冬" }
}
```

`when 3-5` は `when 3,4,5` と等価。

## 関連項目

- マニュアル/文法/フロー制御
- マニュアル/関数/GETTIME
