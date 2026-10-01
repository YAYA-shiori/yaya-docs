# ゴーストのインストール日時を取得する

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

最新版YAYAのみですが、

GETTIME(FATTRIB('../../')[9])

で取れます。汎用配列で<br>
年,月,日,曜日,時,分,秒<br>
が返ります。

あるいは、FATTRIB('../../')[9]のみで、GETSECCOUNT()と引き算すると、インストールされてから今までの経過秒数が取れます。こちらも活用してみて下さい。
