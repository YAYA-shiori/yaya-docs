# LSO
**Category:** メタ操作・特殊関数

## Signature
```
LSO
LSO()
```

## Parameters
無

## Returns
表示前一次選擇操作所選位置的數值。

## Description

是 "last Selection Order" 的縮寫。以表示位置的數值傳回最後一次選擇的結果。

```
request
{
    _i = foo
    LSO
}

foo
{
    "earth"
    "moon"
    "sun"
}
```

若 `"sun"` 被指派給 `_i`，`LSO` 就會是 2（從 0 開始計數）。只要發生擇一選擇，這個函式就會運作。因此，必須在相關處理完成後立即取得其值，否則便沒有意義。

### 請留意取得的位置

如果下列程式碼是要取得 `ANY` 的選擇結果，便是不正確的。此處的 `LSO` 會取得 `{ }` 的選擇結果。因此 `res` 永遠會是 0。

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
    }
    res = LSO
}
```

改成下列寫法後，就會如預期運作。

```
request
{
    {
        "This is a " + ANY("pen", "pencil", "eraser") + "."
        res = LSO
    }
}
```

### 有輸出確定子時

存在輸出確定子（`--`）時，`LSO` 會對所有可能的組合運作。

```
request
{
    {
        "1"
        "2"
        "3"
        --
        "A"
        "B"
    }
    _i = LSO
}
```

例如，上述函式中的 `{ }` 區塊會輸出 `"1A"` `"2A"` `"3A"` `"1B"` `"2B"` `"3B"` 其中之一。`LSO` 的值範圍也與此相同，為 0～5。各值的順序與上述項目相同。

## Compatibility
- YAYA：從初始版本起可使用
- AYA：版本 5.8 以後可使用

## See Also
- ANY
