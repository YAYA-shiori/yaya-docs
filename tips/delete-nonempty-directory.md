# 中身の残っているディレクトリを削除する

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

## 中身の残っているディレクトリを削除する方法

AYA/YAYAに標準で用意されているディレクトリ削除関数、RMDIRでは空のディレクトリしか削除できません。<br>
なので、中身が残っていても削除が可能な関数を作ってみました(deltreeコマンドのようなもの)。

なお、この関数では読み取り専用のファイルやディレクトリなども強制的に削除されます。<br>
また、Windowsの削除コマンドを使っているわけではないので、削除したファイルやディレクトリがゴミ箱など、一時的なディレクトリに入ると言うこともありません。<br>
したがって、ディレクトリ指定を間違うと、場合によっては取り返しが付かない事態になることがありますので、使用する場合は十分ご注意ください。

### 使い方

```
DELTREE(削除したいディレクトリ・ファイル名)
```

### DELTREE関数

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
