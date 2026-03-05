# 中身の残っているディレクトリを削除する

**Source:** Tips/中身の残っているディレクトリを削除する

## 概要

標準の `RMDIR` 関数は空のディレクトリしか削除できません。このページで提供される `DELTREE` 関数を使うと、ファイルが含まれているディレクトリも再帰的に削除できます。

**注意事項:**
- 読み取り専用ファイルも強制削除される
- ファイルはゴミ箱に入らず完全削除される
- ディレクトリ指定を間違えると取り返しが付かない事態になることがある

作成者: せきやひろし

## コード例

```
//ディレクトリ削除関数(再帰あり)
DELTREE
{
	_dirname = _argv[0]

	_attr_array = FATTRIB(_dirname)

	if (_attr_array == -1) {
		-1
		return
	} elseif (_attr_array[2] == 1) {
		while 1 {
			_files = FENUM(_dirname, '|')
			_files = REPLACE(_files, '\', '/')
			_file_array = SPLIT(_files, '|')

			if (ARRAYSIZE(_file_array) == 0) {
				RMDIR(_dirname)
				return
			} else {
				foreach _file_array; _filename {
					_targetfilename = "%(_dirname)/%(_filename)"
					void DELTREE(_targetfilename)
				}
			}
		}
	} elseif (_attr_array[2] == 0) {
		FDEL(_dirname)
		return
	} else {
		0
		return
	}
}
```

## 説明

### 使用方法

```
DELTREE(削除したいディレクトリ・ファイル名)
```

### 動作の流れ

1. `FATTRIB` 関数でファイル属性を取得する
2. ディレクトリの場合、`FENUM` 関数で内容を列挙する
3. 再帰呼び出しで全ファイル・サブディレクトリを削除する
4. 最後に `RMDIR` 関数でディレクトリ本体を削除する
5. ファイルの場合は `FDEL` 関数で直接削除する

## 関連項目

- RMDIR
- FDEL
- FATTRIB
- FENUM
