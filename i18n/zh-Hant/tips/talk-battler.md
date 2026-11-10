# 對話對戰器

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

這是一個讓使用者與人格進行一對一對戰的指令碼。<br>

[此處提供可直接使用的範例。](../attachment/AyaBattler.dic)

---

<span style="color:Red">※此處將 OnChoiceSelect 的選項直接寫成獨立函式。[將選項直接寫成獨立函式](independent-choice-function.md)請參閱此頁。</span>

---

Couperin

---

### 範例：體力變弱時攻擊力加倍

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
