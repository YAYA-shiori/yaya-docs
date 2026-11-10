# Get the Ghost Installation Date and Time

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

This works only with the latest version of YAYA,

GETTIME(FATTRIB('../../')[9])

to retrieve the values. The generic array returns<br>
year, month, day, day of the week, hour, minute, second<br>
.

Alternatively, using only FATTRIB('../../')[9] and subtracting it from GETSECCOUNT() gives you the number of seconds elapsed since installation. Give this a try as well.
