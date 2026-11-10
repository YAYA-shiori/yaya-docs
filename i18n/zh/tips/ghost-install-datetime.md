# 获取人格的安装日期和时间

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

只有最新版 YAYA 支持，

GETTIME(FATTRIB('../../')[9])

即可获取。它会以通用数组的形式返回<br>
年、月、日、星期、时、分、秒<br>
以上各项。

或者，只使用 FATTRIB('../../')[9]，再与 GETSECCOUNT() 相减，即可获取自安装以来经过的秒数。也请试着利用这一方法。
