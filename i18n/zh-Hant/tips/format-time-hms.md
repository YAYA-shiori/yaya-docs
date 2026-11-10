# 將秒數轉換為○小時○分○秒格式

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 函式

```
sec_hms {
_v=TOINT(_argv[0])

_a1=_v/3600
_a2=(_v-(_a1*3600))/60
_a3=(_v-(_a1*3600))-(_a2*60)

_v=(_a1,_a2,_a3)
_v
}
```

### 使用方法

```
sec_hms ( 秒数 )
```

會傳回「[0]小時、[1]分、[2]秒」的陣列。<br>
即使「小時」是 30 小時，也不會轉換成「1 天 6 小時」，而是維持「30 小時」（如果也需要年、月、日等單位，建議自行修改）<br>

### 使用範例

- 使用 yaya_shiori3.dic 中與時間相關的函式 ghostuptime。

```
ゴースト起動時間
{
	//ghostuptimeはゴーストの連続起動時間（単位：秒）
	_h = sec_hms (ghostuptime)[0]
	_m = sec_hms (ghostuptime)[1]
	_s = sec_hms (ghostuptime)[2]
	"\0\s[0]私が起動してから%(_h)時間%(_m)分%(_s)秒経過しました。\e"
}
```
