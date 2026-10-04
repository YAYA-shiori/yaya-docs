# SAORIの使い方

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

## SAORI(SAORI-universal)の使い方

SAORI-universal(dll形式のSAORI)は2種類の返り値(ResultとValue0,Value1...)を持つ。
FUNCTIONEX()自身の返り値はこのResultで、FUNCTIONEX実行後にValue0,Value1...はvalueex0,valueex1...に格納される。
なお、このvalueex\*は同名の汎用配列にも格納される。つまり`valueex[0]`,`valueex[1]`...としてもよい。

サンプル:

```
Test{
 _Result = FUNCTIONEX('SAORI\saori.dll',Argument0,Argument1,...)
 valueex0
}
```

FUNCTIONEXの第一引数はyaya.dllからの相対パスを指定する(上の例ではyaya.dllが置かれているフォルダの中のSAORIフォルダにsaori.dllが置かれている)。
Argument0,Argument1...はsaori.dllの引数。

これにより`_Result`にsaori.dllのResultが格納され、Testはvalueex0に格納されている値、つまりValue0を返す。

### サンプル

mecabを使って形態素解析を行うSAORI-universalである[kisaragi.dll](https://drive.google.com/drive/folders/0B0yCcgxQctDAblpzWXg1bC1fUGM)を使って解説します。

まず解凍後にkisaragiフォルダをghost`\master`以下に配置してください。複数のSAORIを使う場合はSAORIフォルダを作成し、その中に入れておくと管理し易くなります。以下ではghost`\master\SAORI`に配置されているとして説明します。

形態素解析を行う関数は

```
MorphAnalysis{
 _text = "今日はいい天気だ"
 _Rank = FUNCTIONEX('SAORI\kisaragi\kisaragi.dll','parse',_text)
 for _i = 0; _i<_Rank; _i++{
   valueex[_i]+"\n"
 }
}
```

のように書けます。FUNCTIONEXの第一引数はyaya.dllからの相対パスであることに注意してください。kisaragi.dllの場合、前述した"Result"の返り値は形態素の数、valueexに自動的に格納される"Value"の返り値は解析結果の配列となります。
この関数の場合、実行すると形態素解析結果が改行されて出力されます。

## SAORI-basicの使い方および解説

SAORI-basicはコマンドライン引数(main関数がとる引数)を引数とし、標準出力を返す.exeのことを指します。
例えばC++で

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]にはプログラム名前(ほにゃらら.exe)が入り、入力したコマンドライン引数はargv[1]からになります
 cout<<"入力は"<<argv[1]<<endl;
}
```

のようなプログラムをexeファイルとしてコンパイルすれば、これだけでSAORI-basicになります(コンパイル時には静的ビルドなどで依存環境を切っておくことを推奨します)

ゴーストでこのSAORI-basicを使いたい場合は[proxy_ex.dll](https://github.com/ponapalt/csaori/releases/tag/saori_proxy_ex_v1.0)を通して使います。
SAORI-basicの場合、FUNCTIONEXの返り値はmain関数の標準出力のみとなります。使い方は

```
_結果 = FUNCTIONEX('SAORI\proxy_ex.dll', '(プログラム名).exe', Argument0, Argument1,...)
```

このようになりますが、第二引数はyaya.dllではなくproxy_ex.dllからの相対パスであることに注意してください。この例では両者が同じ階層に置かれていることを想定しています。

※注：ここでのArgument\*は、(プログラム名).exeのコマンドライン引数(すなわち前述のC++の例ではargv)を指します

!!! note "Tc604-1以降"
    YAYA 本体が SAORI-basic を直接実行するので、proxy_ex.dll は要りません。FUNCTIONEX の第一引数に yaya.dll からの相対パスで実行ファイルを指定します。

    ```
    _結果 = FUNCTIONEX('SAORI\(プログラム名).exe', Argument0, Argument1,...)
    ```

    標準出力が複数行のときは、`valueex[0]`, `valueex[1]`... で1行ずつ取り出せます。詳しくは [LOADLIB](../functions/LOADLIB.md#saori-basic) を参照してください。

## サクラスクリプト再生中にSAORIを使う

こちらのページに解説があります。<br>
[音を鳴らす](play-sound.md)
