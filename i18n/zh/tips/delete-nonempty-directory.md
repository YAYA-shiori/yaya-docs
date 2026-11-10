# 删除非空目录

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 删除非空目录的方法

AYA/YAYA 标准提供的目录删除函数 RMDIR 只能删除空目录。<br>
因此，我编写了一个即使目录中仍有内容也能删除它的函数（类似于 deltree 命令）。

请注意，此函数也会强制删除只读文件和目录等。<br>
此外，它并不使用 Windows 的删除命令，因此被删除的文件或目录不会进入回收站等临时目录。<br>
因此，如果指定了错误的目录，某些情况下可能会造成无法挽回的后果，使用时请务必小心。

### 用法

```
DELTREE(削除したいディレクトリ・ファイル名)
```

### DELTREE 函数

```
//ディレクトリ削除関数(再帰あり)
DELTREE
{
	_dirname = _argv[0];	//引数を分かりやすい名前の変数に代入

	_attr_array = FATTRIB(_dirname);	//ファイル属性を取得

	if (_attr_array == -1 ){
		-1;	//ファイルが存在しない、などの場合は-1を返して終了
		return;
	} elseif (_attr_array[2]==1) {
		//対象がディレクトリなら、ディレクトリ削除処理実行
		while 1 {	//無限ループ(ディレクトリを確実に消去するため)
			//ディレクトリ内ファイル・ディレクトリ一覧取得
			_files = FENUM(_dirname,'|');		//┐
			_files = REPLACE(_files,'\','/');	//├ここのスプリッタは必要に応じて変更
			_file_array = SPLIT(_files,'|');	//┘

			if (ARRAYSIZE(_file_array) == 0) {
				//ディレクトリ内に何もなければディレクトリ削除実行。
				//RMDIR関数を実行し、その結果をそのまま返す。
				RMDIR(_dirname);
				return;
			} else {
				//取得した一覧を元にファイル・ディレクトリ削除実行
				foreach _file_array; _filename {
					//処理すべきファイル・ディレクトリ名を生成
					_targetfilename = "%(_dirname)/%(_filename)";
					void DELTREE(_targetfilename);	//再帰呼び出し
				}
			}
		}
	} elseif (_attr_array[2]==0){
		//普通のファイルなら単純に削除。FDEL関数の結果をそのまま返す。
		FDEL(_dirname);
		return;
	} else {
		//その他、状況が不明な場合は0を返して終了
		0;
		return;
	}
}
```

- せきやひろし
