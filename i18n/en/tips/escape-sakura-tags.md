# Escape Sakura Script Tags

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

- Use this when you want the tags to be displayed in the balloon as-is instead of being removed. For example, `\s[]`0 is converted to \\`\s[0]`.
- It is safer to use this function when displaying a variable in the balloon if you do not know what it contains.

### Escape all Sakura Script tags

- Use the [Escape~ functions](../system/yaya-optional-dic.md) included in Hello YAYA World or the SimpleYAYA template.

```
EscapeAllTags( エスケープしたい文字列 )
```

#### Example

```
OnGhostChanged
{
_name = EscapeAllTags( reference[0] )
"%(_name)さんから交代したよ～。\e"
}
```

This way, even if the ghost switches from one named "青い`\105`のノート", the balloon will display "青い`\105`のノートさんから交代したよ～。" as-is.

### Escape only dangerous Sakura Script tags

- Use the [Escape~ functions](../system/yaya-optional-dic.md) included in Hello YAYA World or the SimpleYAYA template.

```
EscapeDangerousTags( エスケープしたい文字列 )
```

This escapes only Sakura Script tags that would cause problems if executed, such as vanishbymyself.
For example, when executing talk that includes Sakura Script picked up from somewhere else.

### Remove tags instead of escaping them

- [Remove Sakura Script tags](remove-sakura-tags.md)
