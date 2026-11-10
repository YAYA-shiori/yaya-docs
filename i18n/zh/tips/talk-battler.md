# 对话战斗器

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

这是一个用于进行用户与人格一对一战斗的脚本。<br>

[这里提供了可直接使用的示例。](../attachment/AyaBattler.dic)

---

<span style="color:Red">※这里将 OnChoiceSelect 的选项直接写成了独立函数。请参阅[将选项直接写成独立函数](independent-choice-function.md)。</span>

---

Couperin

---

### 示例：体力变弱时攻击力加倍

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

## 附件

- [AyaBattler.dic](../attachment/AyaBattler.dic)
