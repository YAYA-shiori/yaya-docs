# Migrating from AYA

Migrate an existing AYA5 ghost to YAYA.

## Notes

### DLL name change

The DLL name changes from `aya5.dll` to `yaya.dll`.

- Therefore, you need to rename `aya5.txt` to `yaya.txt`
- The save file name becomes `yaya_variable.cfg`, so the save data is not migrated as-is

A feature is provided to avoid this. Open `aya_shiori3.dic` and add the following code before `OnLoad` in the `load` function.

```
if FSIZE('yaya_variable.cfg') <= 0 {
	RESTOREVAR('aya5_variable.cfg')
	SAVEVAR('yaya_variable.cfg')
	FDEL('aya5_variable.cfg')
}
```

If you have not modified `aya_shiori3.dic`, you can migrate easily by referring to the [system dictionary](../system/yaya-shiori3-dic.md), downloading the required files, and overwriting the existing ones (if you use a backward-compatibility dictionary, add the dictionary for AYA compatibility after `aya_shiori3.dic` in `yaya.txt`. In the current system dictionary, this is `compatible.dic`).

### Changes to the system dictionary

The system dictionary changes (replacing it is recommended).

- In the AYA5 system dictionary, byte value 1 in SAORI return values and similar was replaced with a comma, and numbers were converted to numbers rather than strings; by default, the YAYA system dictionary does not perform these operations
- Some functions (such as `NAMETOVALUE`) are not included in the system dictionary

## Migration procedure

This section describes the migration procedure **if you have not modified `aya_shiori3.dic` in AYA5**. Perform all of the following steps in the ghost's dictionary folder (`ghost/master/`).

1. In `descript.txt`, change `shiori,aya5.dll` to `shiori,yaya.dll`
2. Delete `aya5.dll` and place `yaya.dll` there
3. Rename `aya5.txt` to `yaya.txt`
4. Download [Konnoyayame](http://ms.shillest.net/yayame.xhtml), then either extract the NAR file as a ZIP or install the ghost so that you can access its files
5. Refer to the [system dictionary](../system/yaya-shiori3-dic.md) and copy the contents of the `system` folder
6. Copy `system_config.txt`
7. In `yaya.txt`, remove `dic,aya_shiori3.dic` and replace it with `include, system_config.txt`
8. Open `config.dic` and set `SHIORI3FW.AUTO_DATA_CONVERT` to 1 and `SHIORI3FW.REF_ACCEL` to 0

These steps should resolve most migration-related errors.

## For network distribution

For network distribution, `aya5.dll` and `aya5.txt` are no longer needed, so you can delete them using a `delete.txt` file containing the following, for example.

```
ghost/master/aya5.dll
ghost/master/aya5.txt
```

## Related

- [Creating a ghost with YAYA](./creating-ghost.md)
- [System dictionary/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
