# PARSETOML
**Category:** 型取得/変換

## Signature
```
PARSETOML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | TOML 字串 |

## Returns
- 成功時：轉換 TOML 後的雜湊
- 失敗時：空（VOID）

## Description
解析 TOML 字串，並轉換成雜湊後傳回。支援的值與 [FREADTOML](FREADTOML.md#値の対応) 相同。

從檔案讀取時請使用 [FREADTOML](FREADTOML.md)。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| str 不是字串 | W0009 | 9 |
| 無法解析為 TOML | W0026（也會輸出行號和原因） | 26 |

## Example
```
_t = PARSETOML("a = 1" + CHR(10) + "b.c = 'x'")
_t["a"]                     // 1
_t["b"]["c"]                // x

PARSETOML("a = 1" + CHR(10) + "a = 2")
// 空（警告 W0026 : line 2 : duplicate key : a）
```

## Compatibility
- YAYA: Tc602-5 以後

## See Also
- [FREADTOML](FREADTOML.md)
- [DUMPTOML](DUMPTOML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSEYAML](PARSEYAML.md)
