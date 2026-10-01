# 文バトラー

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

ユーザーとゴーストとの一対一バトルを行うスクリプトです。<br>

[こちらにそのまま使えるサンプルを用意しています。](../attachment/AyaBattler.dic)

---

<span style="color:Red">※ここでは、OnChoiceSelectの選択肢をいきなり独立した関数で書いています。[選択肢をいきなり独立した関数で書く](independent-choice-function.md)を参照してください。</span>

---

Couperin

---

### サンプル：弱ってきたら攻撃力2倍の例

```
damage_value
{
   ///////ゴースト側///////
   if _argv[1] {
      _damage = 0
      case _argv[0] {
         when 1 { // 弱ダメージ(1～14)
            _damage = RAND(13) + 1
         }
         when 2 { // 中ダメージ(11～22)
            _damage = RAND(11)+11
         }
         when 3 { // 強ダメージ(21～30)
            _damage = RAND(10)+21
         }
      }
      
      if ghost_HP < 20 {
         _damage * 2
      }
      else {
         _damage
      }
   }
   ///////ユーザー側///////
   else {
      _damage = 0
      case _argv[0] {
         when 1 { // 弱ダメージ(1～14)
            _damage = RAND(13) + 1
         }
         when 2 { // 中ダメージ(11～22)
            _damage = RAND(11)+11
         }
         when 3 { // 強ダメージ(21～30)
            _damage = RAND(10)+21
         }
      }
      
      if user_HP < 20 {
         _damage * 2
      }
      else {
         _damage
      }
   }
}
```

## 添付ファイル

- [AyaBattler.dic](../attachment/AyaBattler.dic)
