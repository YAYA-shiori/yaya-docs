# Encrypting Dictionaries

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Perform this procedure just before distributing your ghost.

### 1. Download aycencode from this site

- [Redistribution and bundling with your own software are permitted](http://umeici.onjn.jp/)

### 2. Extract the archive and launch aycencode.exe

### 3. Drag the AYA/YAYA dictionary you want to encrypt and drop it into the window that appears

If an encrypted dictionary with the extension “ayc” is created in the same folder as the AYA/YAYA dictionary, the operation was successful.

### 4. Set the encrypted dictionary as a dictionary to load

Specify it in aya.txt or yaya.txt. The format is the same as for a regular dictionary.<br>

```
dic, xxxxx.ayc
```

You can change the dictionary's extension to something else (the same applies to dictionaries before encryption).<br>
You do not need to encrypt every dictionary file; you can encrypt and load only some of them. This is a better approach if you only want to hide certain parts.<br>

## Notes

- This does not make the dictionary completely impossible to inspect. Someone with the necessary knowledge can analyze it if they wish. It is best to think of this as making it “not easy for ordinary users to inspect.”
- Be careful not to include unencrypted dictionaries when distributing your ghost. Also add them to the exclusion settings of your network update automation tool when performing network updates.
- Keep a backup of the original, unencrypted dictionaries.
