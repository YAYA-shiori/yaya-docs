# yaya_shiori3.dic

## システム辞書とは

システム辞書とは、YAYA を「ゴーストの SHIORI として簡単に利用できるようにする」ための、一連の機能をもった YAYA スクリプトファイルの集まりのこと。現在、システム辞書は次の構成になっている（`yaya_base` フォルダ内にある）。

| ファイル | 説明 |
|---------|------|
| `shiori3.dic` | SHIORI コア辞書。SHIORI として動作するための必要最低限の機能を実装している。このページで説明する |
| `compatible.dic` | 過去互換辞書。AYA4、5 と互換動作するための機能を実装している（必要なければ読み込まなくてもよい） |
| `optional.dic` | 追加機能辞書。必須ではないがあると便利な機能を実装している（[yaya_optional.dic](./yaya-optional-dic.md)） |
| `lint.dic` | 読み込み済みの辞書から、未定義・未使用の変数や関数を探す `SHIORI3FW.Lint.Run` を提供する（YAYA Tc574-1以降） |
| `config.dic` | `shiori3.dic` のパラメータを設定・変更するための辞書。この辞書はユーザー（ゴースト作成者）が変更するもの。詳しい内容はファイル自体に書いてある |

`config.dic` を除く辞書は、基本的にはユーザーが変更する必要はない。

最新安定版は、「[はろーYAYAわーるど（紺野ややめ）](http://ms.shillest.net/yayame.xhtml)」内で提供している。適宜更新すること。更新するときは、`yaya.dll` も同時に更新することをお勧めする。最新開発版は、[yaya-dic](https://github.com/YAYA-shiori/yaya-dic) で見られる。

`yaya-dic` を使うときは、基礎設定ファイルに次の行を追加する（[基礎設定](../grammar/01-basic-settings.md)）。

```
dicdir, yaya_base
```

`_loading_order.txt` を編集すると、`optional.dic` を無効にしたり、`compatible.dic` を有効にしたりできる。

## 概要

`yaya_shiori3.dic` は、YAYA ベースのゴーストに SHIORI/3.0 としての核心機能を提供するシステム辞書。

## SHIORI イベントの入出力

ベースウェアから渡される SHIORI イベントは、たとえば次のような文字列。

```
GET SHIORI/3.0
Sender: SSP
Charset: UTF-8
SecurityLevel: local
ID: OnSecondChange
Status: talking
Reference0: 107
Reference1: 0
Reference2: 0
Reference3: 1
Reference4: 0
```

`yaya_shiori3.dic` は、この文字列を解釈して次の動作を行う。

| ヘッダ | 動作 |
|--------|------|
| `ID: OnSecondChange` | イベント名として解釈し、`OnSecondChange` 関数を呼び出す。先頭に `On` がつかない ID は、`On_` をつけた関数を呼び出す（例: `hwnd` → `On_hwnd`） |
| `Sender: SSP` | グローバル変数 `basewarename`、`sender` に値（`"SSP"`）を格納する |
| `Charset: UTF-8` | 文字コード。適切に解釈し、出力時にその文字コードへの変換を行う |
| `Status: talking` | グローバル変数 `status` に値（`"talking"`）を格納する |
| `Reference0: 107` | グローバル変数 `reference[0]` に値（107）を格納する |

上記の動作の結果、`OnSecondChange` 関数内で処理が行われたあと、`yaya_shiori3.dic` はその結果を次のような文字列としてベースウェアに返す。

```
SHIORI/3.0 200 OK
Sender: AYA
Charset: UTF-8
Value: \0\s[0]あ、エミリさん。\1\s[10]テディも元気そうだな。
Reference0: Emily
```

| ヘッダ | 内容 |
|--------|------|
| `SHIORI/3.0 200 OK` | 自動的に適切なコードを返す |
| `Sender: AYA` | 自動付加される |
| `Charset: UTF-8` | 自動的に適切なコードを返す |
| `Value: ～` | 関数の実行結果（要するにトーク）の内容が入る |
| `Reference0: Emily` | `res_reference*`（`*` は数字）という名前のグローバル変数があった場合、ここに入る（ベースウェアは、SHIORI から返された Reference0 を、コミュニケート相手のゴースト名として認識する） |

## ランダムトーク

ランダムトークを簡単に行えるようにするため、`OnAiTalk` 関数を `aitalkinterval` 秒ごとに呼び出す機能を持つ。本来 `OnAiTalk` はベースウェアには存在しない機能で、`yaya_shiori3.dic` がその機能を追加している。

## 内部トランスレート

すべてのイベントの処理後に、`OnTranslateInternal` 関数を呼び出す機能を持つ。その際の引数（`_argv[0]`）は、ベースウェアに出力しようとしているトーク内容になる。この関数で返した内容が、実際にベースウェアに出力されるトークになる。したがって、`OnTranslateInternal` 内で `_argv[0]` を適当に加工して返すことで、すべてのトークに一律変換を行う、などの処理ができる。

## チェイントーク

チェイントークとは、「あるトークを契機として、一連のトークを指定した順序で行う」機能。これも `yaya_shiori3.dic` で実装されている。

トークの `\e` の後に `:chain=○○` と書くと、チェイントークが発動する（`○○` はチェイントークを区別するための識別子で、`end` 以外ならどんな文字列でもよい）。チェイントークが発動した場合、`OnAiTalk` ではランダムトークではなく、上で書いた `○○` 関数（チェイン関数）が呼び出される（この機能は `yaya_shiori3.dic` ではなく、ゴーストテンプレート側で記載されている）。

チェイン関数は、通常の関数とは異なり、次のように記載する（`:chain=hoge` とした場合）。

```
hoge
{{CHAIN
    "\0\s[0]りんご\e"
    "\0\s[1]ごりら\e"
    "\0\s[0]らっぱ\e:chain=end"
}}CHAIN
```

通常の関数では「りんご」「ごりら」「らっぱ」のどれか 1 つが無作為に選択されるが、チェイン関数では、上から順番にトークが連鎖する。`\e` の後に `:chain=end` と書くと、チェイントークを停止できる。

### チェイン区切り文字（`:chain=`）

トークスクリプトの末尾に `:chain=イベント名` を付けると、次のランダムトークの機会に、指定したイベントが呼ばれる。

```
OnMyEvent
{
	'\0\s[0]続きがあるよ。\e' + ':chain=' + 'OnMyEventPart2'
}

OnMyEventPart2
{
	'\0\s[0]これが続きです。\e'
}
```

## 遅延 EVAL

`\e` の後に `:eval=式` と書くと、その式を実行（実際には `EVAL(式)` と書くのと同じ）できる。たとえば `"\0\s[0]はじめまして。\e:eval=aisatu=1"` と書くことで、「あるトークをしゃべることを契機としたフラグ処理」のようなものを簡単に行える。

セキュリティ上の理由から、この機能はデフォルトで無効化されている。有効化したい場合は、セキュリティ上のリスクをよく理解したうえで、`config.dic` 内の `SHIORI3FW.ENABLE_DELAYED_EVAL` を 1 に設定する。

## インストール済みゴーストリスト

`ID: installedghostlist` を解釈し、グローバル変数 `installedghostlist`（ゴースト名の汎用配列）などを作成する。

`OnNotifyInstalledGhostName` などのイベントを受け取ると、次の変数が自動的に更新される。インデックスは対応しており、`installedghostlist[i]` のゴーストのさくら名は `installedsakuralist[i]` になる。

| 変数名 | 内容 |
|--------|------|
| `installedghostlist` | インストール済みゴーストのゴースト名配列 |
| `installedsakuralist` | インストール済みゴーストのさくら名配列 |
| `installedkerolist` | インストール済みゴーストのケロ名配列 |

## SAORI 呼び出し

SAORI 呼び出しを簡単に行えるよう、`yaya_shiori3.dic` で次の関数を提供している。SAORI のロード、アンロードも、`FUNCTIONEX` を利用したときに自動的に行われる。

### FUNCTIONEX

```
FUNCTIONEX( dllname [, Argument0 , Argument1 , ... ] )
```

| 引数 | 説明 |
|------|------|
| `dllname` | 呼び出したい SAORI の DLL 名。`yaya.dll` からの相対パスで指定する |
| `Argument0, 1, ...` | SAORI に与える引数（省略可能） |

`FUNCTIONEX` の返り値は、SAORI の返り値（Result の値）になる。SAORI がそれ以上の返り値（Value0、1、…）を返した場合は、`valueex` 配列および グローバル変数 `valueex0`、`valueex1`、… に格納される。

```
_result = FUNCTIONEX('kawari8.dll', 'こんにちは')
// 追加の戻り値は valueex[0], valueex[1], ... で参照
```

詳しくは [FUNCTIONEX](../functions/FUNCTIONEX.md) を参照。

### SAORI

`FUNCTIONEX` のシノニム（別名）。書き方は `FUNCTIONEX` と同じ。一段下駄が入る分、`FUNCTIONEX` より低速になるが、気にするほどではない。

### FUNCTIONLOAD

SAORI の DLL を読み込む。引数は SAORI の DLL ファイル名。成功時は 1、失敗時は 0 を返す。

```
FUNCTIONLOAD('kawari8.dll')
```

### SHIORI3FW.SaoriUnloadAll

現在ロードされているすべての SAORI の DLL をアンロードする。引数も戻り値もない。

## ベースウェアプロパティ関数

SSP など、DIRECTSSTP に対応したベースウェアのプロパティを読み書きする。

| 関数 | 説明 |
|------|------|
| `GET_PROPERTY(プロパティ名)` | プロパティ値を取得する。成功時はプロパティ値の文字列、失敗時は空文字列を返す |
| `SET_PROPERTY(プロパティ名, 値)` | プロパティに値を設定する。成功時は 1、失敗時は 0 を返す |

```
_vol = GET_PROPERTY('volume')
SET_PROPERTY('volume', '80')
```

## 配列操作

| 関数 | 説明 |
|------|------|
| `JOIN(値0, 値1, ..., 区切り文字)` | 最後の引数を区切り文字として、それ以外の値（配列を渡すと要素が並ぶ）を連結した文字列を返す |
| `REVERSE(値0, 値1, ...)` | 引数の順序を逆にした配列を返す |
| `UNIQUE(値0, 値1, ...)` | 引数から重複を除いた配列を返す（[ARRAYDEDUP](../functions/ARRAYDEDUP.md) のラッパー） |
| `SPLITEX(文字列, 区切り文字)` | [SPLIT](../functions/SPLIT.md) と同じだが、中身が空の要素は配列化しない |
| `MAX(値0, 値1, ...)` | 引数の最大値を返す。文字列が入っている場合は、辞書順で最後のものが返る |
| `MIN(値0, 値1, ...)` | 引数の最小値を返す。文字列が入っている場合は、辞書順で最初のものが返る |
| `AVERAGE(値0, 値1, ...)` | 引数の平均値を返す。文字列が入っている場合は、空文字が返る |

```
_配列 = ("A","B","C","D","E")
結果 = JOIN(_配列, "★")   // "A★B★C★D★E"
```

## テキスト処理・状態確認

### SHIORI3FW.RemoveAllTags

さくらスクリプトタグ（`\0`、`\s[0]` など）をすべて除去した文字列を返す。

```
_plain = SHIORI3FW.RemoveAllTags('\0\s[0]こんにちは。\e')
// → "こんにちは。"
```

タグを除去するのではなく、エスケープして表示したいときは、[SHIORI3FW.EscapeAllTags](./yaya-optional-dic.md#shiori3fwescapealltags) を使う。

### SHIORI3FW.CanTalk

現在ゴーストがしゃべれる状態かどうかを返す。`status` ヘッダに `talking`・`choosing`・`minimizing`・`timecritical` のいずれかが含まれている場合は、しゃべれないと判断する。しゃべれる場合は 1、しゃべれない場合は 0 を返す。

```
if SHIORI3FW.CanTalk {
	// ランダムトーク発動
}
```

## 遅延イベント（「遅れてしゃべる」イベント）

指定した秒数後に、特定のイベントを 1 度だけ発動させる。発動は `OnSecondChange`（1 秒ごと）のタイミングで処理される。

### SHIORI3FW.SetDelayEvent

```
SHIORI3FW.SetDelayEvent( '発生させるイベント名' , 遅れる秒数 [, Reference0, ...] )
```

遅延イベントを登録する。イベント名が空文字列だとキャンセルする。第 3 引数以降は、イベント発動時にセットする Reference 値（省略可）。

```
// 10秒後に OnMyDelayedEvent を発動
SHIORI3FW.SetDelayEvent('OnMyDelayedEvent', 10)

// キャンセル
SHIORI3FW.SetDelayEvent('', 0)
```

### SHIORI3FW.GetDelayEvent

現在登録されている遅延イベントの情報を、`(イベント名, 残り秒数, Reference の配列)` で返す。

## レスポンスヘッダ追加

イベントハンドラのレスポンスに、任意のヘッダを追加できる。設定はリクエストごとにリセットされる。

| 関数 | 説明 |
|------|------|
| `SHIORI3FW.PushAdditionalReturn(ヘッダ名, 値)` | 任意のレスポンスヘッダを追加する |
| `SHIORI3FW.Push_X_SSTP_PassThru(名前, 値)` | `X-SSTP-PassThru-名前` ヘッダを追加する（SSTP パススルーに使用する） |

イベントハンドラ内で次の変数に値を設定すると、レスポンスヘッダに自動的に付加される。

| 変数名 | ヘッダ | 内容 |
|--------|--------|------|
| `res_reference` または `res_reference0` 〜 `res_reference31` | `Reference0:` 〜 | イベント応答の Reference 値。配列または個別の変数で指定する |
| `marker` または `res_marker` | `Marker:` | SSTP マーカー値 |
| `res_securitylevel` | `SecurityLevel:` | セキュリティレベル |
| `res_valuenotify` | `ValueNotify:` | ValueNotify 値 |

```
OnMyEvent
{
	res_reference0 = 'value0'
	res_reference1 = 'value1'
	'\0\s[0]処理しました。\e'
}
```

`res_reference` の上限インデックスは `config.dic` の `SHIORI3FW.RES_REF_MAX`（初期値 32）で決まる。

## 変数管理ユーティリティ

### SHIORI3FW.RegisterTempVar

```
SHIORI3FW.RegisterTempVar( 変数名, ... )
```

終了時（unload 時）に自動削除するグローバル変数を登録する。保存が不要な一時的なグローバル変数の管理に使う。

```
myTempVar = '一時データ'
SHIORI3FW.RegisterTempVar('myTempVar')
```

## 疑似イベント

これらの関数をゴーストの辞書に定義すると、特定のタイミングで呼び出される。

| 関数 | 呼ばれるタイミング |
|------|------------------|
| `OnSHIORI3FW.SurfaceRestore` | AI トーク間隔の 2/3 が経過したとき。トーク前にサーフェスをデフォルトに戻す処理などに使う |
| `OnSHIORI3FW.ChangeSelfInfo` | ゴースト名・シェル名・シェルパス・バルーン名・バルーンパスが更新されたとき |
| `OnSHIORI3FW.WindowCreate` | キャラウィンドウが新たに生成されたとき。`reference[0]` にスコープ番号が入る |
| `OnSHIORI3FW.WindowDestroy` | キャラウィンドウが破棄されたとき。`reference[0]` にスコープ番号が入る |

```
OnSHIORI3FW.SurfaceRestore
{
	'\0\s[0]\1\s[10]\e'
}
```

## システム変数

そのままでは利用が面倒な関数を簡単に利用するため、次の変数が提供されている。システム情報を取得するために使える。これらの変数はシステムが自動的に更新するので、参照専用として使うこと。

### 時刻系変数

| 変数名 | 返り値 |
|--------|--------|
| `year` | 現在日時の年の数値 |
| `month` | 現在日時の月の数値 |
| `day` | 現在日時の日の数値 |
| `weekday` | 現在日時の曜日の数値（0=日曜日、1=月曜日 … 6=土曜日） |
| `hour` | 現在日時の時の数値（24 時間制） |
| `ampm` | 現在日時の午前午後の数値（0=AM、1=PM） |
| `hour12` | 現在日時の時の数値（12 時間制） |
| `hour12ex` | 現在日時の時の数値（12 時間制）。ただし 12 は 0 時または 12 時に表示される |
| `minute` | 現在日時の分の数値 |
| `second` | 現在日時の秒の数値 |
| `systemuptime` | OS 連続起動時間（単位: 秒） |
| `systemupsecond` | OS 連続起動時間を時分秒とした場合の秒の数値 |
| `systemupminute` | OS 連続起動時間を時分秒とした場合の分の数値 |
| `systemuphour` | OS 連続起動時間を時分秒とした場合の時の数値 |
| `ghostupmin` | ゴーストの連続起動時間（単位: 分） |
| `ghostupmin_total` | ゴーストの累計起動時間（単位: 分） |
| `ghostuptimes` | ゴーストの累計起動回数 |

### メモリ系変数

| 変数名 | 返り値 |
|--------|--------|
| `memoryload` | 物理メモリの使用率 |
| `memorytotalphys` | 物理メモリ量 |
| `memoryavailphys` | 空き物理メモリ量 |
| `memorytotalvirtual` | 仮想＋物理メモリ量 |
| `memoryavailvirtual` | 仮想＋物理空きメモリ量 |

### センダーヘッダ系変数

| 変数名 | 返り値 |
|--------|--------|
| `basewarenameex` | ゴーストが起動しているベースウェア名（MATERIA は `embryo`、CROW は `crow`、SSP は `SSP`）。初回起動時の値で、変わらない |
| `basewarename` | 現在のリクエストの送信元ベースウェア名（センダーヘッダ名。ベースウェア名以外のものが入っていることもある） |
| `sender` | `basewarename` と同じ |

### ゴースト・シェル情報

| 変数名 | 内容 |
|--------|------|
| `SHIORI3FW.GhostName` | 現在のゴースト名 |
| `SHIORI3FW.ShellName` / `SHIORI3FW.ShellPath` | 現在のシェル名 / シェルパス |
| `SHIORI3FW.BalloonName` / `SHIORI3FW.BalloonPath` | 現在のバルーン名 / バルーンパス |
| `selfname` / `sakuraname` | さくら（スコープ 0）のキャラ名 |
| `keroname` | ケロ（スコープ 1）のキャラ名 |
| `SHIORI3FW.HWnd` | キャラウィンドウの HWND 配列。`[0]` がさくら側 |
| `SHIORI3FW.BalloonHWnd` | バルーンウィンドウの HWND 配列。`[0]` がさくら側 |
| `SHIORI3FW.LastSurface` | 直前に表示していたサーフェス番号の配列。`[0]` がさくら側 |
| `SHIORI3FW.IsVisible` | サーフェスの表示状態（1=表示中、0=非表示）。`[0]` がさくら側 |
| `SHIORI3FW.UserName` / `SHIORI3FW.UserNameFull` | ユーザー名（短縮 / フルネーム） |
| `SHIORI3FW.UserBirthday` | 誕生日の配列 `[年, 月, 日]`（整数型） |
| `SHIORI3FW.UserSex` | 性別 |
| `SHIORI3FW.LastTalk` | 直前にしゃべったスクリプト（全イベント対象） |
| `SHIORI3FW.LastAITalk` | 直前のランダムトークのスクリプト |
| `SHIORI3FW.Eventid` | 現在処理中のイベント ID |
| `SHIORI3FW.Status` | 初期起動ステータス（`Run` で初期化済み） |
| `SHIORI3FW.UniqueID` | Auth.SSTP で使用する ID |
| `SHIORI3FW.Capability` | ベースウェアのヘッダ処理能力（汎用配列） |

## ユーザー設定変数

ゴーストの動作をカスタマイズするために、読み書きできる変数。

| 変数名 | 初期値 | 内容 |
|--------|--------|------|
| `aitalkinterval` | 180（秒） | AI トーク（ランダムトーク）の発動間隔。0 で無効化 |
| `communicateratio` | 0（%） | AI トークの発動時に、コミュニケート開始を選ぶ割合 |

```
aitalkinterval = 300
```

## config.dic の主要設定

`config.dic` でシステムの動作を変更できる。

| 定数名 | 初期値 | 内容 |
|--------|--------|------|
| `TALK_INTERVAL` | 180 | `aitalkinterval` の初期値（秒） |
| `COM_RATIO` | 0 | `communicateratio` の初期値（%） |
| `SHIORI3FW.IGLIST_ACCEL` | 1 | 1 で、SSP / CROW の NOTIFY イベントを使ってゴーストリストを高速に構築する（さくら名・ケロ名のリストは作られない） |
| `SHIORI3FW.IGLIST_MAX` | 0 | ファイル走査でゴーストリストを構築するときの、ゴーストの最大取得数。-1 で無制限、0 で取得しない |
| `SHIORI3FW.RES_REF_MAX` | 32 | `res_reference*` 変数の上限インデックス |
| `SHIORI3FW.AUTO_DATA_CONVERT` | 0 | 1 で、SAORI の戻り値などの自動型変換と、バイト値 1 のコンマへの置き換えを行う（AYA5 互換） |
| `SHIORI3FW.REF_ACCEL` | 0 | 1 で、`reference0` などの変数を作らず `reference[0]` のみ使う（高速化） |
| `SHIORI3FW.ENABLE_DELAYED_EVAL` | 0 | `:eval=` による遅延 EVAL を有効にする（セキュリティ上の理由から無効を推奨） |

## AI グラフの既定値

SSP の AI グラフ（レーダーチャート）は、SHIORI リソース `getaistate` で描かれる。ゴースト側に `On_getaistate` が無い、または空を返したときは、システム辞書の `SHIORI3EV.On_getaistate` が次の 6 軸を返す。ゴースト側で `On_getaistate` を定義すれば、そちらが優先される。

| ラベル | 表示値 | 加算値 | 最大値 |
|--------|--------|--------|--------|
| `Boot` | `ghostuptimes`（累計起動回数） | 0 | 段階スケール |
| `Uptime(h)` | `ghostupmin_last / 60`（前回までの累計起動時間） | `ghostupmin / 60`（今回の起動分） | 段階スケール |
| `Memory` | `GETVARLIST()` の要素数 | 0 | 段階スケール |
| `Repertoire` | `GETFUNCLIST('On')` の要素数 | 0 | 段階スケール |
| `Talk/h` | `3600 / aitalkinterval`（`aitalkinterval` が 0 以下なら 0） | 0 | 段階スケール |
| `Social` | `communicateratio` | 0 | 100 |

- 段階スケールは、値を収められる最小の 10、20、50、100、200、500、… （`SHIORI3FW.AIGraphMax`）
- `Memory` と `Repertoire` には、システム辞書自身の変数・関数も含まれる
- `Uptime(h)` の表示値と加算値は小数（SSP 2.4.26 以降が小数を扱える）

## 関連

- [yaya_optional.dic](./yaya-optional-dic.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
- [システム辞書内関数マニュアル（yaya-dic）](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
