# EVAL

**Category:** メタ操作・特殊関数

## Signature

```
EVAL( string )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 作為 YAYA 腳本執行的文字字串。可以是單一運算式，也可以是多個陳述式（Tc574-6 / Tc602-9 以後） |

## Returns

- 成功時：執行結果。若只有指派而沒有輸出，則為 VOID（沒有傳回值）
- 解析失敗時：原樣傳回引數字串

## Description

將引數字串作為 YAYA 腳本執行。可用於展開運算式，或在執行時合成函式名稱等。

### 單一運算式

若字串是單一運算式，則傳回該運算式的評估值。指派運算式會指派給呼叫端的變數。

```
_x = EVAL('1 + 2')          // 3
EVAL('_name = "Emily"')     // 呼び出し元のローカル変数 _name に代入される
```

### 多個陳述式（Tc574-6 / Tc602-9 以後）

若引號之外包含 `;`、`{`、`}` 或換行，或開頭的詞語是 `return` `if` `while` `for` `foreach` `switch` `void` `parallel` 其中之一，則會作為多個陳述式執行。寫法與寫在函式本體的 `{ }` 中相同。

```
_r = EVAL('_a = 1; _b = _a + 2; _b')   // 3

_r = EVAL('if _hour < 12 { "おはよう" } else { "こんにちは" }')

_r = EVAL('_s = 0; foreach _list; _v { _s += _v }; _s')
```

若透過 here document 等方式傳入包含換行的字串，就能使用與寫在辭典中相同的格式。換行和 `;` 一樣會成為陳述式分隔符，也可以使用 `//` 或 `/* */` 註解，以及以行尾的 `/` 合併行。

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

Tc574-8 / Tc603-1 以後，也可以在傳入的程式碼中使用 here document。

傳回值的決定方式與函式的傳回值相同。若有多個會輸出的運算式，會從中選出一個；可以用 `--` 串接輸出，若寫入 `return`，則會在該處結束執行並傳回該值。

多個陳述式的執行方式，等同於在呼叫端的 `{ }` 中寫入一個區塊。

- 可以讀寫呼叫端的區域變數（包括 `_argv` 和 `_argc`）
- 在其中建立的新區域變數會在 EVAL 結束時消失
- `break` / `continue` / `return` 會在 EVAL 內完成，不會影響呼叫端的迴圈或函式

```
Foo
{
	_count = 1
	_r = EVAL('_count += 10; _tmp = _count * 2; _tmp')
	// _r は 22、_count は 11、_tmp はここでは存在しない
}
```

不能寫入函式定義或 `#define` 等前置處理器指令。若要定義函式，請使用 APPEND_RUNTIME_DIC。

引號中的 `;` `{` `}` 或換行不會被視為分隔符。`EVAL('"a;b"')`，以及將包含換行的字串以 `"` 括起來並展開嵌入元素的用法，一如以往會作為單一運算式評估。

### 字串中包含 `"` 或 `%` 時

在傳給 EVAL 的字串中使用雙引號時，請使用 `CHR(34)`。例如，要將 `"test"` 指派給變數 `i`，請如下撰寫（Tc569-8 以後，也可以連寫兩個 `""`。[值與變數](../grammar/03-values-and-variables.md#文字列)）。

```
EVAL("i=%(CHR(34))test%(CHR(34))")
```

若要在執行 EVAL 時才展開 `%`，也請將 `%` 寫成 `CHR(37)`。以下範例會執行 `"%(foo)"`。

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
- Tc574-6 / Tc602-9：新增執行多個陳述式的功能（以 `;` 或換行分隔的多個陳述式，以及 if/for 等控制陳述式）；此前僅支援單一運算式，傳入多個陳述式時會解析失敗，並原樣傳回引數字串
- Tc574-8 / Tc603-1：新增在傳入的程式碼中使用 here document 的功能；此前會發生 E0007

## See Also

- ISEVALUABLE
- APPEND_RUNTIME_DIC
- [Shell 模式](../grammar/01-basic-settings.md#シェルモード)（沒有辭典時，會評估 request 的輸入並傳回）
