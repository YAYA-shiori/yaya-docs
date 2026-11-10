# UNDEFGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
UNDEFGLOBALDEFINE( definename )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| definename | 以 `#globaldefine` 宣告的指示詞名稱 |

## Returns
- 0：成功
- 1：失敗

## Description
停用並刪除以 `#globaldefine` 宣告的指示詞。

無法將以 `#globaldefine` 定義的文字直接插入辭典檔案。即使以引號括住，前置處理器仍會套用，因此若要避開此問題，請將目標字串拆開記述（例如，串接 `"TEST_" + "DEF"`）。

## Compatibility
- YAYA：Tc561-1 之後

## See Also
- DICUNLOAD
- SETGLOBALDEFINE
- ISGLOBALDEFINE
- PROCESSGLOBALDEFINE
