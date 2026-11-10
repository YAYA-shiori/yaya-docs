# 将秒数转换为“○小时○分○秒”格式

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 函数

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

### 用法

```
sec_hms ( 秒数 )
```

返回由「[0]小时、[1]分钟、[2]秒」组成的数组。<br>
即使「小时」为30小时，也不会换算成「1天6小时」，而是返回「30小时」（如果还需要年、月、日等单位，建议自行修改）。<br>

### 使用示例

- 使用 yaya_shiori3.dic 中与时间相关的函数 ghostuptime。

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
