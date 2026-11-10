# Checking Dictionary Errors with Tama

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## Checking dictionary errors with “Tama”

You can easily detect errors using the debugging tool “Tama.”

- [Tama Improvement Project](https://github.com/nikolat/tama)　You can download it from the Releases section on the right.
- [“Tama” distribution site](http://umeici.onjn.jp/)　You can download it from “tama(debugger for aya).”

### Step 1

#### 1. Start Tama

Start Tama **before starting the ghost**.

#### 2. Start the ghost

If there are no errors, messages will scroll by at a frightening speed.<br>
If there are errors, something will be displayed in red.

#### 3. Check the errors that appeared

![Image2.png](../attachment/Image2.png)

Orange indicates a warning, and red indicates a fatal error.<br>
The program will still run with orange warnings, but red indicates a **fatal error that prevents the ghost from running**, so you need to fix it.

```
aya_mouse.dic(8) : error E???? ...
```

The name on the far left is the dictionary file where the error occurred, and the number in parentheses indicates the line.

### Step 2

#### 1. Shut down the ghost

**Shut down all ghosts that are under development, and any others that are running.**<br>
“Tama” can also display runtime activity, so if any ghosts are currently running, messages will scroll by at a frightening speed.

#### 2. Drop the AYA DLL onto Tama

![Image1.png](../attachment/Image1.png)

Drop the DLL, not a dictionary file.

#### 3. Check the errors that appeared

This is the same as Step 1, item 3.

### Bonus - Explanation of the right-click menu

**jump to Top**: Scroll to the very top.

**jump to Bottom**: Scroll to the very bottom.

**Copy to clipboard**: Copy the contents to the clipboard.

**receiVe**: ~

Displays the runtime activity of the currently running ghost.<br>
If you want to work on various things in Tama while keeping a ghost running, it is a good idea to clear this check mark.

**reQuest dialog**: This is for debugging aimed at advanced developers. You normally should not use it (hey!).

**Reload(unload and load)**: Reload. If you have edited a dictionary and want to check it again, you can do so directly from this menu without having to drop the DLL again.

**Unload**: Unloads the AYA that was loaded. You normally do not need to use this.

**eXit(auto unload)**: Exits. Clicking the window's × button does the same thing.

## Attachments

- [Image1.png](../attachment/Image1.png)
- [Image2.png](../attachment/Image2.png)
