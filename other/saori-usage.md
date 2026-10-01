# SAORIの使い方

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

## About_SAORI

基本的に伺かのゴーストを作成するときは里々やYAYAなどのSHIORI及びさくらスクリプトを用いて処理を書く。
しかし伺かにはSHIORI以外の汎用言語(例えばCなど)で書かれた処理を実装する機能が存在する。これを「SAORI」サブシステムと呼び、これを利用することでより高度な処理の実装が可能になる。
またSAORIにはSAORI-basicとSAORI-universalと呼ばれる2種類の規格が存在しており、前者はexe形式、後者はdll形式による実装である。

## SAORI-basic

SAORI-basicはコマンドライン引数(main関数がとる引数)を引数とし、標準出力を返す.exeのことを指す。 例えばC++で次のような入力を受け取って返すプログラムを考える:

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]はプログラム名、渡したコマンドライン引数はargv[1]から
 cout<<"入力は "<<argv[1]<<endl;
}
```

これを.exeとしてコンパイルすれば(コンパイル時には依存環境を切るため静的ビルドを推奨(例えばMinGW(gcc)なら-staticオプションを付けるなど))、これだけでSAORI-basicとして使うことができる。
但し伺かの標準的な文字コードがUTF-8ではなくShift-JISである点に注意。(YAYAであればUnicodeに対応しているが里々ではShift-JISしか扱えない)

### YAYAにおける使い方

YAYAでSAORI-basicを使うにはFUNCTIONEX関数とproxy_ex.dll(配布元は <https://github.com/ponapalt/csaori/releases/> )を利用する。これはパイプとしてSHIORI(YAYA)とSAORIの間を繋ぐプログラムである。

```
Sample_1_1{
  _result = FUNCTIONEX('SAORI/proxy_ex.dll', 'sample1_1.exe', "はろーわーるど")
  _result
}
```

`\end`{lstlisting}
FUNCTIONEXの第一引数はyaya.dllからproxy_ex.dllへの相対パス、第二引数はproxy_ex.dllからSAORI-basic本体への相対パスを指定する。また第三引数以降はSAORI-basicに渡す引数である。

### 出力を配列として扱う方法

SAORI-basicの返り値は標準出力であるため、普通は一つの文字列しか返すことができない。しかしYAYAの機能である「デリミタ(区切り文字)による簡易配列」やSPLIT関数を用いることで返り値を配列として扱うことができる。

例えば

```
_test = "こんにちは;;Hello;;Hallo;;Saluton"
```

という";;"をデリミタとして区切った文字列があるとき、

```
 _test[0,";;"]で「こんにちは」
 _test[1,";;"]で「Hello」...
```

のように変数名[序数,"デリミタ"]とすることで配列であるかのように扱うことができる。また、デリミタを複数用意することで多次元配列のような処理も可能である。配列のサイズを取得したいときなど、簡易配列でなく汎用配列として扱いたいときはSPLIT関数を用いる。
サンプル:

```
_test = SPLIT("こんにちは;;Hello;;Hallo;;Saluton",";;")
"配列のサイズは%(ARRAYSIZE(_test))で中身は%(_test[0])とか%(_test[1])とか"
```

以上の方法を用いれば、SAORI作成時にデリミタを使って文字列を出力するようにすることで出力を配列として扱うことが可能になる。

## SAORI-universal

.dll形式のSAORIであり、SAORI-basicと比べると作成にSSTP`\footnote`{Sakura Script Transfer Protocol. Secure Socket Tunneling Protocolではない}の知識が必要である。
またSAORI-basicとは異なり2種類の返り値(ResultとValue0,Value1...)を持つ。
(仕様についての詳細は <http://www.boreas.dti.ne.jp/~sdn/saori.html> を参照のこと。またCにおけるSAORI-universalの作成は <https://github.com/ponapalt/csaori> で公開しているライブラリを用いると容易である)

### YAYAにおける使い方

FUNCTIONEX関数を用いる点は同じだが、SAORI-basicとは異なりproxy_ex.dllを介する必要はない(実際のところproxy_ex.dllがパイプを使って標準出力をSHIORIに渡すSAORI-universalであり、里々ではsatori.dllにその機能が組み込まれているのである)
FUNCTIONEX自身の返り値はResultで、FUNCTIONEX実行後にValue0,Value1...はグローバルな配列である`valueex[0]`,`valueex[1]`...に格納される。
サンプル:

```
SAORI_universal_Test{
 _Result = FUNCTIONEX('SAORI/saori.dll',Argument0,Argument1,...)
 if (_Result == 1){
   valueex[0]
 }
 else{
   "error"
 }
}
```

これはsaori.dllという名前のSAORI-universalを呼び出している例である。FUNCTIONEXの第一引数「'SAORI/saori.dll'」はyaya.dllからsaori.dllへの相対パス、以降のArgumentはsaori.dllに渡す引数である。

## PythonコードのSAORI化

Pythonには科学計算やニューラルネットワークなどに関するライブラリが豊富に存在する。しかしインタプリタ型言語であるため実行するにはPC本体にPython環境が必要となり、これはゴーストの処理を実装する観点としてはユーザ側に環境構築を要請してしまうためそのまま配布するのには向いていない。
しかし.pyを依存するdllなどを含めて.exeにコンパイルすれば単体で実行可能なプログラムとして配布できる。そこで本節ではpythonで書かれたプログラムをSAORI-basicとして実装する方法を解説する。

例えば次のような入力を受け取って返す処理を考える:

```
import sys
#コマンドライン引数を使うためのパッケージ

input = sys.argv[1]
#sys.argv[0]はプログラム名

print("Your input is "+input)
```

このままではPython環境があるPC上でないと実行出来ない。しかし後述するPyInstallerを用いればこれをimportしたパッケージも含めて配布可能な.exeにすることができる。

### PyInstaller

.pyを.exeにコンパイルするプログラムはいくつか存在(cx_freeze, py2exeなど)するが、Python3.x系列に対応していて現在もアップデートが行われているのはPyInstallerのみである。このプログラムはPython環境があればシェル上で

```
 pip install PyInstaller
```

でインストール可能である。

使い方も非常に簡単で、.pyが置いてあるフォルダ上で

```
 PyInstaller (プログラム名).py
```

を実行した後同フォルダ上に生成された「dist」フォルダ内の「プログラム名.exe」を実行すればPythonで書いた処理を出力できる。
配布時にはこのdistフォルダごと配布するか、PyInstaller実行時にonefileオプションをつけて

```
 PyInstaller (プログラム名).py --onefile
```

とすることで一つの実行ファイルにまとめて.exeにコンパイルすることができる。--onefileにした方がプログラムのサイズは小さくなるが、動作速度は遅くなる場合があるため、重い処理ではonefileを使用しない場合を推奨する。
またPyInstallerを実行すると.specという拡張子のファイルが同時に生成される。これはコンパイルの際に参照する設定ファイルであり、基本的に何も指定しなくても自動で最適な設定で処理をしてくれるが、場合に応じてこの.specファイルを編集してもよい(特に無限ループ判定の閾値の部分は処理によっては再定義する必要がある)。この場合は以下のようにspecファイルを渡して実行する。

```
 PyInstaller (プログラム名).spec
```
