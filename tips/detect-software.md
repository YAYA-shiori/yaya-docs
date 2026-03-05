# 使用しているソフトを判別

**Source:** Tips/使用しているソフトを判別

## 概要

YAYA でゴーストが動作しているベースウェア（実行環境）を判別する方法を説明します。`basewarename` 変数または `basewarenameex` 変数を利用します。

## コード例

```
BwName
{
	if basewarename == "embryo"
	{
		//---- 伺か専用
		"MATERIA"
	}
	elseif basewarename == "SSP"
	{
		//---- SSP専用
		"SSP"
	}
	elseif basewarename == "crow"
	{
		//---- CROW専用
		"CROW"
	}
	else
	{
		//---- その他の場合
		"etc"
	}
}
```

## 説明

### basewarename と basewarenameex

`basewarename` は必ずしもベースウェアの正確な名前を返すとは限りません。そのため `basewarenameex` に置き換えることが推奨されています。

`basewarenameex` は「はろーYAYAわーるど」や「SimpleYAYAテンプレート」などに含まれていますが、全てのテンプレートに存在するわけではありません。

### 活用方法

- トークネタ（会話内容）をベースウェアごとに変更する
- ベースウェアごとに機能を制限する
- ベースウェア固有の機能を条件付きで使用する

### 主なベースウェア名

| 変数値 | ベースウェア |
|--------|------------|
| `"embryo"` | 伺か (MATERIA) |
| `"SSP"` | SSP |
| `"crow"` | CROW |

## 関連項目

- basewarename
- basewarenameex
