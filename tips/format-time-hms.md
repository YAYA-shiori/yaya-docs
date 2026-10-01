# 秒数を○時間○分○秒形式にする

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

## 関数

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

### 使い方

```
sec_hms ( 秒数 )
```

「[0]時間、[1]分、[2]秒」の配列が返ります。<br>
「時間」が30時間であっても「1日6時間」にはならず、「30時間」になります（年、月、日の単位も必要な場合は改変推奨）<br>

### 使用例

- yaya_shiori3.dicの時刻系関数ghostuptimeを使用しています。

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
