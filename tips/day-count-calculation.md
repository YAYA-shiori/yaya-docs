# 日数計算

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

日数計算をするための関数。

J_DATE(年,月,日)とすることで、日数を取得できます。<br>
二つの日付に対してJ_DATEを実行し、その差を求めれば、それぞれの日付の間が何日あるかを取得できます。<br>
最後にネットワーク更新が行われてから何日経過したか、などの取得に使えます。

```
//日数計算
J_DATE
{
    _y = TOINT(_argv[0])
    _m = TOINT(_argv[1])
    _d = TOINT(_argv[2])
 
    _result = _d-32075+TOINT(1461*(_y+4800+TOINT((_m-14)/12))/4)+TOINT(367*(_m-2-TOINT((_m-14)/12)*12)/12)-TOINT(3*(TOINT((_y+4900+TOINT((_m-14)/12))/100))/4)
    _result
}
 
//日数と時間の計算
DateTimeCalc
{
    _base_date = _argv[0]   //比較元
    _trgt_date = _argv[1]   //比較先
    _TIME_DIFF = 0
 
    _DATE_DIFF = J_DATE(_trgt_date[0],_trgt_date[1],_trgt_date[2]) - J_DATE(_base_date[0],_base_date[1],_base_date[2])
 
    _trgt_time = TOINT(_trgt_date[3]) * 3600 + TOINT(_trgt_date[4]) * 60 + TOINT(_trgt_date[5])
    _base_time = TOINT(_base_date[3]) * 3600 + TOINT(_base_date[4]) * 60 + TOINT(_base_date[5])
 
    if _trgt_time < _base_time {
       _TIME_DIFF = _trgt_time - _base_time + 86400
    } else {
       _TIME_DIFF = _trgt_time - _base_time
    }
 
    _result = (_DATE_DIFF,_TIME_DIFF)
    _result
}
```

  - せきやひろし

## YAYAでの日数計算

YAYAでは以下の関数を使って行う事もできます。<br>

- [マニュアル/関数/GETTIME](../functions/GETTIME.md)
- [マニュアル/関数/GETSECCOUNT](../functions/GETSECCOUNT.md)
