# PARSEYAML
**Category:** 型取得/変換

## Signature
```
PARSEYAML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | YAML 字串 |

## Returns
- 成功時：轉換 YAML 後的值
- 失敗時：空（VOID）

## Description
解析 YAML 字串，並轉換成雜湊、陣列等值後傳回。支援的寫法和對應的值與 [FREADYAML](FREADYAML.md#対応している書き方) 相同。

從檔案讀取時請使用 [FREADYAML](FREADYAML.md)。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串 | W0009 | 9 |
| 無法解析為 YAML，或使用不支援的寫法 | W0026（也會輸出行號和原因） | 26 |

## Example
```
_y = PARSEYAML("{name: さくら, tags: [ghost, shell]}")
_y["name"]                  // さくら
_y["tags"][1]               // shell

PARSEYAML("- 1" + CHR(10) + "- 0x10" + CHR(10) + "- yes" + CHR(10) + "- '007'")
// 整数 1、整数 16、文字列 yes、文字列 007 の汎用配列

PARSEYAML("a: [1")          // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc602-5 以後

## See Also
- [FREADYAML](FREADYAML.md)
- [DUMPYAML](DUMPYAML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSETOML](PARSETOML.md)
