# SAORI的使用方法

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## SAORI(SAORI-universal)的使用方法

SAORI-universal（DLL形式的SAORI）有两种返回值（Result和Value0、Value1……）。
FUNCTIONEX()自身的返回值是Result，执行FUNCTIONEX后，Value0、Value1……会被存入valueex0、valueex1……。
另外，这些valueex\*也会存入同名的通用数组中。也就是说，也可以使用`valueex[0]`、`valueex[1]`……。

示例：

```
Test{
 _Result = FUNCTIONEX('SAORI\saori.dll',Argument0,Argument1,...)
 valueex0
}
```

FUNCTIONEX的第一个参数指定相对于yaya.dll的路径（在上面的例子中，saori.dll位于存放yaya.dll的文件夹中的SAORI文件夹内）。
Argument0、Argument1……是saori.dll的参数。

这样一来，`_Result`中会存入saori.dll的Result，而Test会返回存入valueex0的值，也就是Value0。

### 示例

下面以使用mecab进行形态素分析的SAORI-universal [kisaragi.dll](https://drive.google.com/drive/folders/0B0yCcgxQctDAblpzWXg1bC1fUGM)为例进行说明。

解压后，请将kisaragi文件夹放在ghost`\master`下。如果要使用多个SAORI，创建SAORI文件夹并将它们放入其中，会更便于管理。以下说明假定它位于ghost`\master\SAORI`中。

进行形态素分析的函数可以写成

```
MorphAnalysis{
 _text = "今日はいい天気だ"
 _Rank = FUNCTIONEX('SAORI\kisaragi\kisaragi.dll','parse',_text)
 for _i = 0; _i<_Rank; _i++{
   valueex[_i]+"\n"
 }
}
```

这样。请注意，FUNCTIONEX的第一个参数是相对于yaya.dll的路径。对于kisaragi.dll，前面提到的“Result”返回值是形态素的数量，而自动存入valueex的“Value”返回值则是分析结果数组。
执行此函数时，形态素分析结果会以换行分隔后输出。

## SAORI-basic的使用方法及说明

SAORI-basic指的是将命令行参数（main函数接收的参数）作为参数，并返回标准输出的.exe。
例如，使用C++编写

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]にはプログラム名前(ほにゃらら.exe)が入り、入力したコマンドライン引数はargv[1]からになります
 cout<<"入力は"<<argv[1]<<endl;
}
```

这样的程序，并将其编译为exe文件，仅此就能得到SAORI-basic（建议在编译时使用静态构建等方式，避免依赖运行环境）

如果要在人格中使用这个SAORI-basic，请通过[proxy_ex.dll](https://github.com/ponapalt/csaori/releases/tag/saori_proxy_ex_v1.0)来调用。
对于SAORI-basic，FUNCTIONEX的返回值只有main函数的标准输出。用法如下：

```
_結果 = FUNCTIONEX('SAORI\proxy_ex.dll', '(プログラム名).exe', Argument0, Argument1,...)
```

需要注意的是，第二个参数是相对于proxy_ex.dll而非yaya.dll的路径。本例假定两者位于同一层级。

※注：这里的Argument\*指的是(プログラム名).exe的命令行参数（也就是前述C++例子中的argv）

!!! note "Tc604-1以降"
    YAYA本体会直接执行SAORI-basic，因此不需要proxy_ex.dll。FUNCTIONEX的第一个参数指定相对于yaya.dll的可执行文件路径。

    ```
    _結果 = FUNCTIONEX('SAORI\(プログラム名).exe', Argument0, Argument1,...)
    ```

    标准输出有多行时，可以使用`valueex[0]`、`valueex[1]`……逐行取出。详情请参阅[LOADLIB](../functions/LOADLIB.md#saori-basic)。

## 在播放Sakura Script期间使用SAORI

相关说明请参阅此页面。<br>
[播放声音](play-sound.md)
