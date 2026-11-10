# SAORI 的使用方法

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## About_SAORI

基本上，製作伺か的人格時，會使用 Satori、YAYA 等 SHIORI，以及 Sakura Script 來撰寫處理程序。
不過，伺か也具備實作以 SHIORI 以外的通用語言（例如 C）撰寫的處理程序的功能。這個功能稱為「SAORI」子系統，藉由使用它，就能實作更進階的處理程序。
此外，SAORI 有稱為 SAORI-basic 和 SAORI-universal 的兩種規格，前者以 exe 格式實作，後者則以 dll 格式實作。

## SAORI-basic

SAORI-basic 指的是以命令列引數（main 函式所接收的引數）作為引數，並傳回標準輸出的 .exe。以下以 C++ 為例，考慮一個接收輸入並傳回結果的程式：

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]はプログラム名、渡したコマンドライン引数はargv[1]から
 cout<<"入力は "<<argv[1]<<endl;
}
```

將這個程式編譯成 .exe 後（建議在編譯時使用靜態建置，以避免依賴環境，例如使用 MinGW(gcc) 時加上 -static 選項），只要這樣就能將它當作 SAORI-basic 使用。
但請注意，伺か的標準字元編碼不是 UTF-8，而是 Shift-JIS。（YAYA 支援 Unicode，但 Satori 只能處理 Shift-JIS）

### 在 YAYA 中的使用方法

在 YAYA 中使用 SAORI-basic 時，會使用 FUNCTIONEX 函式和 proxy_ex.dll（發布來源：<https://github.com/ponapalt/csaori/releases/>）。這是以管道連接 SHIORI（YAYA）與 SAORI 的程式。

!!! note "Tc604-1 之後"
    YAYA 本體會直接執行 SAORI-basic，因此不需要 proxy_ex.dll。請在 FUNCTIONEX 的第一個引數指定從 yaya.dll 到 SAORI-basic 本體的相對路徑，並在第二個引數之後填入要傳給 SAORI-basic 的引數（例如：`FUNCTIONEX('SAORI/sample1_1.exe', "はろーわーるど")`）。標準輸出有多行時，可以使用 `valueex[0]`, `valueex[1]`... 逐行取得。詳細資訊請參閱 [LOADLIB](../functions/LOADLIB.md#saori-basic)。

```
Sample_1_1{
  _result = FUNCTIONEX('SAORI/proxy_ex.dll', 'sample1_1.exe', "はろーわーるど")
  _result
}
```

`\end`{lstlisting}
FUNCTIONEX 的第一個引數指定從 yaya.dll 到 proxy_ex.dll 的相對路徑，第二個引數指定從 proxy_ex.dll 到 SAORI-basic 本體的相對路徑。第三個引數之後則是要傳給 SAORI-basic 的引數。

### 將輸出作為陣列處理的方法

SAORI-basic 的傳回值是標準輸出，因此一般只能傳回一個字串。不過，使用 YAYA 的「以分隔符號簡易表示陣列」功能或 SPLIT 函式，就能將傳回值作為陣列處理。

例如

```
_test = "こんにちは;;Hello;;Hallo;;Saluton"
```

有一個以「;;」作為分隔符號的字串時，

```
 _test[0,";;"]で「こんにちは」
 _test[1,";;"]で「Hello」...
```

只要使用變數名稱[序數,"分隔符號"]，就能像陣列一樣處理。此外，準備多個分隔符號，也能進行類似多維陣列的處理。若要取得陣列大小等，想要將資料作為通用陣列而非簡易陣列處理時，請使用 SPLIT 函式。
範例：

```
_test = SPLIT("こんにちは;;Hello;;Hallo;;Saluton",";;")
"配列のサイズは%(ARRAYSIZE(_test))で中身は%(_test[0])とか%(_test[1])とか"
```

使用上述方法，在製作 SAORI 時，只要讓輸出字串使用分隔符號，就能將輸出作為陣列處理。

## SAORI-universal

這是 .dll 格式的 SAORI；與 SAORI-basic 相比，製作時需要了解 SSTP`\footnote`{Sakura Script Transfer Protocol. Secure Socket Tunneling Protocolではない}。
此外，與 SAORI-basic 不同，它有兩種傳回值（Result 和 Value0、Value1...）。
（規格的詳細資訊請參閱 <http://www.boreas.dti.ne.jp/~sdn/saori.html>。此外，若要以 C 製作 SAORI-universal，使用 <https://github.com/ponapalt/csaori> 公開的函式庫會比較容易。）

### 在 YAYA 中的使用方法

使用 FUNCTIONEX 函式這點相同，但與 SAORI-basic 不同，不需要透過 proxy_ex.dll（實際上，proxy_ex.dll 本身就是使用管道將標準輸出傳給 SHIORI 的 SAORI-universal，而 Satori 則將這項功能整合在 satori.dll 中）
FUNCTIONEX 本身的傳回值是 Result；執行 FUNCTIONEX 後，Value0、Value1... 會存入全域陣列 `valueex[0]`、`valueex[1]`...。
範例：

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

這是呼叫名為 saori.dll 的 SAORI-universal 的範例。FUNCTIONEX 的第一個引數「'SAORI/saori.dll'」指定從 yaya.dll 到 saori.dll 的相對路徑，之後的 Argument 則是要傳給 saori.dll 的引數。

## 將 Python 程式轉換為 SAORI

Python 擁有許多與科學計算、神經網路等相關的函式庫。但由於它是直譯式語言，執行程式時需要在電腦上安裝 Python 環境；從實作人格處理程序的角度來看，這會要求使用者自行建置環境，因此不適合直接發布。
不過，若將 .py 連同其相依的 dll 等檔案一起編譯成 .exe，就能以可獨立執行的程式形式發布。因此，本節將說明如何將以 Python 撰寫的程式實作為 SAORI-basic。

例如，考慮一個接收輸入並傳回結果的處理程序：

```
import sys
#コマンドライン引数を使うためのパッケージ

input = sys.argv[1]
#sys.argv[0]はプログラム名

print("Your input is "+input)
```

這個程式只能在具備 Python 環境的電腦上執行。不過，使用後文將介紹的 PyInstaller，就能將程式及其匯入的套件一併打包成可發布的 .exe。

### PyInstaller

有幾種可將 .py 編譯成 .exe 的程式（例如 cx_freeze、py2exe 等），但只有 PyInstaller 支援 Python 3.x 系列，且目前仍持續更新。只要有 Python 環境，就能在命令列介面中使用

```
 pip install PyInstaller
```

安裝。

使用方法也非常簡單，只要在存放 .py 的資料夾中執行

```
 PyInstaller (プログラム名).py
```

之後，執行同一個資料夾內產生的「dist」資料夾中的「程式名稱.exe」，就能輸出以 Python 撰寫的處理結果。
發布時，可以連同整個 dist 資料夾一起發布；也可以在執行 PyInstaller 時加上 onefile 選項，

```
 PyInstaller (プログラム名).py --onefile
```

將程式整合為單一執行檔並編譯成 .exe。使用 --onefile 能縮小程式大小，但有時會降低執行速度，因此不建議在處理量大的程式中使用 onefile。
此外，執行 PyInstaller 時也會同時產生副檔名為 .spec 的檔案。這是編譯時參照的設定檔；基本上，即使不指定任何設定，PyInstaller 也會自動採用最佳設定進行處理，但也可以視情況編輯這個 .spec 檔案（尤其是無窮迴圈判定的閾值，可能需要依處理程序重新設定）。此時請像以下這樣傳入 spec 檔案並執行。

```
 PyInstaller (プログラム名).spec
```
