# EVAL

**Category:** メタ操作・特殊関数

## Signature

```
EVAL( string )
```

## Parameters

| 參數 | 說明 |
|-----------|-------------|
| string | 作為 YAYA 指令碼執行的文字字串。可以是單一運算式，或一連串陳述式（Tc574-6 / Tc602-9 以後） |

## Returns

- 成功時：執行結果。若只有指派而沒有輸出，則為 VOID（沒有傳回值）
- 解析失敗時：原樣傳回引數字串

## Description

將引數字串作為 YAYA 指令碼執行。可用於展開運算式或在執行時組合函式名稱等。

### 單一運算式

若字串是單一運算式，便會傳回該運算式的求值結果。指派運算式會將值指派給呼叫端的變數。

```
_x = EVAL('1 + 2')          // 3
EVAL('_name = "Emily"')     // 呼び出し元のローカル変数 _name に代入される
```

### 一連串陳述式（Tc574-6 / Tc602-9 以後）

若引號外有 `;`、`{`、`}` 或換行，或開頭的字詞是 `return` `if` `while` `for` `foreach` `switch` `void` `parallel` 其中之一，便會以一連串陳述式的形式執行。寫法與在函式本體的 `{ }` 內撰寫相同。

```
_r = EVAL('_a = 1; _b = _a + 2; _b')   // 3

_r = EVAL('if _hour < 12 { "おはよう" } else { "こんにちは" }')

_r = EVAL('_s = 0; foreach _list; _v { _s += _v }; _s')
```

若透過 Here Document 等方式傳入包含換行的字串，就能使用與寫在辭典中相同的格式。換行與 `;` 一樣會成為陳述式分隔符，也可以使用 `//` 或 `/* */` 註解，以及以行尾的 `/` 合併行。

```
_code = <<'
_s = 0
for _i = 1; _i <= 10; _i++ {
	_s += _i
}
_s
'>>
_r = EVAL(_code)   // 55
```

Tc574-8 / Tc603-1 以後，也可以在傳入的程式碼中撰寫 Here Document。

傳回值的決定方式與函式的傳回值相同。若有多個會產生輸出的運算式，會從中選出結果；可用 `--` 串接輸出，若撰寫 `return`，則會在該處結束執行並傳回該值。

一連串陳述式的執行方式，等同於在呼叫端的 `{ }` 中撰寫一個區塊。

- 可以讀寫呼叫端的區域變數（包括 `_argv` 和 `_argc`）
- 在其中新建的區域變數會在 EVAL 結束時消失
- `break` / `continue` / `return` 會在 EVAL 內部完成，不會影響呼叫端的迴圈或函式

```
Foo
{
	_count = 1
	_r = EVAL('_count += 10; _tmp = _count * 2; _tmp')
	// _r は 22、_count は 11、_tmp はここでは存在しない
}
```

不能撰寫函式定義或 `#define` 等前置處理器指令。若要定義函式，請使用 APPEND_RUNTIME_DIC。

若只是要執行包含控制結構的程式碼，使用 APPEND_RUNTIME_DIC 也可以，但 EVAL 的速度較快。這是因為 APPEND_RUNTIME_DIC 需要將函式登錄至函式表，而 EVAL 只需建立一個執行用的區塊並執行。

引號內的 `;` `{` `}` 或換行不會被視為分隔符。`EVAL('"a;b"')` 或是將含有換行的字串用 `"` 括起來以展開嵌入元素，和以往一樣會作為單一運算式求值。

### 在字串中包含 `"` 或 `%` 時

在傳入 EVAL 的字串中使用雙引號時，請使用 `CHR(34)`。例如，若要將 `"test"` 指派給變數 `i`，請如下撰寫（Tc569-8 以後也可以連續撰寫兩個 `""`。[值與變數](../grammar/03-values-and-variables.md#文字列)）。

```
EVAL("i=%(CHR(34))test%(CHR(34))")
```

若要在 EVAL 執行時展開 `%`，也請將 `%` 替換為 `CHR(37)`。以下範例會執行 `"%(foo)"`。

```
EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")
```

將 EVAL 的結果轉換為字串的 `TOSTR(EVAL("formula"))`，與嵌入展開 `"%(formula)"` 會產生相同結果。

## Example

```
EVAL("i=1")

EVAL("i=%(CHR(34))test%(CHR(34))")

EVAL("%(CHR(34))%(CHR(37))(foo)%(CHR(34))")

EVAL('_n = 0; while _n < 3 { _n++ }; _n')   // 3
```

## Compatibility

- YAYA：從初版起支援
- AYA：5.8 以後
- Tc574-6 / Tc602-9：新增執行一連串陳述式的功能（以 `;` 或換行分隔的多個陳述式，以及 if/for 等控制陳述式）；此前僅能執行單一運算式，若傳入一連串陳述式，解析會失敗並原樣傳回引數字串
- Tc574-8 / Tc603-1：新增在傳入的程式碼中使用 Here Document 的功能（此前會發生 E0007）

## See Also

- ISEVALUABLE
- APPEND_RUNTIME_DIC
- [Shell 模式](../grammar/01-basic-settings.md#シェルモード)（沒有辭典時，會對 request 的輸入執行 EVAL 並傳回）
