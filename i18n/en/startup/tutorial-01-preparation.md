# Tutorial 1: Preparation

## Download the required items

- **[SSP](http://ssp.shillest.net/) (latest version)**: The current mainstream baseware. It is feature-rich, lightweight, and continues to be updated, so use it unless you have a particular reason not to. This tutorial also assumes that you are using this baseware.
- **yaya.dll (latest version)**: YAYA's SHIORI engine. Download it from the [yaya-shiori releases](https://github.com/YAYA-shiori/yaya-shiori/releases).
- **[Template ghost](creating-ghost.md)**: There are several types, but this tutorial uses the [SimpleYAYA template](../other/simple-yaya-template.md). Install it in the latest version of SSP that you prepared above.

In most cases, the yaya.dll bundled with a ghost is old. Replace it with the latest version you downloaded above (the location is “(the folder containing ssp.exe)\ghost\(the template ghost's folder name)\ghost\master”).

## Set up an environment that makes development easier

### SSP Development Palette

First, start SSP, then right-click the ghost → Settings → Baseware Settings → General → check “Enable developer features” (a warning dialog will appear, but you can safely accept it).

Next, right-click → Functions → open the Development Palette. It includes a set of debugging features that are useful for ghost development. It is a good idea to keep it open while developing.

![SSP Development Palette](../attachment/img_tutorial_01_002.png)

### YAYA debugging tool

Download the [debugger “Tama”](http://umeici.onjn.jp/) and extract it somewhere convenient. See also: [Checking dictionary errors with Tama](../tips/tama-error-check.md)

## Prepare a text editor and YAYA syntax highlighting settings (optional)

You can create a ghost with Windows Notepad, but dictionaries are easier to read when syntax highlighting is set up for YAYA. Choose one you like from the [editor syntax highlighting files](../tips/editor-color-files.md). With JmEditor, it looks like this.

![Syntax highlighting example in JmEditor](../attachment/img_tutorial_01_001.png)

## Set up file associations

Set up file associations for the three extensions “.dic” (dictionary), “.log” (execution log), and “.cfg” (save data), so that double-clicking them opens them in a text editor. The procedure for setting up associations differs by operating system, so it is not covered here. Look it up using a search engine or similar.

If you have prepared a text editor with YAYA syntax highlighting settings, associate “.dic” files with that editor.

## Next step

- [Tutorial 2: Write some dialogue](./tutorial-02-writing-dialogue.md)

## Related

- [SimpleYAYA template](../other/simple-yaya-template.md)
- [Troubleshooting](../other/troubleshooting.md)
