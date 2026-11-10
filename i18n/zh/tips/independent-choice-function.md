# 将选项直接写成独立函数

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

```
 OnChoiceSelect
 {
    if ISFUNC(reference0) {
    EVAL(reference0)
    }
 }
 
 OnAnchorSelect
 {
    if ISFUNC(reference0) {
    EVAL(reference0)
    }
 }
```

这样就可以在词典中直接使用与 `\q[]` 标签或 `\_a[]` 标签所创建的选项／锚点标识符相同的名称。

### 注意

由于选项／锚点的标识符会直接成为函数名，请确保标识符名称不符合以下任何规则。

- 以数字 0～9 开头。
- 以下划线（"_"）开头。
- 包含以下字符。
空格　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　<　=　>　?　@　[　]　`　{　|　}　<br>

- 与保留字完全一致。

## 相关页面

- [将切换反应也直接写成独立函数](independent-switch-function.md)
- [从锚点标签跳转到 URL](url-jump-from-anchor.md)
