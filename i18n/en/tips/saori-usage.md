# How to Use SAORI

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## How to Use SAORI (SAORI-universal)

SAORI-universal (SAORI in DLL format) has two types of return values (Result and Value0, Value1...).
The return value of FUNCTIONEX() itself is Result, and after FUNCTIONEX finishes executing, Value0, Value1... are stored in valueex0, valueex1....
These valueex\* are also stored in a generic array with the same name. In other words, you can also use them as `valueex[0]`, `valueex[1]`....

Example:

```
Test{
 _Result = FUNCTIONEX('SAORI\saori.dll',Argument0,Argument1,...)
 valueex0
}
```

The first argument of FUNCTIONEX specifies a relative path from yaya.dll (in the example above, saori.dll is located in the SAORI folder inside the folder where yaya.dll is located).
Argument0, Argument1... are the arguments for saori.dll.

This stores the Result from saori.dll in `_Result`, and Test returns the value stored in valueex0, that is, Value0.

### Example

This example uses [kisaragi.dll](https://drive.google.com/drive/folders/0B0yCcgxQctDAblpzWXg1bC1fUGM), an SAORI-universal that performs morphological analysis using mecab.

First, extract the files and place the kisaragi folder under ghost`\master`. If you use multiple SAORI, it is easier to manage them by creating a SAORI folder and placing them there. The following instructions assume that it is located at ghost`\master\SAORI`.

The function for performing morphological analysis can be written as follows:

```
MorphAnalysis{
 _text = "今日はいい天気だ"
 _Rank = FUNCTIONEX('SAORI\kisaragi\kisaragi.dll','parse',_text)
 for _i = 0; _i<_Rank; _i++{
   valueex[_i]+"\n"
 }
}
```

Note that the first argument of FUNCTIONEX is a relative path from yaya.dll. In the case of kisaragi.dll, the previously mentioned "Result" return value is the number of morphemes, and the "Value" return value, which is automatically stored in valueex, is an array of analysis results.
When this function runs, the morphological analysis results are output on separate lines.

## How to Use and Explanation of SAORI-basic

SAORI-basic refers to an .exe that takes command-line arguments (the arguments received by the main function) and returns standard output.
For example, in C++:

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]にはプログラム名前(ほにゃらら.exe)が入り、入力したコマンドライン引数はargv[1]からになります
 cout<<"入力は"<<argv[1]<<endl;
}
```

If you compile a program like this as an exe file, it will work as SAORI-basic (when compiling, it is recommended that you isolate the dependency environment by using static builds or similar methods).

To use this SAORI-basic in a ghost, use it through [proxy_ex.dll](https://github.com/ponapalt/csaori/releases/tag/saori_proxy_ex_v1.0).
For SAORI-basic, the return value of FUNCTIONEX is only the standard output of the main function. Use it as follows:

```
_結果 = FUNCTIONEX('SAORI\proxy_ex.dll', '(プログラム名).exe', Argument0, Argument1,...)
```

Note that the second argument is a relative path from proxy_ex.dll, not yaya.dll. This example assumes that both are located at the same directory level.

Note: Here, Argument\* refers to the command-line arguments for (プログラム名).exe (that is, argv in the C++ example above).

!!! note "Tc604-1以降"
    YAYA itself runs SAORI-basic directly, so proxy_ex.dll is not needed. Specify the executable file as a relative path from yaya.dll in the first argument of FUNCTIONEX.

    ```
    _結果 = FUNCTIONEX('SAORI\(プログラム名).exe', Argument0, Argument1,...)
    ```

    If the standard output has multiple lines, you can retrieve them one line at a time using `valueex[0]`, `valueex[1]`.... For details, see [LOADLIB](../functions/LOADLIB.md#saori-basic).

## Using SAORI While Playing Sakura Script

See this page for an explanation.<br>
[Playing sounds](play-sound.md)
