# Deleting a Directory That Is Not Empty

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## How to Delete a Directory That Is Not Empty

The directory deletion function provided by default in AYA/YAYA, RMDIR, can only delete empty directories.<br>
So, here is a function that can delete directories even when they still contain files (similar to the deltree command).

Note that this function forcibly deletes read-only files and directories as well.<br>
Also, since it does not use the Windows deletion command, deleted files and directories are not placed in a temporary directory such as the Recycle Bin.<br>
Therefore, depending on the circumstances, specifying the wrong directory can lead to irreversible consequences, so please use this function with great care.

### Usage

```
DELTREE(削除したいディレクトリ・ファイル名)
```

### DELTREE Function

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

- Sekiya Hiroshi
