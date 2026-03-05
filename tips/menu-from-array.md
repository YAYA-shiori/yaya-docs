# 簡易配列からメニューを構築する

**Source:** Tips/簡易配列からメニューを構築する

## 概要

動的に要素数が変化する配列からメニューを構築し、選択判定を行う実装方法を説明します。

## コード例

### 初期化関数

```
MyTestMenuItem {
    testmenuitem1 = "てすと１,てすと２,てすと３"
    testmenuitem2 = "テスト１,テスト２,テスト３,テスト４,テスト５"
}
```

### OpenMenu関数内でのメニュー表示

```
OpenMenu {
    // ...（通常のメニュー項目）
    "\q[メニュー１,TESTMENU1]\n"
    "\q[メニュー２,TESTMENU2]\n"
    // ...
}
```

### OnChoiceSelectでの選択判定

`STRSTR`と`ERASE`関数を組み合わせてメニュー項目IDを抽出し、`case`文で処理を分岐します。

```
OnChoiceSelect {
    if STRSTR(reference0, "TESTMENU") >= 0 {
        _id = ERASE(reference0, "TESTMENU")
        case _id {
            when "1" {
                // testmenuitem1の処理
                _items = SPLIT(testmenuitem1, ",")
                _i = 0
                for _i < ARRAYSIZE(_items) {
                    // 各要素を処理
                    _i++
                }
            }
            when "2" {
                // testmenuitem2の処理
            }
        }
    }
}
```

## 実装手順

1. `OnFirstBoot`および`OnBoot`イベントで初期化関数`MyTestMenuItem`を呼び出す
2. `OpenMenu`関数内にメニュー選択肢タグを埋め込む
3. `OnChoiceSelect`で選択されたIDを判定し、対応する配列を処理する
4. `for`ループで配列の各要素を動的に処理する

## 説明

この実装パターンは、要素数が動的に変化する配列を扱う場合に適しています。カンマ区切り文字列を配列として扱い、`ARRAYSIZE`で要素数を取得して`for`ループで繰り返し処理することで、配列の要素数に依存しない汎用的なメニュー構築が可能です。

## 関連項目

- Tips/配列の要素数を取得
- Tips/選択肢をいきなり独立した関数で書く
- マニュアル/関数/ARRAYSIZE
- マニュアル/関数/SPLIT
