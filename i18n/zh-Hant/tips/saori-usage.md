# SAORI 的使用方法

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## SAORI（SAORI-universal）的使用方法

SAORI-universal（DLL 格式的 SAORI）有兩種傳回值（Result 和 Value0、Value1……）。
FUNCTIONEX() 本身的傳回值是 Result，而 FUNCTIONEX 執行後，Value0、Value1……會存入 valueex0、valueex1……。
另外，這些 valueex\* 也會存入同名的通用陣列。也就是說，也可以使用 `valueex[0]`、`valueex[1]`……來存取。

範例：

```
Test{
 _Result = FUNCTIONEX('SAORI\saori.dll',Argument0,Argument1,...)
 valueex0
}
```

FUNCTIONEX 的第一個引數指定相對於 yaya.dll 的路徑（以上例來說，saori.dll 放在 yaya.dll 所在資料夾中的 SAORI 資料夾）。
Argument0、Argument1……是 saori.dll 的引數。

如此一來，saori.dll 的 Result 會存入 `_Result`，而 Test 會傳回存放在 valueex0 的值，也就是 Value0。

### 範例

以下使用以 mecab 進行形態素分析的 SAORI-universal [kisaragi.dll](https://drive.google.com/drive/folders/0B0yCcgxQctDAblpzWXg1bC1fUGM) 說明。

解壓縮後，請將 kisaragi 資料夾放在 ghost`\master` 底下。若要使用多個 SAORI，建立 SAORI 資料夾並將它們放在其中，會比較容易管理。以下假設檔案放在 ghost`\master\SAORI` 中。

進行形態素分析的函式可以寫成

```
MorphAnalysis{
 _text = "今日はいい天気だ"
 _Rank = FUNCTIONEX('SAORI\kisaragi\kisaragi.dll','parse',_text)
 for _i = 0; _i<_Rank; _i++{
   valueex[_i]+"\n"
 }
}
```

。請注意，FUNCTIONEX 的第一個引數是相對於 yaya.dll 的路徑。以 kisaragi.dll 為例，前面提到的 "Result" 傳回值是形態素數量，自動存入 valueex 的 "Value" 傳回值則是分析結果的陣列。
執行這個函式後，形態素分析結果會逐行輸出。

## SAORI-basic 的使用方法與說明

SAORI-basic 指的是以命令列引數（main 函式所接收的引數）作為引數，並傳回標準輸出的 .exe。
例如，在 C++ 中

```
#include <iostream>
using namespace std;
int main(int argc,char *argv[]){
 //argv[0]にはプログラム名前(ほにゃらら.exe)が入り、入力したコマンドライン引数はargv[1]からになります
 cout<<"入力は"<<argv[1]<<endl;
}
```

編譯成 exe 檔後，這樣就能成為 SAORI-basic（建議編譯時使用靜態建置等方式，避免依賴執行環境）。

若要在人格中使用這個 SAORI-basic，請透過 [proxy_ex.dll](https://github.com/ponapalt/csaori/releases/tag/saori_proxy_ex_v1.0) 呼叫。
SAORI-basic 的 FUNCTIONEX 傳回值只有 main 函式的標準輸出。使用方法如下：

```
_結果 = FUNCTIONEX('SAORI\proxy_ex.dll', '(プログラム名).exe', Argument0, Argument1,...)
```

請注意，第二個引數是相對於 proxy_ex.dll，而不是 yaya.dll 的路徑。本例假設兩者放在同一層資料夾中。

※註：此處的 Argument\* 指的是 (プログラム名).exe 的命令列引數（也就是前述 C++ 範例中的 argv）

!!! note "Tc604-1以降"
    YAYA 本體會直接執行 SAORI-basic，因此不需要 proxy_ex.dll。FUNCTIONEX 的第一個引數指定相對於 yaya.dll 的執行檔路徑。

    ```
    _結果 = FUNCTIONEX('SAORI\(プログラム名).exe', Argument0, Argument1,...)
    ```

    標準輸出有多行時，可以用 `valueex[0]`、`valueex[1]`……逐行取出。詳情請參閱 [LOADLIB](../functions/LOADLIB.md#saori-basic)。

## 播放 Sakura Script 時使用 SAORI

相關說明請參閱此頁。<br>
[播放音效](play-sound.md)
