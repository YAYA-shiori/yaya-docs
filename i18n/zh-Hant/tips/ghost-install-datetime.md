# 取得人格的安裝日期時間

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

僅適用於最新版 YAYA，

GETTIME(FATTRIB('../../')[9])

即可取得。會以通用陣列傳回<br>
年、月、日、星期、時、分、秒<br>
。

或者，只使用 FATTRIB('../../')[9] 並與 GETSECCOUNT() 相減，就能取得從安裝至今經過的秒數。也請試著活用看看。
