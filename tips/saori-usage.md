# SAORIの使い方

**Source:** Tips/SAORIの使い方

## 概要

YAYA/03 でSAORI（外部DLL）を使う方法の解説。SAORI-universal（DLL形式）とSAORI-basic（EXE形式）の2種類がある。

## SAORI-universal（DLL形式）

`FUNCTIONEX()` を使って呼び出す。戻り値は2種類：

- **Result:** `FUNCTIONEX()` 自体の戻り値
- **Value0, Value1, ...:** 実行後に `valueex0`, `valueex1` 変数に格納される

### 基本構文

```
Test
{
  _Result = FUNCTIONEX('SAORI\saori.dll', Argument0, Argument1, ...)
  valueex0
}
```

第1引数は `yaya.dll` からの相対パスで指定する。

### 実装例（形態素解析）

`kisaragi.dll` を使った形態素解析の例：

```
MorphAnalysis
{
  _text = "今日はいい天気だ"
  _Rank = FUNCTIONEX('SAORI\kisaragi\kisaragi.dll', 'parse', _text)
  for _i = 0; _i<_Rank; _i++ {
    valueex[_i]+"\n"
  }
}
```

## SAORI-basic（EXE形式）

コマンドライン引数と標準出力を使うEXEファイル形式。`proxy_ex.dll` を仲介として使う必要がある。

## 注意事項

- SAORIはSAKURAスクリプト再生中に呼び出す場合、別途考慮が必要（音声出力などのTipsページを参照）

## 関連項目

- マニュアル/関数/FUNCTIONEX
- マニュアル/関数/LOADLIB
- マニュアル/関数/UNLOADLIB
- other/saori-usage.md
