# テキストファイルから汎用配列を作成

**Source:** Tips/テキストファイルから汎用配列を作成

## 概要

改行で区切られたテキストファイルの内容を読み込んで、汎用配列として変数に格納する方法を説明しています。

例として `words\food.txt` に以下の内容が記載されている場合を想定:

```
だいふく
おさしみ
とうふ
ラーメン
```

## コード例

```
FCHARSET("Shift-JIS")
_flag = FOPEN("words\food.txt", "r")
food = IARRAY
while 1 {
    _word = FREAD("words\food.txt")
    if (_word == -1) {
        break
    }
    food = (food, _word)
}
FCLOSE("words\food.txt")
```

## 説明

処理の流れ:

1. `FCHARSET` でファイルの文字コードを指定（UTF-8 の場合は `"UTF-8"` に変更）
2. `FOPEN` でファイルを読み込みモード `"r"` で開く
3. `IARRAY` で空の汎用配列を初期化
4. `FREAD` でファイルから1行ずつ読み込む
5. `FREAD` の戻り値が `-1`（ファイル終端）になったら `break` で終了
6. 配列に要素を `(food, _word)` の形で追加
7. `FCLOSE` でファイルを閉じる

実行結果:

| インデックス | 値 |
|-------------|-----|
| `food[0]` | だいふく |
| `food[1]` | おさしみ |
| `food[2]` | とうふ |
| `food[3]` | ラーメン |

## 関連項目

- FOPEN
- FREAD
- FCLOSE
- FCHARSET
- IARRAY
