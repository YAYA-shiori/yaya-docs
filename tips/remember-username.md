# ユーザーの名前を覚える

**Source:** Tips/ユーザーの名前を覚える

## 概要

ゴーストがユーザーの名前を `inputbox` ダイアログを通じて取得し、グローバル変数 `username` に保存する方法を説明しています。保存した名前はその後のセリフで `%username` として参照できます。

## コード例

### 基本実装（シンプル版）

```
ChoiceUsernameEntry
{
    "\0お名前、教えてください。\![open,inputbox,OnInputUsername,-1]\e"
}

OnInputUsername
{
    username = EscapeAllTags(reference[0])
    if username == ""
    {
        username = '名無し'
        "\0教えてくれないの？\n\w9じゃあ勝手に%usernameって呼んじゃうね。\e"
    }
    else
    {
        "\0じゃあこれから、\w5%usernameって呼ぶね。\e"
    }
}
```

- `EscapeAllTags` でSakuraスクリプトタグを除去してから保存する
- 空入力の場合は `'名無し'` をデフォルト値として使用する

### 応用実装（敬称選択付き）

```
ChoiceUsernameEntry
{
    "\0お名前、教えてください。\![open,inputbox,OnInputUsername,-1]\e"
}

OnInputUsername
{
    inputted_name = reference[0]
    "/
    \0呼び方は、どうするの？\n\n[half]/
    \![*]\q[ちゃん,Oninputted_name1]\n/
    \![*]\q[さん,Oninputted_name2]\e"
}

Oninputted_name1
{
    "/
    \0「%inputted_nameちゃん」でいい？\n\n[half]/
    \![*]\q[いいよ,Oninputted_name1_determination]\n/
    \![*]\q[まちがい,ChoiceUsernameEntry]\e"
}

Oninputted_name1_determination
{
    username = "%inputted_nameちゃん"
    "\0じゃあこれから、\w5%usernameってよぶね。\e"
}

Oninputted_name2
{
    "/
    \0「%inputted_nameさん」でいい？\n\n[half]/
    \![*]\q[いいよ,Oninputted_name2_determination]\n/
    \![*]\q[まちがい,ChoiceUsernameEntry]\e"
}

Oninputted_name2_determination
{
    username = "%inputted_nameさん"
    "\0じゃあこれから、\w5%usernameって呼ぶね。\e"
}
```

## 説明

- `\![open,inputbox,コールバック関数名,-1]` : inputbox ダイアログを開く Sakura スクリプト
- `reference[0]` : ユーザーが入力したテキスト
- `EscapeAllTags` : 入力値から Sakura スクリプトタグを除去するセキュリティ処理
- 敬称選択版では `inputted_name` に一時保存し、確認後に `username` へ格納する
- 保存した名前は `%username` でセリフ内から参照できる

## 関連項目

- SAVEVAR（変数の永続化）
