# Talk Battler

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

This is a script for one-on-one battles between the user and a ghost.<br>

[A sample you can use as-is is available here.](../attachment/AyaBattler.dic)

---

<span style="color:Red">※Here, the OnChoiceSelect choices are written directly as independent functions. See [Writing choices directly as independent functions](independent-choice-function.md).</span>

---

Couperin

---

### Example: Double attack power when health is low

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

## Attachments

- [AyaBattler.dic](../attachment/AyaBattler.dic)
