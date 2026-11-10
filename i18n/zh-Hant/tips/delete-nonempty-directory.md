# 刪除仍有內容的目錄

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 刪除仍有內容的目錄的方法

AYA/YAYA 標準提供的目錄刪除函式 RMDIR 只能刪除空目錄。<br>
因此，我試著建立一個即使目錄內仍有內容也能刪除的函式（類似 deltree 命令）。

請注意，此函式也會強制刪除唯讀檔案或目錄等項目。<br>
此外，它並非使用 Windows 的刪除命令，因此刪除的檔案或目錄不會進入資源回收筒等暫存目錄。<br>
因此，如果指定錯誤的目錄，某些情況下可能會造成無法挽回的結果，使用時請務必小心。

### 使用方法

```
DELTREE(削除したいディレクトリ・ファイル名)
```

### DELTREE 函式

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
