# CUTSPACE

**Category:** 文字列操作

## Signature

```
CUTSPACE(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 處理對象的字串 |

## Returns

成功時：移除字串開頭和結尾的空白字元（半形空白、全形空白、定位字元）後的字串
失敗時：VOID

移除字串兩端的空白字元。字串內部的空白（單字之間）會保留。

## Example

```
CUTSPACE(' さくら  まゆら   ') // 「さくら  まゆら」を返す
```

## Compatibility

- YAYA：從初版起即可使用
- AYA：5.8 版以後
