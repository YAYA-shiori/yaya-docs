# SAORI 的用法

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## 关于 SAORI

通常在制作伺か人格时，会使用 Satori、YAYA 等 SHIORI 以及 Sakura Script 来编写处理逻辑。
不过，伺か也具有一种功能，可以实现用 SHIORI 以外的通用语言（例如 C）编写的处理逻辑。这被称为「SAORI」子系统，通过使用它可以实现更高级的处理。
此外，SAORI 存在称为 SAORI-basic 和 SAORI-universal 的两种规范，前者以 exe 格式实现，后者以 dll 格式实现。

## SAORI-basic

SAORI-basic 指的是以命令行参数（main 函数接收的参数）作为参数，并返回标准输出的 .exe。例如，考虑一个用 C++ 编写、接收并返回如下输入的程序：

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]はプログラム名、渡したコマンドライン引数はargv[1]から
 cout<<"入力は "<<argv[1]<<endl;
}
```

将其编译为 .exe 后（编译时建议使用静态构建，以切断对依赖环境的依赖（例如，使用 MinGW(gcc) 时添加 -static 选项等）），只需这样就可以将它用作 SAORI-basic。
但请注意，伺か的标准字符编码不是 UTF-8，而是 Shift-JIS。（YAYA 支持 Unicode，但 Satori 只能处理 Shift-JIS）

### YAYA 中的用法

要在 YAYA 中使用 SAORI-basic，需要使用 FUNCTIONEX 函数和 proxy_ex.dll（发布地址为 <https://github.com/ponapalt/csaori/releases/>）。这是一个通过管道连接 SHIORI（YAYA）与 SAORI 的程序。

!!! note "Tc604-1 及之后"
    YAYA 本体会直接执行 SAORI-basic，因此不需要 proxy_ex.dll。请在 FUNCTIONEX 的第一个参数中指定从 yaya.dll 到 SAORI-basic 本体的相对路径，并在第二个及之后的参数中写入传递给 SAORI-basic 的参数（例：`FUNCTIONEX('SAORI/sample1_1.exe', "はろーわーるど")`）。标准输出有多行时，可以通过 `valueex[0]`、`valueex[1]`...逐行取出。详情请参阅 [LOADLIB](../functions/LOADLIB.md#saori-basic)。

```
Sample_1_1{
  _result = FUNCTIONEX('SAORI/proxy_ex.dll', 'sample1_1.exe', "はろーわーるど")
  _result
}
```

`\end`{lstlisting}
FUNCTIONEX 的第一个参数指定从 yaya.dll 到 proxy_ex.dll 的相对路径，第二个参数指定从 proxy_ex.dll 到 SAORI-basic 本体的相对路径。第三个及之后的参数则是传递给 SAORI-basic 的参数。

### 将输出作为数组处理的方法

SAORI-basic 的返回值是标准输出，因此通常只能返回一个字符串。不过，使用 YAYA 的「通过分隔符（分隔字符）实现的简易数组」功能或 SPLIT 函数，就可以将返回值作为数组处理。

例如

```
_test = "こんにちは;;Hello;;Hallo;;Saluton"
```

存在一个以「;;」为分隔符分隔的字符串时，

```
 _test[0,";;"]で「こんにちは」
 _test[1,";;"]で「Hello」...
```

像这样写成变量名[序数,"分隔符"]，就可以像数组一样处理。此外，通过设置多个分隔符，也可以实现类似多维数组的处理。需要获取数组大小等信息时，如果希望将其作为通用数组而非简易数组处理，请使用 SPLIT 函数。
示例：

```
_test = SPLIT("こんにちは;;Hello;;Hallo;;Saluton",";;")
"配列のサイズは%(ARRAYSIZE(_test))で中身は%(_test[0])とか%(_test[1])とか"
```

使用以上方法，在创建 SAORI 时让它使用分隔符输出字符串，就可以将输出作为数组处理。

## SAORI-universal

这是 .dll 格式的 SAORI，与 SAORI-basic 相比，创建时需要了解 SSTP`\footnote`{Sakura Script Transfer Protocol. Secure Socket Tunneling Protocolではない}。
此外，它与 SAORI-basic 不同，具有两种返回值（Result 和 Value0、Value1...）。
（有关规范的详细信息，请参阅 <http://www.boreas.dti.ne.jp/~sdn/saori.html>。此外，使用 <https://github.com/ponapalt/csaori> 上发布的库，可以轻松创建 C 语言版的 SAORI-universal。）

### YAYA 中的用法

同样使用 FUNCTIONEX 函数，但与 SAORI-basic 不同，无需通过 proxy_ex.dll（实际上，proxy_ex.dll 本身就是通过管道将标准输出传递给 SHIORI 的 SAORI-universal，而在 Satori 中该功能已内置于 satori.dll 中）
FUNCTIONEX 自身的返回值是 Result，执行 FUNCTIONEX 后，Value0、Value1... 会存储在全局数组 `valueex[0]`、`valueex[1]`... 中。
示例：

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

这是调用名为 saori.dll 的 SAORI-universal 的示例。FUNCTIONEX 的第一个参数「'SAORI/saori.dll'」是从 yaya.dll 到 saori.dll 的相对路径，之后的 Argument 是传递给 saori.dll 的参数。

## 将 Python 代码实现为 SAORI

Python 拥有许多与科学计算、神经网络等相关的库。不过，由于它是一种解释型语言，运行时需要 PC 本机安装 Python 环境；从实现人格处理逻辑的角度来看，这就要求用户配置环境，因此不适合直接分发。
不过，将 .py 连同其依赖的 dll 等一起编译为 .exe 后，就可以作为独立运行的程序进行分发。因此，本节将介绍如何将 Python 编写的程序实现为 SAORI-basic。

例如，考虑一个接收并返回如下输入的处理：

```
import sys
#コマンドライン引数を使うためのパッケージ

input = sys.argv[1]
#sys.argv[0]はプログラム名

print("Your input is "+input)
```

这样无法在没有 Python 环境的 PC 上运行。不过，使用下文介绍的 PyInstaller，就可以将导入的包也包含在内，生成可供分发的 .exe。

### PyInstaller

虽然存在一些可将 .py 编译为 .exe 的程序（如 cx_freeze、py2exe 等），但只有 PyInstaller 支持 Python3.x 系列并且目前仍在更新。只要有 Python 环境，就可以在 shell 中通过

```
 pip install PyInstaller
```

安装。

使用方法也非常简单，在放置 .py 的文件夹中执行

```
 PyInstaller (プログラム名).py
```

之后，运行同一文件夹中生成的「dist」文件夹内的「程序名.exe」，即可输出用 Python 编写的处理结果。
分发时，可以直接分发整个 dist 文件夹；也可以在运行 PyInstaller 时添加 onefile 选项，

```
 PyInstaller (プログラム名).py --onefile
```

这样就能将其编译为一个可执行文件 .exe。使用 --onefile 时程序体积会更小，但运行速度可能会变慢，因此对于耗时较长的处理，建议不要使用 onefile。
此外，运行 PyInstaller 时还会同时生成一个扩展名为 .spec 的文件。这是编译时会参照的设置文件；通常即使不指定任何内容，它也会自动使用最合适的设置进行处理，但也可以根据情况编辑此 .spec 文件（特别是无限循环判定阈值部分，有时需要根据处理内容重新定义）。此时，像下面这样传入 spec 文件运行。

```
 PyInstaller (プログラム名).spec
```
