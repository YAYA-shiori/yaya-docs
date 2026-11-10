# How to Use SAORI

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## About_SAORI

When creating an Ukagaka ghost, you generally write its behavior using a SHIORI such as Satori or YAYA, together with Sakura Script.
However, Ukagaka also provides a feature for implementing behavior written in a general-purpose language other than SHIORI (such as C). This is called the “SAORI” subsystem, and using it makes it possible to implement more advanced behavior.
There are also two SAORI specifications, called SAORI-basic and SAORI-universal: the former is implemented as an exe file, and the latter as a dll file.

## SAORI-basic

SAORI-basic refers to an .exe that takes command-line arguments (the arguments accepted by the main function) as its arguments and returns standard output. For example, consider a C++ program that receives and returns the following input:

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]はプログラム名、渡したコマンドライン引数はargv[1]から
 cout<<"入力は "<<argv[1]<<endl;
}
```

If you compile this as an .exe (static linking is recommended to avoid dependencies at compile time; for example, with MinGW (gcc), add the -static option), you can use it as SAORI-basic as is.
Note, however, that the standard character encoding for Ukagaka is Shift-JIS, not UTF-8. (YAYA supports Unicode, but Satori can only handle Shift-JIS.)

### Using It with YAYA

To use SAORI-basic with YAYA, use the FUNCTIONEX function and proxy_ex.dll (available from <https://github.com/ponapalt/csaori/releases/>). This program connects SHIORI (YAYA) and SAORI through a pipe.

!!! note "Tc604-1以降"
    YAYA itself executes SAORI-basic directly, so proxy_ex.dll is not needed. Specify the relative path from yaya.dll to the SAORI-basic executable as the first argument to FUNCTIONEX, and write the arguments to pass to SAORI-basic as the second argument onward (for example: `FUNCTIONEX('SAORI/sample1_1.exe', "はろーわーるど")`). When standard output consists of multiple lines, you can retrieve them one line at a time with `valueex[0]`, `valueex[1]`, and so on. For details, see [LOADLIB](../functions/LOADLIB.md#saori-basic).

```
Sample_1_1{
  _result = FUNCTIONEX('SAORI/proxy_ex.dll', 'sample1_1.exe', "はろーわーるど")
  _result
}
```

`\end`{lstlisting}
The first argument to FUNCTIONEX specifies the relative path from yaya.dll to proxy_ex.dll, and the second argument specifies the relative path from proxy_ex.dll to the SAORI-basic executable. The third argument onward are the arguments to pass to SAORI-basic.

### Handling Output as an Array

Since the return value of SAORI-basic is standard output, it usually can return only a single string. However, you can handle the return value as an array by using YAYA's “simple arrays” based on delimiters, or the SPLIT function.

For example,

```
_test = "こんにちは;;Hello;;Hallo;;Saluton"
```

when you have a string delimited by ";;",

```
 _test[0,";;"]で「こんにちは」
 _test[1,";;"]で「Hello」...
```

you can treat it as an array by writing variable_name[ordinal,"delimiter"]. You can also use multiple delimiters to perform processing like that of a multidimensional array. Use the SPLIT function when you want to handle the data as a generic array rather than a simple array, such as when you want to get the array size.
Example:

```
_test = SPLIT("こんにちは;;Hello;;Hallo;;Saluton",";;")
"配列のサイズは%(ARRAYSIZE(_test))で中身は%(_test[0])とか%(_test[1])とか"
```

Using the method above, you can handle output as an array by having SAORI output a string that uses delimiters.

## SAORI-universal

This is a .dll-based SAORI. Compared with SAORI-basic, creating one requires knowledge of SSTP`\footnote`{Sakura Script Transfer Protocol. Secure Socket Tunneling Protocolではない}.
Unlike SAORI-basic, it has two types of return values: Result and Value0, Value1, and so on.
(For details on the specification, see <http://www.boreas.dti.ne.jp/~sdn/saori.html>. For creating SAORI-universal in C, it is easier to use the library available at <https://github.com/ponapalt/csaori>.)

### Using It with YAYA

The use of the FUNCTIONEX function is the same, but unlike SAORI-basic, SAORI-universal does not need to go through proxy_ex.dll. (In fact, proxy_ex.dll is a SAORI-universal that uses a pipe to pass standard output to SHIORI, and Satori has this functionality built into satori.dll.)
The return value of FUNCTIONEX itself is Result, and after FUNCTIONEX is executed, Value0, Value1, and so on are stored in the global array `valueex[0]`, `valueex[1]`, and so on.
Example:

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

This example calls a SAORI-universal named saori.dll. The first argument to FUNCTIONEX, "'SAORI/saori.dll'", is the relative path from yaya.dll to saori.dll; the subsequent arguments are passed to saori.dll.

## Making Python Code into SAORI

Python has a wealth of libraries for scientific computing, neural networks, and other uses. However, because it is an interpreted language, running Python requires a Python environment on the user's PC. This means that distributing it as is is not suitable for implementing a ghost's behavior, since it would require users to set up an environment.
However, if you compile a .py file into an .exe along with the dll files it depends on, you can distribute it as a standalone executable. This section explains how to implement a program written in Python as SAORI-basic.

For example, consider code that receives and returns the following input:

```
import sys
#コマンドライン引数を使うためのパッケージ

input = sys.argv[1]
#sys.argv[0]はプログラム名

print("Your input is "+input)
```

As is, this can only run on a PC with a Python environment. However, using PyInstaller, described below, you can make it into a distributable .exe that includes the packages it imports.

### PyInstaller

There are several programs that compile .py files into .exe files, such as cx_freeze and py2exe, but PyInstaller is the only one that supports the Python 3.x series and is still being updated. If you have a Python environment, you can install this program from the shell with

```
 pip install PyInstaller
```

.

It is also very easy to use. In the folder containing the .py file, run

```
 PyInstaller (プログラム名).py
```

Then run “program_name.exe” in the “dist” folder created in the same folder to output the behavior written in Python.
When distributing it, you can distribute the entire dist folder, or combine everything into a single executable and compile it to an .exe by adding the onefile option when running PyInstaller:

```
 PyInstaller (プログラム名).py --onefile
```

Using --onefile makes the program smaller, but may slow it down, so avoid using onefile for processing-intensive programs.
Running PyInstaller also generates a file with the .spec extension. This is a configuration file referenced during compilation. In general, PyInstaller automatically uses optimal settings even if you do not specify anything, but you can edit this .spec file as needed (in particular, depending on the processing, you may need to redefine the threshold for infinite-loop detection). In that case, run PyInstaller with the spec file as follows:

```
 PyInstaller (プログラム名).spec
```
