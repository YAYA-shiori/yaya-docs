# Write Choices Directly as Independent Functions

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

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

With this setup, you can write dictionary entries using the identifiers of choices or anchors created with the `\q[]` or `\_a[]` tags as their names.

### Notes

Since the identifier of a choice or anchor becomes the function name as-is, choose an identifier that does not match any of the following rules.

- Begins with a digit from 0 to 9.
- Begins with an underscore ("_").
- Contains any of the following characters.
Space　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　<　=　>　?　@　[　]　`　{　|　}　<br>

- Exactly matches a reserved word.

## Related Pages

- [Write switch reactions directly as independent functions](independent-switch-function.md)
- [Jump to a URL from an anchor tag](url-jump-from-anchor.md)
