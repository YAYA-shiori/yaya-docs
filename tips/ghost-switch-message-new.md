# ゴースト切替えメッセージを変化させる(新)

**Source:** Tips/ゴースト切替えメッセージを変化させる(新)

## 概要

複数ゴーストへの切り換え反応を管理する際の可読性を向上させた実装方法。従来の `OnGhostChanging` と `OnGhostChanged` を専用ヘルパー関数に置き換え、ゴーストごとに個別の関数を定義できるようにします。

ゴースト名に含まれる特殊文字（`!`, `%`, `"`, `#`, `$`, `&`, `(`, `)`, `*`, `+`, `,`, `-`, `/`, `:`, `;`, `<`, `=`, `>`, `?`, `@`, `[`, `]`, `` ` ``, `{`, `|`, `}`, `~` など）はすべてアンダースコア `_` に置換されます。

例: `+Emily+` → 関数名 `OnGhostChanged__Emily_`

## コード例

### ヘルパー関数（辞書の末尾に追加）

```
TranslateSystemChar
{
    _text = TOSTR(_argv[0])
    _text = RE_REPLACE(_text,"[ !%(CHR(0x22))%(CHR(0x25))#$&()*+,\-/:;<=>?@\[\]`{|}~]","_")
    _text
}

ExecuteChangeCallTalk
{
    _ghostname = TranslateSystemChar(reference0)
    _funcname = "%(_argv[0])_%(_ghostname)"
    if ISFUNC(_funcname) {
        _script = EVAL(_funcname)
        if STRLEN(_script) != 0 {
            _script
            return
        }
    }
    _funcname = "%(_argv[0])Other"
    if ISFUNC(_funcname) {
        _script = EVAL(_funcname)
        if STRLEN(_script) != 0 {
            _script
            return
        }
    }
    if _argc >= 2 {
        _script = EVAL(_argv[1])
        if STRLEN(_script) != 0 {
            REPLACE(_script,"\\-","")
            return
        }
    }
}

OnGhostChanging { ExecuteChangeCallTalk("OnGhostChanging","OnClose") }
OnGhostChanged  { ExecuteChangeCallTalk("OnGhostChanged","OnBoot") }
OnGhostCalling  { ExecuteChangeCallTalk("OnGhostCalling") }
OnGhostCalled   { ExecuteChangeCallTalk("OnGhostCalled","OnBoot") }
OnGhostCallComplete { ExecuteChangeCallTalk("OnGhostCallComplete") }
OnOtherGhostClosed  { ExecuteChangeCallTalk("OnOtherGhostClosed") }
```

### ゴースト専用関数の定義（命名規則: `[イベント名]_[Sakura名]`）

```
OnGhostChanged_ゴーストA
{
    if "お料理" _in_ reference1 {
        "(文章1)"
    }
    elseif "薬" _in_ reference1 {
        "(文章2)"
    }
    else {
        "(文章3)"
    }
}
```

## 説明

### 対応イベント一覧

| 関数名 | 機能 |
|--------|------|
| `OnGhostChanging` | 他ゴーストへ切り替え時 |
| `OnGhostChanged` | 他ゴーストから切り替えられた時 |
| `OnGhostCalling` | ゴースト呼び出し開始時 |
| `OnGhostCallComplete` | ゴースト呼び出し完了時 |
| `OnGhostCalled` | 他ゴーストから呼び出された時 |
| `OnOtherGhostClosed` | 他ゴースト終了時 |

### `ExecuteChangeCallTalk` の動作

1. `reference0`（ゴースト名）の特殊文字をアンダースコアに変換
2. `[イベント名]_[ゴースト名]` の関数があれば実行
3. なければ `[イベント名]Other` の関数があれば実行
4. それもなければフォールバック（OnClose / OnBoot 等）を実行

## 関連項目

- Tips/ゴースト切替えメッセージを変化させる
- ISFUNC
- EVAL
