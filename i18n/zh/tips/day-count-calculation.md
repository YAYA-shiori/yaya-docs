# 天数计算

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

用于计算天数的函数。

使用J_DATE(年,月,日)即可获取天数。<br>
分别对两个日期执行J_DATE，再求出差值，即可得到两个日期之间相隔的天数。<br>
可用于获取距离上次网络更新已经过去了多少天等信息。

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

## 使用YAYA计算天数

在YAYA中也可以使用以下函数来进行计算。<br>

- [手册/函数/GETTIME](../functions/GETTIME.md)
- [手册/函数/GETSECCOUNT](../functions/GETSECCOUNT.md)
